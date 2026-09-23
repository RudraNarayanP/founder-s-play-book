# S-1 Graphics Recovery — Inventory

**Agent:** Level-3 Graphics Recovery
**Date of work:** 2026-09-23
**Company:** Amazon.com, Inc. (CIK 0001018724)
**Target:** graphics files behind the Form S-1 figure caption
`[PICTURES OF THE COMPANY'S WELCOME, SEARCH, REVIEW AND ORDERING WEB PAGES]`

---

## RESULT: NULL. Zero image files exist in EDGAR for any Amazon 1997 registration filing.

**Images recovered: 0. Total bytes of image data: 0.**

The premise of this task — that the screenshots survive as graphics files in the accession and were
merely "lost when the filing was read as ASCII" — is **disproved**. They were never transmitted
electronically. What the caption marks is **not an omitted image but a printer's art-direction
instruction, printed in square brackets in the text itself**. Those brackets are the whole of the
visual record inside the filing, and they are already in the ASCII we hold.

No image-download step was possible, so there is nothing to magic-byte-check as an image. The proof
is arithmetic and is given below because section E will be written from it.

---

## 1. Why the graphics do not exist: the closing arithmetic

EDGAR's own directory listing renders the *names* of pre-1998 submission documents as blank strings
(the `index.json` emits `"name":""` with a real `"size"`, and the HTML listing emits
`<img src="/icons/">` with an empty icon). That rendering bug is the origin of the "there are hidden
files here" hypothesis. The counts close exactly against the header's `PUBLIC DOCUMENT COUNT`, and
the byte totals close against the complete submission text file:

| Accession | Form | Filed | Rows in `index.json` | Unnamed rows | `PUBLIC DOCUMENT COUNT` | Match |
|---|---|---|---|---|---|---|
| 0000891618-97-001309 | S-1 (original) | 1997-03-24 | 41 | 38 | 38 | yes |
| 0000891020-97-000603 | S-1/A | 1997-04-21 | 12 | 9 | 9 | yes |
| 0000891020-97-000659 | S-1/A | 1997-04-29 | 6 | 3 | 3 | yes |
| 0000891020-97-000755 | S-1/A | 1997-05-09 | — | — | 4 | yes (local copy) |
| 0000891020-97-000822 | S-1/A | 1997-05-13 | 8 | 5 | 5 | yes |
| 0000891020-97-000839 | S-1/A | 1997-05-14 | 5 | 2 | 2 | yes |
| 0000891020-97-000847 | S-1/A | 1997-05-14 | 5 | 2 | — | row count 2 |
| 0000891020-97-000868 | 424B1 (final prospectus) | 1997-05-15 | 4 | 1 | — | row count 1 |

Every accession's surplus rows are exactly `3` generated wrapper files
(`-index-headers.html`, `-index.html`, `.txt`) plus the documents. There is no remainder for graphics.

**The clincher on the original S-1:** the 38 unnamed files sum to **1,438,356 bytes**
(sizes: 5319, 26204, 25896, 80480, 47141, 18022, 19292, 19055, 15736, 18981, 25864, 125034, 91063,
20566, 146083, 65786, 1854, 590, 2150, 59955, 18325, 32632, 78794, 2676, 52038, 11945, 10458, 12845,
13854, 278583, 4231, 13267, 4479, 13694, 1239, 25921, 22361, 25943). The complete submission text
file `0000891618-97-001309.txt` is **1,444,013 bytes**; the 5,657-byte difference is the PEP header,
the SEC-HEADER block and the document delimiters. Those 38 files *are* the text file, byte for byte.

Independently, the local complete submission text holds exactly **38 `<DOCUMENT>` blocks**, every one
typed `S-1` or `EX-*` (EX-2.1 … EX-27.1, EX-23.1, EX-11.1, plus a `<TYPE>10-K405`-style financial
data schedule at sequence 38). Descriptions run "FORM S-1", "AGREEMENT AND PLAN OF MERGER",
"BYLAWS", "OPINION OF PERKINS COIE", the investment-letter and lease exhibits, "STATEMENT OF NET
LOSS PER SHARE", "CONSENT OF ERNST & YOUNG", "FINANCIAL DATA SCHEDULE". There is **no
`<TYPE>GRAPHIC` document anywhere** in any Amazon filing on disk.

Encoding tests on the three prospectus texts, all clean:

- non-ASCII bytes: **0** (so nothing was mojibake'd or lost in an ASCII read)
- `<img` tags: **0**; `.gif` / `.jpg` / `.jpeg` / `.png` references: **0**
- `binhex` / `begin 6` / `uuencode` / base64 attachment blocks: **0**
- `<FILENAME>` tags: absent from the 1997 SGML header format itself, which is why the listing has
  nothing to print — not evidence of stripped binaries.

Note on the earlier grep hit that looked like a `GRAPHIC` type: it is the substring in
"demo**graphic**" and "geo**graphic**". False positive.

---

## 2. What the caption actually is

Required table, populated honestly. No image rows exist; the rows below are the bracketed
instructions, which are text, plus the retrieval artifacts held in this directory.

| filename | bytes | source accession | media type | what it depicts | legible details | integrity check |
|---|---|---|---|---|---|---|
| *(no image files exist)* | 0 | — | — | — | — | — |

### 2a. The picture instructions, verbatim, by filing location

The original S-1 carries one collective caption. The amendments replaced it with **eight separately
specified pictures, each with its own quoted caption line** — an art plan for the prospectus cover
and inside back cover. Quoted exactly as they appear in the ASCII; the ellipses are the filer's.

| # | Location | Bracketed instruction (verbatim) | Legible details |
|---|---|---|---|
| 1 | S-1 original, `<PAGE> 28`, line 1970/1987 of `s1_original_0000891618-97-001309.txt` | `[PICTURES OF THE COMPANY'S WELCOME, SEARCH, REVIEW AND ORDERING WEB PAGES]` | Names four page types: **welcome, search, review, ordering**. Sits immediately after "THE AMAZON.COM BOOKSTORE" intro and before "Browsing." |
| 2 | S-1/A 755 and 839, prospectus **cover, page 3** | `[PICTURE OF THE COMPANY'S WELCOME WEB PAGE ACCOMPANIED BY TEXT, "Customers enter the bookstore through Amazon.com Web site and can . . ."` | WELCOME page. Caption text quoted. |
| 3 | same block | `PICTURE OF THE COMPANY'S WEB PAGE FOR SEARCHING BY AUTHOR, TITLE, AND SUBJECT, ACCOMPANIED BY TEXT, ". . . conduct targeted searches of over 2.5 million titles in the Amazon.com catalog. . . "` | SEARCH page. **2.5 million titles** stated on the cover. |
| 4 | same block | `and PICTURE OF THE COMPANY'S AMAZON.COM JOURNAL WEB PAGE, ACCOMPANIED BY TEXT, ". . . browse from among highlighted selections and other features . . ."]` | AMAZON.COM JOURNAL page — an editorial/browse page, not "review". |
| 5 | S-1/A 755 and 839, **page 66** (page 65 is marked "(This page intentionally left blank)") | `[PICTURE OF THE COMPANY'S WEB PAGE FOR THE AMAZON.COM 500, ACCOMPANIED BY TEXT, "...browse the 500 current bestsellers and titles Amazon.com believes will be future best-sellers -- all at a 40% discount to list price...";` | AMAZON.COM 500 page; **40% discount** claim on the page furniture. |
| 6 | same block | `PICTURE OF THE COMPANY'S WEB PAGE FOR EDITORS MAILING LIST SIGN UP, ACCOMPANIED BY TEXT, "...register for personalized services...";` | Editors' e-mail list sign-up page. |
| 7 | same block | `PICTURE OF THE COMPANY'S WEB PAGE FOR FINALIZING ORDERS, ACCOMPANIED BY TEXT, "...and order books 24 hours a day, 7 days a week, worldwide without having to go to the store...";` | ORDERING page. |
| 8 | same block | `PICTURES OF THE COMPANY'S WAREHOUSE, THE SCANNING OF A BARCODE ON A BOOK, AND PEOPLE FULFILLING BOOK ORDERS;` | Photographs, not screens: warehouse, barcode scan, fulfilment labour. |
| 9 | same block | `and PICTURE OF A FORM OF THE COMPANY'S E-MAIL CONFIRMATION OF AN ORDER.]` | An order-confirmation e-mail specimen. |

**Which of the four requested page types are actually represented:** *welcome* — yes, specified
twice (items 1, 2). *search* — yes (items 1, 3). *ordering* — yes (items 1, 7). *review* — named
only in the original S-1's collective caption (item 1); the amendments swap it for an
**Amazon.com Journal** page and never re-specify a review screen. **All four are specified only as
instructions; none is present as a rendered image in any EDGAR file.**

### 2b. Retrieval artifacts kept in this directory (not images; they are the proof of the null)

| filename | bytes | source | media type | what it depicts | integrity check |
|---|---|---|---|---|---|
| `idx_1309.json` | 3,347 | `…/000089161897001309/index.json` | JSON | 41 rows, 38 unnamed | parses; sizes sum 1,438,356 |
| `idx_839.json` | 616 | `…/000089102097000839/index.json` | JSON | 5 rows, 2 unnamed | parses |
| `idx_868.json` | 542 | `…/000089102097000868/index.json` | JSON | 424B1, 1 unnamed | parses |
| `idx_000089102097000603.json` | 1,146 | index.json | JSON | 9 unnamed | parses |
| `idx_000089102097000659.json` | 693 | index.json | JSON | 3 unnamed | parses |
| `idx_000089102097000822.json` | 841 | index.json | JSON | 5 unnamed | parses |
| `idx_000089102097000847.json` | 616 | index.json | JSON | 2 unnamed | parses |
| `dir_1309.html` | 16,870 | directory listing HTML | HTML | shows `<img src="/icons/">` + empty link text for all 38 | name-loss bug visible |
| `hdr_000089102097000603.txt` | 6,206 | range request, first 2,500 bytes | text | `PUBLIC DOCUMENT COUNT: 9` | header fields present |
| `hdr_000089102097000659.txt` | 403,334 | full file (range ignored by server) | text | `PUBLIC DOCUMENT COUNT: 3` | header present |
| `hdr_000089102097000822.txt` | 6,173 | range request | text | `PUBLIC DOCUMENT COUNT: 5` | header present |
| `sum_1309.html` | 17,905 | filing-detail page | HTML | offers only the `.txt`; no document links into the folder | parses |
| `subs.json` / `subs2.json` | 159,857 / 20,784 | submissions index + pre-2000 chunk | JSON | 14 pre-1998 accessions enumerated | parses |
| `resp_839_headers.txt` | 1,529 | HTTP response headers | text | `HTTP/1.1 200 OK`, `Content-Encoding: gzip` | proves the UA/Referer header recipe works |
| `hdr_1309.html` | 339 | `-index-headers.html` | HTML | **404** — EDGAR does not generate this for 1997 accessions | error page |
| `filelist_1309.xml` | 341 | `filelist.xml` probe | XML | **404 NoSuchKey** | error page |

**Access note for later agents (this cost calls to learn):** `User-Agent: FounderPlaybook Research
AdminContact@example.com` + `Accept-Encoding: gzip, deflate` + `Referer: https://www.sec.gov/`
returns `200 OK` from both `www.sec.gov` and `data.sec.gov`. Bodies are gzipped; use `curl
--compressed`. The `index.json` files are only ~0.5–3 KB, so no decompression problem. HTTP range
requests are honoured for *some* legacy archives and ignored for others — verify byte counts.

---

## 3. Residual gap (what is NOT disproved)

This null is scoped to **EDGAR's electronic files**. It does not say the screenshots never existed.
They were shot for the paper prospectus: the bracketed instructions prove the company photographed
its own welcome, search, Amazon.com 500, mailing-list sign-up, ordering pages, warehouse and e-mail
confirmation in or before **May 1997**, for the prospectus cover and page 66.

Still unexamined, and cheap to state as unknown rather than resolved:

- The **paper original** at the SEC Public Reference Room (film number 97561192, file 333-23795) and
  the microfilm/fiche of the 1997-03-24 S-1 would carry the actual images. Not retrievable by this
  agent.
- **Five 1997 accessions were not opened** (curl budget spent): `0000891020-97-000704` (8-A12G),
  `0000950151-97-000177` (S-8), `0000891020-97-001148` (10-Q), `0000891020-97-001216` (S-8 POS),
  `0000950151-97-000357` (8-K), `0000891020-97-001466` (10-Q). None is a prospectus, and the S-8/8-K/
  10-Q forms have no reason to carry marketing screenshots, but their file lists are unverified.
- The **1998 10-K405** (0000891020-98-000448) was read locally only: 6 documents, all text, zero
  image references, no caption.

Treat "recover the S-1 screenshots from EDGAR" as **closed, negative**. Do not re-run it: the file
counts and the 1,438,356 / 1,444,013 byte identity are the reason, and reproducing them takes 15
requests.
