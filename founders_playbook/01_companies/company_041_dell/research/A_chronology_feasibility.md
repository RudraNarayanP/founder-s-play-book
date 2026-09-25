# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:41:19Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: WRITTEN 2026-09-26

**Tier call: T3 register as §15.2 is literally measured — with one named test gating promotion to T2, and T1 structurally unreachable for Stage 1.**

The §15.2 test is "how many of the five corpus families return **in-window** Tier-1 text". For
Dell's founding window (1984 – mid-1988) the answer measured on this pass is **one**: digitised
periodicals. Families a (filings) and b (web archives) do not merely fail to have been searched —
they are **provably floored after the window**, from bytes on disk (`sources/_index/`,
`sources/_index_cik0000826083/sources/_index/`, Wayback CDX). Family d (corporate print) was
queried four explicit ways before any "paper-only" wording appears in this file — the Walmart
misgrading rule — and returned a near-null on the routes tested, with the two routes that decided
Walmart (HathiTrust, Google Books) left genuinely UNTRIED. Family e (documentary/auction) was
**never touched by any tool this run** and is reported as UNTRIED, not null.

| family | in-window Tier-1 text? | what it actually returns for 1984–1988 |
|---|---|---|
| a filings (EDGAR) | **NO** — floor 1994-02-11, proven from the full-history index of both CIKs, zero UNANSWERED slices | Tier-1 *retrospective* statements about the window (1994 10-K, filed 1994-04-01) + the named paper registration statements 33-21823 (1988-05-12) and 33-38991 (amended to 1991-03-27) |
| b web archives | **NO** — earliest `dell.com` capture 1996-12-21 (CDX, HTTP 200) | nothing before the window is reachable; §14 rule 6's mid-1990s floor confirmed, not assumed |
| c periodicals | **YES** — 2 dated in-window Tier-1 primary artifacts held as bytes | BYTE Apr 1987 "PC's Limited" full-page ad (1,769,686 B held, 21 in-page hits); BYTE Oct 1988 "Dell Computer Corporation" ad (1,650,019 B held, 5 hits); 2 further issues = clean issue-level nulls |
| d corporate print | **NOT ESTABLISHED** — queried, near-null on IA routes | `(dell) AND collection:(annualreports)` numFound **0**; the 550 `title:("dell computer")` items are post-1995 product manuals (current-state, §5-inadmissible as early state) |
| e documentary | **UNTRIED** | no request sent by any tool this pass; README lists family 4 as unqueried, no API verified |

**Implied agent-run budget: 3–4 runs (T3).** Deliverable shape: short evidence-bound narrative +
full `sources.csv`, `conflicts.csv`, `data_gaps.csv` + the UNTRIED list; §K (money), §N (decisions)
and §U (conflicts) still mandatory at T3, and at Dell they are where the honest emptiness lives:
**there is no held Tier-1 figure of any kind for 1984–1988** — not capital, not revenue, not head-
count, not the $1,000. §K must be written as UNKNOWN with provenance, not filled from memoir.

**Promotion gate (the one thing that can change this verdict).** A second family must return in-
window Tier-1 text. The single highest-yield untried test is the **printed Dell Computer
Corporation annual report / proxy run FY1989–FY1993 and the 1988 prospectus, searched in HathiTrust
and Google Books** — the class of route that flipped Walmart from forensic-core to T1/T2. If a
bounded pass (≤6 requests) lands any in-window corporate-print text, Dell is **T2 core (6–9 runs)**
and §A–§U is evidence-bound rather than register-shaped. If it lands nothing, T3 stands and the
label is now supported by a tested null rather than an assumption. T1 (≥3 families) cannot be
reached for Stage 1 under any outcome, because a and b are floored by the filing regime and the
medium, not by our effort.

**The two traps the brief named are both settled, not inherited.** (1) *Founding and IPO predate
EDGAR's phase-in*: confirmed from the full-history index of the legacy registrant — **earliest
filing of any kind 1994-02-11 (SC 13G/A); earliest 10-K 1994-04-01 for FY ended 1994-01-30; no S-1
appears among 1,851 enumerated filings**, and neither index reports an UNANSWERED slice, so this is
a documented null and not a fetch failure. The 1988 S-1 exists — the 1994 10-K names it by
registration number and filing date — but it is a paper document. (2) *The modern registrant is a
merger shell*: CIK **1571996 = Dell Technologies Inc.**, whose own enumerated history begins
2013-07-24, whose first registration-type filings are the EMC-merger `425` (2015-10-13) and `S-4`
(2015-12-14), and whose first 10-Q primary document is literally named `denaliq1fy1710q.htm`
(Denali Holding, the acquisition vehicle). The founding entity's history lives at a **different
CIK: 0000826083 (name carried: "DELL INC"; efts display names "DELL COMPUTER CORP" 2001-2003,
"DELL INC" 2004+)**. Any statement that "Dell Technologies was founded in 1984" is a **cross-CIK
assertion** and must cite 826083, not the ranked registrant.

**What is genuinely recoverable for Stage 1, and what is not.** Recoverable: the company's own
contemporaneous self-description of the direct-sale model, its guarantee, its price/speed ladder
and its channel, from in-window Tier-1 advertisements (family c), plus the corporate-structure
skeleton from Tier-1 retrospective filing text (family a) — dates of Texas incorporation, the
October 1987 Delaware reorganisation, the existence and filing dates of the two S-1s, and the fact
that the founder's own employment agreement runs to **1984-05-03 with "a predecessor of Dell
Computer Corporation"**. Not recoverable from anything held: the founding capital, the name-change
document itself, the IPO pricing, revenue or head-count 1984–1988, and Michael Dell's pre-1984
activity. **Founder pre-history stays at UNKNOWN, enumerated in §Boundaries, not deleted.**

**Lineage warning for the fleet (single-source risk, §3).** The circulating founding story — $1,000
of capital, a University of Texas dormitory, telephone-order assembly — appears **nowhere in any
Tier-1 document held by this probe**: zero occurrences of "PC's Limited", of any capital figure,
and of any dormitory account in the 237 KB FY1994 10-K, and the phrase "PC's Limited" returns only
**8 hits across all of EDGAR full text (floor 2001), none of them Dell's**. Wherever the fleet finds
the $1,000, it will almost certainly be the company's own retrospective (its prospectus/memoir/PR)
reprinted: **one source, however many places reprint it**, and it must be recorded at the confidence
a single self-reported retrospective supports, with `independence_note` naming the lineage.

## Family a filings

STATUS: WRITTEN 2026-09-26

Two registrants, enumerated completely, both by `tools/sec_intake.py index` (no UNANSWERED slices in
either `_INDEX.md` — so every zero below is a null, not a failed fetch).

**(a1) The ranked registrant — CIK 0001571996 "Dell Technologies Inc." (ticker DELL).**
`sources/_index/_INDEX.md`, 1,951 filings. **Earliest form by date: DFAN14A 2013-07-24**
(accession 0001193125-13-300601), then `425` 2015-10-13, `S-4` 2015-12-14, `UPLOAD` 2016-01-14,
`8-K` 2016-06-09, first `10-Q` 2016-06-10 (primary document `denaliq1fy1710q.htm`), first `10-K`
**2017-03-31** (`delltechnologiesfy1710k.htm`). **Zero filings dated 1984-01-01 → 1996-12-31.**
This is the EMC-merger vehicle carrying the name, not the 1984 founder: the `denali…` filename and
the 2015 `425`/`S-4` pair are the provenance of that statement, and they are bytes on disk rather
than an inference from the press.

**(a2) The founding-lineage registrant — CIK 0000826083, name carried in the submissions header:
"DELL INC".** `sources/_index_cik0000826083/sources/_index/_INDEX.md`, 1,851 filings.
**Earliest filing of any form: SC 13G/A, 1994-02-11** (0000748054-94-000017). **Earliest 10-K:
1994-04-01** (0000950134-94-000347, FY ending 1994-01-30). Then 10-Q 1994-06-08, DEF 14A 1994-05-24,
S-8 1994-07-14, 8-K/S-3/SC 13E4 1995-02-21, 10-K405 1995-03-17 (FY 1995-01-29) and 1996-03-28
(FY 1996-01-28). **No S-1 of any vintage appears in the enumerated history**, and none can: the
whole EDGAR corpus for this registrant starts 1994-02-11, six years after the founding and five
after the IPO. This is the floor the brief asked to be established *from the index rather than
assumed* — it is now established, with the accession numbers that define it.

**(a3) In-window Tier-1 text from family a: none. Retrospective Tier-1 text about the window:
substantial.** Held: `sources/sec/0000950134-94-000347_0000950134-94-000347.txt`, 237,339 bytes,
26,544 words, with sidecar. Label every citation below **94-10-K@l.nnn**:

- **94-10-K@l162** — "Dell Computer Corporation was originally incorporated in Texas in May 1984.
  In October 1987, the current Delaware corporation was formed and the renamed successor to the
  Texas company became a subsidiary of the Delaware corporation." → Tier-1 fixes: Texas
  incorporation **May 1984**; Delaware reorganisation **October 1987**; the words "the renamed
  successor" assert a rename **without naming the earlier name**.
- **94-10-K@l3327-3331** (exhibit 10.18) — "Agreement between the Company and Michael S. Dell dated
  May 12, 1988, … the Employment Agreement between Michael S. Dell and **a predecessor of Dell
  Computer Corporation dated May 3, 1984** (incorporated by reference to Exhibit 10.25 of Amendment
  No. 3 to the Company's Registration Statement on Form S-1, as filed with the Securities and
  Exchange Commission on March 27, 1991, Registration No. 33-38991)". → Tier-1 fixes: the founder's
  relationship with the predecessor entity is document-dated **1984-05-03**, and a second Form S-1
  (33-38991) was still being amended on **1991-03-27**.
- **94-10-K@l3288-3295** — exhibits 10.11/10.12 incorporate by reference "the Company's Registration
  Statement on Form S-1 as filed with the Securities and Exchange Commission on **May 12, 1988,
  Registration No. 33-21823**", and name a "Lease Agreement for Arboretum Point dated **July 25,
  1987**". → the IPO registration statement is proven to exist, with a filing date, by a Tier-1
  document — while the document itself is **not on EDGAR**.
- **94-10-K@l3230/3238** — option plans filed with the Commission **September 20, 1988, Registration
  No. 33-24621**. → a second 1988 registration number that a careless pass will mistake for the IPO.
- **94-10-K@l150** — "Since incorporating in 1984, the Company has grown rapidly…"
- **94-10-K@l117-119** — "Dell Computer Corporation … is the fifth largest personal computer vendor in
  the world and had fiscal 1994 consolidated net sales of $2.87 billion"; **@l1852** three-year
  net-sales row under the caption "FISCAL YEAR 1994 / 1993 / 1992" = **$2,873,165 / $2,013,924 /
  $889,939** (thousands). → the **earliest Tier-1 EDGAR fiscal-year figure reachable for this
  registrant is FY1992**, thirteen years after the founding. A five-year Item 301 table was searched
  for and its heading string does not appear in this accession — do not assume FY1990 exists here.
- **94-10-K@l165-170** — Austin, Texas base; fifteen named subsidiaries; "quoted on the NASDAQ
  National Market System under the trading symbol DELL".

**(a4) Negative results inside family a, stated as nulls over held bytes.** "PC's Limited",
"PCs Limited" and "Michael Dell" as a *founder-pre-history* narrative: **0 occurrences** in the held
237 KB. EDGAR full-text (`efts.sec.gov`, live 2026-09-26, HTTP 200): the phrase `"PC's Limited"`
returns **8 hits, all non-Dell** (Edge Technology Group 10QSB 2001-11-19; Neah Power Systems
10SB12G/A ×4); `"Dell Computer Corporation" AND forms:10-K` with a 1994-01-01→2000-12-31 window
returns **0** — which is a **window artefact of the full-text index, not a corpus null**: efts'
earliest-dated hit in an unbounded query is **2001-01-10**, so full text reaches back only to 2001
and cannot speak to 1988 at all. `"Michael S. Dell" AND forms:10-K` returns 110 hits spanning
CIK 0000826083 (2003 "DELL COMPUTER CORP", 2004+ "DELL INC") and CIK 0001571996 (2020+), which is
how the legacy CIK was identified.

**(a5) UNANSWERED inside family a — must not be read as absence.** `--cik 826086` (a wrong legacy-CIK
guess) → submissions fetch **HTTP 404**. `sec.gov/cgi-bin/browse-edgar` company search →
**HTTP 503 on two attempts** (3 tries each), so the CIK could not be confirmed through the normal
name-search route and was instead recovered from `efts` hit metadata. First `doc_listing` call on
accession 0000950134-94-000347 → **timeout**, retried successfully. `sec_intake.py auto` with
`--from 1994-03-01 --to 1994-12-31` stored **0 documents** — because these 1994-era rows carry an
empty `primaryDocument` field and `pick_auto()` skips them: **a tool limitation, not an empty
archive**; the same accession was retrieved by explicit `grab`. Any fleet member that concludes
"nothing early is on EDGAR" from an `auto` run alone will be right by accident, not by method.

## Family b web

STATUS: WRITTEN 2026-09-26

**Nothing in-window is reachable, and this is measured rather than assumed.** Wayback CDX
(`web.archive.org/cdx/search/cdx?url=dell.com&limit=2&filter=statuscode:200`, HTTP 200): earliest
capture of `dell.com` and of `www.dell.com` = **1996-12-21 05:30:00 UTC**
(`http://www.dell.com:80/`), with the next at 1996-12-22 09:18. Latest capture 2026-09-21. So the
company's own archived web presence begins **eight years after the founding and eight years after
the IPO**, and no founding-decade self-published web text exists to be found.

The only live unknown is `pcslimited.com`, whose CDX query **timed out (HTTP 0, UNANSWERED after 2
tries)** — an untested route, not a null, and worth one bounded re-run by the fleet: if a defunct
`pcslimited.com` capture existed it would be a Tier-1 "archived company page" (§5) of the founding
era, which is exactly the class of document that would promote the verdict.

Method-level status: §14 rule 6's finding that web archives reach nothing before the mid-1990s is
**reproduced here for Dell at 1996-12-21**, so family b is excluded from the tier count on evidence,
not on reputation. No `WebSearch`/`WebFetch` calls were spent by this probe (budget 6, used 0): all
network calls above went through the repo's own intake scripts and their User-Agent/backoff path.

## Family c periodicals

STATUS: WRITTEN 2026-09-26

**The only family that returns in-window Tier-1 text — and it returns it as the company's own
contemporaneous advertising, which is Tier-1 primary (§5), not press commentary.**

Inventory established first, so that later passes search a known-present corpus: IA
`advancedsearch` on `collection:(byte-magazine)` returns **159 items for 1986-1989 by title query,
54 by collection query, 28 for 1987-1988, 11 for year 1988** (identifiers `BYTE-1988-06/08/09/10/12`,
`byte-magazine-1988-03/04/05/07`, `byte-1988-07_202104`, `byte-1988-11-next`);
`title:("PC magazine") AND year:[1986 TO 1989]` → **57 items**; `title:(infoworld) AND
year:[1987 TO 1990]` → **26 items**. The trade-press back-file that §14 rule 6 says carries the
1950s-1980s is **present for the personal-computer press in 1984-1993** — the opposite of Walmart's
retail-trade case, where the corresponding runs were absent from IA.

Per the proven limit, `text:`/advancedsearch matches **annotations, not OCR**, so nothing was
believed until bytes were held. Four issues fetched into `sources/periodicals/` (each with a
`.meta.json` sidecar recording URL, route, bytes, fetch time) and grepped locally:

| item (label) | bytes held | "PC's Limited" | "Dell Computer" | "Michael Dell" |
|---|---|---|---|---|
| `byte-magazine-1987-04` = BYTE 12/04, Apr 1987 | 1,769,686 | **TIER1_CANDIDATE — 21 hits** | 0 (NULL over held KB) | 0 (NULL) |
| `BYTE-1988-10` = BYTE 13/10, Oct 1988 | 1,650,019 | 0 (NULL) | **TIER1_CANDIDATE — 5 hits** | 0 (NULL) |
| `byte-magazine-1988-03` | 1,555,215 | 0 (NULL) | 0 (NULL) | 0 (NULL) |
| `BYTE-1988-12` | 2,417,361 | 0 (NULL) | 0 (NULL) | 0 (NULL) |

**Dell-PCSL-87A — BYTE April 1987, full-page PC's Limited advertisement (headline "CREDIBLE
VALUES."), company self-published, in-window.** Verbatim, from held bytes at l.22204-22214:
"In three years, PC's Limited has revolutionized the way America buys personal computers by
manufacturing demonstrably better systems and then selling them directly to end users at remarkably
low prices. That's why we've shipped tens of thousands of computers to date." And l.22214: "It's
also why the trade press has praised our machines with comments like 'a perfect tool' and 'an
incredible value.' … Because PC's Limited gives you more speed with 8 and 12 MHz machines. Plus a
megabyte of high-speed RAM." And l.22222: "we back what we sell with industry-leading free 800-line
technical support, an unconditional 30-Day Money-Back Guarantee, and a full One-Year Limited
Warranty." Usable for: the direct-sale model as the company's own claim **in the founding decade**
(not a 1994 or 2002 retrospective); a shipped-units magnitude ("tens of thousands … to date",
basis unnamed — cumulative, undated, no period); the 8/12 MHz price-performance position; the
guarantee/warranty/support apparatus; and a self-dated founding (**"in three years" from April 1987
→ ≤ April 1984**, consistent with but independent of 94-10-K@l162). Not usable for capital, revenue,
head-count, or the founder's activity.

**Dell-DELL-88B — BYTE October 1988, Dell Computer Corporation advertisement copy, in-window.**
Verbatim from held bytes: l.42117 "Your Dell computer also comes with a thirty-day money back
guarantee."; l.42183 "Your Dell computer is supported by a team of technical experts that can be
reached every business day, from 7AM to 7PM (CST), simply by calling (800) 624-9896."; l.42816
"© 1988 DELL COMPUTER CORPORATION." with an AD-code line, and adjacent copy "Available January 1,
1989. **Payments based on a 36-month open-end lease.**". Usable for: the Dell brand in
company-published print by **1988-10** (an independent in-window corroboration of the rename
bracket), continuity of the 30-day guarantee from the 1987 ad, a named 800 number and its service
hours, and the existence of lease financing as a purchase channel. **Caveat recorded as a conflict
(C-4): the same OCR column run interleaves "Honeywell Bull technician" text with the Dell copy, so
any service-partnership reading of this page is unverified until the ad is checked at page level.**

What family c is *not* yet: mined. Four issues out of a 159-item 1986-1989 run is a sample chosen to
prove the family lives, not a sweep. The named high-yield targets for the fleet, in priority order,
are in §Untried.

**Transport disclosure.** All archive.org bytes in this section were pulled with `--insecure`
(`transport: "UNVERIFIED TLS"` is stamped in every sidecar), because this machine's CA store is
stale for the archive.org CDN. Per the tool's own rule, **these bytes must not carry High confidence
until re-checked**; a verified-TLS control fetch was attempted and returned `cached`, i.e. it hit the
local cache and therefore **did not test the verified route** — the control is inconclusive, and the
cap stands. EDGAR bytes (family a) were fetched over normally verified TLS.

## Family d corporate print

STATUS: WRITTEN 2026-09-26

Queried **before** any "paper-only" wording, per the Walmart lesson. Four explicit IA routes:

| query | result | reading |
|---|---|---|
| `(dell) AND collection:(annualreports)` | **numFound 0** (HTTP 200) | the dedicated digitised annual-report collection holds **no Dell report at all** — this is the route that found Wal-Mart's complete FY1972→FY1997 run, so its emptiness is a finding about Dell, not about the method |
| `title:("dell computer") AND year:[1984 TO 1996]` | numFound **0** | title-metadata null; advancedsearch quoting is metadata-only and inconsistent, so this is inventory, not proof of absence |
| `(dell computer corporation) AND year:[1986 TO 1992] AND mediatype:texts` | numFound **2**: `the-taxpayer-magazine-018-ctf`, a CIA RDP reading-room virus memo — **neither is Dell print** | noise-only |
| `title:(dell) AND year:[1986 TO 1996] AND mediatype:texts` (47) / `title:("dell computer") AND mediatype:texts` (**550**) | top items are `manualsonline-*`, `manualzilla-*`, `manualsbase-*` user guides for monitors, drives and power vaults | **current-state artefacts are not evidence of early state (§5)** — a 2005 monitor manual says nothing about 1986, and a naive byte count would report 550 "Dell documents" |

Verdict on family d as tested: **near-null on Internet Archive**, and — critically — **the family is
NOT closed.** The two routes that could still decide it were never queried for Dell: **HathiTrust
Babel full text** (documented as positive-but-intermittent, 403-challenged in some windows, and
requiring `--insecure-hosts babel.hathitrust.org`), and **Google Books volumes** (keyless Atom feed
documented working, v1 API 429 for everyone). `tools/queries.json` carries tasks for apple, walmart
and unitedhealth only — **no Dell row exists**, and that file is shared and outside this probe's
write target (§14 rule 4), so `periodical_harvest.py --company dell` cannot be run and was not
faked. The orchestrator must add a Dell block to `queries.json` as an explicit outbound task.

Also untested for Dell and squarely inside this family's definition: the **printed FY1989-FY1993
Dell Computer Corporation annual reports and proxies** (the paper years that sit in the EDGAR gap)
and the **1988 prospectus itself** — the single document that would settle pre-IPO revenue,
capitalisation, the share-offer terms and the PC's Limited → Dell rename chain in one Tier-1 read.
**No line of this file says "paper-only".** It says: paper routes on IA tested and empty; HathiTrust,
Google Books and physical/auction scanning untested.

## Family e documentary

STATUS: WRITTEN 2026-09-26

**UNTRIED. No request of any kind was sent to an auction, museum, special-collections or manuscript
route by this probe**, so this family returns neither text nor null. `tools/HARVEST_README.md`
records family 4 (`auction / museum / documentary sale records`) as **"UNQUERIED — no API verified;
remains UNANSWERED, never null"**, and `tools/ia_text.py` reaches only the IA item/OCR layer, which
is where Apple's Christie's lot data did *not* come from.

For Dell the plausible in-window documentary targets, named as search targets and **not** as claims
(no evidence exists here that any of them hold anything), are: incorporation and name-change records
for a Texas corporation founded at Austin in May 1984 (Texas Secretary of State / county-level
records), the founder's own papers or the corporate archive of an Austin company founded in 1984,
early PC's Limited sale or consignment items at auction, and the NASDAQ listing file referenced by
94-10-K@l168. Apple's probe recovered founding artefacts at auction; **until the same query class is
run for Dell, family e is an open flanking route, and it is the only family this probe did not even
attempt.** A null reported here would have been a fabrication.

## Boundaries

STATUS: WRITTEN 2026-09-26

Stage boundaries are set at the **fixing document**, not at the remembered date. Every date below
names the document that fixes it; a date whose document is not held is written UNKNOWN even where
the brief supplied it.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Stage 1 start (earliest Tier-1-fixable founder/company event) | **1984-05-03** — employment agreement between Michael S. Dell and "a predecessor of Dell Computer Corporation" | 94-10-K@l3327-3331 (exhibit 10.18, referencing Ex 10.25 of S-1 Am. No. 3, Reg. No. 33-38991) | High (Tier-1 filing text; the referenced agreement itself is paper-only) |
| Texas incorporation of the entity later called Dell Computer Corporation | **May 1984** (month-level only; the filing gives no day) | 94-10-K@l162 | High for "May 1984"; the identity of the May-1984 Texas corporation with "PC's Limited" is **Medium — inference, see C-1** |
| In-window self-dating of the start | "In three years, PC's Limited has…" → operating by **April 1984** at the latest | Dell-PCSL-87A (BYTE Apr 1987, l.22204) | Medium (company's own ad rhetoric, month-level) |
| Rename / reorganisation | **October 1987** — Delaware corporation formed, "the renamed successor to the Texas company became a subsidiary" | 94-10-K@l163 | High for October 1987 (Tier-1) |
| Rename bracket from in-window print | name in use is **PC's Limited at 1987-04**, **Dell Computer Corporation at 1988-10** | Dell-PCSL-87A; Dell-DELL-88B (l.42816 "© 1988 DELL COMPUTER CORPORATION") | High (two independent in-window Tier-1 artefacts, one year apart) |
| Stage 1 end (IPO) — registration statement filed | **1988-05-12**, Registration No. **33-21823** | 94-10-K@l3288-3292 | High that a Form S-1 was filed that day; **the brief's "IPO 1988" is a registration date, not a pricing date** |
| IPO pricing / first trade date | **UNKNOWN** | nothing held; paper-only on EDGAR (floor 1994-02-11), web floor 1996-12-21 | — |
| Distractor registration | 1988-09-20, Registration No. **33-24621** — the 1986/1987 option plans, **not** the IPO | 94-10-K@l3230, @l3238 | High |
| Later S-1 still open in 1991 | Registration No. **33-38991**, Am. No. 3 filed **1991-03-27** (also the vehicle that carries the 1984 employment agreement) | 94-10-K@l3330-3333 | High |
| Second registration-type anchor | 1988-05-12 agreement between the Company and Michael S. Dell | 94-10-K@l3327 | High |
| Earliest Tier-1 fiscal-year figure on EDGAR | **FY1992 net sales $889,939 (000s)**; FY1993 $2,013,924; FY1994 $2,873,165 | 94-10-K@l1849-1852 caption+row | High |
| **EDGAR floor, legacy registrant** | **1994-02-11** (SC 13G/A); earliest 10-K 1994-04-01 (FY 1994-01-30); **no S-1 among 1,851 filings**; no UNANSWERED slice | `sources/_index_cik0000826083/sources/_index/_INDEX.md` | High |
| **EDGAR floor, ranked registrant** | **2013-07-24** (DFAN14A); EMC `425` 2015-10-13, `S-4` 2015-12-14; first 10-Q 2016-06-10 as `denaliq1fy1710q.htm`; first 10-K 2017-03-31 | `sources/_index/_INDEX.md` | High |
| **Web-archive floor** | **1996-12-21 05:30 UTC**, `http://www.dell.com:80/` | Wayback CDX, HTTP 200 | High |
| Stage 1 / Stage 2 cut | **1988-05-12** (S-1 filed) as the last Tier-1-fixable founding-window event | fixing document: 94-10-K exhibit list | Medium — the substantive IPO completion is unproven here, so the cut is documentary, not economic |
| Stage 2 / Stage 3 cut | recommend the **EDGAR-text floor 1994-02-11** as Stage 3's evidence anchor, with Stage 2 = 1988-05-12 → 1994-02-10 written largely from family c press + paper years | fixing documents: the two `_INDEX.md` files | Medium — a judgment about evidence reach, not a boundary Dell ever declared |
| Entity switch inside Stage 3 | 2013 (Del/TDC era) → **2015-10-13 EMC `425`**, **2016-06-09 first 8-K of the shell**, **2016-09-07 `8-A12B`/CERTNYSE** relisting | `sources/_index/_INDEX.md` | High |

**Founder pre-history — kept at UNKNOWN, enumerated rather than deleted.** Nothing held establishes:
Michael Dell's activity before 1984-05-03; whether the first business was operated from a
university dormitory, a residence, or a leased office (the earliest Tier-1 address evidence held is
a **lease agreement for Arboretum Point dated 1987-07-25**, 94-10-K@l3292-3295, four years in); the
**$1,000** of capital and its source (a parental loan, a job saving, or a revenue-funded start);
whether "PC's Limited" was a sole proprietorship before it was a Texas corporation, or incorporated
from day one; the first customer, first order, first product line, or first supplier; whether the
founder was enrolled at a university and when any enrolment ended; and the identity of any co-
founder, early employee, or outside investor before 1988. Each is a legitimate §S gap with a named
route in §Untried — none is answerable from EDGAR (floored 1994) or the web (floored 1996), and the
only family that could answer most of them is the company's own **paper** prospectus plus the
unmined periodical run.

**KNOWABLE / NOT KNOWABLE for Stage 1.** KNOWABLE from held bytes: the direct-sale model as the
company's own public claim (1987, 1988); the guarantee/warranty/support apparatus and its phone
number and hours; the 8/12 MHz product position; cumulative shipment magnitude stated as "tens of
thousands"; the corporate-structure skeleton (May-1984 Texas, October-1987 Delaware, 1988 S-1s,
1991 amendment); FY1992-1994 net sales. NOT KNOWABLE without new documents: every 1984-1988
financial quantity, the IPO terms, the naming/renaming instrument, and the whole founder
pre-history. UNKNOWN as of this probe but plausibly recoverable: everything in §Untried items U1-U6.

## Conflicts

STATUS: WRITTEN 2026-09-26

**C-1 — Does any Tier-1 document say PC's Limited *became* Dell Computer Corporation?**
CLAIM A: "founded 1984 as PC's Limited, renamed Dell" (the brief's premise; the standard account).
CLAIM B: 94-10-K@l162 says only "Dell Computer Corporation was originally incorporated in Texas in
May 1984 … the renamed successor to the Texas company", never naming the earlier name; the string
"PC's Limited" occurs **0 times** in the held filing and 0 times in Dell's EDGAR full text.
WHY THEY DIFFER: the filing's exhibit chain refers to the 1984 counterparty as "**a predecessor of
Dell Computer Corporation**" — a rename is asserted but the pre-rename name is never given in Tier-1
text held here; the name survives only in in-window print (Dell-PCSL-87A). EVIDENCE WEIGHT: Tier-1
retrospective filing text (one lineage) vs Tier-1 in-window self-published advertising.
BEST-SUPPORTED INTERPRETATION: a Texas business founded by/with Michael Dell in May 1984, trading as
PC's Limited in 1987 print, and a "renamed successor" carrying the Dell name by 1988 print — but the
**legal identity link is unproven at Tier 1 in this corpus**. RESIDUAL UNCERTAINTY: High on the
instrument (amendment vs new incorporation vs share exchange). CONFIDENCE: Medium for the sequence,
Low for the identity link. FOLLOW-UP: the 1988 S-1 (33-21823) or the Texas corporation record.

**C-2 — Start date: 1984-05-03 vs "May 1984" vs "in three years" (≤1984-04).**
94-10-K@l3327 dates an employment agreement with the predecessor to **1984-05-03**; @l162 gives the
Texas incorporation as **May 1984**; BYTE April 1987's own "in three years" implies operation from
**about April 1984**, i.e. *before* the May-1984 incorporation date. WHY THEY DIFFER: they measure
different events — start of trading (advertising, undated) vs incorporation (dated), and the ad's
"three years" is a rounded marketing figure, not a filing. BEST-SUPPORTED INTERPRETATION: business
activity **pre-dates** the 1984-05-03 document date; the incorporation is the earliest *documentary*
anchor, not the earliest *activity* anchor. CONFIDENCE: High that both are true; the distinction, not
the date, is the finding. Do not let the fleet write "founded May 3, 1984" as the start of
operations.

**C-3 — "IPO 1988": which 1988?** CLAIM A: S-1 filed **1988-05-12** (33-21823). CLAIM B:
**1988-09-20**, Registration No. 33-24621 — a registration of the 1986/1987 option plans.
WHY THEY DIFFER: both are "registrations filed in 1988" in the same exhibit list, and a form-blind
reader merges them. BEST-SUPPORTED INTERPRETATION: 33-21823 is the equity-registration candidate;
33-24621 is not an IPO. Neither fixes a pricing date. CONFIDENCE: High on the distinction (the
exhibit descriptions differ), Medium on which one is "the IPO" — **no document held fixes the IPO
date, and "1988" must be carried as a registration year until the paper file or in-window press
confirms completion**.

**C-4 — 1988 service-partnership reading of the Dell ad.** CLAIM (tempting, from adjacency): Dell
advertised Honeywell Bull on-site service in 1988. COUNTER: the OCR text run interleaves columns,
so "we'll send a Honeywell Bull technician" (l.42110-42112) and "Your Dell computer also comes
with…" (l.42117) may be **different advertisers on the same page spread**; only the
"© 1988 DELL COMPUTER CORPORATION" + AD-code line (l.42816) is safely Dell's. EVIDENCE WEIGHT:
held bytes, but page structure unverified. BEST-SUPPORTED INTERPRETATION: Dell's own copy = the
30-day guarantee, the 800 number, the hours, the warranty, the lease offer; the Honeywell Bull text
is **UNVERIFIED attribution**. CONFIDENCE: Low, and it must be page-checked before use.

**C-5 — The $1,000 / dorm-room account.** No occurrence in any held Tier-1 document (family a grep
= 0; family c sample = 0). Any later recovery of this figure will very likely be a **reprint of the
company's own retrospective** — its prospectus, its later history pages, or the founder's memoir —
which per §3 is **one source however many places reprint it**, capped at single-document
confidence with `independence_note: same lineage as the corporate self-history`. This probe records
it as **not evidenced here**, not as false: absence in four BYTE issues and one 1994 filing cannot
overturn a claim whose natural home is the 1988 prospectus (paper) or 1985-1986 press (unmined).

**C-6 — Entity/lineage conflict at the registrant level.** CLAIM A (from the ranked universe row):
"Dell Technologies, founded 1984" — one continuous company. CLAIM B (from the two indices):
the ranked registrant **CIK 1571996 begins 2013-07-24** as the Denali/EMC vehicle, while the
1984-lineage registrant is **CIK 0000826083 (DELL INC / Dell Computer Corp)**, whose own EDGAR
history begins 1994-02-11. WHY THEY DIFFER: a merger shell inherited the brand and the ticker, and
EDGAR keeps them as separate CIKs. BEST-SUPPORTED INTERPRETATION: founding-window research must be
run against **826083**; anything cited from 1571996 is post-2013 and hindsight-contaminated for
Stage 1 (§2, §6). CONFIDENCE: High. This is the trap in operational form and the fleet brief must
carry it.

## Nulls

STATUS: WRITTEN 2026-09-26

A null is a zero **over bytes held**. Anything else is labelled UNANSWERED or UNTRIED, per §15.1
and §14 rule 6. All file paths below are under
`founders_playbook/01_companies/company_041_dell/`.

**Documented nulls (in-window, verified against held bytes):**
1. `"PC's Limited"` / `"PCs Limited"` — **0 occurrences** in 237,339 B of `sources/sec/0000950134-94-000347_0000950134-94-000347.txt` (the earliest Dell 10-K, FY1994, filed 1994-04-01). The founding name is absent from Dell's own earliest electronic filing.
2. Any founding capital figure, dormitory/residence statement, first-customer, first-order or head-count statement — **0 in the same 237 KB**, and 0 in the four BYTE issues (7,392,281 B held in total across `sources/periodicals/`).
3. `"Michael Dell"` — 0 occurrences in `BYTE-1988-10` (1,650,019 B), `byte-magazine-1988-03` (1,555,215 B), `byte-magazine-1987-04` (1,769,686 B), `BYTE-1988-12` (2,417,361 B): the founder is **not named** in the company's own advertising in these issues.
4. `"Dell Computer"` — 0 in `byte-magazine-1987-04` (1,728 KB of OCR held): the Dell brand had not yet displaced "PC's Limited" in the company's April-1987 print. Issue-level nulls, not corpus-level.
5. **Filings dated 1984-01-01 → 1993-12-31: 0** among 1,851 enumerated filings for CIK 0000826083 (`sources/_index_cik0000826083/sources/_index/submissions.csv`), and **0** among 1,951 for CIK 0001571996; both `_INDEX.md` files report **"(none)"** under *UNANSWERED slices*, so these are nulls and not fetch failures.
6. **No form S-1 of any year** appears in either enumerated index.
7. **Wayback: 0 captures of `dell.com` before 1996-12-21** (CDX, HTTP 200, `filter=statuscode:200`).
8. **`(dell) AND collection:(annualreports)`: numFound 0** (HTTP 200) — no Dell item in IA's digitised annual-report collection at all.
9. **`(dell computer corporation) AND year:[1986 TO 1992] AND mediatype:texts`: numFound 2, both irrelevant** (a taxpayer magazine, a CIA reading-room memo).
10. **EDGAR full text, `"PC's Limited"`: 8 hits, 0 of them Dell** (Edge Technology Group, Neah Power Systems) — HTTP 200.

**UNANSWERED — requests that did not get an answer; never reportable as absence:**
- `--cik 826086` submissions → **HTTP 404** (a wrong CIK guess; superseded by 826083, found via efts).
- `sec.gov/cgi-bin/browse-edgar` company search → **HTTP 503** on both routes and all attempts.
- `web.archive.org/cdx` for `pcslimited.com` → **read timeout** (route untested, one re-run queued as U5).
- first `doc_listing` on accession 0000950134-94-000347 → **timeout**; succeeded on the retry.
- `sec_intake.py auto --from 1994-03-01 --to 1994-12-31` → **0 documents stored, because `pick_auto()` skips rows with an empty `primaryDocument`**: a tool gap on pre-1995 accessions, recorded so no later agent mistakes it for an empty archive.
- `chronicling_america` for Dell → never requested here; README documents it as 403-by-policy, so it is a **known-dead route, not a null**.
- The verified-TLS control re-fetch of `byte-magazine-1987-04` returned `cached` → the TLS-verified route for archive.org is **untested**, and all IA bytes stay capped at less than High confidence.
- IA `fulltext/inside.php` — deliberately **not used**: the Walmart control test proved it returns 0 matches even for "America" in a 100-page magazine, so a zero from it is void. Any Dell "periodical coverage" claim sourced from that endpoint must be discarded.

## Untried

STATUS: WRITTEN 2026-09-26

Everything below was **never attempted** by this probe. Ordered by expected yield per request; the
tier verdict is explicitly conditional on U1 and U2, and the probe's own budget was the reason they
were not run. `queries.json` has **no Dell block** and is shared (outside this probe's write
target), so the scripted harvest could not be run for Dell at all.

- **U1 — HathiTrust + Google Books for Dell corporate print** (family d, the tier-deciding test). Add a `dell` block to `tools/queries.json` (`hathitrust` + `google_books` + `corporate_print`) and run `python tools/periodical_harvest.py --company dell --insecure-hosts babel.hathitrust.org`. Target artefacts: printed Dell Computer Corporation annual reports **FY1989-FY1993** and the **1988 prospectus**. **This is the route that flipped Walmart; it is also the route that could promote Dell to T2.**
- **U2 — Auction / museum / special-collections sweep** (family e, entirely untouched): Texas Secretary of State / county corporation records for a May-1984 Austin incorporation and any name amendment; Austin/Texas business-paperage and university archives; auction catalogues for PC's Limited artefacts. No command exists for this family yet — it needs a tool, not a retry.
- **U3 — the rest of the digitised periodical run.** 159 BYTE items for 1986-1989 (54 in `collection:(byte-magazine)`), **57 PC Magazine items 1986-1989**, **26 InfoWorld items 1987-1990**, and BYTE/Kilobaud/Creative runs for **1984-1985, never enumerated for Dell at all**. Fetch `_djvu.txt` and grep `PC'?s Limited|Dell Computer|Michael Dell`. Highest-yield single query: an **IPO-week 1988** magazine search for the offering terms — the one in-window money figure most likely to exist in public print.
- **U4 — the 1988 S-1 itself (33-21823) and S-1/A chain, and 33-38991**, as **paper**: SEC public-reference retrieval or a scanned copy surfaced by U1/U2. The named documents to request are the exhibit list of the FY1994 10-K: **Ex 10.25 (May 3, 1984 employment agreement, predecessor named)**, **Ex 10.22/10.23 (option plans, Reg. 33-24621)**, **Ex 10.24/10.25 lease (Arboretum Point, 1987-07-25)**.
- **U5 — `pcslimited.com` and any predecessor domain in CDX** (retry after the timeout), plus a CDX sweep of `dell.com` paths (`/history`, `/about`) for self-published founding pages captured 1996-1999 that a lineage audit could date.
- **U6 — local and business newspapers for Austin 1984-1988** (Austin American-Statesman; Crain's Austin) through a route not yet tried for Dell, and **Inc./Fortune/BusinessWeek founder profiles 1988-1992** — the natural home of the $1,000 account, where its **first published telling** can be identified and the reprint lineage broken.
- **U7 — XBRL series (`sec_intake.py facts`)** was **not run**: XBRL reaches back only to the 2009+ era for any registrant, so it cannot touch 1984-1996; it is listed here so its absence from `sources/` is a recorded choice rather than an oversight.
- **U8 — the FY1995/FY1996 10-K405s already enumerated** (1995-03-17, 1995-04-07, 1995-04-20, 1996-03-28) were **not grabbed**; they are the cheapest remaining Tier-1 text on disk and may repeat or extend the founding sentence — one `grab` each.
- **U9 — Gates/re-register housekeeping:** this probe wrote only its dossier and `sources/`; it created **no CSVs**, so `gates.py --checks csv,keys` runs against the registers the Stage-1 fleet will create.

**Biggest single gap, stated plainly:** for Dell's founding window there is **no Tier-1 financial
observation of any kind** — no capital, no revenue, no units, no head-count, no first order — and the
one document that carried all of them (the 1988 registration statement) sits below the EDGAR floor at
paper, while the press that reviewed the company in 1985-1987 remains unmined. "We cannot know the
money story of Dell's first four years from public electronic records" is this probe's deliverable.

---

### Probe ledger (bytes on disk at close-out)

| path | bytes | what it settles |
|---|---|---|
| `sources/sec/0000950134-94-000347_0000950134-94-000347.txt` (+ `.meta.json`) | 237,339 | earliest Dell 10-K on EDGAR (FY1994): May-1984 Texas incorporation, Oct-1987 Delaware rename, S-1 Reg. 33-21823 filed 1988-05-12, Reg. 33-24621 1988-09-20, Reg. 33-38991 Am.3 1991-03-27, 1984-05-03 predecessor employment agreement, FY1992-1994 net sales |
| `sources/periodicals/byte-magazine-1987-04_djvu.txt` (+ sidecar) | 1,769,686 | PC's Limited April-1987 advertisement — in-window Tier-1 self-published founding-decade text |
| `sources/periodicals/BYTE-1988-10_djvu.txt` | 1,650,019 | Dell Computer Corporation October-1988 advertisement — brand, guarantee, 800 number, lease offer |
| `sources/periodicals/byte-magazine-1988-03_djvu.txt` | 1,555,215 | issue-level null (0 hits over 1,518 KB) |
| `sources/periodicals/BYTE-1988-12_djvu.txt` | 2,417,361 | issue-level null (0 hits over 2,360 KB) |
| `sources/_index/{_INDEX.md,submissions.csv,submissions.json}` | 1,951 filings | CIK 1571996 shell history, floor 2013-07-24 |
| `sources/_index_cik0000826083/sources/_index/{_INDEX.md,submissions.csv,submissions.json}` | 1,851 filings | CIK 826083 lineage, floor 1994-02-11, no S-1, no UNANSWERED slice |

Nothing was deleted; no git operation was run; the two background/failed fetch attempts are recorded
above as UNANSWERED rather than discarded. IA bytes carry `transport: UNVERIFIED TLS` in their
sidecars and are capped below High confidence until re-checked (disclosed per §15.1 tooling note);
`--insecure` was used for archive.org only, and EDGAR traffic used verified TLS. Web
search/fetch budget: **0 of 6 spent** — every network call went through `tools/sec_intake.py` or
`tools/ia_text.py` and their own request paths.

## SUPERSEDED / RE-GRADED 2026-09-27

<!-- Appended by regrade-t3-batch. Nothing above this heading is rewritten or deleted. Full figures in
     company_041_dell/research/A3_intake_regrade.md. Entity question (1571996 shell vs 826083 founding
     registrant) NOT re-opened: this pass used CIK 826083 as this file settled it. -->

**What changed: family (a)'s verdict as *worded*, not Dell's evidence base.** Re-measured with the rebuilt
`sec_intake.py`, window **1984-01-01 → 1996-12-31** (all observed this session):

- `index --dry-run` and live `index` → **1,851 filings, "DELL INC ()"**; `sources/_index/submissions.csv`
  parses to **55 in-window rows, ALL 55 with a blank `primaryDocument`**, minimum date **1994-02-11**.
  This **confirms** §Verdict trap 1 and (a2) exactly: earliest filing of any kind **SC 13G/A 1994-02-11**
  (0000748054-94-000017), earliest **10-K 1994-04-01**, **no S-1 among the 55**, nothing at all 1984–1993.
  The EDGAR floor is now a tool measurement rather than a hand-built index.
- `auto … --max-docs 25` → **9 documents stored, 2,317,629 bytes, 306,443 words, 0 UNANSWERED** (exit 0)
  against this file's **1** SEC document on disk. New holdings: SC 13G/A 1994-02-11 10,407 B · 10-K 1994-04-01
  237,339 B (re-fetched at the identical byte count — probe and script agree) · DEF 14A 1994-05-24 238,177 B ·
  8-K 1995-02-21 21,859 B · S-3 1995-02-21 166,623 B · 10-K405 1995-03-17 589,859 B · 424B2 1995-06-09
  63,763 B · POS AM 1995-06-26 7,650 B · **10-K405 1996-03-28 981,952 B**.
- Bytes are filings, not apology pages: `grep -l -i "File Unavailable|Temporarily Offline|NoSuchKey"` over
  `sources/sec/*.txt` → **0 matches**. Phrase counts read out of the stored bytes: FY1994 10-K
  **"1984"×4, "Michael"×18, "33-21823"×3, "PC's Limited"×0**; FY1996 10-K405 **"1984"×3, "Michael"×25,
  "33-21823"×2, "PC's Limited"×0**. **The §lineage warning is re-confirmed on 5.3× more bytes, not refuted**:
  the founding story still appears nowhere in family (a); only the retrospective dates and the 1988 S-1's
  registration number do.
- **Family (a) verdict: in-window Tier-1 text = YES (1994-02-11 → 1996-03-28); founding-window (1984 – mid-1988)
  text = still NULL.** Earliest held = earliest in index = SC 13G/A 1994-02-11, so there is no front-of-window
  drop here (unlike Costco). **46 of 55 in-window filings were not fetched and were not reported UNANSWERED**
  (10-Qs, SC 13E4, PRE 14A, 8-A12G …): UNTRIED, not null.

**Tier: T2 PROVISIONAL under §15.2's literal test; this file's T3 remains correct under its own founding-window
test — the orchestrator must rule on the convention.** Family (a) holds in-window Tier-1 text on dates inside
the assigned window, so counted that way (a)+(c) = 2 families → **T2 core (6–9 runs, 22k/stage)**. This file
scored (a) NO because it required text *from* 1984–1988 — the same retrospective-in-window text that made
Costco's (a) and Nvidia's (a) YES, so the fleet is currently inconsistent and the difference is convention,
not measurement. Marked **PROVISIONAL** also because the family-count test the probe deferred is still open:
**(d) HathiTrust and Google Books remain UNTRIED** (the routes that flipped Walmart; the IA routes stayed
near-null) and **(e) documentary was never touched** — the gap is being closed fleet-side, `tools/queries.json`
now parses to **427 tasks across 50 companies including a `dell` block**, so those two are script-triable and
still unrun. What is **not** superseded under either reading: **T1 remains structurally unreachable for
Stage 1** (a floored 1994-02-11 by the filing regime, b floored 1996-12-21 by the medium), the promotion gate
(printed FY1989–FY1993 AR/proxy run + the 1988 prospectus in HathiTrust/Google Books) is unchanged, family (c)
is unchanged (BYTE Apr 1987 1,769,686 B / Oct 1988 1,650,019 B remain the only in-window 1984–1988 Tier-1
carriers), and **§K still has no Tier-1 1984–1988 figure of any kind**.

**Disclosure and defect against this file's own artifacts.** `index`/`auto` write under
`<company-dir>/sources/_index` and `sources/sec` with **no CIK in the path**, so running intake for **826083**
**overwrote in place** the `sources/_index/` copy of the **1571996** shell index this file cites as (a1).
Pre-state captured before the run: header `# SEC submissions index -- Dell Technologies Inc. (CIK 0001571996,
DELL)`, **1,951 rows, min 2013-07-24, max 2026-09-24**. The (a1) facts survive only in this file's prose and
that transcript; the bytes are gone from that path. Nothing else was deleted, moved, or git-touched, and
`sources/_index_cik0000826083/` (the 826083 copies) were left intact and parse identically. **Recommendation
to the tool owner (not edited by this pass): key index output by CIK, and have `resolve --ticker DELL` name
the legacy registrant instead of returning only the merger shell.** `facts` again printed
`sources/financials/xbrl_early_series.csv` and wrote no file.

