# EXTRACT — web / documentary family, company_025 (Home Depot) — probe-homedepot, 2026-09-26

Fetched with the sanctioned web tool by agent `probe-homedepot`. Raw bytes of these pages were NOT
retained (text-returning fetch); what is preserved below is the returned text, quoted verbatim, with
URL and retrieval timestamp, per §14.9. Nothing here was placed in a temp directory.

## 1. Georgia Historical Society — "A State of Innovation: Home Depot"
- URL: https://www.georgiahistory.com/a-state-of-innovation-home-depot/
- Retrieval: 2026-09-26, via WebFetch (page states its own date)
- Stated publication date: **July 20, 2016**
- Tier: 2 (serious third-party historical society, retrospective) — NOT Tier-1, NOT in-window (2016)
- Verbatim, as returned:
  - "Bernie Marcus and Arthur Blank founded The Home Depot in 1978."
  - "opened the first two Home Depot stores on June 22, 1979, in Atlanta, Georgia"
- Bearing: the only third-party dated statement recovered that carries BOTH a founding year (1978)
  and an opening date (1979-06-22) with a store count (two). It is retrospective by 37 years, so it
  is tagged `RETROSPECTIVE SOURCE` (§6) and cannot by itself fix the date.
- Route note: the same organisation physically marked the site — see the company news release
  "The Home Depot Receives Official Georgia Historical Marker at Atlanta"
  (https://corporate.homedepot.com/news/company/home-depot-receives-official-georgia-historical-marker-atlanta,
  surfaced 2026-09-26, **not fetched**). GHS holdings are the documentary-family candidate for this
  company (a marker implies accessioned site records; contents UNKNOWN).

## 2. Home Depot corporate "THD Timeline.pdf" — FETCHED, NOT READ
- URL: https://corporate.homedepot.com/sites/default/files/THD%20Timeline.pdf
- Retrieval: 2026-09-26, via WebFetch. Response: "Input is raw PDF code. No Home Depot timeline
  visible. Metadata date: `D:20200220124640-05'00`. No founding or IPO data available."
- Interpretation: the tool returned the PDF source rather than its text layer; **this is a route
  failure, not an absence of content.** The company's canonical date list is therefore UNREAD.
  PDF metadata dates the file 2020-02-20 (i.e. a 2020 self-narrative about 1978–2020 — retrospective).
- FETCH REQUEST: download the PDF bytes to `sources/corporate_print/` and extract with a PDF-capable
  route; then compare its 1978/1979/1987 lines against §1 above and against the 1980 trade print
  (HD-a series). Do not cite this file as evidence until its text is held.

## 3. Wayback CDX — homedepot.com floor (family b)
Query A: `http://web.archive.org/cdx/search/cdx?url=homedepot.com&matchType=exact&from=1990&to=2000&fl=timestamp,original,statuscode,length&limit=12`
Query B: same with `url=www.homedepot.com`. Retrieved 2026-09-26. Verbatim rows (A):

    19961105232803 http://www.homedepot.com:80/ 200 1149
    19961220031830 http://www.homedepot.com:80/ 200 1146
    19970129005830 http://www.homedepot.com:80/ 200 1148
    19970129005830 http://www.homedepot.com:80/ 200 1256
    19970710234947 http://www.homedepot.com:80/ 200 1256
    19970822194917 http://homedepot.com:80/ 200 720
    19971018224357 http://www.homedepot.com:80/ 200 1256
    19971212054615 http://www.homedepot.com:200 ... 452
    19980207082911 http://www.homedepot.com:80/ 200 462
    19980509130220 http://homedepot.com:80/ 200 459
    19981205093159 http://www.homedepot.com:80/ 200 458
    19981212014522 http://www.homedepot.com:80/ 200 457

(rows reproduced as returned; one 1997-12-12 row's status/length printed `200 ... 452` in the response.)
Query B returned the identical first capture `19961105232803`, so bare-host and `www.` are **one test,
not two** — the host is normalised. Earliest capture = **1996-11-05**, 1,149 B, HTTP 200.
`from=1990&to=1996` produced no earlier row than the above.

## 4. Internet Archive reel map for the trade-print families (enumeration, not content)
Queries of 2026-09-26 against `https://archive.org/advancedsearch.php` (field-list form `fl=`),
`sort=year asc`. These are catalogue rows; content claims require the fetched `_djvu.txt` layer.

| title run | identifiers (year) | reels |
|---|---|---|
| Discount Store News, 1976–1990 → numFound **11** | micro_IA40706901_0406 (1980), …05_0021 (1981), …08_0058 (1982), …11_0343 (1983), …15_0204 (1984), …18_0158 (1985), …21_0148 (1986), …24_0308 (1987), …28_0008 (1988), …31_0077 (1989), …34_0339 (1990) | 11 |
| Chain Store Age, 1976–1990 → numFound **20** | Supermarkets 1980 (…01_0404); Executive 1981 (…05_0022); Supermarkets 1981 (…05_0019); Executive 1982 (…08_0056); Supermarkets 1982 (…08_0055); Supermarkets 1983 (…11_0341); Gen. Merch. 1983 (…11_0347); Executive 1983 (…11_0344); Executive 1984 (…15_0205); Gen. Merch. 1984 (…15_0159); Gen. Merch. 1985 (…18_0162); Executive 1985 (…18_0159); Exec 1986 (…21_0149); Gen. Merch. Trade 1986 (…21_0159); Executive 1987 (…24_0309); Gen. Merch. Trade 1987 (…24_0312); Executive 1988 (…28_0009); Gen. Merch. Trade 1988 (…28_0012); Executive 1989 (…31_0078); Executive 1990 (…34_0340) | 20 |
| National Home Center News, 1976–1992 → numFound **10** | 1982 (…08_0060), 1983 (…11_0346), 1984 (…15_0207), 1985 (…18_0161), 1986 (…21_0156), 1987 (…24_0311), 1988 (…28_0011), 1989 (…31_0080), 1990 (…34_0342), 1992 (…41_0155) | 10 |
| Building Supply Home Centers, 1976–1992 → numFound **1** | sim_building-supply-business_january-december-1988_154-155_index (1988, index volume only) | 1 |

**No Discount Store News or Chain Store Age reel is enumerated for 1978 or 1979** — the founding two
years are absent from this digitised run (a boundary, not a judgement that the issues did not exist).
Total enumerated reels in-window-to-1990: **41**. This probe held and grepped **3**.

## 5. Metadata for the three held text layers (sidecars live beside each .txt)
- micro_IA40706901_0406 — Discount Store News, metadata `date: 1980`, layer 1,987,023 B, transport **verified TLS**
- micro_IA40706924_0308 — Discount Store News, metadata `date: 1987`, layer 1,700,633 B, transport **UNVERIFIED TLS (`--insecure`, stale local CA: `SSL: CERTIFICATE_VERIFY_FAILED … certificate has expired` on the verified route)** — citations from this layer are capped at Medium until re-checked. The item's own text-layer filenames carry issue dates (`… 18. july 20 1987_djvu.txt`, `… 23. oct 12 1987_djvu.txt`, `… 13. may 11 1987_djvu.txt`).
- micro_IA40706921_0149 — Chain Store Age Executive, metadata `date: 1986`, layer 223,991 B, transport **verified TLS**
- insidehomedepoth0000rous (Roush, *Inside Home Depot*, McGraw-Hill 1999) — record EXISTS; text-layer fetch returned **HTTP 401** twice (lending-gated) → UNANSWERED, no bytes held.

## 6. Issue-date attribution method used on held bytes (needed for §6 time audit)
Running heads were located in the same flat layer as the passage, and the passage's line number was
bracketed by them:
- DSN passage at line 19008: heads at 18803 `MARCH 10, 1980` and 19175 `DISCOUNT STORE NEWS, MARCH 10, 1980`; `Vol. 19, No. ‹› March 10, 1980` at 19597 ⇒ **1980-03-10 issue**.
- DSN passage at line 53746: heads at 53725 and 54209 both `August 10, 1987` ⇒ **1987-08-10 issue**.
Page and column numbers are NOT recoverable from the flat OCR layer; they are recorded as UNKNOWN.
