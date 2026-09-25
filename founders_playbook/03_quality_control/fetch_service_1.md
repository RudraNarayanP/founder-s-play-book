# fetch_service_1.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:45:16Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Target 1 Apple 1976 print

**Requested by `company_004_apple/_parts/s1_p2.md` §E-U(i) / DG-4:** Kilobaud 1976-09 and 1976-11, and
Creative Computing 1976 text layers, into `company_004_apple/sources/periodicals/`, grepped for
`Apple`, `666`, `666.66`, `Personal Computer`, `byte`, `Markkula`, `Wayne`, `[0-9]{3}\.[0-9]{2}`.

**Headline yes/no: NO genuine Apple-placed 1976 price line exists in held print after this pass.**
`666.66` occurs in **zero** document bytes under any `sources/` tree (repo-wide re-grep: every hit is
analysis commentary in `_parts/` and `research/`). The only dollar-shaped 666 in held 1976 bytes is still
`sources/ia_byte_1976/byte-1976-12.txt:39849` — "a $666 value", a competitor's strike-through anchor.

### 1a. Kilobaud 1976 — UNANSWERED, and the reason is not a missing text layer

| probe | result |
|---|---|
| `metadata/Kilobaud197609` | HTTP 200, **2-byte body `{}`** — no item record |
| `metadata/Kilobaud197611` | HTTP 200, 2-byte `{}` |
| `metadata/Kilobaud197606` (the identifier the house note probed) | HTTP 200, 2-byte `{}` |
| `details/Kilobaud197609` · `details/Kilobaud197606` | **HTTP 404** both |
| `ia_text.py search identifier:(Kilobaud1976* OR …)` | 0 rows (advancedsearch is unreliable from this egress — see §Nulls) |
| `title:(kilobaud)` full enumeration | numFound **159**; year histogram 1977 ×27, 1978 ×25, 1979 ×28, 1980 ×24, 1981 ×23, 1982 ×12, 1984 ×9, 1987 ×1, 1995 ×1, undated ×9 — **zero 1976 rows** |

**Finding that corrects an inherited note.** `A_chronology_feasibility.md` AP-34 and `s1_p2.md` §E.4 state
that Kilobaud's 1976 items "carry no `_djvu.txt` text layer ⇒ scans only". What is actually true is
stronger and different: **no 1976 Kilobaud item resolves at these identifiers at all** (404 + empty metadata
record), and the earliest Kilobaud year enumerated on IA is **1977**. Kilobaud 1976 therefore stays
**UNANSWERED** (unresolved item, 404), never a text-layer null and never an absence of coverage. For
contrast, Kilobaud 1977-onward *is* layered (`metadata/Kilobaud197701` → `Kilobaud 1977-01_djvu.txt`,
746,892 B; `kilobaudmagazine-1977-05` → 672,171 B) — outside the requested window, so **not fetched**
(UNTRIED; see §Left for a human).

### 1b. Creative Computing 1976 — bytes held, and a true null

Enumerated: `title:("creative computing") AND year:1976` → numFound 24, of which the 1976 issues exist in
~5 parallel binding families (duplicate bindings of the same issues). Fetched with
`ia_text.py fetch --insecure` into `company_004_apple/sources/periodicals/`, each with its `.meta.json`:

| issue / identifier | bytes | `Apple` | `666` | `666.66` | `Markkula`/`Wayne` | `[0-9]{3}\.[0-9]{2}` |
|---|---|---|---|---|---|---|
| Mar-Apr 1976 `CreativeComputingV02n02MarApr1976` | 453,250 | **0 — NULL** | 0 | 0 | 1 (`Wayne A. Wickelgren`, an unrelated name) | ≥10 (BASIC numeric tables, e.g. L12782 `658.3301`) |
| Sep-Oct 1976 `CreativeComputingV02n05SepOct1976` | 490,131 | 4 hits, **all idiom** (L4087/4116/4285 "Big Apple", L11405 "apples to zoos") | 0 | 0 | 1 (`c/o Dwayne Jeffries`) | ≥13 (L104 `$125.00`, L130 `$395.00`, L234 KIM-1 order form `$245.00`) |
| Nov-Dec 1976 `CreativeComputingV02n06NovDec1976` | 463,891 | **0 — NULL** | 5, all non-price (L6964 phone `(501) 666-2839`, L7369 `(201) 342-6667`, L14982/14991 `66.666` BASIC output, L16436 `66667`) | 0 | 0 | ≥5 (L4201 `$395.00`, L4251 `$250.00`) |
| Jan-Feb 1976 `sim_creative-computing_january-february-1976_2_1` | 312,475 | **0 — NULL** | 0 | 0 | 0 | present (subscription rates) |
| May-Aug 1976 `sim_creative-computing_may-august-1976_2_3-4` | 292,534 | 1, OCR noise (L3049 "picking apple the dark") | 0 | 0 | 0 | present |
| Jan-Feb 1976 `Creative_Computing_v02n01_Jan-Feb1976` | **3,414** | thin-layer ⇒ **UNANSWERED** | — | — | — | — |
| Jan-Feb 1976 `creativecomputingjanfeb1976` | **0 — UNANSWERED** | no bytes | — | — | — | — |

**Held total: 2,012,281 B (5 complete issue layers) + a 3,414 B stub = 2,015,695 B across 7 identifiers.**

Two labels that must not be read as coverage:
* `creativecomputingjanfeb1976` *does* have a 389,016 B layer per its metadata
  (`Creative Computing Jan-Feb 1976_djvu.txt`), but the filename contains a **space** and
  `ia_text.ocr_url()` does not URL-encode it ⇒ HTTP 404 ⇒ **UNANSWERED, script transport limitation, not
  an absent layer**. The same issue's bytes are held anyway via the `sim_*` binding above.
* `Creative_Computing_v02n01_Jan-Feb1976` arrived (3,414 B) but **is not the issue text** — it is a single
  advertising page ("Computer Art for people … HEWLETT-PACKARD COMPUTERS"). Identifier does not deliver
  what it claims; bytes kept and labelled.

**Order forms found in 1976 Creative Computing are the magazine's own**, never Apple's:
`CreativeComputingV02n02MarApr1976_djvu.txt:1269` (CREATIVE COMPUTING ORDER FORM), `:1432`, `:1487`;
`…V02n05SepOct1976:3761`; `…V02n06NovDec1976:1605`, `:21129`;
`sim_…january-february-1976_2_1:13136` (T-SHIRT ORDER FORM). No Apple order form, no Apple price line.

**Re-verified against the previously held BYTE 1976 run** (12 issues, `sources/ia_byte_1976/`, not re-downloaded):
pattern `Apple…$<digit>` / `$<digit>…Apple` on one line returns **no matches** in any of the twelve; the
`666` family returns exactly the one IMSAI anchor. So after adding 2.01 MB of new 1976 print, the corpus's
Apple-placed-1976-price answer is still **NO** — held 1976 print now carries **zero** Apple-placed price
lines, and `$666.66` remains correctly held at FOUNDER CLAIM / UNKNOWN.

**TLS stamp:** every byte in this section arrived over **unverified TLS** (`--insecure`, stale local CA
store); each sidecar records `"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"`.
**These bytes may not carry High confidence until re-checked.**

## Target 2 Walmart FY1975 pages

**Item located:** `1975-annual-report-for-walmart-stores-inc` (server `ia600408.us.archive.org`,
dir `/13/items/…`, 19 files). The metadata-declared page-image/text-PDF routes the request pointed at are
`.pdf` 4,854,934 B and `_text.pdf` 4,852,652 B (the brief's "~3.2 MB" does not match what this item
declares today), plus `_jp2.zip` 12,808,426 B. **Those three are images, not text, and were NOT fetched.**

**But a machine-readable layer the project had never read does exist for exactly those pages:**
`1975-annual-report-for-walmart-stores-inc_hocr.html`, 1,313,302 B — a **second, independent OCR pass over
the same scans, carrying word-level `x_wconf` confidences**. Fetched via curl on the metadata-declared
server+dir (`tools/ia_text.py` resolves only `*_djvu.txt`, so it cannot reach this layer — script limit,
recorded in §Left for a human). Byte count matches the metadata declaration exactly. Sidecar:
`1975-annual-report-for-walmart-stores-inc_hocr.html.meta.json`.
**Total bytes added this target: 2,680,318 B** (FY1975 hOCR 1,313,302 + FY1976 hOCR 1,367,016), plus 2 sidecars.

### 2a. The dropped FY1975 own-column numerals: the hOCR layer does carry glyphs

`WALMART_AR_1975.txt`'s own header says FY1975 net sales / total assets / equity are "NOT recoverable from
this text layer". The hOCR layer prints them in the Five Year Financial Review block — **with the engine's
own confidence attached**, verbatim (word(conf)):

> `… 78(4) Set(0) Side(0) 2(0) … adoption … in a redaction in net hie, mie of $2.(23) 3^7.(0) 106(3) per shore.(7) 1975(0) $236,208,880(6) S(27) 12,208,039(9) $.95*(5) 104(44) …`

and in the shareholders' letter:

> `… total stores . . . 104,(5) to be exact. Wal-Mart(18) sales(13) were $236.2(34) million(16) compared to $167.6(34) million(21) last year, an increase of 4)(7) percent … Total sales,(15) including leased departments (shoes,(11) jewelry,(10) and pharmacies)(12) were $255.8(13) million …`

**Retrieval note, not an interpretation:** the string the corpus has been calling a 2/3-digit ambiguity
(`$226,209` vs `$236,209`) renders in this layer as `$236,208,880` — **at word confidence 6**, and the
`1975` column head beside it at confidence 0. I am reporting what the bytes print and what the OCR engine
scored them; I am not certifying the figure. Whether these glyphs settle the FY1975 top line is a call for
an analyst with the page image in front of them.

### 2b. The "illegible supplier percentage"

The sentence is **FY1976's, not FY1975's** — `sources/periodicals/WALMART_AR_1976.txt:424`:
`supplier  to  the  Wal-Mart  stores  accounted  for  more  than  29c  of`.
The FY1976 hOCR layer was fetched to test it. It prints (word(conf)):

> `… In the fiscal year 1976.(9) no(7) supplier(9) to the Wal-Mart(35) stores(11) accounted(13) for(42) more(7) than(9) 29c(0) of(27) the Company's(12) purchases.(22) …`

**The token "29c" carries `x_wconf 0` — the OCR engine itself reports zero confidence.** Two independent
OCR passes over the same scan produce the same ambiguous glyph string "29c" and neither scores it. So this
is a **digitisation limit, not a null**: no machine-readable layer on this item will resolve it, and the
only route left is the human eye on the page image (`_jp2.zip` / `_text.pdf`, deliberately not fetched into
`sources/` as 12.8 MB of images). **Status: UNANSWERED.** (Two corpus notes for whoever adjudicates: the
same hOCR renders FY1976's warehouse as `238.800(16)` square foot, i.e. comma/period drift is active in
these numerals; and `research/A2_chronology_finance.md` carries the sentence twice, W-57 as "29c / not
recoverable" and W-92 as "more than 2%" as FACT — both from the same held line. That is an analyst conflict,
flagged not resolved.)

**TLS:** both hOCR bytes arrived over **unverified TLS** (`--insecure`, stale local CA store), stamped in
each sidecar. Not High-confidence until re-checked.

## Target 3 pre-1972 Wal-Mart

**Requested:** FY1962–FY1971 annual reports and the 1970 registration statement/prospectus.
**Bytes stored: 0 — nothing to store; every route came back with no item.** Labelled below.

**(i) Direct item-level probes — the strongest evidence, and it is a per-identifier answer, not a search.**
The held FY1972–FY1980 reports all live in one identifier family,
`<year>-annual-report-for-walmart-stores-inc`. Every year FY1962→FY1971 was probed directly
(`metadata/<id>` and `details/<id>`):

| identifier probed | `metadata/<id>` | `details/<id>` |
|---|---|---|
| `1962-… -inc` … `1971-…-inc` (all 10 years) | HTTP 200 with a **2-byte body `{}`** — no item record | **HTTP 404** |

Ten identifiers, ten 404s. For contrast, the same call on `1972-annual-report-for-walmart-stores-inc`
and the FY1975/FY1976 items returns a full file list. **Verdict: no pre-1972 Wal-Mart annual report exists
on IA at this family's identifiers.**

**(ii) Collection-level check — positive evidence of absence, bounded to this collection.**
`collection:(walmart_reports)` → **numFound 42, 42 rows returned, zero non-annual-report items, earliest
member `1972-annual-report-for-walmart-stores-inc`** (run is contiguous 1972 → 2005+). Because a collection
enumeration returns its whole membership rather than a ranked page of a noisy index, this is a genuine
**bounded null for the printed-annual-report family**: the IA Walmart report shelf starts at FY1972, exactly
as the dossier assumed.

**(iii) Open searches — UNANSWERED, not nulls.**
* `title:("wal-mart" OR "wal-mart stores")` → numFound **7,848**, and the 200 rows served are
  `gov.uscourts.*` order PDFs and hash-named items — token noise, 0 pre-1972 rows.
* `prospectus AND wal-mart` → numFound **2**: `VOA_Africa_20190318_180000` (a radio broadcast) and one
  CIA reading-room document. Both false positives.
* `identifier:(Kilobaud1976*)`-style prefix and date-filtered variants returned 0 rows for queries that must
  match (see §Nulls), so **every 0-row search in this target is recorded as UNANSWERED.**
* Consistent with the held probe file `sources/periodicals/ia_anywalmart.json`
  (`(title:(walmart) OR title:(wal-mart) OR description:(wal-mart)) AND year:[1945 TO 1975]` → numFound 11:
  7 CIA reading-room false positives + the FY1972–FY1975 reports).

**(iv) The 1970 registration statement / prospectus — route NOT available to this agent.**
That document is an SEC object, and my brief forbids running `tools/sec_intake.py` (another agent owns it
right now); HathiTrust / Google Books / EDGAR were outside my permitted retrieval tools. **UNTRIED, not a
null.** IA returned no copy at any route tried above.

## Target 4 Microsoft 1986-1990

**Requested:** the periodical and corporate-print shelves for 1986–1990, which the probe reported as
**zero documents in any family**. **Bytes stored this pass: 3,739,411 B (2 Byte issues) into
`company_011_microsoft/sources/periodicals/`, each with a `.meta.json` sidecar.**

Availability probes on the `byte-magazine-YYYY-MM` family (the family whose 1976 run the project already
holds):

| identifier | metadata | declared layer |
|---|---|---|
| `byte-magazine-1986-01` | resolves, 16 files | `1986_01_BYTE_11-01_Robotics_djvu.txt` — 1,850,712 B |
| `byte-magazine-1987-06` | resolves, 14 files | `1987_06_BYTE_12-06_CAD_Mice_12-MHz_ATs_IBM_PS2_Family_djvu.txt` — 1,803,456 B |
| `byte-magazine-1988-08` | resolves, 12 files | `BYTE-1988-08_djvu.txt` — 1,888,699 B |
| `byte-magazine-1989-11` | **HTTP 200, body `{}` — unresolved** | — |
| `byte-magazine-1990-03` | **HTTP 200, body `{}` — unresolved** | — |

Fetched (2 of 3 resolvable probes, to stay inside budget) and grepped locally with `ia_text.py grep`:

| file held | bytes | verdict | first hits (line : text) |
|---|---|---|---|
| `byte-magazine-1986-01_djvu.txt` | 1,850,712 | **TIER1_CANDIDATE — `Microsoft` ≥40 hits** (tool caps at 40; true count not enumerated) | L82 masthead/trademark block "…Microsoft is a registered trademark…"; L83 "trademark of Microsoft Corp WordPerfect is a trademark of Satellite …"; L147 "Microsoft's Word … And do it as fast as" (advert copy) |
| `byte-magazine-1988-08_djvu.txt` | 1,888,699 | **TIER1_CANDIDATE — `Microsoft` ≥40 hits** | L219 "Microsoft C 5.0"; L254 "the Turbo Linker version 1.): Microsoft C version 5.0 and the MS overlay …" |

**What this changes and what it does not.** The "zero documents in any family" verdict for 1986–1990 is no
longer sustainable as a retrieval statement: the periodical shelf *does* carry layered issues in that window
and they are now on disk. But the hits visible so far are **third-party print about Microsoft** — trademark
blocks, compiler product names, advertisement copy — not Microsoft-issued documents; whether any of it is
Tier-1 for a founding-era claim is an analyst call, and I make none.

**UNTRIED (remainder, closed out at budget, not nulls):**
* Byte months **1986-02 → 1990-12** other than the 3 probed (the 1989-11 / 1990-03 misses may be a binding
  difference — the SEARCH_LOG records `-rescan` twins and 1988–1995 thinning — but they were not re-probed).
* **PC Week** — not queried at all.
* **InfoWorld** — not queried for 1986–1990 (the title is enumerated in the Apple notes at 120 Google-Books
  `bub_gb_*` items, none opened).
* **Microsoft official/annual publications** (10-K text, annual report, Microsoft Systems Journal, Press
  Packets) — not queried; the corporate-print shelf under `company_011_microsoft/sources/corporate_print/`
  was not touched by this pass.

**TLS:** both files arrived over **unverified TLS** (`--insecure`), stamped in the sidecars ⇒ not
High-confidence until re-checked.

## Nulls vs UNANSWERED

Tally kept deliberately separate. A **NULL** = bytes held, searched, zero hits. An **UNANSWERED** = the
bytes never arrived (404 / `{}` metadata record / timeout / script cannot reach the route), which is never
evidence of absence.

**NULLS (3) — real searched-byte zeros:**
1. Creative Computing Mar-Apr 1976 — 453,250 B held, `Apple` **0**, `666` **0**, `666.66` **0**.
2. Creative Computing Nov-Dec 1976 — 463,891 B held, `Apple` **0** (5 × `666` hits are phone numbers and
   BASIC output, none a price).
3. Creative Computing Jan-Feb 1976 (`sim_creative-computing_january-february-1976_2_1`) — 312,475 B held,
   `Apple` **0**, `666` **0**.
   Plus one near-null stated precisely: Sep-Oct 1976 (490,131 B) and May-Aug 1976 (292,534 B) hold
   **zero Apple-company references** — every `apple` hit is an idiom ("Big Apple", "apples to zoos") or OCR
   noise ("picking apple the dark"). `666.66` is absent from all 6 held 1976 layers.

**UNANSWERED (8) — bytes never arrived:**
1. `Kilobaud197609` — metadata 200/`{}` (2 B), details **404**. Never resolved.
2. `Kilobaud197611` — same. (And `Kilobaud197606`, the identifier behind the house "no text layer" note:
   same.)
3. `creativecomputingjanfeb1976` — 389,016 B layer declared in metadata but unreachable: filename contains
   a space and `ia_text.ocr_url()` does not URL-encode ⇒ HTTP 404. **Script limit, not an absent layer.**
4. `Creative_Computing_v02n01_Jan-Feb1976` — arrived at 3,414 B, too thin to call a null (the layer is one
   Hewlett-Packard advertising page, not the issue).
5. Walmart FY1975 current-year statement numerals as *paired values* — hOCR glyphs present at confidence 0–6,
   so unreadable with confidence; only the page images remain.
6. The FY1976 supplier-percentage token — `29c` at `x_wconf 0` in a second independent OCR pass.
   **Digitisation limit, not a null.** Image route only.
7. Wal-Mart pre-1972 open searches (`title:"wal-mart"` 7,848 noise rows; `prospectus AND wal-mart` 2 false
   positives) — 0 useful rows is UNANSWERED from this egress.
8. `byte-magazine-1989-11`, `byte-magazine-1990-03` — metadata `{}`, never resolved.

**UNTRIED (never attempted, budget):** Kilobaud 1977+ (layered, outside the requested window); Popular
Electronics; Walmart `_jp2.zip` (12.8 MB page images) and `_text.pdf`; the 1970 registration statement via
EDGAR/HathiTrust/Google Books (tooling owned elsewhere); Microsoft 1986-02→1990-12 beyond the 3 probes;
PC Week; InfoWorld 1986–1990; Microsoft corporate-print/annual publications.

**Positive-but-labelled:** the only dollar-shaped 666 anywhere in held 1976 bytes is still
`company_004_apple/sources/ia_byte_1976/byte-1976-12.txt:39849` — "a $666 value" (competitor anchor), and
`666.66` still occurs in **zero document bytes** repo-wide (every repo hit is analysis commentary).

## Left for a human

**Bytes added by this pass (all new files; nothing existing was edited, moved or deleted):**

| company | path | new files | bytes |
|---|---|---|---|
| Apple | `founders_playbook/01_companies/company_004_apple/sources/periodicals/` | 6 layers + 6 `.meta.json` | 2,015,695 B (5 usable issues = 2,012,281 B; 1 stub 3,414 B) |
| Walmart | `founders_playbook/01_companies/company_002_walmart/sources/periodicals/` | 2 hOCR layers + 2 `.meta.json` | 2,680,318 B |
| Microsoft | `founders_playbook/01_companies/company_011_microsoft/sources/periodicals/` | 2 layers + 2 `.meta.json` | 3,739,411 B |
| **Total** | | **10 documents + 10 sidecars** | **8,435,424 B ≈ 8.4 MB** |

Every byte in the table arrived over **unverified TLS** (`--insecure`, stale local CA store); each sidecar
carries `"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"`. **None of it may carry
High confidence until a human re-checks the route.**

**For a human eye, in priority order:**
1. **Walmart FY1975 + FY1976 page images** — `1975-…_jp2.zip` (12.8 MB) / `_text.pdf` (4,852,652 B) and the
   FY1976 equivalents. Two specific readings are open: FY1975's own-column net sales / total assets / equity
   (hOCR prints `$236,208,880` at confidence 6 against column head `1975` at confidence 0), and FY1976's
   supplier-concentration token printed `29c` at confidence 0. **The 2/3-digit ambiguity ($226,209 vs
   $236,209) and the "29 vs 2" reading cannot be closed by any script on this item.**
2. **Re-check the Apple Byte 1976 negative against an actual Apple-placed advertisement.** The Wikimedia-hosted
   October 1976 Apple-1 advert (Interface Age insert per `research/D_adversarial.md` W8/W11) is the only lead
   that could still produce a genuine in-window Apple price line; **Interface Age 1976 has 7 IA items and no
   item-level probe was made for them by this pass** (UNTRIED).
3. **Script defects found while servicing these requests (for whoever owns `tools/`; I did not touch it):**
   * `ia_text.py` passes the page count as `rows[]`, which the IA API answers with **exactly 1 doc** —
     `search --rows 200` returned 1 row for queries whose `numFound` is 159/170. Use `rows=` (verified by
     raw curl) or the enumeration silently under-reports by two orders of magnitude.
   * `ia_text.ocr_url()` does not URL-encode the filename, so **every text layer whose name contains a
     space 404s** (`creativecomputingjanfeb1976`, and by the same mechanism the whole `Kilobaud 1977-01`
     family of space-named layers, which the 2026-09-25 SEARCH_LOG already flagged as a naming trap).
   * `ia_text.py` resolves only `*_djvu.txt`; it cannot reach `_hocr.html`, which is the layer that
     recovered content the `djvu.txt` pass dropped for Walmart FY1975. Both Walmart fetches above were
     therefore done with curl on the metadata-declared `server`+`dir`.
   * `grep_local()` caps at 40 hits and the CLI prints 12, so "40 in-page hits" in a verdict means
     **≥40**, not exactly 40.
4. **Conflicts this pass surfaced but did not adjudicate** (analyst-owned):
   `research/A2_chronology_finance.md` W-57 vs W-92 read the same held line
   (`WALMART_AR_1976.txt:424`) as "29c / not recoverable" and as "more than 2%" as FACT respectively.
5. **Apple verdict for the record:** after adding 2.0 MB of genuine 1976 print, **no Apple-placed 1976 price
   line exists in held bytes**, and `666.66` still appears in **zero** document bytes anywhere under
   `sources/` — it remains correctly held at FOUNDER CLAIM / UNKNOWN. Kilobaud 1976 is **UNANSWERED** (the
   items do not resolve), and the inherited statement that "Kilobaud's 1976 items carry no text layer"
   should be corrected to: *no 1976 Kilobaud item exists at those identifiers at all; the IA run begins at
   1977* (`s1_p2.md` §E.4, AP-34, DG-4 — instruction-layer files I did not edit).

