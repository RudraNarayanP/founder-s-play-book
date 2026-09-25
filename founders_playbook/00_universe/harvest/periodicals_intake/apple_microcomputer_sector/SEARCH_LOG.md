# SEARCH LOG — target 2: APPLE / MICROCOMPUTER-SECTOR periodicals via Internet Archive

Run window **2026-09-25T06:59Z → 07:16Z**. Requests are itemised in `../_REQUEST_LEDGER.tsv`.

**Baseline this pass had to beat** (from `company_004_apple/sources/_RETRIEVAL_LOG.md` and the
`ia_byte_*` / `ia_homebrew` directories): BYTE **1976-01…1976-12** (all 12), BYTE **1977-04, -05,
-06, -07**, BYTE **1980-12** and **1981-02**, plus 13 Homebrew Computer Club newsletters.
The brief required that anything added here be a **NEW TITLE or a NEW YEAR, and say which**. It does;
the labels are in the right-hand column of §A and §B.

## A. BYTE — new years, enumerated and two retrieved

| item | state |
|---|---|
| `identifier:(byte-magazine*)` → HTTP 200, **numFound 230** (223 issue-level + 7 stray files/collections) | **POSITIVE (inventory)** — **NEW YEARS** below |

Issue-level identifier pattern is stable: `byte-magazine-YYYY-MM`, with `-rescan` twins on some
months. Full availability by year, with what the project already holds struck out:

| year | issues on IA | **NEW (not held)** |
|---|---|---|
| 1975 | 09, 10, 11, 12 (Vol 00 Nos 01-04 — the founding quarter) | **ALL 4 NEW** |
| 1976 | 01-12 | 0 — all held |
| 1977 | 01, 02, 03 (+03-rescan), 04, 05, 06, 07, 08, 09, 10, 11 (+11-rescan), 12 | **01, 02, 03, 08, 09, 10, 11, 12 = 8 new months** |
| 1978 | 01-12 (+6 rescan twins) | **ALL 12 NEW** |
| 1979 | 01-12 (+5 rescan twins) | **ALL 12 NEW** |
| 1980 | 01-12 (+1 rescan) | 11 new (1980-12 held) |
| 1981 | 01-12 | 11 new (1981-02 held) |
| 1982-1987 | 12-19/yr (incl. rescan twins) | **ALL NEW** |
| 1988-1995 | 1988 10 · 1989 7 · 1990 2 · 1991 4 · 1992 8 · 1993 3 · 1995 1 | **ALL NEW**, thinning after 1987 |

Retrieved this pass (whole text layers to scratch outside the repo, then bounded):

| identifier | issue | layer | state |
|---|---|---|---|
| `byte-magazine-1977-09` | Vol 02 No 09 "Music and Computers" | 860,344 B / **135,895 words**, HTTP 200 07:04:47Z, byte-exact | **POSITIVE — NEW MONTH.** → `BYTE_1977-09_EXTRACT_apple2_ad_and_editorial.txt` (25 "Apple" hits) |
| `byte-magazine-1975-09` | Vol 00 No 01 "The Worlds Greatest Toy" — the first BYTE ever published | 443,605 B / 63,757 words, HTTP 200 07:04:52Z, byte-exact | **POSITIVE — NEW YEAR.** Content test: **0 "Apple" hits** (recorded as a documented negative, not a null on the run) |

## B. The four other titles named in the brief

| title | query | numFound | state | text layer proved? |
|---|---|---|---|---|
| **Kilobaud** | `identifier:(Kilobaud*) OR title:(kilobaud)` | **179** | POSITIVE (inventory) — **NEW TITLE**; per-year in the returned set: 1977 ×27, 1978 ×25, 1979 ×28, 1980 ×24, 1981 ×24, 1982 ×20, 1983 ×10, 1984 ×10, 9 undated. Two binding families coexist: `KilobaudYYYYMM` and `kilobaudmagazine-YYYY-MM` (the latter renames to *Kilobaud Microcomputing* 1980 → *Microcomputing* 1981-82) | **YES — and it corrects a house note.** `metadata/Kilobaud197701` → HTTP 200 → file list contains **`Kilobaud 1977-01_djvu.txt`, 746,892 B**. `_RETRIEVAL_LOG.md` records "Kilobaud 1976 … have no `_djvu.txt` text layer → scans only"; that holds for the three **1976** items probed there (`Kilobaud197606/10/12`), but **1977-onward Kilobaud does have a text layer** — and note the layer filename contains a **space**, so any `startswith(<identifier>)` layer test will miss it. 1975/1976 Kilobaud: not re-probed → UNTRIED |
| **Interface Age** | `title:("interface age") OR identifier:(Interface-Age*)` | **99** | POSITIVE (inventory) — **NEW TITLE**; per-year 1975 ×1, 1976 ×7, 1977 ×3, 1978 ×1, 1979 ×14, 1980 ×13, 1981 ×14, 1982 ×15, 1983 ×4, 27 undated | **MIXED.** `metadata/InterfaceAge197910` → HTTP 200, real item, layer **`Interface Age 1979-10_djvu.txt` 643,138 B**. But `metadata/InterfaceAge197610` → HTTP 200 with a **2-byte body `{}`** — the identifier appears in the search index and resolves to nothing. Same for `creativecomputing-1977-11`. **State: UNANSWERED (metadata 200/empty-object) for that item**, so "Interface Age 1976 is unreadable" must not be written either way until a live 1976 identifier is taken from the search body |
| **Creative Computing** | `identifier:(CreativeComputing*) OR identifier:(creative-computing*)` | **197** | POSITIVE (inventory) — **NEW TITLE**; per-year 1974 ×2, 1975 ×7, 1976 ×9, 1977 ×14, 1978 ×14, 1979 ×24, 1980 ×26, 1981 ×15 … 1985 ×13. **Nov/Dec 1977 exists in at least three parallel bindings**: `CreativeComputing_v03n06_NovDec1977`, `creative-computing-november-december-1977`, `CreativeComputingbetterScan197711` | **YES.** `CreativeComputing_v03n06_NovDec1977` → HTTP 200 → layer `Creative_Computing_v03n06_Nov_Dec_1977_djvu.txt` **691,621 B**. Retrieved whole and mined → `CREATIVECOMPUTING_1977-11_EXTRACT_apple_mentions.txt`: **3 "Apple" hits** (reader's software catalogue naming Sol-20/PET/Radio Shack/Apple II; two dealer ads). **No Apple review in this issue** — said plainly, not oversold |
| **Popular Electronics** | `identifier:(Popular-Electronics*) OR identifier:(pop-electronics*) OR (title:("popular electronics") AND YEAR:[1974 TO 1978])` | **144** | POSITIVE (inventory) — **NEW TITLE**; per-year 1974 ×16, 1975 ×24, 1976 ×29, 1977 ×25, 1978 ×26 + strays. Identifier families: `197811PopularElectronics` (date-prefixed) and `popularelectroni05unse_2` (METS-style) | **NOT PROBED → UNTRIED.** No `metadata/<id>` call was spent here. The call to make: `metadata/197503PopularElectronics` → layer → grep `Apple`, `Altair`, `Micro Instrumentation and Telemetry Systems` |

## C. What this pass does NOT claim

* It does not claim any **new Apple-specific fact**. The BYTE Sept 1977 advertisement adds a
  verifiable address/telephone string for Apple Computer Inc. (`20863 Stevens Creek Boulevard,
  Bldg. B3-C, Cupertino, California 95014`, `(408) 996-1010`) and a price pair
  (**$1298 system / $598 board-only**) in a *new month* of a held title; the project's held June 1977
  BYTE advertisement already carries the $1,298/$598 pair. Treat this as corroboration of the same
  terms in a later issue, not as a new claim.
* It does not claim the four titles are "unread" or "paper-only" anywhere: every probe that came
  back with a layer came back with a **readable** one.
* It does not re-download anything the project already holds (no BYTE 1976, no 1977-04…07, no
  1980-12, no 1981-02).

## D. UNTRIED, with the call and the reason it waited

1. **BYTE 1975-10, -11, -12** (3 new issues of a new year, ~440-600 KB each): `metadata/byte-magazine-1975-10`
   → `GET https://<server><dir>/1975_10_BYTE_00-02_…_djvu.txt`. Reason: 1975-09 was enough to prove
   the year readable; the remaining three add founding-era sector context (Altair, Homebrew) that the
   dossier already carries from the Homebrew newsletters.
2. **BYTE 1981-03…1981-12** — the IPO year, 10 new months, the class of material that flipped
   Walmart's verdict (a printed trade-press contemporaneous witness to the money). Highest-value
   remaining Apple call. Reason: 10 × (metadata + text) = 20 requests against a 21-request remainder;
   spent instead on proving the four other titles exist and are layered.
3. **Kilobaud 1976 re-probe** (`metadata/Kilobaud197606`) — to test whether the house "no text layer"
   note is a 1976-only or a whole-title condition, now that 1977-01 has one.
4. **InfoWorld / Personal Computing / Compute!** — not in the brief's list and adjacent to the
   held-period; not queried at all.
5. Any **whole-issue dump** into the repository. Every issue here is 60-130 k words; the house cap is
   60,000. All four retrieved issues were mined in scratch and shipped as bounded extracts.
