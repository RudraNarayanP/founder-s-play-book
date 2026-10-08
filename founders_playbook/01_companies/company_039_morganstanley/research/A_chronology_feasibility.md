# Stage-1 chronology-feasibility PROBE — MORGAN STANLEY (company_039_morganstanley, Fortune rank 39)

Owner: `probe-morganstanley` · Method: `PROBE_BRIEF_SHARED.md` + `00_METHOD_AND_STYLE.md` §3/§14/§15.2 + RD-112/124/130/134/135.
Web calls this pass: **0.** All figures are measurements from bytes on disk under `sources/` (commands → outputs at §10).
Brand-vs-registrant worked examples read before writing: `company_012_jpmorgan`, `company_024_citigroup`, `company_036_goldman` probes. STATUS: WRITTEN

---

## 1. Windows PROPOSED and the measured intake state

**Stage-1 (origin) window: 1924-01-01 → 1950-12-31 — PROPOSED, not inherited.** `00_universe/fortune_top_50_2026.csv`
has no founding-date column. The window is bounded by the event dates the corpus itself prints (§2): the earliest date
the registrant's paper assigns to any ancestor is **1924** ("Dean Witter & Co., organized in 1924", S-4/A l.4739), the
brand line's own date is **1935** (New York incorporation, S-4/A l.4776), and the last in-line origin act before the
post-war paper restructurings is the **1941** partnership reconstitution (S-4/A l.4777-4778). No held byte names an
origin act between 1942 and 1960. The `harvest_mine.py` window `1924-01-01..1960-12-31` (recorded in
`sources/harvest_mine/_index.json`) coincides at the floor but is a **search setting**; my ceiling is 1950, derived
from the event list, not from the tool.

**Intake state — the fleet REFUSED record is superseded by bytes on disk.** The RD-135 de-spaced-slug refusal is
repaired: `sources/_index/_registrant_CIK0000895421.json` records guard **ok**, reason
`slug token(s) ['morganstanley'] match registrant 'MORGAN STANLEY' (CIK 0000895421)`, built 2026-10-06T11:46:35Z.
A canonical index therefore exists and `sec_intake index` was **not** re-run (none of my calls minted new intake
artefacts; everything below is read-and-grep).

Measured index (`submissions.csv`, header enumerated first: `filingDate,form,accession,reportDate,primaryDocument,source`):
- **110,365 rows**; registrant answering "Morgan Stanley" = **CIK 0000895421**, tickers `MS` + nine MS-preferred lines.
- `former_names` (verbatim): `MORGAN STANLEY`, `MORGAN STANLEY`, `MORGAN STANLEY DEAN WITTER & CO`,
  `MORGAN STANLEY DEAN WITTER DISCOVER & CO`, **`DEAN WITTER DISCOVER & CO`**.
- Walk is **uncapped** (RD-134 fix visible): 46 archive slices (`CIK0000895421-submissions-NNN.json`) plus `recent`.
- **Date perimeter 1993-11-08 → 2026-10-06**; rows with filingDate before 1960: **0**. The 1993-11-08 floor is EDGAR's
  own floor, not a finding about 1924-1950. Caveat on the floor row itself: the SC 13D/A `0001021408-01-503754` printed
  as earliest in `_INDEX.md` carries a **-01- (2001) accession** with a 1993 filingDate — an index row is not a fact
  (§3); the perimeter claim rests only on the column minimum.
- **The ticker trap did NOT fire** — the floor is 1990s, not 2020s, so this is not a recent holding-company shell
  (contrast the XOM/ExxonMobil case in the brief). But a **reverse** brand-vs-registrant split did fire, and it is
  this company's central finding: see §2.

`sources/sec/_RUN.json`: window **1960-12-31..2020-12-31** (the forward recital pass), attempted 135, **stored 20**,
unanswered 11, skipped 104, identity OK (20+11+104=135), 5,953,859 B / 766,236 words, built 2026-10-06T11:48:20Z.
The 20 stored documents span **1996-07-11 → 2001-02-14** (`_MANIFEST.csv`, 20 `status:ok` rows): S-3 1996 (Dean
Witter), 8-K 1996, SC 13G/A + SC 13D 1997-02, **10-K405 1997-03-31** (Dean Witter, Discover FY1996), **S-4/A
1997-04-11 + S-4/A 1997-06-02 + 424B2 1997-06-04** (the merger papers), 10-K + DEF 14A 1998-02-20, 10-K405 1999-02-23,
POS AM 1999-10-13, 10-K405 2000-02-25, 424B2 + 8-K 2000-06, SC 13G/13D 2000, and **three documents of the single
accession 0000950134-01-001364** (SC 13G/A 2001-02-14 — one filing, three documents, not three witnesses).
md5 over all 21 held text layers → **0 duplicate pairs**. Shelf: periodicals **1** layer, corporate_print **0** files
(the brief's "2 periodicals" is not what the directory holds: `find periodicals -type f ! -name '*.meta.json' | wc -l` → 1).
No in-window (1924-1950) SEC document exists in any stored path — expected from the perimeter. STATUS: WRITTEN

## 2. The registrant is the DEAN WITTER paper — the brand line arrives by marriage (STATUS: WRITTEN)

This is JPMorgan's "EDGAR name history runs through Chemical" finding, reproduced on Morgan Stanley's own bytes, in
reverse polarity: here the modern registrant's **paper** line is older than the brand's, and the brand is the
acquired one.

**Line A — the registrant line (CIK 895421, continuous on EDGAR).** Carriers, file+line:
- `sources/sec/0000950130-96-002544_0000950130-96-002544.txt` (S-3, 1996-07-11) l.3564 —
  *"Dean Witter, Discover Co., a Delaware corporation (the …)"* : this CIK's own pre-merger paper is Dean Witter's.
- `sources/sec/0000950130-97-001437_0000950130-97-001437.txt` (10-K405 for FY1996, filed 1997-03-31, under CIK 895421)
  l.203 — *"The Company traces its origins to Dean Witter & Co., organized in 1924. In 1978, Dean Witter & Co.
  Incorporated (the successor to Dean Witter & Co.) merged with Reynolds Securities Inc., and in 1981 Dean Witter
  Reynolds Organization Inc. was acquired by Sears…"* (also l.724, same volume, "founded in 1924").
- `sources/sec/0000950130-00-000882_0000950130-00-000882.txt` (10-K405 FY1999) l.283-287 — *"The Company is a
  combination of Dean Witter, Discover & Co. … and Morgan Stanley Group Inc. … and was formed pursuant to a merger of
  equals that was effected on May 31, 1997 … The Company was originally incorporated under the laws of the State of
  Delaware in 1981"*; and the subsidiaries-exhibit footnote at l.16793 — *"Morgan Stanley Dean Witter & Co. was
  incorporated in Delaware in 1981."*

**Line B — the brand line (Morgan Stanley, a different legal person on held evidence).** The fullest recital in the
corpus is the merger registration statement, filed under CIK 895421 but stating Morgan Stanley Group's history:
- `sources/sec/0000950130-97-001661_0000950130-97-001661.txt` (S-4/A, 1997-04-11) l.4775-4784 —
  *"Morgan Stanley & Company, Incorporated was incorporated under the laws of the State of New York in 1935 and was
  liquidated and reconstituted as Morgan Stanley & Co. ('MS & Co.'), a partnership, in 1941. Morgan Stanley & Co. was
  incorporated under the laws of the State of Delaware in 1969 … Morgan Stanley Holdings Incorporated was incorporated
  under the laws of the State of Delaware in 1975 to own all of the stock of Morgan Stanley & Co. …, and changed its
  name to Morgan Stanley Inc. in 1978 and, in 1985, to Morgan Stanley Group Inc. Morgan Stanley conducted its initial
  public offering … in 1986."* (The same document recites the Dean Witter chain at l.4739 — one document, two legal
  persons, two date-series: exactly the attribution discipline this company requires.)
- Cross-carrier: `0000950130-98-000803` (10-K FY1997, 1998-02-20) l.213-217 — *"Dean Witter Discover was incorporated
  under the laws of the State of Delaware in 1981, and its predecessor companies date back to 1924. Morgan Stanley was
  incorporated under the laws of the State of Delaware in 1975, and its predecessor companies date back to 1935."*
  And inside the FY1996 Dean Witter 10-K, describing the merger counterparty at l.155 — *"A leader in investment
  banking since its formation in 1935, Morgan Stanley ranked first…"*

**Independence count, per §3:** these five carriers are **two retrospective self-narrative lineages** — Dean
Witter's own (l.203/l.724, echoed by the merged company's 10-Ks) and Morgan Stanley Group's (S-4/A l.4775-4784,
echoed by the merged 10-Ks) — authored 62-73 years after the dates they recite, not a witness count. The earliest
carrier of the 1935 date is 1997; no 1935, 1941 or 1924 document is on disk.

**The brief's "1924 split from J.P. Morgan & Co." is not what the bytes carry.** On held bytes, 1924 names **Dean
Witter & Co.'s organization**, nothing else (`grep -n "1924"` → 6 lines, all Dean Witter attribution or the merged
"date back to 1924" boilerplate). A 1924 separation of a Morgan house securities unit is attested **nowhere** in the
corpus: `Wrenflesley` **0** hits; the only `J.P. Morgan` string in all 21 layers is
`0000950130-98-000790` l.1734 — *"Franklin Resources, Inc.; J.P. Morgan & Co. Incorporated; Lehman Brothers"* — an
## 3. The founder-claim battery: nine partners, the charter, and the naming traps (STATUS: WRITTEN)

The popular origin story (nine partners departing J.P. Morgan & Co. after Glass-Steagall; a 1935 partnership
agreement; a charter) was tested against every held byte, pattern by pattern, commands at §10:

| claim component | measured on held bytes | verdict |
|---|---|---|
| the nine partners by name (`Beasley\|Steers\|Harold Stanley\|Whitney Straight\|Batterbee\|Cary\|Dunlop`) | **0 occurrences** across all 21 layers | **NO CARRIER in family (a)**. A partnership-departure story needs a print/manuscript carrier; none held. |
| literal `nine partners` | 0 occurrences | no carrier |
| `J.P. Morgan` adjacency to the origin story | exactly **1** `J.P. Morgan` string corpus-wide — a 1998 proxy holdings table (l.1734 of `0000950130-98-000790`), naming a different firm | the departure-from-JPM narrative is **uncarried**; the one occurrence is a neighbour-company decoy |
| `Glass-Steagall` | **2**, both in the FY1999 10-K (`0000950130-00-000882` l.816, l.10721), in the **1999 repeal** boilerplate ("…sections of the 1933 Glass-Steagall Act. Its passage allows commercial banks…") | a statute citation about Gramm-Leach-Bliley, **not** a 1935 origin recital — RD-124/RD-131 decoy class |
| a 1924 Morgan charter | `1924` = 6 lines, all attributed to Dean Witter & Co. or merged-company boilerplate (file list at §10); `Wrenflesley` 0 | **the 1924 date in this corpus belongs to Dean Witter, not to any Morgan split** |
| OCR "Moran" variant of Morgan (the JPMorgan probe's trap) | `Moran` → **3 hits, all `Moranta, Inc.`** (Georgia, 1979) in the subsidiaries exhibits of the FY1997/FY1998/FY1999 10-Ks — a real corporate name, not an OCR Morgan | tested before asserting; no Moran-decoy and hence no hidden Morgan naming in held bytes. The test does **not** extend to corpora not on disk. |

**Entity-adjacency discipline** (Morgan and Stanley are common surnames/place names): every promoted naming in this
probe is the full adjacency `Morgan Stanley` — **2,439** corpus occurrences — or `Dean Witter` (2,731). Bare `Stanley`
and bare `Morgan` were **not** promoted anywhere in this dossier. Decoys checked: `Stanford` 1 (a person-name table),
`Stanley Works` 0.

**Role/naming artefact, not founder claim** (the Goldman `SAMUEL SACHS` certificate rule): the one held periodical —
`sources/periodicals/gov.gpo.fdsys.CHRG-106hhrg66775_djvu.txt`, a 106th-Congress House hearing printed by GPO
(929,463 B; meta sidecar: fetched 2026-09-29T18:16:19Z, transport UNVERIFIED TLS) — names the modern brand 7 times,
always adjacency-bearing and always post-1997: e.g. l.170 *"Morgan Stanley Dean Witter & Co., Harvey B. Mogenson"*,
l.8818 *"statement of Harvey B. Mogenson, Managing Director, Morgan Stanley"*. That is a **1999-2000 hearing
testimony listing — a role naming of an officer, zero origin content**, and the file's own subject (U.S. tax rules
and international competitiveness) post-dates the Stage-1 window by half a century. Recorded as artefact;
in-window content from it = **0**. STATUS: WRITTEN

## 4. Five-family verdict — each family explicit; no untried family reported as a null (STATUS: WRITTEN)

| Family | State | Measured basis |
|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED** (for what it is): in-window origin text **0**, recital text strong | Full walk, 110,365 rows, perimeter 1993-11-08→2026-10-06, 0 rows before 1960 — the Stage-1 window is below EDGAR's floor, a **measured perimeter**, not a silence claim about the firm. Forward recital pass stored 20 docs 1996-2001; they carry the two-line history (§2), class RETROSPECTIVE, earliest recitation 1997. |
| **(b) Web archives** | **UNTRIED** | No `sources/web_archive/` directory exists (`ls -d` → No such file); 0 calls made. Not a null. Wayback floor (~1996) is in any case ~50 years past the window. |
| **(c) Periodical corpora** | **TRIED–UNANSWERED/partial** — remedy named | Fleet index measured today: **79 candidate rows** for morganstanley (header enumerated; `Counter` at §10): internet_archive TIER1_CANDIDATE 35, LEAD_ONLY 20, UNANSWERED 2, NULL 1; google_books 12; chronicling_america 2 UNANSWERED (`SKIPPED: hard stop: 5 consecutive failures (host halted)`) + 2 ERROR-404-with-saved-body; hathitrust 1 UNANSWERED (host halted). Local mine `research/A4_harvest_mine.md` (mtime **2026-09-29 23:46:19 +0530**, re-read immediately before quoting): 32 candidates at its moment, **6 mined, 25 untried at `--limit`**, verdicts 1 TIER1_CANDIDATE_TEXT (the 1999 GPO hearing, out-of-window) + 5 UNANSWERED (HTTP 503/401). **The one genuinely in-window item is `PvyrwBlrrQUC`, "Standard Corporation Descriptions", dated 1940 — UNANSWERED at HTTP 503, never opened.** In-window Tier-1 text returned: **0**. |
| **(d) Digitised corporate print** | **TRIED–UNANSWERED — never NULL (RD-130)** | `sources/corporate_print/` holds **0 files**. Fleet CP rows: 1 UNANSWERED (`global max-requests cap 400 reached`), 1 NULL whose own wording is `numFound=0 FOR THESE EXACT PARAMS ONLY` under the task's `year_range [1920, 2000]` facet (measured in `tools/queries.json`: both morganstanley CP tasks are year-faceted) — per RD-130 a faceted zero is a statement about our parameter; 1 TIER1_CANDIDATE = `internetadvertis00mary` (1997 "The internet advertising report" — out-of-window, and it mined as UNANSWERED HTTP 401). A facet-free CP run has **never** been executed for this company. |
| **(e) Auction / museum / manuscript** | **UNTRIED** | No directory, no query block (`tools/queries.json` has 8 morganstanley tasks, none manuscript-class), and no verified tool reaches it on 0 web budget. The documents this family uniquely holds — the 1935 partnership agreement, the 1941 reconstitution papers, 1924-1941 Morgan/Wrenflesley-era records — are exactly what family (a) structurally cannot supply. |

STATUS: WRITTEN

## 5. Per-stage tiers — measured against each stage's own window (RD-112) (STATUS: WRITTEN)

- **Stage 1 (origin, PROPOSED 1924-01-01→1950-12-31): T3 — register — PROVISIONAL.** Families returning in-window
  Tier-1 text = **0 of 5**. (a) answered but is out-of-window by construction (EDGAR floor) and its recitals are
  1997-2000 retrospectives; (c) and (d) TRIED–UNANSWERED with named remedies; (b) and (e) UNTRIED. §15.2: ≤1 → T3.
  **Provisional** is the honest word: three families were never answered, and (c) holds one unmined 1940 item that
  could single-handedly make history (it would be the corpus's first in-window naming).
- **Planning note for later stages (not this probe's tier):** any stage window containing **1996-08-01→2001** puts
  family (a) in-window with Tier-1 density (S-4/A, 424B2, five 10-Ks, DEF 14A) — but those narrate the **merger and
  the paper lines**, i.e. the registrant's self-history of the 1997 event, contemporaneously. A 1969-1986 window
  would sit inside EDGAR's floor but outside our stored set's floor (1996) and mostly outside EDGAR's too — the
  brand-line registrant (Morgan Stanley Group Inc.) may hold earlier paper under **its own CIK**, which our intake
  has not enumerated (§6).
- **Dispatch arithmetic:** Stage 1 is 3-4 agent runs at 8k w/stage. 15-20 runs would be issued only on a false T1 —
  and no family a 0-web probe can run reaches T1 for a 1924-1950 origin (structural, as in the JPMorgan probe).

## 6. Untried — must be re-approached, never re-declared empty (STATUS: WRITTEN)

1. **Family (d) corporate print, facet-free** — never run for morganstanley (both CP tasks carry `year_range
   [1920,2000]`; RD-130 says a faceted zero is not an answer). The class of document that flipped Boeing/Kroger/
   Walmart tiers is a bank's own printed house/anniversary history and its annual-report run; a 50th-anniversary
   history (if it exists for 1975-or-1985 vintages) is ONE retrospective lineage however many copies surface (§3).
2. **Family (c): the 25 candidates `harvest_mine` left untried at its `--limit`** (A4, mtime 2026-09-29 23:46:19
   +0530), and the index as it stands today (79 rows) minus the 6 mined — including every retry of the five
   HTTP-503/401 items. Highest-priority untried byte: **`PvyrwBlrrQUC` Standard Corporation Descriptions, 1940** —
   in-window by its own metadata.
3. **The brand-line registrant** — CIK 895421's paper answers as Dean Witter Discover (§2); "MORGAN STANLEY GROUP
   INC" / "MORGAN STANLEY INC" / "MORGAN STANLEY HOLDINGS" are not in its `former_names` (measured: 0 occurrences of
   either string in `_registrant_CIK0000895421.json`) and no separate index for them exists under this company-dir.
   Their EDGAR paper (1993-1996 shell era at best; the 1986 IPO is pre-EDGAR-floor either way) has never been listed.
4. **Family (b) web archives** — 0 calls; no directory; a CDX pass has never been opened for this company.
5. **Family (e)** — 0 calls; no tool; finding aids for the 1935 partnership papers and for J. P. Morgan & Co.
   partnership records (the departure side of the story) are outside every scripted route here.
6. **SEC tail of the forward pass** — `_UNANSWERED.csv` = 11 rows, all document-level 404s on SGML/primary paths
   (e.g. rank 14 `0000950103-00-000710:0001.txt`, "NoSuchKey" on three path forms); `_SKIPPED.csv` = 104 rows marked
   "beyond --max-docs" — the forward window's 135-attempted stream was cut at 20, so filings between 1996 and 2020
   beyond the cap were never opened. STATUS: WRITTEN

## 7. FETCH REQUESTs — script-owned lanes; declining is correct behaviour (STATUS: WRITTEN)

```
FETCH REQUEST: periodical_harvest --company morganstanley --facet-free
  (family (d): re-run the two CP tasks WITHOUT year_range; RD-130. Also re-run the CA tasks once the host halts
  stop: 2 UNANSWERED + 2 ERROR-404 rows currently bound the CA answer.)
FETCH REQUEST: harvest_mine --company morganstanley --limit 79
  (raise past the --limit 6/32 slice; fleet lane owns this file — this probe deliberately did not run it;
  priority list: PvyrwBlrrQUC 1940, houseofmorganame0000cher 1990 (J.P. Morgan line, adjacent lineage),
  19890828-robert-baldwin-morgan-sta (oral history), witterunilifeblood00jeanrich 1967 (Witter naming),
  internationaldir0033unse (International Directory of Company Histories vol 33, 2000).)
FETCH REQUEST: sec_intake index "MORGAN STANLEY GROUP INC" --company-dir founders_playbook/01_companies/company_039_morganstanley
  ONCE; artefacts are CIK-keyed so the CIK0000895421 index cannot be clobbered; if the floor comes back 2020s,
  the ticker trap fired and re-resolve by name (RD-135 / XOM precedent).
FETCH REQUEST: a manuscript/auction route (no tool exists) for: the Morgan Stanley & Co. 1935 partnership
  agreement / 1941 reconstitution papers; any 1924-1941 securities-house charter record; the firm's own
  anniversary/house history in print. Names without bytes in this dossier.
```
STATUS: WRITTEN

## 8. Refused to claim (and why) (STATUS: WRITTEN)

- **1924 as a Morgan Stanley founding date.** Refused outright. On held bytes 1924 is exclusively **Dean Witter &
  Co.'s organization year** (6/6 lines; S-4/A l.4739 is the carrier). The brief's "1924 split from J.P. Morgan & Co."
  has **no carrier of any kind on disk** (`Wrenflesley` 0, JPM-adjacency 0). Importing it would be the Ford/Citi
  error — a tool constant or a popular memory dressed as evidence.
- **1935 (or 1924) as settled fact.** Refused. Class **RETROSPECTIVE SOURCE / FOUNDER CLAIM**, confidence **Low**:
  every carrier is a 1997-2000 registrant self-narrative, two authoring lineages (§2), none in-window.
- **The nine partners, their departure, or any named partner.** Refused — 0 occurrences; a partner roster cannot be
  written from general history here.
- **Corroboration inflation.** Refused: five carriers ≠ five witnesses (two lineages, §3); the three
  `0000950134-01-001364` documents are ONE 2001 filing; 2,439 `Morgan Stanley` occurrences across post-1996 filings
  name a brand, not an origin.
- **"J.P. Morgan & Co. Incorporated" at DEF 14A l.1734 as an ancestor naming.** Refused — a holdings-table line
  naming a different legal person (the JPMorgan probe's own registrant, if anything).
- **`Moranta, Inc.` as an OCR "Morgan" variant.** Refused both directions: it is a real Georgia subsidiary, and I do
  not extend the tested-absent result to corpora not on disk.
- **Any of (b)(e) as a null; (d)'s faceted NULL as a null; "the company filed nothing pre-1960".** Refused —
  measured perimeter / UNANSWERED / UNTRIED respectively (RD-130, RD-134, NR-1).
- **"2 periodicals" from my brief.** Published measurement instead: **1** held periodical layer. STATUS: WRITTEN

## 9. Route most likely to change the verdict (STATUS: WRITTEN)

**Retry the already-indexed in-window periodical item `PvyrwBlrrQUC` ("Standard Corporation Descriptions", 1940) —
currently a bare HTTP-503 UNANSWERED on the fleet's own index — backed by the facet-free corporate-print run.** A
1940 corporation-directory naming of "Morgan Stanley & Co." would be the corpus's **first in-window Tier-1 text**,
moving family (c) to TRIED–ANSWERED and Stage 1 from T3 to T2 without touching any retrospective-lineage assumption;
the corporate-print run is what could make it two families and adjudicate the 1935-then-partnership question the
filings cannot. Both routes are cheap, script-owned, and already have candidate rows — they were refused by
transport (503/401) and by our own YEAR facet, not by the archive. STATUS: WRITTEN

## 10. Provenance of the numbers I published (commands → outputs) (STATUS: WRITTEN)

All greps run from `founders_playbook/01_companies/company_039_morganstanley/` unless stated; `sources/sec/*.txt` +
`sources/periodicals/*.txt` = the 21 held text layers.

- Index enumeration: `python -c` over `sources/_index/submissions.csv` → `HEADER: ['filingDate','form','accession',
  'reportDate','primaryDocument','source']`, `rows 110365`, `min date 1993-11-08 max date 2026-10-06`; distinct
  `source` = 46 slice files + `recent`; `rows <1960: 0`. `_registrant_CIK0000895421.json` read verbatim (§1); guard
  `ok` with de-spaced-slug reason (RD-135 fix visible). `_INDEX.md`: "UNANSWERED slices … (none)".
- `_RUN.json`: window `1960-12-31..2020-12-31`, attempted 135 / stored 20 / unanswered 11 / skipped 104, identity OK,
  5,953,859 B / 766,236 w, built 2026-10-06T11:48:20Z. `_MANIFEST.csv` header enumerated
  (`rank,slot,cik,accession,file,path,bytes,words,status,form,filingDate,url,why,listing`), 20 `ok` rows, listed at §1.
- Recital greps: `grep -n -iE "incorporated in (the State of )?(Delaware|New York)|New York partnership|…"` →
  l.-references quoted at §2; `grep -n "1935"` → 3 lines (l.155 / l.4776 / l.217); `grep -n "1924"` → 6 lines;
  S-4/A l.4775-4784 read verbatim via `sed -n '4770,4795p'`; DWD 10-K l.203 + merged 10-K l.213-217 via `sed`.
- Adjacency battery (`for p in …; do grep -hoiEr "$p" sec/*.txt periodicals/*.txt | wc -l`): `J\. ?P\. Morgan|JP
  Morgan` → **1**; `Morgan Stanley` → **2,439**; `Dean Witter` → **2,731**; `merger of equals` → **8**; `Stanford` →
  **1**; `Stanley Works` → **0**; `Wrenflesley` → **0**; `Beasley|Steers|Harold Stanley|Whitney Straight|Batterbee|Cary|Dunlop`
  → **0**; `nine partners` → **0**; `Glass-Steagall` → 2 (l.816, l.10721, FY1999 10-K); `Moran` → 3 (all `Moranta,
  Inc.`, Georgia 1979).
- `grep -n -iE "MORGAN STANLEY GROUP|MORGAN STANLEY INC|HOLDINGS" sources/_index/_registrant_CIK0000895421.json` → 0.
- Shelf: `find periodicals -type f ! -name '*.meta.json' | wc -l` → **1**; `find corporate_print -type f | wc -l` →
  **0**; `ls -d web_archive` → No such file; `md5sum sec/*.txt periodicals/*.txt | sort | uniq -d | wc -l` → **0**.
- Fleet index (read-only; lanes owned elsewhere): `python -c` over `00_universe/harvest/candidates.csv` filtered
  `company == morganstanley` → 79 rows, header enumerated first (`company,source_family,query,item_id,title,
  date_or_issue,url,snippet_or_hitcount,http_status,classification,retrieved_at`), class Counter at §4(c); the CA/CP/HT
  rows' `SKIPPED: hard stop … (host halted)` / `global max-requests cap 400 reached` / `FOR THESE EXACT PARAMS ONLY`
  snippets quoted verbatim at §4. `tools/queries.json` morganstanley block: 8 tasks (CA 2, IA 2, CP 2, HT 1, GB 1),
  both CP tasks with `year_range: [1920, 2000]`.
- `research/A4_harvest_mine.md`: re-read immediately before quoting (mandated); mtime `2026-09-29 23:46:19.406 +0530`;
  numbers taken: 32 candidates / 6 mined / 25 untried / verdict classes as at §4(c). Today's 79-row count and its
  32-row count are both true at their own moments (JPMorgan precedent).
- Gates: `python tools/gates.py --company-dir founders_playbook/01_companies/company_039_morganstanley --checks
  csv,keys --fail-on substantive --out founders_playbook/03_quality_control/morganstanley_s1_probe_gates.md` →
  substantive checks PASS; 2 of 2 checks reported coverage-only findings ("expected for a freshly probed company",
  not failing on `--fail-on substantive`).
- Transport caveat carried from every sidecar: `"transport": "UNVERIFIED TLS"` — no confidence in this file is set
  above Medium on byte-reads alone (JPMorgan probe's rule).


