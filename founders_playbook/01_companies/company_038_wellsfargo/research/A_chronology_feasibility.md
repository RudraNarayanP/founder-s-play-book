# A — Chronology feasibility probe: Wells Fargo (Fortune rank 38)

Owner: `probe-wellsfargo`. Stage-1 PROBE only — no volume, no registers, no ids, no certification.
Company dir (absolute): `E:\founder's playbook\founders_playbook\01_companies\company_038_wellsfargo`
All `sources/...` paths below are relative to that directory.

**CONFIDENCE CAP (binding on every line here).** Nothing in this dossier is stated above **Medium**.
The 7 Internet Archive text layers under `sources/periodicals/` all carry sidecars reading
`"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"` (measured with
`json.load(...)['transport']` over `sources/periodicals/*.meta.json`: 7 present, 7 UNVERIFIED).
The 58 SEC sidecars carry **no** `transport` field at all (measured: `Counter({'(absent)': 58})`),
so SEC bytes are on-disk-and-hashed but not TLS-attested either. Every SEC count below is a
disk measurement, not a transcript figure.

**Two web calls were made by scripts, zero by this agent.** `tools/ia_text.py` (list-files, fetch) and
`tools/legacy_cik.py` (search) are the sanctioned script forms; `harvest_mine.py` and
`periodical_harvest.py` were **not** run, per the brief. Six new text layers were added to
`sources/periodicals/` by `ia_text.py fetch` this pass (commands in §4); nothing was deleted, moved
or renamed. Add-only.

STATUS: WRITTEN

---

## 0. Counts, each with the command that produced it

| count | value | how it was measured |
|---|---|---|
| files in the company dir now | **149** | `glob <dir>/**/* ` + `os.path.isfile` |
| SEC submissions indexed | **17,483 rows** | `csv.DictReader` over `sources/_index/submissions.csv` |
| index filing-date perimeter | **1994-01-12 → 2026-10-06**, 0 empty dates | `min/max` of `filingDate` over those rows |
| archive slices read | **10** (`recent` + `-001…-009`), **0 UNANSWERED** | `Counter(r['source'])`; `_INDEX.md` "UNANSWERED slices: (none)" |
| filings before 2001-01-01 / before 1997-01-01 | **731 / 376** | counted over `filingDate` |
| SEC text layers stored | **58 `.txt` + 58 sidecars**, 53 distinct accessions | `glob sources/sec/*.txt`, `*.meta.json` |
| stored SEC bytes / words | **21,647,455 B / 2,734,996 words** | `os.path.getsize`, whitespace split |
| stored SEC filing span | **1994-01-12 → 2000-07-18**, all `http_status` 200 | sidecar `accession` joined to index `filingDate` |
| IA text layers stored | **10** (`sources/periodicals/`) | `glob`; 1 pre-existing + 9 fetched this pass (8 `ok`, 1 `UNANSWERED` HTTP 401) |
| candidate rows for this slug | **95** (of 4,706 csv rows) | `csv.DictReader` over `00_universe/harvest/candidates.csv`, `company == 'wellsfargo'` |
| distinct `item_id`s in those rows | **79**; mined by the harvest pass: **6** | set-comparison against `sources/harvest_mine/_index.json` `items` |
| byte-identical duplicate layers | **0 groups** | md5 over all **68** `.txt` under `sources/` (58 SEC + 10 IA), 24,090,042 B total (rule 4) |

**CSV headers enumerated before any field was read** (hard rule 3).
`sources/_index/submissions.csv` header, printed from `fieldnames`:
`filingDate, form, accession, reportDate, primaryDocument, source` — six columns, no
`query_label` / `period_or_date` / `source_query`.
`00_universe/harvest/candidates.csv` header:
`company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification, retrieved_at`.

STATUS: WRITTEN

---

## 1. INTAKE STATE — the refusal was the guard, and the retry pass landed

The fleet record still says the intake failed. It is stale on disk:
`00_universe/_FLEET_INTAKE.tsv` → `wellsfargo … rc1/inwindow0/UNANS0 … no document stored; identity
guard refused the write; … REFUSED`, and `_FLEET_INTAKE_lane2.log` repeats it. **Neither line describes
the corpus now.** `00_universe/_IDENTITY_FIX.log` prints the refusal text twice:

> `*** REFUSED-WRONG-REGISTRANT: EDGAR answered 'WELLS FARGO & COMPANY/MN' for CIK 0000072971 but this directory is 'company_038_wellsfargo'. Everything went to …\sources\_index\quarantine\CIK0000072971; no canonical index was touched.`

That is RD-135's own diagnosis: the guard required a whole word of the registrant name to equal the slug
token, and no word of `WELLS FARGO & COMPANY/MN` is `wellsfargo`. It was refusing the **correct** registrant.

**Quarantine read (it is a full corpus, not an empty result).** `sources/_index/quarantine/CIK0000072971/`
holds the 2026-09-29 19:30 UTC artefacts: `_registrant_CIK0000072971.json` with
`"guard": "quarantine"`, `"count": 17418`, and the reason string quoted above; `_INDEX_CIK0000072971.md`
(5,410 B); `submissions_CIK0000072971.csv` (1,659,379 B, sha1 `70713b164d0c`). Same CIK, same registrant,
65 fewer filings than the retry. Nothing in quarantine contradicts the canonical index; it is the older
snapshot of the same answer, kept out of the canonical path by the tool. **Left exactly where it is.**

**The canonical index exists.** `sources/_index/_registrant_CIK0000072971.json`, built
`2026-10-06T11:49:55Z`: `"guard": "ok"`, guard reason `"slug token(s) ['wellsfargo'] match registrant
'WELLS FARGO & COMPANY/MN' (CIK 0000072971)"`, `count 17483`, `csv_sha1 285df4aff827…`.
`_INDEX.md` line 6 prints the same guard verdict and line 91 says **UNANSWERED slices: (none)** — so the
RD-134 slice-walk cap is not truncating this registrant: 10 slices, and the oldest slice
(`-009`, 256 rows) reaches `1994-01-12`. **No `index` re-run was needed and none was done.**
EDGAR's own floor is the binding perimeter here, not the walk: the measured floor is
**1994-01-12** and it is reported as a perimeter, not as "Wells Fargo filed nothing before 1994".

`sources/_index/submissions.csv` and `_INDEX.md` are **byte-identical** to
`submissions_CIK0000072971.csv` and `_INDEX_CIK0000072971.md` (sha1 equality measured True for all three
pairs, `legacy_copy_written: true`). Duplication, not a second registrant — the RD-098 shape, harmless today.

**Two defects in the run record, measured not inherited.** `sources/sec/_RUN.json` (built
`2026-10-06T11:50:53Z`, window `1998-12-31..2020-12-31`, `--max-docs 30`):

1. `"identity_ok": false` — `"stored(28) + unanswered(3) + skipped(108) = 139 vs attempted(139) -> BROKEN"`.
   The arithmetic *does* foot to 139; it is BROKEN because of `duplicate_slots:
   ["nameless:0000940180-00-000552:3365 in skipped and skipped"]` — one nameless slot counted twice.
   This is RD-112 defect 2's class (nameless-row bookkeeping) seen from the other side: the self-check now
   **fires**, and it fires on a double-count rather than a drop. Stored counts cannot be taken from this
   record; the 58-doc/53-accession figures in §0 are disk measurements.
2. `sources/sec/_UNANSWERED.csv` (3 rows) lists `0000072971-00-000027` and `0000072971-00-000028` as
   `UNANSWERED … 404 … / HTTP 403` — but **both accessions are on disk** in `sources/sec/` with
   `http_status: 200` sidecars (30 doc-files at mtime 11:49 from the in-window pass, 28 at 11:50 from the
   recital pass). The run record and the disk disagree; the disk wins for coverage, the run record wins
   for "what this one pass did". Third row is honest and important: `UNANSWERED NOT-ENUMERATED:
   5411 in-window filings were never listed because --max-docs 30 was reached`.

**The recital route already ran and already answered.** The forward pass (window 1998-12-31..2020-12-31)
put on disk the two filings that print the founding sentence — `sources/sec/0000912057-00-012168_…txt`
(FY1999 10-K, filed 2000-03-17) and `sources/sec/0001047469-99-010171_…txt` (FY1998 10-K405, filed
1999-03-17). §3 quotes them. No further intake run is required for the verdict.

STATUS: WRITTEN

---

## 2. What the corpus now holds for 1852-1905 — five pre-1905 express-era layers, opened this pass

`sources/corporate_print/` was **empty** when this pass started (measured: 0 files) and
`sources/periodicals/` held one layer. The harvest index already carried entity-adjacent express-era items
that no agent had opened. Three were reachable by `tools/ia_text.py list-files` (each reporting
`"text_layers": 1`) and fetched with `tools/ia_text.py fetch … --insecure`. All three name
**`Wells, Fargo & Company`** — with the comma — the express-era form, not the registrant's form.

### 2.1 `sources/periodicals/tariffstablesofd00wellrich_djvu.txt` — 24,865 B, 4,158 lines — 1868, company-issued

```
L7    | TARIFFS
L10   | WELLS,  FARGO  &  COMPANY'S
L13   | OVERLAND    EXPRESS.
L18   | J.  O.  SEYMOUR  &  CO.,  PRINTERS,  9  AND  11  NASSAU  ST.
L20   | 1868.
L112  | 2   WELLS,    FARGO   &   CO.?S   OVERLAND   EXPRESS.     (running head, repeated ~30 pages)
L1026 | Note.- The above points from Salt Lake City, are all within the lines of the California
        and Oregon Express, and charges are, in all cases, in gold coin.
```

Whitespace-normalised census: `wells, fargo` **46** · `fargo & co` **45** · `overland` **30** ·
`freight` **20** · `gold coin` **1** · `1852` **0** · `founded` **0** · `incorporated` **0**.
A rate table from Omaha westward, printed in New York. **The earliest company-issued naming of the express
person on this disk** — an 1868 *document*, not a recital: the entity existed and was printing tariffs under
that name, and it carries its own monetary basis ("in gold coin"), so the gold-vs-currency question does not
have to be inferred. It states no founding date and no state of incorporation.

### 2.2 `sources/periodicals/wellsfar00well_djvu.txt` — 94,994 B, 3,758 lines — 1882, company-issued

IA title "Wells, Fargo & co's express. 1882. Instructions. For the use of …". At line level:
L1/L3 "James Heron, / Secretary, San Francisco."; L50 "WELLS, FARGO & COMPANY"; L63 "C. F. Crocker, |
J. C. Fargo,"; L94 "The business of Wells, Fargo & Co.'s Express is to forward, by…".
Census: `wells, fargo` 46 · `express` 66 · `freight` 23 · `gold coin` 1 · `gold dust` 1. Front matter OCR is
degraded (L6-L13 are library-stamp noise), so **no date is claimed from the body**; the 1882 is the item's
title date, which is a metadata statement and is flagged as such. `C. F. Crocker` and `J. C. Fargo` are
**officers named in an instruction booklet — roles, not founders** (RD-116).

### 2.3 `sources/periodicals/catahist00well_djvu.txt` — 97,830 B, 2,092 lines — 1893, company-issued: the load-bearing layer

"Wells, Fargo & Company — Catalogue … Historical Exhibit, Etc. at the World's Columbian Exposition, Chicago,
Illinois, U.S.A." (L1-L14; L155 "Chicago, Ill., 1893."). The company exhibiting **its own history 41 years
after 1852**:

```
L32-43  "Wells, Fargo & Company, Organized 1852. / Express and Banking. / Incorporated 1866. /
         Cash Capital and Surplus, $6,2^0,000."   <- L43 OCR-broken: a figure to foot, never to quote
L126-129 "The founding of Wells, Fargo & Company dates back to the spring of 1852, when Henry Wells,
         Wm. G. Fargo, John Livingston, D. N. Barney and others … organized a company bearing that name,
         with a capital of $300,000, to do an express and banking business in California"
L168-176 1845 "Wells & Co's Western Express"; 1850 "Wells & Co., Livingston & Fargo and Butterfield,
         Wasson & Co. combined their interests and organized a joint stock company, to be known as the
         American Express Company … and Mr. Wells was elected President. In 1852 he was chiefly
         instrumental in forming another organization, known ever since as Wells, Fargo & Company"
L208-212 "E. B. Morgan, of Aurora, N. Y., First President of Wells, Fargo & Co., from March 18, 1852,
         to November 25, 1853"
L265-274 "Louis McLane, Fourth President, from February 18, 1867, to February 18, 1868 … Upon the
         consolidation of Wells, Fargo & Co., The Holladay Overland Mail and Express Co., the Overland
         Mail Co., and the Pioneer Stage Co., under the title of Wells, Fargo & Co."
L1031    "91. Wells, Fargo & Co's First Advertisement, 1852. (Photographed.)"
L1055    "…among the proprietors of which were Henry Wells, and Wm. G. Fargo, who subsequently founded
         Wells, Fargo & Co."   (an 1845 way-bill receipt, exhibited)
L141 / L711-712 "established the famous Pony Express" / "…and consequent Discontinuance of the Pony
         Express. Also, a Pony Express Notice, dated April 18, 1860."
L509     the only "earthquake" here describes a gas/wagon incident ("…under the impression that it was
         an earthquake") — it is NOT the 1906 San Francisco earthquake
```

**What it settles, what it does not.** It is the first held artefact to print `Organized 1852` **and**
`Incorporated 1866` side by side — the company itself distinguishing the 1852 association from an 1866
corporate act. It names **four** organizers (Henry Wells, Wm. G. Fargo, John Livingston, D. N. Barney),
against the modern filings' two. It prints an express-era consolidation chain (Holladay Overland Mail and
Express Co. / Overland Mail Co. / Pioneer Stage Co. → "the title of Wells, Fargo & Co.") anchored on the
1867-68 McLane presidency. **Every one of those dates is printed in 1893.** Class: RETROSPECTIVE
INTERPRETATION at Tier-1 carrier strength — Citigroup's 1910-volume position exactly, and the Target/B1
warning binds verbatim: an 1893 statement about 1852 is not an 1852 document. Independence: L35, L41,
L126, L208 and L272 are five statements in **one** document → corroboration count **1**.

**Entity adjacency, measured (trap 2).** Across the three express-era layers `wells, fargo` = 46 / 46 / 70
while bare `wells` = 37 / 47 / 85 — the adjacency is real naming, not surname noise. The name form in the
1868-1893 print is `Wells, Fargo & Company` (comma); in the 1994-2000 filings it is `Wells Fargo & Company`
(no comma). `wells fargo` (no comma) = **0** hits in `wellsfar00well`; `wells, fargo` is the only form in the
1868 tariff. **A grep for one form silently misses the other — any later pass must run both.**

**A4's promoted row, re-read (A4 read in full before quoting).** A4 L5 says "35 candidate rows in the
harvest index; 6 items mined; 27 left untried" and A4 L25 labels `01.-wells-fargo-annual-report-archive`
**in-window / TIER1_CANDIDATE_TEXT** at 1,195,717 B. Three corrections:

1. `candidates.csv` now carries **95** rows for `company == 'wellsfargo'` (of 4,706 total rows). 6 mined →
   **89 never mined**. A4's 35/6/27 was true of the index when A4 ran; the fleet reharvest (RD-130/RD-134)
   grew it. Inherited, not adopted.
2. Those bytes are the **2018 Annual Report**. Sidecar URL:
   `…/Wells%20Fargo%20%26%20Company%202018%20Annual%20Report%20V2_djvu.txt`; at line level L28
   "2018 FINANCIAL REPORT", L511 "February 15, 2019", L2866-2867 "…$1.90 trillion in assets. Founded in
   1852 and headquartered in San Francisco…". The `title:1919` / "in-window" label is the **IA item title**
   ("Wells Fargo & Company Annual Reports: 1919-") echoing — RD-124's column-echo class — and A4's own
   footnote L32 already warns the scan date is often the digitisation year. **A4's only
   `TIER1_CANDIDATE_TEXT` row is post-boundary, and its `in-window` cell was wrong.**
3. That item has **30 text layers**, not one (`list-files` measured): 1919, 1987, 1998, 1999-2016, 2017-2021
   "V2", 2022-2024. The 1919 and 1987 layers are genuinely in-window and had never been fetched. §2.4 opens
   them.

### 2.4 The two in-window annual-report layers, opened

**`sources/periodicals/01.-wells-fargo-annual-report-archive__Wells_Fargo_Company_WFC_Annual_Report_1919_djvu.txt`
— 23,931 B, 1,076 lines.** Not one year: fiscal-year headers at L22 (FY1919), L258 (1920), L532 (1921),
L711 (1922), L940 (1923) — a bound layer spanning 1919-1923 (RD-124's bound-run class, in reverse).
The most consequential content of this pass — the express person describing its own exit:

```
L47   "The income for the year, aside from the item of express operations in Cuba, was derived solely
        from investments and real estate."
L52   "…the Company was still engaged in general express operation during the first half of 1918."
L55-56 "The adjustment of the Company's outstanding accounts for the period of its operations prior to
        its enforced retirement from the express business on June 30, 1918 …"
L58-60 "…the accounting and agency work, by an agreement with that Company, was done by the American
        Railway Express Company on the basis of actual cost."
L90-92 "The only real estate owned by the Company, aside from an office building in Portland, Oregon, is
        certain unimproved lots in San Francisco, Calif., … both of which came into the Company's
        possession through one of its former banks."
L559  "…and $90,000 from Wells Fargo Nevada National Bank stock for the first half of 1921. This bank
        stock was disposed of during the latter half of the year for $3,000,000…"
L178-180 "Capital Stock: Authorized …$24,000,000.00"
L975  "At the meeting of stockholders held on February 6, 1923, action was taken reducing the capital stock"
```

So the 1919-1923 "Wells Fargo & Company" is a company **out of the express business since June 30, 1918**,
living on American Railway Express shares and real estate, selling its `Wells Fargo Nevada National Bank`
stock. It prints the banking successor's **period name** — `Wells Fargo Nevada National Bank`, a string that
occurs **0** times across all 58 held SEC bytes. Trap (1) gets a first-party carrier: the express-era person
went out of the express business and was liquidating assets while the name sat on a bank with a different
name.

**`…_Annual_Report_1987_djvu.txt` — 170,502 B.** L22 "WELLS FARGO & COMPANY AND SUBSIDIARIES"; L327
"our home state of California". `1852` **0** · `founded` **0** · `stagecoach` **0** · `history` 2 (both in a
deferred-tax sentence). The 1987 California bank's own report carries **no founding narrative at all** — a
measured silence, and evidence that the "Founded in 1852" sentence is a late-1990s onward habit, not a
long-running disclosure practice.

**`…_Annual_Report_1998_djvu.txt` — 344,832 B.** The first report of the merged company; prints both the
revival and the merger:
```
L83-86   "product of 1,500+ mergers in 147 years including, / most recently, the merger involving Norwest
          … presents combined results as if the merger had been [in effect for all periods presented]"
L104-108 "Our trademark, the stagecoach, is the symbol of Wells Fargo's role in the development of the
          Western United States … a hallmark of our company since 1852."
L208-209 "Your new company — the result of the recent merger / of equals involving Norwest Corporation and
          Wells Fargo & [Company]"
L267-291 "two entrepreneurs named Henry Wells and William G. Fargo … 147 years ago after the California
          gold rush. They helped create the U.S. service economy — by reducing time and distance relative
          to money."
L11480-11481 "THE COACH The stagecoach - symbol of Wells Fargo since 1852 - originally made in Concord, N.H."
```
**Arithmetic tension, recorded not resolved:** "147 years ago" measured from 1998 lands on **1851**, while
the same document says "since 1852" (L108) and "Founded in 1852" appears in the later reports. One document,
two implied years, no basis printed for either. ESTIMATE/DERIVED at best; the derivation must be shown.

STATUS: WRITTEN

---

## 3. The registrant's own filings print a name revival — quoted, and attributed to a legal person

**Which legal person is CIK 0000072971.** Every one of the 58 held SEC documents resolves to
CIK `0000072971`, and the conformed name on that CIK is **`NORWEST CORP` for every filing dated
1994-01-12 → 1996-04-26** and **`WELLS FARGO & CO/MN` for every filing dated 1999-01-19 → 2000-07-18**
(per-file identity table measured over the SEC headers; `STATE OF INCORPORATION: DE` on 53 of 58).
Norwest Center, Sixth & Marquette, Minneapolis MN is the business address on the 1994 cover pages
(`sources/sec/0000072971-94-000003_…txt` L36, L81-85).

**The name-change chain the registrant's own header prints** — `sources/sec/0000072971-99-000001_…txt` L48-54:

```
FORMER COMPANY:  FORMER CONFORMED NAME: NORWEST CORP            DATE OF NAME CHANGE: 19920703
FORMER COMPANY:  FORMER CONFORMED NAME: NORTHWEST BANCORPORATION DATE OF NAME CHANGE: 19830516
```

**Those header dates are not corporate acts, and one of them is measurably a system stamp.**
`DATE OF NAME CHANGE: 19920703` occurs on **118 FORMER CONFORMED NAME rows across 12 other companies'
trees** in this repository (`grep -rh -B1 … founders_playbook/01_companies/*/sources/sec/*.txt`), attached
to 15 unrelated registrants — `AMERICAN TELEPHONE & TELEGRAPH CO`, `BELL ATLANTIC CORP`,
`CHEMICAL BANKING CORP`, `DELL COMPUTER CORP`, `MELLON BANK CORP`, `MELVILLE CORP`, `PRIMERICA CORP /NEW/`,
`SALOMON INC`, `SOUTHWESTERN BELL CORP`, `URCARCO INC`, `FIRST UNION CORP`, `FIRST GOLDEN BANCORPORATION`,
`FUND AMERICAN ENTERPRISES HOLDINGS INC`, `CARDINAL DISTRIBUTION INC`, `NORWEST CORP`. Fifteen unrelated
companies did not all rename on 1992-07-03; that is EDGAR's backfill date. `19830516` by contrast appears
in **51 files, all of them in this company's tree** — but the same caution binds. **Neither header date
may be published as the date the company took the Wells Fargo name.** Class: FACT for the *existence of
the name-change record*; the event date is **UNKNOWN** from family (a) headers.

**The event date is carried by narrative, not by the header.** Two independent filings print it:

- `sources/sec/0000072971-99-000019_…txt` (SC 13G/A, filed 1999-02-16) L178-182:
  > "On November 2, 1998, Wells Fargo & Company merged into WFC Holdings Corporation, a wholly-owned
  > subsidiary of Norwest Corporation. WFC Holdings Corporation was the surviving company in the merger.
  > Immediately after the merger, Norwest Corporation changed its name to Wells Fargo & Company
  > (Wells Fargo-post-merger)."
- `sources/sec/0000912057-00-012168_…txt` (FY1999 10-K, filed 2000-03-17) L237-241:
  > "On November 2, 1998, the merger involving Norwest Corporation and Wells Fargo & Company (the Merger)
  > was completed. Norwest Corporation changed its name to 'Wells Fargo & Company' and the former Wells
  > Fargo & Company (the former Wells Fargo) became a wholly-owned subsidiary of Norwest Corporation."

**And the two registered persons are distinguished by file number in the same 10-K** — L1323-1326:
> "The Company's SEC file number is 001-2979. On or before November 2, 1998, the Company filed documents
> with the SEC under the name Norwest Corporation. The former Wells Fargo filed documents under SEC file
> number 001-6214."

So family (a) itself says: **the registrant is the ex-Norwest person (001-2979); the 1852-descended person
(001-6214) is a different registrant that became a subsidiary.** The 1852 line is not this CIK's origin; it
is a name the CIK acquired.

**What the registrant prints about 1852 — and to whom it attributes it.**
`sources/sec/0000912057-00-012168_…txt` L258-271 (and the same paragraph in the FY1998 10-K405
`0001047469-99-010171_…txt` L276-281 — one corporate record reprinted, **not** two witnesses):

```
L258 The former Wells Fargo's principal subsidiary, Wells Fargo Bank, N.A., continues
L259 to be a significant subsidiary of the new Company. The bank was the successor to
L260 the banking portion of the business founded by Henry Wells and William G. Fargo
L261 in 1852. That business later
L267 operated the westernmost leg of the Pony Express and ran stagecoach lines in
L268 the western part of the United States. The California banking business was
L269 separated from the express business in 1905, was merged in 1960 with American
L270 Trust Company, another of the oldest banks in the Western United States, and
L271 became Wells Fargo Bank, N.A., a national banking association, in 1968.
```

Read as a lineage statement rather than a date: **1852 is attributed to a business, not to the registrant;
the registrant's holding company descends from Norwest; the 1852 business reaches the registrant through
Wells Fargo Bank, N.A., which is a subsidiary of a company that was acquired.** The filing also prints the
break: the California banking business was **separated from the express business in 1905** — the express
company and the bank are two lines from that year forward, and the 1996 First Interstate acquisition
(L273-276) sits on the California line, not the Norwest line.

**Term census over all 58 held SEC bytes** (whitespace-normalised whole-text, per hard rule 8):
`1852` **2** · `henry wells` **2** · `william g. fargo` **2** · `pony express` **2** · `american trust` **2**
· `1905` **2** · `1960` **2** · `express company` **0** · `1906` **2** · `earthquake` **2** ·
`norwest` **19,185** · `wells fargo` **11,590**.
The 1852 sentence exists in exactly **two files**, and they are the same company's FY1998 and FY1999
annual reports. Everything else in family (a) is Norwest's own record.

**The `1906` hit is a decoy and must not be recycled.** Both occurrences are in
`sources/sec/0000912057-94-002538_…txt` (Norwest S-4/A, filed 1994-08-08) and belong to **Copper
Bancshares / The American National Bank of Silver City, New Mexico**: L729-733 "Bancshares is a one-bank
holding company organized under the laws of New Mexico in 1979 … Originally organized under New Mexico law
in 1906"; L2852-2853 "The predecessor to the Bank was incorporated as a New Mexico banking corporation on
March 2, 1906." The two `earthquake` hits are insurance/force-majeure boilerplate
(`0000950131-95-007777` L6165, `0000927356-00-000178` L7750). **Nothing in family (a) is a Wells Fargo
1906 record.** The 1906 earthquake-and-records story therefore has **no carrier in the corpus** and is
recorded UNKNOWN (§5), not as fact and not as a refutation.

**In the Norwest-era files, "Wells Fargo" is the *other* bank.** Three pre-merger occurrences, all read
at line level: `0000950109-94-000528` L1574 (a proxy peer-group index listing "Wells Fargo & Co." among 30
banks, alongside Norwest Corporation); `0000950131-95-003387` L2227 ("…and Wells Fargo & Company
(collectively, the 'Norwest Composite')" — a compensation peer set); `0000950131-94-001669` L12039 (a
peer list with Signet, SunTrust, U.S. Bancorp, Wachovia). Family (a) names Wells Fargo as a **comparison
group** before 1998 and as **itself** only after. That inversion is the registrant's own evidence that the
1998 event was a name acquisition, not a continuation.

STATUS: WRITTEN

## 4. What this pass added to `sources/`, and the command that added it

Eight layers were fetched successfully by this pass, plus one refusal recorded in U-1; a ninth arrived from a
concurrent writer and is accounted for in §13. All landed in `sources/periodicals/` — that is where
`ia_text.py fetch` writes; nothing under `sources/` was moved, renamed or deleted.

```
python tools/ia_text.py list-files --id <identifier> --insecure
python tools/ia_text.py fetch --id <identifier> --company-dir founders_playbook/01_companies/company_038_wellsfargo --insecure
python tools/ia_text.py fetch --id 01.-wells-fargo-annual-report-archive         --file "Wells Fargo & Company (WFC) Annual Report 1919_djvu.txt" ... (same for 1987, 1998)
```

| identifier | IA `year` | bytes | what the bytes actually are | in-window? |
|---|---|---|---|---|
| `tariffstablesofd00wellrich` | 1868 | 24,865 | company tariff, "Wells, Fargo & Company's Overland Express", printed Nassau St, New York, imprint **1868** (L20) | **YES** |
| `wellsfar00well` | 1882 | 94,994 | company express instructions, 1882; James Heron, Secretary, San Francisco | **YES** |
| `catahist00well` | 1893 | 97,830 | company exhibit catalogue, World's Columbian Exposition, Chicago 1893 | **YES** |
| `instru00well` | 1868 | 115,639 | "Instructions to agents and employes of Wells, Fargo & Co.'s Overland Express, with tariff of rates"; OCR badly degraded (L1 "OVERIAND EXPRESS", L14 "mSTEUCTlONS") | **YES** |
| `robertjdmackieag00alexrich` | 1884 | 91,961 | **third-party litigation print**: "Robert J.D. Mackie agst. Richard P. Lounsbery and Ben Ali Haggin, James B. Haggin, and Wells, Fargo & Co." — a California answer/admission; L82-83 "this defendant admits that the principal place of business of said corporation defendant was at and in the City of San Francisco"; L22-26 carries a "BANCROFT LIBRARY / THE LIBRARY OF THE UNIVERSITY OF CALIFORNIA" provenance stamp | **YES**, and it is the only **non-self-narrative** in-window naming of the express person |
| `01.-wells-fargo-annual-report-archive` × 3 layers (1919, 1987, 1998) | 1919 / — / — | 23,931 / 170,502 / 344,832 | see §2.4; the "1919" layer is a bound 1919-1923 run | 1919-run YES (Stage 2 as proposed below); 1987/1998 in the later windows |

Duplicate check (hard rule 4): md5 over all **68** held `.txt` gave **0 duplicate groups**, so none of these
is a re-shelved copy of another, and `instru00well` vs `tariffstablesofd00wellrich` are two different 1868
company printings, not one document twice. `instructionstoag00wellrich` (1868, "Instructions to agents and
employes of the **California and Oregon** Express") appeared in the same IA creator answer and is
**UNTRIED** — a third 1868 company printing nobody has opened (U-1).

STATUS: WRITTEN

---

## 5. Family (b) is NOT route-less any more — measured, and this slug is not in the domain ledger

`tools/cdx_intake.py` exists (Internet Archive CDX intake for family (b), storing into
`<company>/sources/web_archive/`). `tools/web_domains.json` carries `slugs` for exactly
**5** companies: `cencora, centene, elevance, marathon, microsoft` — **`wellsfargo` is absent**. Therefore:

- `python tools/cdx_intake.py enumerate --slug wellsfargo --company-dir <dir>` →
  `{"domain": "", "verdict": "UNTRIED", "http_status": 400, "note": "no domain supplied for this slug"}`.
  That is the tool telling the truth: **UNTRIED, not NULL.**
- Supplying a domain **cited from held bytes** — `wellsfargo.com`, printed in
  `sources/periodicals/01.-wells-fargo-annual-report-archive_djvu.txt` L32940 ("the internet (wellsfargo.com)") —
  `python tools/cdx_intake.py enumerate --domain wellsfargo.com --frm 1996 --to 1999 --company-dir <dir>`
  returned `http_status 200`, `verdict: ANSWERED`, `captures: 500`, `capped: true`
  ("this is a FLOOR, not a census"), earliest listed capture `19961226210910`.
  **No snapshot bodies were stored and no directory was created** — `enumerate` writes nothing, verified:
  `sources/web_archive/` does not exist after the call.

Consequence, stated narrowly: for the windows this probe is about (1852-1905) family (b) cannot help —
its measured floor here is **1996-12-26**, ~144 years after the organization act — but the fleet's standing
"family (b) has no route at all" claim is out of date, and a *later* stage window (1996-1998: the merger,
the renaming) is now reachable by a scripted route that has not been run for this slug. Registering the
cited domain in `tools/web_domains.json` is an **orchestrator action**, not mine; this probe edited no file
outside its own dossier.

STATUS: WRITTEN

---

## 6. Five-family verdict (every family gets a state; three states only)

| family | state | what was run, and what it returned | in-window Tier-1 text for the origin era? |
|---|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED** | canonical index on disk: 17,483 filings, perimeter **1994-01-12 → 2026-10-06**, 10/10 slices read, `UNANSWERED slices: (none)`; guard `ok`; 58 stored docs / 53 accessions / 21,647,455 B, all `http_status: 200`. Recital route ran (forward window 1998-12-31..2020-12-31). | **NO.** Measured floor 1994-01-12, ~142 years after the organization act. The family answers *whose* lineage (the Norwest line, §3), not the origin. |
| **(b) Web archives** | **TRIED–UNANSWERED** | `tools/cdx_intake.py` exists but this slug has **no** entry in `tools/web_domains.json` (5 slugs only), so `enumerate --slug wellsfargo` returns `UNTRIED / http 400 / "no domain supplied"`. Supplying a domain cited from held bytes (`wellsfargo.com`, §5) returned `ANSWERED, captures: 500, capped: true`, earliest **1996-12-26**. **No snapshot bodies stored.** | **NO**, and structurally cannot be: floor 1996-12-26. **Remedy:** register the cited domain (orchestrator), then `cdx_intake.py run --slug wellsfargo --frm 1996 --to 1999 --per-domain 3`. Not a null. |
| **(c) Periodical corpora** | **TRIED–UNANSWERED** | Chronicling America: **8/8** stored responses `http_status: 404` at 85,272-85,274 B (apology-page size class), on 2 query shapes × 4 nightly runs; `_CA_ENDPOINT_TEST.md` records **every** candidate shape `CHALLENGED 403` from this egress and "ANSWERED shapes: none". HathiTrust: **0** shelf responses for this slug; 1 candidate row `SKIPPED: hard stop: 5 consecutive failures (host halted)`. Google Books: 4 responses `200` (27,593 B feed, `totalResults=300`, 10 volumes returned) but every Wells-looking volume is `viewability=no_pages`; the 5 ids the mine attempted all died `HTTP 503 … 0 bytes`. | **NO text held.** Each route refused; none is empty. Remedies named (U-1, U-2). |
| **(d) Digitised corporate print** | **TRIED–ANSWERED — the only family that answers the origin era** | four company-issued pre-1905 printings now on disk (1868 tariff, 1868 Overland-express instructions, 1882 express instructions, 1893 exhibit catalogue), **plus one adverse third-party record (1884)**, plus a bound 1919-1923 annual-report run and the 1987/1998 reports (§2, §4). The harvest shelf's own corporate-print queries returned `numFound: 1` because they carry `AND YEAR:[1850 TO 1995]` and require a title word (`annual`/`report`) — RD-130's facet class again. Dropped both: `creator:("Wells, Fargo & Company") AND mediatype:(texts)` → `numFound: 12`, `creator:("Wells, Fargo")` → `numFound: 15`, five of them pre-1900. | **YES — 5 documents in-window** for a 1852-1905 origin window (1868, 1868, 1882, 1884, 1893): four entity-adjacent company printings and one adverse third-party record. |
| **(e) Auction / museum / manuscript** | **UNTRIED** | no tool in `tools/` reaches a sale-room or finding-aid system and this probe ran **0** web calls. One on-disk pointer exists: `sources/periodicals/robertjdmackieag00alexrich_djvu.txt` L22-26 carries a **"BANCROFT LIBRARY / THE LIBRARY OF THE UNIVERSITY OF CALIFORNIA"** provenance stamp inside a digitised item — i.e. express-era papers are known to sit in a research library. That names a route; it evidences nothing. | **UNKNOWN** — untried, never null (§14 r6: this family has flipped tiers before). |

**Count for §15.2:** families returning **in-window Tier-1 text** for the origin era = **1** — (d).
(a) answers but always out of window; (b)/(c) were tried and refused; (e) was never tried. (c) and (d) are
**not** counted twice for the same bytes: every item in §2 arrived through the Internet Archive carrier, and
a scanner is a carrier, not a second lineage (§3). The item *class* (company-issued print) puts them in (d).

STATUS: WRITTEN

---

## 7. Per-stage tiers, measured against each stage's own window (RD-112)

**No window here is inherited.** `00_universe/fortune_top_50_2026.csv` has **no founding-date column** —
header measured: `rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city,
hq_state, fortune_industry, universe_source_url, verified_by_second_source, confidence, notes` — and the
Wells Fargo row carries only revenue/profit/HQ/industry. `tools/harvest_mine.py` L67 carries
`"wellsfargo": ("1852-01-01", "1998-12-31")`, whose own header comment calls such windows "deliberately
WIDE **where the founding date is itself unestablished in our corpus**". That is a search setting, so it is
used as one and never cited as evidence. The three windows below are **PROPOSED**, each bounded by a date
the record itself prints.

| stage | PROPOSED window | boundary justified by | families with in-window Tier-1 text | tier | cap / ≈ runs |
|---|---|---|---|---|---|
| **1 — origin** | 1852-01-01 → **1905-12-31** | opens on the organization act printed by the company itself (`catahist00well` L35 "Organized 1852", L126-129 "spring of 1852 … organized a company"); closes on the 1905 separation of banking from express, printed in the registrant's FY1999 10-K L268-269 | **1** — (d): 1868 tariff, 1868 instructions, 1882 instructions, 1884 adverse record, 1893 catalogue | **T3 register — PROVISIONAL** | 8k w/stage, 3-4 runs |
| **2 — banking successor line** | 1906-01-01 → **1968-12-31** | starts after the 1905 split; ends on "became Wells Fargo Bank, N.A., a national banking association, in 1968" (10-K L271), with the 1960 American Trust merger inside it (L269-270) | **1** — (d): the bound FY1919-FY1923 report run, which prints the express person's retirement and the `Wells Fargo Nevada National Bank` stock | **T3 register — PROVISIONAL** | 8k w/stage, 3-4 runs |
| **3 — the registrant line, ending at the name change** | 1969-01-01 → **1998-11-02** | closes on the merger date the registrant's own filings print (SC 13G/A L178; 10-K L237) | **2** — (a) 30 stored docs at `1994-01-12 ≤ filingDate ≤ 1998-11-02` (measured; 731 pre-2001 rows exist in the index) **and** (d) the 1987 and 1998 annual-report layers | **T2 core — PROVISIONAL** | 22k w/stage, 6-9 runs |
| — the express-era **founding moment** 1852-01-01 → 1866-12-31 | recorded separately, because it is the honest answer to "what can Stage 1 be written from?" | `Organized 1852` and `Incorporated 1866` both appear only in an 1893 company catalogue (L35, L41) | **0** — the earliest held naming is the 1868 tariff, whose imprint carries a **year, not a date**, so it sits at least 12 months past the 1866 close; every 1852/1866 statement is retrospective (1893 at 41 years' remove, 1999-2000 at 147) | **T3, and empty at that** | — |

**Planning tier = T3** for the origin stage (≤1 family), with Stage 3 reaching T2 on (a)+(d). Per RD-112, any
future re-grade must name the window it moved:
* a Chronicling America or HathiTrust answer lands in **(c)** and moves **Stage 1 → T2** (2 families);
* registering the (b) domain moves **Stage 3 only**, and only past enumeration;
* an auction/museum/finding-aid answer moves **Stage 1** (the express-era papers, not the bank's);
* nothing at all can move the 1852-1866 sub-window to a document tier — its emptiness is structural, the
  same shape as Citigroup's Stage 1 route-(f) gap.

STATUS: WRITTEN

---

## 8. Carriers found for the origin / predecessor question (file + line)

| # | carrier | file | line(s) | what it actually carries | class | conf |
|---|---|---|---|---|---|---|
| C1 | 1893 company exhibit catalogue | `sources/periodicals/catahist00well_djvu.txt` | L35, L41 | "Organized 1852" / "Incorporated 1866" — **two dates for two different acts** | RETROSPECTIVE INTERPRETATION, company self-narrative | Medium |
| C2 | same | same | L126-129 | spring 1852; **four** organizers (Henry Wells, Wm. G. Fargo, John Livingston, D. N. Barney); capital `$300,000`; "to do an express and banking business in California" | self-narrative, 41 years after | Medium |
| C3 | same | same | L208-214 | "First President … **from March 18, 1852**, to November 25, 1853" — the only day-level 1852 date in the corpus | self-narrative | Medium |
| C4 | same | same | L265-274 | the consolidation of Wells, Fargo & Co. + Holladay Overland Mail and Express Co. + Overland Mail Co. + Pioneer Stage Co. "under the title of Wells, Fargo & Co.", anchored on a presidency 1867-02-18 → 1868-02-18 | self-narrative, dated internally | Medium |
| C5 | 1868 tariff | `sources/periodicals/tariffstablesofd00wellrich_djvu.txt` | L10, L13, L18, L20, L1026 | the **earliest held naming of the express person**, as operating print rather than narrative: "WELLS, FARGO & COMPANY'S OVERLAND EXPRESS", imprint 1868; charges "in all cases, in gold coin" | FACT (contemporaneous company print) | Medium |
| C6 | 1868 agent instructions | `sources/periodicals/instru00well_djvu.txt` | L1-L22 (title block) | a **second** 1868 company printing; OCR badly degraded ("OVERIAND EXPRESS", "mSTEUCTlONS") — a pointer, not quotable text | FACT that the print exists | Low |
| C7 | 1882 express instructions | `sources/periodicals/wellsfar00well_djvu.txt` | L1, L3, L50, L63, L94 | "James Heron, Secretary, San Francisco"; "WELLS, FARGO & COMPANY"; officers C. F. Crocker, J. C. Fargo — **roles, not founders** (RD-116) | FACT (contemporaneous) | Medium |
| C8 | 1884 **third-party** litigation print | `sources/periodicals/robertjdmackieag00alexrich_djvu.txt` | L39-41, L82-83 | "Mackie agst. … **Wells, Fargo & Co.**"; "this defendant admits that the principal place of business of said corporation defendant was at and in the City of San Francisco" — the only **non-self-narrative** in-window naming of the express person | CONTEMPORARY OBSERVATION (adverse filed record) | Medium |
| C9 | bound report run FY1919-FY1923 | `sources/periodicals/01.-wells-fargo-annual-report-archive__Wells_Fargo_Company_WFC_Annual_Report_1919_djvu.txt` | L47, L52, L55-56, L58-60, L90-92, L559, L975 | "enforced retirement from the express business on **June 30, 1918**"; income "derived solely from investments and real estate"; assets = American Railway Express shares; "**Wells Fargo Nevada National Bank** stock … disposed of … for $3,000,000" | FACT (company-authored, contemporaneous with the wind-down) | Medium |
| C10 | registrant FY1999 10-K | `sources/sec/0000912057-00-012168_0000912057-00-012168.txt` | L237-244, L258-271 | merger completed 1998-11-02; **Norwest** changed its name to "Wells Fargo & Company"; the former WF became its subsidiary; 1852 attributed to "the banking portion of the business founded by Henry Wells and William G. Fargo"; 1905 split; 1960 American Trust; 1968 national association | RETROSPECTIVE SOURCE (147 years removed) | Medium |
| C11 | registrant SC 13G/A | `sources/sec/0000072971-99-000019_0000072971-99-000019.txt` | L145, L178-182 | "**Wells Fargo & Company (formerly known as Norwest Corporation)**"; the former WF merged **into WFC Holdings Corporation**, a Norwest subsidiary; "WFC Holdings Corporation was the surviving company"; "Immediately after the merger, Norwest Corporation changed its name" | FACT (filed self-identity) | Medium (held below High by the cap) |
| C12 | registrant FY1999 10-K, exhibit list | `sources/sec/0000912057-00-012168_…txt` | L1323-1326 | "The Company's SEC file number is **001-2979** … The former Wells Fargo filed documents under SEC file number **001-6214**" — two registered persons, one name | FACT | Medium |
| C13 | registrant cover pages | `sources/sec/0000072971-99-000001_…txt` | L48-54 | former names NORWEST CORP / NORTHWEST BANCORPORATION with EDGAR-recorded dates | FACT that the header says so; **not** a corporate act | Medium |

**Corroboration count for the 1852 claim is 1, not 4.** C1-C4 are one document; C10 and C11 are the same
registrant's own filings tracing to one corporate record (§3); C5-C7 name the entity without dating its
origin. Only **C8 is an independent origin** — an adverse record produced by other parties — and it names the
express person at 1884 with no reference to 1852. So "founded 1852" rests on company self-narrative at
Medium, and **no held byte is a 1852 document**.

STATUS: WRITTEN

---

## 9. Load-bearing open questions

**Q1 — Which legal person, and does any held byte connect it to the registrant?**
Two persons, one gap. Person A = "Wells, Fargo & Company" (express; `Organized 1852 / Incorporated 1866` per
C1; last first-party trace = the 1919-1923 run C9, which prints its exit from express and the disposal of the
Nevada bank stock). Person B = CIK 0000072971, `NORTHWEST BANCORPORATION → NORWEST CORP → WELLS FARGO &
CO/MN`, DE-incorporated, Minneapolis-headquartered (C11, C13). The bridge is **asserted, not evidenced**: no
held byte contains a charter, a 1905 separation instrument, a 1960 merger agreement or a 1968 association
record. Publishing "Wells Fargo (CIK 72971) was founded in 1852" would be an invented claim; what C11/C12
actually print is that **the name moved to the survivor**.

**Q2 — What became of person A after 1923?** UNKNOWN. `list-files` on the bound archive item returns 30
layers whose named years are 1919, 1987, 1998-2016, 2017-2021 "V2", 2022-2024 — measured, no 1924-1986 layer
exists in that item. The hole is a gap in what is held, not evidence that the company vanished.

**Q3 — First experiment / first operating act in 1852?** UNKNOWN. No held byte describes an 1852 act, office,
route or shipment. C2 asserts offices "established in all the mining camps of any consequence" — a 1893
generalisation with no camp, date or result named. The nearest concrete held facts are 1868 (a tariff from
Omaha, C5) and 1882 (a business-definition page, C7).

**Q4 — The 1906 earthquake and the gold-rush freight stories (trap 3) currently have no carrier.**
* `earthquake`: 4 occurrences corpus-wide — `sources/sec/0000950131-95-007777` L6165 and
  `sources/sec/0000927356-00-000178` L7750 are force-majeure boilerplate; the 2018 report L14305 is a risk
  factor ("such as earthquakes, tornados, and hurricanes"); `catahist00well` L509 uses the word for a
  **wagon/gas scare** ("…under the impression that it was an earthquake"). Nothing on San Francisco 1906.
* `1906`: 2 occurrences, **both naming a different bank** — The American National Bank of Silver City, New
  Mexico, "Originally organized under New Mexico law in 1906" (`sources/sec/0000912057-94-002538` L733) and
  "incorporated as a New Mexico banking corporation on March 2, 1906" (L2852-2853). A later pass must not
  read that as a Wells Fargo date.
* gold-rush/freight: the closest carriers are C5's gold-coin clause (1868) and `catahist00well` L380 ("'The
  Days of 49' (a poster)"), L1031 ("Wells, Fargo & Co's First Advertisement, 1852. (Photographed.)"), L1037
  ("…1852. (Photographed.)"). The 1852 handbill itself is **not** in the corpus — it is evidenced only as a
  photograph someone exhibited in 1893. Every folklore-grade claim therefore carries that 1893 pointer or
  UNKNOWN.

**Q5 — 2016 account-fabrication matter — post-boundary (PB).** Present in held bytes only in the 2018 report:
`sources/periodicals/01.-wells-fargo-annual-report-archive_djvu.txt` L3021 ("in September 2016 we …"),
L3039-3040 ("potentially unauthorized accounts"), L23707-23709 ("unauthorized accounts identified … exceeds
plaintiffs' 3.5 million"), L2955 and L3000 (2018 consent orders). All **(PB)** — outside every window in §7,
and none of it may be used to explain the origin. The 58 stored SEC filings stop at 2000-07-18 and contain
no reference to it.

STATUS: WRITTEN

---

## 10. What this probe refused to claim, and why

1. **Refused: 1852 as the registrant's founding date.** Every 1852 statement in the corpus is retrospective
   (1893 catalogue; 1999-2000 recital; 1998 and 2018 reports) and the recital itself attributes 1852 to **the
   acquired company's bank subsidiary**, not to CIK 72971. Kept as C1-C4 / C10 at Medium, one lineage.
2. **Refused the EDGAR header dates as corporate acts.** `DATE OF NAME CHANGE: 19920703` is measured across
   118 rows / 15 unrelated registrants / 12 company trees — a systemic stamp. The name change is carried by
   narrative text (C11), and the header/former-name chain is a *record*, not an event.
3. **Refused the 1906 = earthquake reading.** Both `1906` hits name The American National Bank of Silver
   City, New Mexico (`0000912057-94-002538` L733, L2852-2853). The 1893 catalogue's single `earthquake` is a
   wagon/gas scare (L509). The 1906 story stays UNKNOWN with no carrier.
4. **Refused the 1949 "company histories" as carriers.** `wellsfargoadvanc0000edwa` appears in **8 candidate
   rows** (`_s8g6`, `_r7t6`, `_e0z4`, `bwb_Y0-BOL-516`, `wellsfargoadvanc0000unse_m5s9`, …) — one 1949 work in
   many scan copies. Counting rows as witnesses is RD-121/RD-124's error; not one byte is held here.
5. **Refused the Google Books "Annual Report" rows as this company's print.** Their titles name other
   issuers — "…Stockholders of the Bal[timore]" (1901), "St. Louis Sou…" (1919/1920/1910/1912), "Connecticut"
   (1915), "Annual Report of the Public Utilities Commission" (1915). Their `TIER1_CANDIDATE` label is the
   query echoing; the mine got 0 bytes on all five (HTTP 503). **UNANSWERED, not NULL, and not ancestors.**
6. **Refused `numFound` as yield.** `"Wells Fargo" AND mediatype:texts` answers **10,974**, and **all 20
   surfaced docs** are collection `['usfederalcourts','USA…]` — modern bankruptcy captions naming today's
   bank as a litigant. A search signal is not a count of evidence (RD-121 r2).
7. **Refused to count (c) and (d) twice for one carrier.** The 1868/1882/1893 items arrived through the
   Internet Archive; their artefact class is company print, so they count once, in (d) (§3, hard rule 4).
   Their directory location (`sources/periodicals/`, where `ia_text.py fetch` writes) is recorded as a
   **route-vs-shelf disagreement**, not resolved: `sources/corporate_print/` stayed empty because this probe
   moves nothing.
8. **Refused A4's `in-window` label on its only Tier-1 row.** Those bytes are the 2018 report; A4's own
   footnote (L32) already warns scan dates are digitisation years.
9. **Refused to call anything "absent".** Pre-1994 EDGAR is a measured perimeter; Chronicling America and
   HathiTrust are refused endpoints; auction/museum and web-archive bodies are untried; the 5,411 filings
   `--max-docs` never listed are unenumerated.
10. **Refused `legacy_cik.py search` as a predecessor-CIK answer.** It returns **1** candidate — CIK
    0000072971, the survivor — so the former Wells Fargo's own registrant identity (SEC file 001-6214) is
    **not** reachable by name here. Recorded as FETCH REQUEST FR-2.
11. **Refused to name any founder-role beyond what the print says.** Henry Wells and William G. Fargo are
    named as organizers **by the company in 1893** (C2) and **by the registrant in 1999** (C10); E. B. Morgan
    is named as *First President*; C. F. Crocker and J. C. Fargo are *officers* in 1882. No role was upgraded
    to a founder claim, and John Livingston / D. N. Barney appear only in the 1893 list.
12. **Refused to state anything above Medium.** TLS is unverified on all 7 IA sidecars; SEC sidecars carry no
    transport attestation at all.
13. **Refused to run `harvest_mine.py` / `periodical_harvest.py`** (brief), and refused to touch `tools/`,
    the log, another company's tree, or `web_domains.json` — §5's family-(b) finding is reported for the
    orchestrator, not implemented here.
14. **Refused to mint source ids, write registers, or certify depth.** No volume authored; §13 schemas not
    populated.

STATUS: WRITTEN

---

## 11. `## Untried` — every route not run, with its command

Each line below is a search never run or a body never opened, **not** a null.

- **U-1 (d)/(c) — the rest of the IA creator answer.** `creator:("Wells, Fargo") AND mediatype:(texts)`
  answers **numFound 15** with **no YEAR facet**; the YEAR-faceted form answers **10** (measured this pass —
  so RD-130's facet is *dropping* 5 in-window company items here, not adding noise). Opened: 5. Never opened:
  `instructionstoag00wellrich` (1868, "Instructions to agents and employes of the **California and Oregon**
  Express"), `bankinginthiswor00wellrich` (1888), `annualreport1919well` (university-of-Illinois copy — check
  md5 against C9 before counting it as a second witness), `1882-wf-chinese-business-directory` (1882).
  Command: `python tools/ia_text.py fetch --id <identifier> --company-dir <dir> --insecure`.
- **U-2 (c) — Chronicling America, the route that can name the express company contemporaneously.** Its 8
  stored responses are all `404` at ~85,273 B, and `00_universe/harvest/_CA_ENDPOINT_TEST.md` shows all 7 URL
  shapes `CHALLENGED 403` from this egress. **Remedy is egress, not code**: re-run from the GitHub Actions
  runner (the corpus' own nightly lane), for the 1852-1905 span with entity adjacency, per RD-130/RD-134.
  Owned by `periodical_harvest.py`, which this probe was forbidden to run. **This is the single family whose
  answer would move Stage 1 from T3 to T2.**
- **U-3 (c) — HathiTrust.** 1 candidate row, `SKIPPED: hard stop: 5 consecutive failures (host halted)`;
  **0** shelf responses exist for this slug (measured over `harvest/hathitrust/*.meta.json`). Re-run when the
  host answers.
- **U-4 (c) — Google Books page text.** 12 rows, 2 `LEAD_ONLY` with `viewability=no_pages`, and the 5 ids the
  mine tried died at HTTP 503. Some are other issuers (refusal 5); `49MmEAAAQBAJ` (2021, a Berkshire history)
  and `DxcDAAAAYAAJ` are not this company's print at all.
- **U-5 (c)/(d) — 89 of 95 candidate rows never mined**, 79 distinct `item_id`s vs 6 mined
  (`sources/harvest_mine/_index.json`: `candidates 35, mined 6, untried_by_limit 27` — the csv has grown
  since A4). The `--limit 6` is a search setting; nothing in those 89 rows is a finding until fetched.
- **U-6 (a) — the unenumerated filings.** `_UNANSWERED.csv`: "5411 in-window filings were never listed
  because --max-docs 30 was reached", plus 2 accessions whose SGML refused (404 `NoSuchKey` then 403).
  Command for a bounded re-pass: `python tools/sec_intake.py auto "Wells Fargo & Company" --company-dir <dir>
  --from 1994-01-12 --to 1998-11-02 --max-docs 40` — the pre-merger Norwest window, which would thicken
  Stage 3 rather than Stage 1.
- **U-7 (a) — the pre-1998 *former* Wells Fargo registrant.** C12 prints its file number (001-6214) but no
  CIK; `legacy_cik.py search` returns only the survivor. See FR-2.
- **U-8 (b) — web-archive bodies.** No snapshot stored; `sources/web_archive/` does not exist for this
  company. §5 has the measured enumeration and the domain-citation defect.
- **U-9 (e) — auction / museum / manuscript.** Never touched; no tool, 0 web budget. C8's **Bancroft
  Library** provenance stamp is the only on-disk pointer to where express-era papers sit, and it is a route
  name, not evidence. §14 r6: this family has flipped tiers before.
- **U-10 (d) — the house organ.** Wells Fargo's own magazine/newsletter series and the 1960-1998 California
  bank's annual reports (1905-1959) are **entirely unheld**: 7 layers on disk, of which only C1-C7 are
  pre-1968. The bound archive item has no 1924-1986 layer (Q2), so a different supplier is needed.

### FETCH REQUESTs

```
FETCH REQUEST: FR-1
  identifier : 01.-wells-fargo-annual-report-archive
  documents  : "Wells Fargo & Company (WFC) Annual Report 1919_djvu.txt" (already held, 23,931 B) —
               the item's remaining 27 layers are 1999-2024 and post-boundary; NOT requested.
  need       : Wells Fargo & Company annual reports for 1906-1918 and 1924-1959 (the Q2 hole), which this
               item does not hold. Ask: does any IA item or HathiTrust volume carry them?
  why it matters : it is the only known route to a first-party document naming the express person inside
                   the Stage-1 window.
  status for this probe : UNTRIED (no script in this repo reaches a non-IA 1906-1959 report set).

FETCH REQUEST: FR-2
  accession  : none held — the predecessor registrant itself.
  need       : the CIK of the entity that filed under SEC file number 001-6214 ("the former Wells Fargo",
               printed at sources/sec/0000912057-00-012168_…txt L1323-1326), then
               `python tools/sec_intake.py index "<that registrant>" --company-dir <dir>`.
  why it matters : its 1994-1998 filings would print that person's own history section, which is the
               nearest thing to a filing-era statement about 1852-1905 that EDGAR can still answer.
  note       : `legacy_cik.py search "Wells Fargo & Company"` returns only CIK 0000072971 (the survivor),
               so the lookup needs a file-number route, not a name route.
  status for this probe : UNTRIED.

FETCH REQUEST: FR-3
  accession  : 0000950131-94-000049 (S-4, 1994-01-25) — earliest S-4 in the index, no primaryDocument
               (698 such nameless rows exist, "fetchable as <accession>.txt").
  need       : full submission `0000950131-94-000049.txt`; two stored accessions 404/403'd on exactly this
               shape (`_UNANSWERED.csv` ranks 20, 22).
  why it matters : a 1994 Norwest S-4 will print Norwest's own history, i.e. the registrant line without
               the Wells Fargo name attached — the control document for trap (1).
  status for this probe : UNANSWERED (endpoint refused: NoSuchKey then HTTP 403 after 2 tries).
```

STATUS: WRITTEN

---

## 12. Verdict, and the route that would change it

**Origin stage (Stage 1 as proposed): T3 register, PROVISIONAL — 1 family (d) returning in-window Tier-1
text, 4 in-window documents, all company-issued, all retrospective on the 1852 act itself.**
Stage 2 as proposed: T3 (1 family). Stage 3 as proposed: **T2 core** (2 families: (a) from 1994-01-12 and
(d) the 1987/1998 report layers). The famous founding year is carried by self-narrative at 41 and 147 years'
remove; the express person's *later* life (1868-1923) is carried by first-party print that is now on disk,
and one adverse record (C8, 1884) names it independently.

**The route most likely to change the verdict is Chronicling America (family (c)) re-run from an egress the
LOC does not Cloudflare-challenge** — it is the only untried-answering route that can put a
**third-party, contemporaneous** 1852-1905 naming of "Wells, Fargo & Company" into the corpus, which would
take Stage 1 from 1 family to 2 and from T3 to T2. Its close second is U-1: the 5 IA creator-matched company
items that the YEAR facet hides and no agent has opened (`instructionstoag00wellrich` 1868 is the same
legal person in the same year as C5).

STATUS: WRITTEN

---


---

## 13. Late-arriving bytes, accounted for (§14 rule 11)

`sources/periodicals/` holds **10** `.txt` layers at close-out. Nine are this dossier's own or pre-existing.
The tenth did **not** arrive from this pass:

| file | sidecar | what it is | verdict |
|---|---|---|---|
| `NPDP19380212_djvu.txt` (282,316 B) | `fetched: 2026-10-06T12:49:22Z`, `transport: UNVERIFIED TLS` | Hong Kong Daily Press, 1938-02-12 — a candidate row this probe never fetched (it is `L3738` in `candidates.csv`, `classification: TIER1_CANDIDATE`) | **DECOY, measured.** All 5 `wells fargo` hits in its OCR are **the 1937 motion picture** *Wells Fargo*, listed as cinema programming: "QUEEN'S: *Wells Fargo* … ALHAMBRA: *Wells Fargo*", and a review paragraph — "WELLS FARGO Painted on an heroic canvas … it is one of those pictures which everybody should see … Joel [McClelland], Frances Dee and Bob Burns … a cavalcade of American history from the discovery of gold in California until the end of the War Between the States". It names **a film title twice-plus and the gold-rush subject of that film, never the company**. Entity adjacency (`wells, fargo`) = **0**. |

Recorded so the next pass does not count it: this row is **family (c) bytes that answer nothing**, and it is
the cleanest illustration in this dossier of trap (2) — print from the exact era, in a real periodical, with
the exact words, and it is about a Hollywood picture. `classification: TIER1_CANDIDATE` in the harvest index
is a query echo, not a naming (hard rule 6). **It changes no tier and is cited here only as a negative.**
Because another writer put it there, it is left exactly where it is (§14 rule 4, hard rule 2).

STATUS: WRITTEN
