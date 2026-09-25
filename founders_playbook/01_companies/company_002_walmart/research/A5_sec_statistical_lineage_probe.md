# A5 — The SEC statistical lineage probe: does a government-published, third-party, contemporaneous document name Wal-Mart inside Stage 1?

Company: Walmart (Wal-Mart Stores, Inc.) · Stage 1 · file opened 2026-09-25 · successor to
`A4_independent_periodicals.md` §Host-family re-probe items 1–4 and A4-44(i)/(iii).
Requests spent: **29 of a hard cap of 30** (26 URL-level calls plus 3 Python-client pre-attempts that
403'd before the curl fallback). **No further request was made after the 29th.**

> **PROVENANCE HEADER — read before citing anything below.**
> (1) One body in this file — the re-walked 573-hit HathiTrust result page — arrived over a
> **skipped-verification channel**: it was fetched through the harvester's own
> `Http.fetch()` with `--insecure-hosts babel.hathitrust.org`, and its sidecar records
> `tls_verify: "skipped (--insecure/--insecure-hosts)"`, `client: "curl (--use-curl fallback)"`.
> Any quotation resting on that body is resting on bytes this machine did not cryptographically
> verify. **2) Every other request in this pass went out through `curl` with TLS verification ON**
> (curl's own trust store, no `-k`; Git's curl 8.7.1, which the harvester's notes identify as the
> only client on this box HathiTrust serves) and its sidecar records
> `tls_verify: "on (curl default trust store)"`. The two long texts that carry the findings below —
> the SEC Statistical Bulletin of November 1970 and the SEC's *Securities Traded on Exchanges* as of
> 31 December 1970 — are in that second, verified class, and they are **the only two documents whose
> full text was read in this pass**.
> (3) Raw bodies are **outside the repository**, at
> `$TEMP/a5_sec_lineage_20260926/{hathitrust,internet_archive,google_books}/<sha1>.<ext>` plus
> `<sha1>.meta.json` sidecars written by `tools/periodical_harvest.py::Archive` (23 sidecars; the
> Federal Register calls were made with a raw binary and one file, `fr1.json`, sits in the same
> scratch root). This follows A4's precedent that probe bodies are not written into the repo, and
> the reason `candidates.csv` was **not** appended by this pass.
> (4) No repository file other than this one was created or modified.

---

## Hypothesis and why it mattered

**The hypothesis under test.** Wal-Mart's Stage-1 depth verdict is stuck at *single-lineage*: every
contemporaneous document the dossier holds is the registrant's own annual report or its auditor's
opinion (A3 §7.2(c), count of independent lineages = 1). Method §14 rule 6/§14.6 requires four corpus
families to be *seen*, and no third-party document has yet named the company in-window. A4's re-probe
found that HathiTrust's full-text search — previously recorded as "blocked" (a client CA-store fault,
`HARVEST_README.md` trap 2) — answers, and that a `"Wal-Mart"` search facetted to 1970–1979 returns
**573 full-view candidates whose first page is dominated by U.S. Securities and Exchange Commission
serials**. The inference tested was: *the SEC Statistical Bulletin / annual Statistical Report family
published, in-period, data on registered corporations, so one of those volumes naming Wal-Mart would
be the first government-published, third-party, contemporaneous record of the company — a lineage
wholly independent of the registrant and its auditor.*

**Why it mattered even if it failed.** The verdict cannot move on a hit count, and it cannot move on a
family nobody has opened. Either the SEC line supplies a page (and the independent-lineage count moves
above 1) or it does not (and §14.6's periodical/filing families can be closed *for this company* with
a stated perimeter instead of an assumption). Both outcomes are worth a pass; only "unread" is worth
nothing.

---

## What was tried (with every request, status and bytes)

Client key: **P** = harvester `Http.fetch()` (urllib first, curl fallback, `--insecure-hosts`);
**C** = `curl` direct, verification on, no `-k`; **C+L** = `curl -L`.

| # | Cli | Request | Status | Bytes | What it settled |
|---|---|---|---|---|---|
| 1 | P | urllib pre-attempt of #2 (`babel/cgi/ls`, 1970–79 facet) | 403 | — | challenge; fallback needed |
| 2 | P | `https://babel.hathitrust.org/cgi/ls?field1=ocr;q1=%22Wal-Mart%22;a=srchls;lmt=ft;facet=bothPublishDateRange%3A%221970-1979%22` | 200 | 369,495 | **573 reproduced exactly** (`data-prop-total-records="573"`, `"num_found":573`, 100 record blocks, 9 result pages). TLS skipped — see provenance header |
| 3 | P | urllib pre-attempt of #4 | 403 | — | as above |
| 4 | P | `…/cgi/ls?q1=%22Wal-Mart%22;field1=ocr;a=srchls;id=hvd.hl4rdm` | 200 | 393,192 | **the volume restriction was silently DROPPED**: page reports 94,222 records and its own analytics URL is `/ls/srchls?q1="Wal-Mart"&field1=ocr` — no `id` |
| 5 | P | urllib pre-attempt of #6 | 403 | — | as above |
| 6 | P | `…/cgi/ls?q1=%22Wal-Mart%22;field1=ocr;a=srchls;lsid=hvd.hl4rdm` | 200 | 390,290 | same drop, same 94,222. **No "search within this volume" spelling worked** |
| 7 | C | `https://babel.hathitrust.org/cgi/pt?id=hvd.hl4rdm` (volume page) | **403** | 5,303 | body `<title>Just a moment…</title>` — Cloudflare challenge. **Text wall, rung 5 unreachable** |
| 8 | C | `https://catalog.hathitrust.org/api/volumes/brief/htid/hvd.hl4rdm.json` | 200 | 825 | record 102719172; title *Directory of companies filing annual reports with the SEC under the Securities Exchange Act of 1934. Alphabetically and by industry groups*; oclc 236045285; item rightsCode `pd`, usRightsString **Full view**, **enumcron 1971** (the search page had dated it 1970) |
| 9 | C | `…/api/volumes/brief/htid/uc1.32106017378883.json` | 200 | 5,516 | record 007150441, ISSN 0500-3679, OCLC 6614503, LCCN 59061379; a run of `uva.x0019…` holdings, all `pd` / Full view |
| 10 | C | `https://babel.hathitrust.org/cgi/imgsrv/html?id=hvd.hl4rdm&seq=1` (page OCR) | **403** | 66,873 | body `<title>Error - Blocked from HathiTrust</title>`. **The page-text endpoint refuses this machine too** |
| 11 | C | `…/cgi/ls?field1=ocr;q1=%22Wal-Mart%20Stores%22%20Bentonville;a=srchls;lmt=ft;facet=bothPublishDateRange%3A%221970-1979%22` | 200 | 336,304 | **197 records** (page 1 of 2) — the narrow corporate-name + home-town set; composition in Findings A5-05 |
| 12 | C | `federalregister.gov/api/v1/documents.json?conditions[term]="Wal-Mart Stores"…` (unencoded brackets) | no HTTP status | 0 | curl exited: **my URL syntax fault, not a host answer** |
| 13 | C | same, term `"Wal-Mart"` | no HTTP status | 0 | same client fault |
| 14 | C | percent-encoded `…conditions%5Bterm%5D=%22Wal-Mart%20Stores%22&…1962-01-01…1979-12-31…` | 200 | 112 | `{"description":"Documents matching '\"Wal-Mart Stores\"' and published from 01/01/1962 to 12/31/1979","count":0}`. **A 0 that indicts the index**: the FR API's `term` full-text search covers 1994+, so this is NOT a 1962–79 null |
| 15 | C | `…/cgi/ls?…;bib=007150441` (third within-record spelling) | 200 | 399,683 | restriction dropped again; 13,526 records. Confirms trap: **an HT count from a URL whose params were ignored is a count of a different query** |
| 16 | C | `…/cgi/ls?…;facet=authorStr%3A%22United%20States.%20Securities%20and%20Exchange%20Commission%22;facet=bothPublishDateRange%3A%221970-1979%22` | 200 | 8,563 | no `total-records` marker at all — a no-result/error page from **my unverified facet value** (the site's own hrefs carry `authorStr:` with a value shape I had not read off a live page). UNANSWERED, not a null |
| 17 | C | `archive.org/advancedsearch.php?q=title:("statistical bulletin") AND title:("securities and exchange commission")&rows=15` | 200 | 3,706 | **numFound 353**; identifiers are `sim_sec-monthly-statistical-review_<YYYY-MM>_<vol>_<iss>`; **1970 issues present** |
| 18 | C | `…q=collection:(sim_sec-monthly-statistical-review) AND YEAR:[1970 TO 1979]` | 200 | 325 | numFound **0** — my invented collection value; per-param EMPTY only |
| 19 | C | #17 re-run with `rows=400` | 200 | 78,415 | all 353 rows returned; **the 1970s subset is exactly 24 issues: monthly 1970-01…1970-12 (v.29) and 1971-01…1971-12 (v.30), every one `mediatype=texts`. IA's run of this title stops at Dec 1971** |
| 20 | C | `archive.org/download/sim_sec-monthly-statistical-review_1970-11_29_11/…_djvu.txt` | 302 | 0 | redirect not followed (`_fetch_curl` sends no `-L`); `Location: dn760102.eu.archive.org/0/items/…` |
| 21 | C | same for `…_1970-12_29_12` | 302 | 0 | `Location: dn760104…` |
| 22 | C | `https://dn760102.eu.archive.org/0/items/sim_sec-monthly-statistical-review_1970-11_29_11/…_djvu.txt` | 200 | **47,206** | **the whole November 1970 SEC Statistical Bulletin, read** — see A5-03 |
| 23 | C | `https://dn760104.eu.archive.org/0/items/sim_sec-monthly-statistical-review_1970-12_29_12/…_djvu.txt` | **500** | 170 | nginx Internal Server Error — the December 1970 issue was **not** obtained. UNANSWERED |
| 24 | C | `…advancedsearch.php?q=title:("statistical review") AND title:("Securities and Exchange Commission")&rows=300` | 200 | 376 | numFound **0**: IA holds no separate *Monthly statistical review* run for 1972–79 either. Per-param EMPTY (tokenisation caveats apply) |
| 25 | C | `…q=title:("official summary of security transactions") OR title:("securities traded on exchanges") OR title:("companies filing annual reports")&rows=120` | 200 | 6,793 | **numFound 42**: 34× `securitiestraded<YYYY>unit` (annual editions incl. **1961, 1963, 1965, 1970**), 1× `micro_IA41152628_0056` *Official summary of security transactions and holdings* 1981-01-12, **0** items of the "companies filing annual reports" directory → that class is HathiTrust-only |
| 26 | C+L | `archive.org/download/securitiestraded1970unit/securitiestraded1970unit_djvu.txt` | 200 | **941,197** | **the complete SEC register of exchange-traded securities as of 31 December 1970, 153,481 words, read and grepped** — see A5-04 |
| 27 | C | #11 with `;pageNum=2` (records 101–197) | 200 | 336,239 | page 2 composition: *United States civil aircraft register* (FAA) volumes 1971–1978 dominate, plus USPTO trademark indexes and Copyright Office parts — A5-05 |
| 28 | C | `books.google.com/books/feeds/volumes?q=%22Wal-Mart+Stores%22+%22Bentonville%22&maxResults=10` | 200 | 23,849 | 10 volumes, all out of window (2009 biography; 1992/1999 store directories). Confirms A4's finding that the feed cannot be date-scoped |
| 29 | C | `…advancedsearch.php?q=title:("official summary of security transactions") AND YEAR:[1970 TO 1980]&rows=60` | 200 | 363 | numFound **0** — the NYSE *Official Summary* series is on IA only as a 1981 microfilm part. Per-param EMPTY within a stated perimeter |

**Deliberately not attempted** (they would have spent the last request on a route this pass had already
proved dead): any further `/cgi/pt` or `imgsrv` variant; EDGAR full-text; a browser session.

---

## Findings

A5-01 Claim: **The 573-record candidate pool is real and exactly reproducible, and its first page is
what A4 said it was, but larger: of its 100 record blocks, 52 are Securities and Exchange Commission
serials** — 26 × *Statistical bulletin — Securities and Exchange Commission* (1973, 1974, 1975 issues
and half-year bindings), 16 × *Official summary of security transactions and holdings* (1972, 1974,
1975, 1976, 1977, 1978, 1979), 5 × *Directory of companies filing annual reports with the Securities
and Exchange Commission under the Securities Exchange Act of 1934* (hvd.hl4rdm, hvd.hl4rgq,
uc1.32106017378883, uc1.32106017378891, mdp.39015062978278), 3 × *SEC monthly statistical review*
(v.32 1973 ×2, v.33 1974), 1 × *Securities traded on exchanges under the Securities Exchange Act of
1934, 1978* (mdp.39015062978302), 1 × *Official list of section 13(f) securities, 1979NO1*
(osu.32435051816825). The remainder is other government serials (10 NLRB, 7 USITC, 4 Tax Court
reports, 3 CPSC, 2 Federal Register, 3 unattributed "Annual report", 3 EDA, 2 NAS treasurer, 2 LC
bulletin, 2 *Soldiers*, 1 *News digest*, 1 FTC merger report, 1 Army lawyer, 1 standards-testing
index, 1 FEC campaign-expenditures, 1 *American rehabilitation*, 1 DAV convention) and **3 unrelated
environmental impact statements** (ien.35556031059090 Nevada municipal airport 1974;
ien.35556030222962 Loring AFB 1977; ien.35556030138432 Highway 177/18 Manhattan 1976).
Date: 2026-09-25 — Source: request #2 (HTTP 200, 369,495 B) read from the saved body, 0 further
requests — Class: FACT — Conf: High — Conflicts: none. **But this row is about a search index, not
about a company: a record block is a pointer.**

A5-02 Claim: **HathiTrust's page text is unreachable from this machine by every scripted route tested,
and the union catalogue silently discards attempts to search inside a single volume.** `/cgi/pt?id=…`
→ 403 with a Cloudflare challenge body (5,303 B, `<title>Just a moment…</title>`);
`/cgi/imgsrv/html?id=…&seq=1` → 403 with 66,873 B of `<title>Error - Blocked from HathiTrust`; and
three different within-record spellings (`;id=`, `;lsid=`, `;bib=`) each returned HTTP 200 **with the
restriction dropped** — i.e. the same corpus-wide query, whose record counts then read 94,222 and
13,526 instead of a single volume's hits. The catalog brief-record API is the only HathiTrust service
that answered a script unconditionally and with verification on (825 B, 5,516 B).
Date: 2026-09-25 — Source: requests #4/#6/#7/#9/#10/#15 — Class: FACT (route evidence) —
Conf: High — Corroboration: `HARVEST_README.md` §3 ("'Full view' therefore means *a human can open
it*, not *this tool can read it*") — Consequence: **every one of the 52 SEC records in A5-01 is a
LEAD, not a witness, until a human opens it or an OA copy is found elsewhere.**

A5-03 Claim: **The SEC Statistical Bulletin does print company names, but only for a fixed sample of
100 giant NYSE stocks, and the issue nearest the Wal-Mart float contains no Wal-Mart text of any
kind.** The November 1970 issue (v.29 no.11; IA `sim_sec-monthly-statistical-review_1970-11_29_11`;
47,206 B of OCR read whole, TLS verified) opens:
> "…NOVEMBER 1970 STATISTICAL BULLETIN / UNITED STATES SECURITIES AND EXCHANGE COMMISSION /
> Washington, D. C. 20549…"

Its headings are aggregate tables — "NEW SECURITIES OFFERINGS · Estimated Gross Proceeds from New
Securities Offered for Cash in the United States", "SECURITIES REGISTERED UNDER THE SECURITIES ACT OF
1933 · **Total Effective Registrations**", "REGISTERED AND EXEMPTED SECURITIES EXCHANGES", NYSE
round-lot/odd-lot and short-sale tables, AMEX tables. **Exactly one table carries issuer names:**
> "ODD-LOT CUSTOMERS' PURCHASES AND SALES ON THE NEW YORK STOCK EXCHANGE **IN 100 SELECTED COMMON
> STOCKS** … NAME OF STOCK | WEEK ENDED October 2, 1970 | October 9, 1970 | October 16, 1970 |
> October 23, 1970 … | Admiral Corporation 552 | 575 | 746 … | Allied Chemical Corporation 3,827
> 3,956 4,036 | 5,298 | 3,452 | Allis Chalmers Mfg. Co. … | American Airlines, Inc. … | American
> Brands, Inc. … | American Can Company …"

Greps over the whole issue: `Wal-Mart`/`Wal Mart`/`walmart` = **0**, `Walton` = **0**, `Bentonville` =
**0**. Note the data month: **October 1970**, the month this dossier's chronology places the public
float, and a month in which the bulletin could only have named a company whose stock was in its
100-stock NYSE sample. **The class is therefore structurally incapable of supplying a Wal-Mart figure
for 1970, and (given a fixed 100-stock universe) very probably not for later years either.**
Date: 2026-09-25 — Source: request #22, body 47,206 B, read whole and grepped — Class: FACT (presence
of the tables and the zero counts) / INFERENCE (that the later run keeps the same structure — IA's
copy stops at Dec 1971) — Conf: High as read / Medium as extrapolated.

A5-04 Claim — **the pass's strongest single result: the SEC's own complete 1970 issuer register is
silent on the company, and that silence is a page-level, third-party datum.**
*"Securities Traded on Exchanges Under the Securities Exchange Act of 1934, As of December 31, 1970"*
(United States Securities and Exchange Commission; IA `securitiestraded1970unit`; HTTP 200,
**941,197 B / 153,481 words read whole over a TLS-verified channel**). The volume's own title page and
front matter, verbatim:
> "…ECURITIES TRADED ON EXCHAP[J]GES / Under the Securities Exchange Act of 1934 / ^5 of December 31,
> 1970 / United States SECURITIES AND EXCHANGE COMMISSION Washington, D. C. 20549 … ‖ **This
> publication contains the alphabetical list by issuers of all securi¬ ties admitted to trading on
> stock exchanges under the Securities Exchange Act of 1934 except securities exempted under
> Section 3**…"

This is not a sample: it is a **complete enumerating register of exchange-listed issuers**, so its
silence is evidence. Grepped for the whole universe: `Wal-Mart` = **0**, `Wal Mart` = **0**,
`Walton` = **0**, `Bentonville` = **0**, `Rogers, Ark` = **0**. The alphabetical "W" position the
company would occupy is present and legible, which excludes the alternative explanation that the OCR
lost the block: `WALTER E HELLER & CO`, `WALTER E HELLER INTERNATIONAL`, `WALTER K JOHDER? [WALTER K
I DDE G CUMPANY INC (OtL)]`, `WALGREEN COMPANY`, `WALLACE-MURRAY CORP`, `WALTHAM INDUSTRIES CORP`,
`WALWORTH COMPANY`, `WALCO NATIONAL CORP` (OCR variants `WALWCPTH CCMPANY`, `WALTER JIM CORP`).
Date: 2026-09-25 — Source: request #26, 941,197 B — Class: FACT (the counts and the surrounding lines);
INFERENCE (what the absence proves, immediately below) — Conf: High on the text, High on the perimeter
statement, **Medium on any chronological use** — Corroboration: none; this is a single-source document
class and no second copy was fetched — Conflicts: none registered.
**Perimeter of the silence (stated so no one over-reads it):** the register covers *securities admitted
to trading on stock exchanges* only. It does **not** enumerate Securities Act of 1933 registrants,
does **not** enumerate Exchange Act §12(g) registrants that traded over the counter, and expressly
excepts §3(a)-exempted securities. So this document cannot witness OTC registration or any sales
figure; what it witnesses is **exchange listing status as of one date**. Read against the dossier's
own chronology (IPO 1970, NYSE listing 1972 — dates carried elsewhere in this company's files, **not
re-verified in this pass**), the register independently corroborates *non-listing at 31 December 1970*.

A5-05 Claim: **The narrow corporate-name query ranks a different agency's registers above the SEC ones,
and the best positive candidate the pass found is not an SEC document at all.**
`"Wal-Mart Stores" Bentonville`, full view, facet 1970–1979 = **197 records** (2 pages). Page 1's top
hits are NLRB publications (*Court decisions relating to the National Labor Relations Act*, v.26
1973–74, four holdings: uc1.b3659076 / coo.31924054313113 / uc1.b4234380 / mdp.39015086162875;
*Decisions and orders of the NLRB*, v.201 1973: uiug.30112132482461, ien.35559002018582; four
holdings of the *Classified index of decisions of the regional directors*), *Federal register* volumes
1977–1979, and *SEC news digest* 1972/1973/1977. **Page 2 is dominated by a class the 573-record set
does not surface at all: the FAA *United States civil aircraft register*, editions 1971–1978**
(mdp.39015023915757, osu.32435061966578, uiug.30112084299723… coo.31924096396092,
uiug.30112120071185, 21+ holdings), whose entire format is *owner name + city + state*.
Date: 2026-09-25 — Source: requests #11 and #27, bodies read locally — Class: FACT (the counts,
titles, dates) / **UNKNOWN (whether any of them names this company — no text reachable, A5-02)** —
Conf: High as to composition, UNKNOWN as to content — Note: the exact-phrase-plus-home-town
co-occurrence in a register-of-owners is a far stronger prior than the bare hyphenated phrase that
produced the 573, and it points at the Department of Transportation, not the SEC.

A5-06 Claim: **The reachable portion of the SEC statistical run is bounded, and it stops before the
years that matched.** Internet Archive holds this title as 353 items with `_djvu.txt` layers, of which
**the 1970s subset is 24 monthly issues, January 1970 – December 1971 (v.29 and v.30) only**. Every
HathiTrust *Statistical bulletin* record that matched "Wal-Mart" in A5-01 is a 1973/1974/1975 volume —
**outside IA's copy** — and three attempts to find the later run on IA (by the alternative title
*Monthly statistical review*, and for the NYSE *Official summary of security transactions and
holdings* within 1970–1980) each returned HTTP 200 with **numFound 0**.
Date: 2026-09-25 — Source: requests #17, #19, #24, #25, #29 — Class: FACT (the coverage boundary) —
Conf: High for the read range; **the 0s are per-parameter nulls on an index whose tokenisation this
project has already been burned by** (`HARVEST_README.md` §5: `title:("wal-mart")` does not match
"Walmart Stores"), so they bound *my query*, not the corpus — Conflicts: none.

A5-07 Claim: **The Federal Register route, which would have been the cheapest way to read a government
page naming the company, is closed for this window by its own index design.**
`federalregister.gov/api/v1/documents.json?conditions[term]="Wal-Mart Stores"`, publication date
1962-01-01…1979-12-31 → HTTP 200, 112 B, `count: 0` with the query echoed back verbatim. The API's
`term` parameter searches a full-text index that covers **1994 forward**; a 0 across 1962–1979 is an
index limitation, **not** a statement that the Federal Register contains no Wal-Mart text in the
1970s — which A5-05's result page makes look unlikely (2 *Federal register* volumes matched the
narrow phrase).
Date: 2026-09-25 — Source: request #14 (after two requests of my own making that never got a status) —
Class: FACT (the response) / **UNANSWERED (the corpus question)** — Conf: High as to the reply —
Follow-up owner: govinfo's `FH`/`FR` granoida search or the FR's own `date`-browsable pre-1994 text,
neither queried here.

---

## Verdict on the hypothesis

**PARTLY CONFIRMED — and only at the lowest of the three rungs.** Stating the rungs explicitly:

| Rung | Claim | Result |
|---|---|---|
| 1. The family exists, is government-published, is contemporaneous, and covers the window | *Real, and larger than hoped*: 52 of the first 100 candidates are SEC serials (A5-01), incl. three complete issuer/list registers dated 1970, 1972, 1978 and a *Directory of companies filing annual reports* editions 1970–1972 | **CONFIRMED** (catalog API + OCR-field-restricted search + one volume read whole) |
| 2. Its text is reachable to this project | Reachable for **1948–Dec 1971 monthly issues via Internet Archive** (A5-03 read) and **for one annual register edition, the 31 Dec 1970 one, 941 KB read whole** (A5-04). **Not reachable** for the 1972–1979 volumes that actually generated the hits (HathiTrust text wall, A5-02; IA copy of the later run not found, A5-06) | **CONFIRMED for 1970–71; REFUTED-as-reachable for 1972–79** |
| 3. A volume of it names the company | **Not found.** Every text read prints zero occurrences of `Wal-Mart`, `Wal Mart` or `Walton`; the one issue nearest the float names companies only in a fixed 100-stock NYSE odd-lot table the company could not be in (A5-03); the one complete register read is a *register of exchange-listed issuers* at 31 Dec 1970 and Wal-Mart is absent from it while its "W" neighbours are legible (A5-04) | **NOT CONFIRMED — and for the read range, refuted on the page, not on a count** |

**Earliest independent document that actually names the company: none was reached by this pass.** The
hypothesis that the SEC Statistical Bulletin / Statistical Report lineage would supply the first
third-party document naming Wal-Mart inside Stage 1 is, on the evidence now read, **not supported for
any part of the window that could be opened, and closed on its merits for 1970–71.**

Three things are *not* refuted, and must not be reported as such:
1. **The 1972–1979 SEC volumes.** A *Securities traded on exchanges* edition dated 1978 and a
   1979NO1 *Official list of section 13(f) securities* both sit in the hit set; those classes **do**
   enumerate issuers, and after the NYSE float the company should be in them. They are
   **UNREAD-BEHIND-A-WALL (UNANSWERED)**, not empty.
2. **The Department of Transportation line** (A5-05): a 1971–1978 run of FAA civil aircraft registers
   ranked in a `"Wal-Mart Stores" Bentonville` full-view search is the most probable positive-naming
   document class this project has ever located for this company — and it is a *different agency*, so
   it is not merely the registrant's filing reprinted. Unread.
3. **The NLRB line** (A5-05): four holdings of *Court decisions relating to the National Labor
   Relations Act* v.26 (1973–74) and *Decisions and orders* v.201 (1973) rank at the very top of the
   narrow name+town query. A labor-board or enforcement-court proceeding naming "Wal-Mart Stores, Inc."
   of Bentonville would be a *third-party adjudication* — the purest lineage class in §14.6, since
   nothing in it is registrant-supplied. Unread.

---

## What this changes for the depth verdict

**The independent-lineage count for the financial record stays at 1.** Nothing reached in this pass
names the company, let alone carries a figure. A3 §7.2(c)'s sentence — "no number of further years of
Wal-Mart's own annual reports can move this verdict; only a different publisher can" — still stands,
and this pass has now read two different publishers' documents without finding the name in either.

What does change, stated conservatively:

1. **A second, genuinely independent *class* is now documented as existing and as partly readable**
   (rung 1 and half of rung 2). That converts the largest hole in §14 rule 6's four-family sweep from
   "HathiTrust: blocked/UNANSWERED" into "HathiTrust: search open, catalog open, **page text closed to
   scripts** — and the same corpus partly open on Internet Archive". That is a *route* change, not a
   verdict change.
2. **One fact about the company now has independent corroboration where it had none.** The SEC's
   complete 31 December 1970 register of exchange-traded issuers omits Wal-Mart while printing its
   alphabetical neighbours (A5-04). Under §14.6 that is **evidence of *listing status*, not of sales**
   — it does not corroborate a single dollar figure, store count or growth rate, and it must not be
   entered as a second lineage for any number. What it does establish independently of the registrant
   and its auditor is the negative proposition "not exchange-listed as of 31 Dec 1970", which is the
   kind of chronology claim this dossier otherwise takes only from the company's own telling. If A3's
   Stage-1 chronology asserts the 1970 float and a later exchange listing, this register is now its
   one third-party witness — **for the absence half of that sentence only**.
3. **A whole family of expected evidence is closed out with a reason, not a shrug.** The SEC Statistical
   Bulletin cannot supply Wal-Mart figures for the read range, because its only issuer-naming table is
   a fixed 100-stock NYSE odd-lot sample. A future pass should not spend requests hoping that a
   different month of 1970–71 yields a Wal-Mart line; the structure, not the luck, is against it.
4. **The priority order for the next pass is now determined by content rather than by guesswork**:
   (i) open the NLRB v.26 / NLRB Decisions and Orders v.201 hits and the FAA *civil aircraft register*
   editions 1971–1978 — by browser, or on IA, or at govinfo, since HathiTrust's text is scripted-dead;
   (ii) the 1978 *Securities traded on exchanges* and the 1979NO1 *Official list of §13(f) securities*
   for a positive *listing* naming after October 1972; (iii) the *Directory of companies filing annual
   reports with the SEC* editions 1970/1971/1972 (full view, `pd`, but IA holds none of them, so the
   browser is the route) for a positive *registration* naming.
5. **Nothing here licenses relaxing the provisional/proven distinction elsewhere.** The 573 and 197
   counts are index properties of a union catalogue; the 3 environmental impact statements in the hit
   set, and the 94,222/13,526 phantom counts produced when HathiTrust drops a restriction parameter
   (A5-02), show how easily this pool generates confident nonsense.

---

## Data gaps

**EMPTY — searched, the record is silent, within the stated perimeter (never a corpus null):**
- E-A5/1. The SEC Statistical Bulletin **November 1970 issue** (v.29 no.11) contains **0** occurrences
  of Wal-Mart / Wal Mart / Walton / Bentonville across its whole 47,206-byte text layer. Perimeter:
  that issue only; the 1972–79 issues were not reachable (see U-A5/1).
- E-A5/2. The SEC's complete **alphabetical register of securities traded on exchanges as of
  31 December 1970** (941,197 B, 153,481 words) contains **0** occurrences of the company's name,
  its founder's surname, or either Arkansas town, while printing WALGREEN / WALWORTH / WALTHAM /
  WALLACE-MURRAY / WALCO. Perimeter: exchange-listed securities under the '34 Act; **not** Securities
  Act registrants, **not** §12(g)/OTC registrants, **not** §3(a)-exempted securities.
- E-A5/3. IA holds **no** 1972–1979 issues of this bulletin under either title (353 items total,
  1970s subset = 24, January 1970 – December 1971), and **no** NYSE *Official summary of security
  transactions and holdings* within YEAR 1970–1980 (the single item found is 1981-01-12).
  Perimeter: IA's metadata index and my title spellings (see HARVEST_README §5 on hyphen/quote
  tokenisation), so bound-copy-under-a-different-title is not excluded.
- E-A5/4. **No** "companies filing annual reports with the SEC" directory exists on IA at all
  (0 of 42 rows in the three-class query) — that class is HathiTrust-only, hence text-blocked.
- E-A5/5. Google Books' keyless feed for `"Wal-Mart Stores" "Bentonville"` returned **10 volumes, none
  in window** (2009, 1999, 1992 …). Perimeter: a relevance-capped top-10 from an endpoint that
  **cannot be date-scoped** (`HARVEST_README.md` trap 1) — therefore a *reach* result, not an absence.

**UNANSWERED — a route exists, it was reached, it refused an application-layer reply:**
- U-A5/1. **HathiTrust full-view page text**, for all 52 SEC records of A5-01 and for the NLRB/FAA
  hits of A5-05: `/cgi/pt` → 403 challenge (5,303 B); `/cgi/imgsrv/html` → 403 "Blocked from
  HathiTrust" (66,873 B). This is the pass's dominant gap: the *documents are identified, dated and
  rights-proven, and their pages cannot be opened by a script.*
- U-A5/2. **The December 1970 issue** (v.29 no.12) — IA content server returned **HTTP 500** (nginx,
  170 B), one attempt. Retryable at 1 request.
- U-A5/3. **HathiTrust author-facet restriction** — `facet=authorStr:"United States. Securities and
  Exchange Commission"` answered 200 with 8,563 B and **no count field**; the value shape was copied
  from a record label, not from a live facet href. My parameter, not the corpus.
- U-A5/4. **Federal Register 1962–1979** — the API's `term` index is 1994+ (A5-07), so its `count: 0`
  is not a null. govinfo / FR date-browsable pre-1994 text never queried.
- U-A5/5. **Chronicling America** (all paths, incl. `/robots.txt`) remains 403 as their policy —
  unchanged by this pass, still the largest single hole for 1945–1962 Arkansas print.

**UNTRIED — not attempted, recorded so the next pass neither re-burns nor mistakes it for a null:**
- X-A5/1. **Read the NLRB and FAA hits** (A5-05) — 8 NLRB holdings + 21 FAA aircraft-register
  editions, full view, `pd`, the two classes most likely to name the company positively. Not opened:
  they need a browser session or a govinfo/IA equivalent, and no request of this pass's remaining
  budget could reach their text.
- X-A5/2. **The 1978 *Securities traded on exchanges* and the 1979NO1 *Official list of §13(f)
  securities*** — the same complete-register genre that gave a clean negative for 1970, at a date when
  the company should appear. HathiTrust-only as far as tested; IA not searched by those exact series
  terms for a 1978/1979 binding.
- X-A5/3. **EDGAR full-text and the SEC Reference Room** for the registration statements themselves
  (never queried by any harvest pass of this project).
- X-A5/4. **The *Directory of companies filing annual reports* 1970/1971/1972 volumes**, whose rights
  are proven `pd`/Full view (A5-02's catalog calls) and whose genre is *exactly* a name register.
- X-A5/5. **A keyed Google Books v1 `dateRestrict=1970-1979`** (the only date-honouring Books route).
- X-A5/6. Whether the bulletin's 100-selected-stocks table changed composition after 1972 (the run I
  could read stops at Dec 1971) — a browser pass over any 1973–1975 issue settles it in one page.

---

## Outbound corrections

1. **To `A4_independent_periodicals.md` §Host-family re-probe item 2, and to `S0137`/`U-A4/9`.** The
   page-1 composition was "USITC publications … and one unrelated Nevada EIS" (A4) — correct but
   understated. It is: 26 SEC Statistical Bulletins, 16 SEC/NYSE official summaries, 5 SEC company
   directories, 3 SEC monthly statistical reviews, 1 SEC *Securities traded on exchanges* 1978,
   1 SEC 13(f) list, and 3 unrelated environmental impact statements, among 48 other government
   serials. **A4's caution in re-probe item 3 is VINDICATED, not weakened**, by the pass that tested
   it: the SEC line republishes registrant data, and the two SEC documents actually read name no one.
2. **The sentence "no third-party document has yet named the company in-window" stays TRUE and must
   not be softened** by anyone reading "573 candidates + SEC serials found". This pass found a
   publisher, not a naming.
3. **`HARVEST_README.md` §3 / trap 2 needs one new fact**: HathiTrust's *search* answers this machine
   through curl, and its *catalog* API answers verified, but **both text routes (`/cgi/pt`,
   `/cgi/imgsrv/html`) refuse even the working client** — so "HathiTrust is now open" is true of
   rungs 2–3 and false of rung 5, and the productive pattern stays *HT search → htid → rights via
   catalog API → text via IA copy or browser*. Additionally: **`/cgi/ls` silently drops unknown
   restriction parameters (`id=`, `lsid=`, `bib=`) and returns a corpus-wide count** (94,222 and
   13,526 in this pass) — an HT count read off such a URL indicts the request, not the corpus. This
   is the same failure family as `facet=DateRange:"1960-1969"`; a CONTROL task should be added.
4. **A3 §7.2(c) (depth verdict)** may record: the SEC statistical lineage has now been *tested on text*
   for 1970–71 and yields no company naming, but it also may not be recorded as closed for 1972–79.
   The independent-lineage count is **UNCHANGED at 1**.
5. **`MASTER_RESEARCH_LOG.md`** should record A5 as: hypothesis PARTLY CONFIRMED (rungs 1 and
   partial 2; rung 3 negative on every text read), 29/30 requests, one substantive new third-party
   document class for the *listing* question, and the next named-witness attempt re-ranked from
   "SEC statistical volumes" to "NLRB decisions and FAA aircraft registers, then the 1978/1979 SEC
   issuer registers".
6. **Date-field caution for the merge**: IA's `date` for `securitiestraded1970unit` is `1936-01-01`
   (series start) while the volume's own title page says **As of December 31, 1970**; and HathiTrust's
   search page dated `hvd.hl4rdm` "1970" while its catalog `enumcron` says **1971**. **In-window
   dating for this class must come from the printed title page, not from either index.**

---

## CSV append rows

Schemas follow `company_001_amazon/*.csv`. `source_id` values **S0139–S0141 are proposed**; the merge
agent owns renumbering against the live register. No CSV file was written by this pass.

### `sources.csv` — header
```
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
```
### `sources.csv` — rows
```
S0139,1,"Securities and Exchange Commission's complete alphabetical register of issuers whose securities were admitted to trading on stock exchanges contains no entry for Wal-Mart Stores as of 31 December 1970: 0 occurrences of 'Wal-Mart'/'Wal Mart'/'Walton'/'Bentonville' in 153,481 words of text, while the same alphabetical position prints WALGREEN COMPANY, WALWORTH COMPANY, WALTHAM INDUSTRIES CORP, WALLACE-MURRAY CORP and WALCO NATIONAL CORP","Securities traded on exchanges under the Securities Exchange Act of 1934, as of December 31, 1970","United States Securities and Exchange Commission (Washington, D.C. 20549)","government publication (complete issuer register)","primary (as to listing status only)","1970-12-31","1971","2026-09-25","https://archive.org/download/securitiestraded1970unit/securitiestraded1970unit_djvu.txt","Internet Archive item securitiestraded1970unit; raw 941,197-byte OCR body held outside the repository at $TEMP/a5_sec_lineage_20260926/internet_archive/117f58117ad37959.txt (sidecar sha1 117f58117ad37959, HTTP 200, tls_verify=on (curl default trust store), client=curl -L)",1,FACT,High,"FULLY INDEPENDENT of the registrant and its auditor as to exchange-listing status: the SEC's own statutory register of exchange-traded issuers, published by a third party, contemporaneous, and complete rather than a sample. It carries NO company figure and is NOT a second lineage for any number. Perimeter of the silence: exchange-listed securities only — it does not enumerate Securities Act of 1933 registrants, does not enumerate Exchange Act s.12(g)/over-the-counter registrants, and excepts s.3(a)-exempted securities, so it cannot witness OTC registration at all.","Front matter, verbatim OCR: 'ECURITIES TRADED ON EXCHAP[J]GES / Under the Securities Exchange Act of 1934 / ^5 of December 31, 1970 / United States SECURITIES AND EXCHANGE COMMISSION Washington, D. C. 20549 … This publication contains the alphabetical list by issuers of all securi-ties admitted to trading on stock exchanges under the Securities Exchange Act of 1934 except securities exempted under Section 3'","The volume's own title page is the dating authority: IA's metadata 'date' field reads 1936-01-01 (series start) and must not be used. Single-source class, no second copy fetched. Absence of the name is the datum; absence of OTC registration is NOT."
S0140,1,"The SEC Statistical Bulletin of November 1970 (v.29 no.11, data month October 1970 — the month of the company's public float) contains no mention of the company, and the publication's only issuer-naming table is a fixed sample of 100 selected NYSE common stocks in which an unlisted Arkansas retailer could not appear","Statistical bulletin — Securities and Exchange Commission, v.29 no.11 (November 1970)","United States Securities and Exchange Commission","government publication (monthly statistical series)","primary (as to the publication's structure)","1970-11","1970-11","2026-09-25","https://dn760102.eu.archive.org/0/items/sim_sec-monthly-statistical-review_1970-11_29_11/sim_sec-monthly-statistical-review_1970-11_29_11_djvu.txt","Internet Archive item sim_sec-monthly-statistical-review_1970-11_29_11; raw 47,206-byte OCR body outside the repository at $TEMP/a5_sec_lineage_20260926/internet_archive/b0a2d556246d0b65.txt (HTTP 200, tls verified by curl)",1,FACT,High,"Independent publisher, and the lineage test in A4 re-probe item 3 is SATISFIED AND THEN OVERTAKEN: this bulletin republishes registrant filings as aggregates ('SECURITIES REGISTERED UNDER THE SECURITIES ACT OF 1933 - Total Effective Registrations'), so even a positive naming here would have been evidence of registration, not of sales. Greps: Wal-Mart 0, Wal Mart 0, Walton 0, Bentonville 0 across the whole issue.","Masthead: 'NOVEMBER 1970 STATISTICAL BULLETIN UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D. C. 20549'. The single name-bearing table: 'ODD-LOT CUSTOMERS' PURCHASES AND SALES ON THE NEW YORK STOCK EXCHANGE IN 100 SELECTED COMMON STOCKS … NAME OF STOCK | WEEK ENDED October 2, 1970 | October 9, 1970 | October 16, 1970 | October 23, 1970 … | Admiral Corporation 552 | 575 | 746 … | Allied Chemical Corporation 3,827 3,956 4,036 | 5,298 | 3,452 | Allis Chalmers Mfg. Co. … | American Airlines, Inc. …'","Bounds the family for 1970-71 only. IA's copy of this title ends December 1971, so the 1973-1975 bulletin volumes that produced the 573-hit pool remain unread (HathiTrust text walled). Do not read this row as closing the SEC line for 1972-79."
S0141,1,"Route-state record: HathiTrust's search and catalog API are reachable from this machine, but its page text is not; consequently the 52 Securities and Exchange Commission records in the 1970-1979 'Wal-Mart' result pool are identified, dated and rights-proven and still cannot be read by a script","HathiTrust full-view search and catalog brief-record API responses, 2026-09-25 (A5 pass)","HathiTrust / University of Illinois, Harvard, UC, UVA depositors (union catalogue); probe by THE FOUNDER'S PLAYBOOK","route probe (search index and catalogue metadata)","secondary","2026-09-25","2026-09-25","2026-09-25","https://babel.hathitrust.org/cgi/ls?field1=ocr;q1=%22Wal-Mart%22;a=srchls;lmt=ft;facet=bothPublishDateRange%3A%221970-1979%22","Bodies outside the repository at $TEMP/a5_sec_lineage_20260926/{hathitrust,internet_archive,google_books}/ with 23 sidecars. NOTE the skipped-verification channel: the 573-count page (369,495 B) was fetched through the harvester with --insecure-hosts babel.hathitrust.org and its sidecar records tls_verify='skipped'; every other response was fetched by curl with verification ON, and both long texts relied on in this file are in that second class",n/a,FACT,High,"A different HOST family, not a different lineage of a publisher. Page-1 composition of the 573 pool, counted from the saved body: 26 SEC Statistical bulletins, 16 Official summary of security transactions and holdings, 5 Directory of companies filing annual reports with the SEC, 3 SEC monthly statistical review, 1 'Securities traded on exchanges … 1978', 1 'Official list of section 13(f) securities 1979NO1' = 52 SEC records of 100, plus 10 NLRB, 7 USITC, 4 Tax Court, 3 CPSC, 2 Federal Register, 3 EDA, 3 unattributed 'Annual report', 3 environmental impact statements (Nevada municipal airport 1974; Loring AFB 1977; Highway 177/18 Manhattan 1976) and 24 other government serials","Text wall established with the bytes: /cgi/pt?id=hvd.hl4rdm -> HTTP 403, 5,303 B, body <title>Just a moment…</title>; /cgi/imgsrv/html?id=hvd.hl4rdm&seq=1 -> HTTP 403, 66,873 B, <title>Error - Blocked from HathiTrust</title>. Catalog API unchallenged: hvd.hl4rdm -> record 102719172, rightsCode pd, usRightsString 'Full view', enumcron 1971 (HathiTrust's own search page had dated it 1970)","Registered so no future pass mistakes the re-opened door for evidence walked through it. Also records a trap: /cgi/ls DROPS unknown restriction parameters (id=, lsid=, bib=) and returns a corpus-wide count - 94,222 and 13,526 in this pass - so a count off such a URL indicts the request, not the corpus."
```

### `quantitative.csv` — header
```
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
```
### `quantitative.csv` — rows
```
Walmart,stage1,1970-12-31,"OCCURRENCES of 'Wal-Mart' / 'Wal Mart' / 'Walton' / 'Bentonville' in the SEC's complete alphabetical register of exchange-traded issuers as of 31 Dec 1970 (0 / 153,481 words)",0,occurrences,"S0139","1971",FACT,High,"0 matches / 153,481 words / 941,197 bytes of OCR text read whole; the same W-block legibly prints WALGREEN, WALWORTH, WALTHAM, WALLACE-MURRAY, WALCO, so OCR loss of the block is excluded","A DENOMINATED NEGATIVE, not a company metric: this register enumerates exchange-listed issuers only, so the 0 witnesses the ABSENCE OF EXCHANGE LISTING at that date and nothing about sales, stores or registration under the Securities Act. Independent of the registrant and its auditor; does NOT move the independent-lineage count."
Walmart,stage1,1970-11,"OCCURRENCES of the company's name in the SEC Statistical Bulletin issue nearest its public float (data month October 1970)",0,occurrences,"S0140","1970-11",FACT,High,"0 matches across 47,206 bytes / whole issue read; the issue's only issuer-naming table is a fixed sample of '100 SELECTED COMMON STOCKS' on the NYSE","Structural, not lucky: an OTC retailer could not appear in this publication's naming table. Closes the Statistical-Bulletin line for 1970-71 (IA's copy stops Dec 1971); the 1973-75 volumes that produced the hit pool remain UNREAD (U-A5/1). Independent-lineage count UNCHANGED at 1."
Walmart,stage1,1970-1979,"ROUTE-STATE (not a company metric) — Securities and Exchange Commission records among the first 100 of the 573 full-view candidates matching 'Wal-Mart' in the 1970-1979 decade facet",52,records-of-100,"S0141","2026-09-25",FACT,High,"Counted from the saved result body: 26 Statistical bulletins + 16 Official summaries + 5 company directories + 3 monthly statistical reviews + 1 'Securities traded on exchanges 1978' + 1 'Official list of s.13(f) securities 1979NO1' = 52","A composition count of a search index, not a naming. Of the 52, the text layer of NONE has been reached; two SEC documents of the window were read from Internet Archive instead and neither names the company (S0139, S0140)."
```

### `timeline.csv` — header
```
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
```
### `timeline.csv` — rows
```
Walmart,stage1,1970-12-31,"The SEC's published alphabetical register of all issuers whose securities were admitted to trading on stock exchanges under the Securities Exchange Act of 1934, as of this date, contains no Wal-Mart entry (while printing WALGREEN, WALWORTH, WALTHAM, WALLACE-MURRAY and WALCO in the same block): independent corroboration that the company's shares were NOT exchange-listed at the end of its float year","United States Securities and Exchange Commission; Wal-Mart Stores, Inc. (absent)","Washington, D.C.; Bentonville, Arkansas",S0139,INFERENCE,Medium,none,"The register's own front matter states the universe, so the silence is informative rather than a sampling artefact. INFERENTIAL because the datum is an absence and because the IPO/listing dates it corroborates were NOT re-verified in this pass - they are taken from this dossier's own chronology. Perimeter: exchange listing only; says nothing about Securities Act or OTC status. This row does not create a second lineage for any figure."
Walmart,stage1,2026-09-25,"Research-state event, not a company event: the SEC statistical lineage was tested on page text for the first time. Two SEC documents were read whole (47,206 B and 941,197 B), neither names the company, and HathiTrust's text layer proved script-unreachable (/cgi/pt and /cgi/imgsrv/html both 403), so the 52 SEC records in the 1970-79 hit pool stay UNANSWERED","THE FOUNDER'S PLAYBOOK A5 pass; HathiTrust; Internet Archive",n/a,S0141,LEAD,High,none,"Registered because it converts the largest §14 rule 6 hole from 'host blocked' to 'host open, text closed', and re-ranks the next attempt at the Department of Transportation (FAA civil aircraft register 1971-78) and the National Labor Relations Board (Court decisions v.26 1973-74; Decisions and orders v.201 1973) hits, which the narrow name-plus-home-town query ranks above the SEC ones. Independent-lineage count stays 1."
```

### `conflicts.csv` — header
```
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
```
### `conflicts.csv` — rows
```
Walmart,stage1,U-A5/1,A5 §Verdict; §What this changes 3,"The SEC statistical lineage would supply the first government-published, third-party, contemporaneous record naming the company (inference from the 573-record 1970-79 pool whose first page is 52 SEC serials)","A4 §Host-family re-probe items 2-3; S0137 re-walked (S0141)","2026-09-25","The two SEC documents of that family whose text could actually be read name no one: the November 1970 Statistical Bulletin has 0 occurrences and its only naming table is a fixed 100-stock NYSE sample, and the SEC's complete 31 Dec 1970 issuer register has 0 occurrences in 153,481 words","S0140; S0139","1971; 1970-11","A count from a search index measured which volumes a bot ranked, not which volumes print a name; the naming structure of the bulletin family (fixed sample, aggregate registration tables) and the coverage boundary of the readable copy (IA stops Dec 1971) were both unknown when the inference was made","The two read documents are Tier-1, TLS-verified, complete texts read whole; the inference they contradict rested on a hit count whose text was never opened","The hypothesis is PARTLY CONFIRMED only: the family exists and is partly readable, and for 1970-71 it is closed on its merits. It is NOT closed for 1972-79, where the hits actually came from and where two complete-issuer registers (1978, 1979NO1) sit unopened behind a script-level text wall","Whether any 1972-1979 SEC volume prints 'Wal-Mart Stores' - UNKNOWN, no text reachable (U-A5/1); and whether the NLRB v.26 / FAA aircraft-register hits name the company - UNKNOWN (X-A5/1)",High on the two reads; UNKNOWN on the unread 1972-79 half
```

---

*End A5. Files touched: this one. Requests: 29 of 30. Nothing deleted, nothing tidied, no register or
CSV written.*
