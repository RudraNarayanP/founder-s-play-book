# SEARCH LOG — target 3: UNITEDHEALTH GROUP (company_003) — 1974-1980 Minnesota business press and health-management trade print

Run window **2026-09-25T06:59Z → 07:03Z**. Requests itemised in `../_REQUEST_LEDGER.tsv`.
The point of this target, per the brief: the company_003 dossier is forensic-core largely for want of
**an independent contemporaneous witness**. Everything below is third-party print from the window,
not company print and not retrospective.

## A. THE FIND — *Minnesota Medicine*, journal of the Minnesota Medical Association (SIM microfilm run)

| item | state |
|---|---|
| `title:("minnesota medicine") OR title:("minnesota state medical journal") OR title:("banner life")` → HTTP 200, **numFound 711** | POSITIVE (inventory). Issue-level SIM identifiers exist and read like `sim_minnesota-medicine_1944-07_27_7`, `sim_minnesota-medicine_1924-04_7_4` — i.e. **single issues, with volume/issue numbers, back to 1924** |
| `identifier:(sim_minnesota-medicine*) AND YEAR:[1968 TO 1986]` → HTTP 200, **numFound 19** | **POSITIVE and simultaneously a hard EMPTY**: the 19 hits are **exactly one annual INDEX volume per year, 1968-1986, unbroken** (`sim_minnesota-medicine_1974_57_index` … `_1980_63_index`). **No single-issue scans were digitised inside 1968-1986.** The issues that do exist on this route are 1919-1963 (seen in the 711-item set) |

**Retrieved and read: all seven index volumes of the dossier's window (1974-1980).** Each text layer
pulled whole at HTTP 200, byte-for-byte equal to the size declared by its own `metadata/<id>`:

| year | identifier | Vol | layer | words |
|---|---|---|---|---|
| 1974 | `sim_minnesota-medicine_1974_57_index` | 57 | 56,258 B | 8,201 |
| 1975 | `sim_minnesota-medicine_1975_58_index` | 58 | 35,570 B | 5,322 |
| 1976 | `sim_minnesota-medicine_1976_59_index` | 59 | 33,240 B | 4,815 |
| 1977 | `sim_minnesota-medicine_1977_60_index` | 60 | 31,793 B | 4,418 |
| 1978 | `sim_minnesota-medicine_1978_61_index` | 61 | 19,672 B | 2,812 |
| 1979 | `sim_minnesota-medicine_1979_62_index` | 62 | 32,452 B | 4,592 |
| 1980 | `sim_minnesota-medicine_1980_63_index` | 63 | 28,680 B | 4,086 |

URLs are the metadata→server+dir form (servers `ia800704`, `ia800708`, `ia800803`, `ia800709`,
`ia801804`, `ia803103`, `ia801905`; times 07:02:18Z → 07:03:24Z in the ledger).
Extract shipped: **`MINNESOTA_MEDICINE_INDEX_1974-1980_EXTRACT_hmo_debate.txt`** (30,801 words of
source mined → ~1,600 words transcribed, each with a character offset).

**What it yields — citable, contemporaneous, independent, Minnesota:**

| year | line as OCR'd | cite it as |
|---|---|---|
| 1974 | "Health Planning (January) 7" — a standing editorial department of the journal | Minnesota Medicine vol 57 (1974), p 7, editorial department |
| 1976 | "Health Planning Law (PL. 93-641). (August) 511" | Minnesota Medicine vol 59 (1976), p 511 — the National Health Planning and Resources Development Act, as the Minnesota profession saw it |
| 1976 | "A Look at Child Health Manpower in Minnesota. Distribution and Context within the Health Planning Regions. … 580" | vol 59, p 580 |
| 1977 | "Report on MSMA Health Planning Program. John B. Coleman (February) 139"; "Message on Health by Minnesota's New Governor, Rudy Perpich. (March) 155" | vol 60, pp 139, 155 |
| 1978 | "Conversation with Dr. Richard K. Simmons, Family Practitioner and **Medical Director of the Physicians Health Plan**, November, 665" | vol 61, p 665 — a named Minnesota prepay plan, in the profession's own journal |
| 1979 | "**HMOs — Their Limitations and Role.** Alfred F. Anderegg, 797" | vol 62, p 797 |
| 1980 | "**HMOs — A Matter of Choice.** (February) 77" · "**Responses to HMO Editorial.** (April) 231" · "Kretchman, Lorraine A.: HMOs. (June) 391" | vol 63, pp 77, 231, 391 — the journal ran an HMO editorial in Feb 1980, printed physician replies in April, and a letter in June |

**Honest negative on the same seven volumes** (grep over the whole text layers, zero hits each):
`Burdic` 0 · `Charter Med` 0 · `Metropolitan Health` 0 · `United Health`/`UnitedHealth` 0 ·
`prepaid` 0 · `Blue Cross` 0 · `closed panel` 0. **The journal's index does not name the new HMOs in
1974-1980.** What it carries is the organised profession's debate about the form — which is the
environment UnitedHealthCare of the North (1977) was founded into, and it is independent and
contemporaneous. Two readings of that silence are open and this pass does not choose between them:
either the journal ignored the startups, or the article-level text (which exists only for 1919-1963
issues on this route) says more than the index does.

## B. Health-management trade print

| query | numFound | state |
|---|---|---|
| `(title:("health maintenance organization") OR title:("hmo report") OR title:("prepaid health care") OR title:("managed care") OR title:("health care management")) AND mediatype:(texts) AND YEAR:[1968 TO 1986]` | 40 | **MIXED.** (i) `sim_abstracts-of-health-care-management-studies_*` — a SIM digitised **annual serial: index volumes for vol 4 (1968) through vol 22 (1986), one per year, unbroken** → POSITIVE (inventory), UNTRIED for content; *Abstracts of Health Care Management Studies* is the health-management field's own annual bibliography and would list a Minnesota HMO study if one was written. (ii) `micro_IA41152920_0126` "Health Maintenance Organization: Concept and Functions. Conference Proceedings" 1972 → LEAD_ONLY. (iii) `preliminaryfeasi00char` / `apreliminaryfeas1094520994` / `preliminaryfeasi00charpdf` (1975-06) — **checked and killed**: metadata says "A preliminary feasibility study of the establishment of a health maintenance organization **on the Monterey Peninsula**", collection `navalpostgraduateschoollibrary`. A **California** HMO feasibility study, not Charter Med. Text layer 153,340 B if anyone ever wants a 1975 comparison specimen |
| `title:("medical economics") AND YEAR:[1970 TO 1985]` | 25 | POSITIVE (inventory) — annual index volumes `sim_medical-economics_1977_54_index`, `_1980_57_index`, … one per year. **Not pulled** (budget) — see the Apple/Walmart stub file §5 for the call |
| `(title:(hmo) AND (title:(directory) OR title:(statistics) OR title:(census))) OR title:("health maintenance organizations: a directory") OR title:("1979 hmo")` | 2 | **EMPTY for the window** — the only hits are `isbn_9781592372041` (HMO/PPO Directory 2008) and `hmoppodirectory20000laur` (2018). The DHEW/HCFA era HMO directories are **not on IA under these title forms** |
| `(title:(hmo) AND (creator:("health services administration") OR creator:("health care financing administration") OR creator:("department of health") OR creator:("dHEW"))) OR title:("health maintenance organizations statistics") OR title:("directory of health maintenance organizations")` | 14 | EMPTY for the window — all 14 are 1983-1991 Medicare/S-HMO demonstration reports to Congress (`interimreporttoc19unit*`, `disenrollmentexp00unit`, `designof2ndgener00finc`). Post-window for company_003's founding decade |

## C. Minnesota business press — the negative the brief asked to have proven

| query | numFound | state |
|---|---|---|
| `(title:("minnesota business") OR title:("st. paul business") OR title:("twincities business") OR title:("crm magazine") OR title:("minnesota monthly") OR title:("twin city reporter") OR title:("northland business")) AND mediatype:(texts)` | **6** | **EMPTY for the window.** The six: a 1981 microform survey, `landofgiantshist0000lars` "Land of the giants: a history of Minnesota business" (1979 — a book, in-window, Tier-2), a 1991 education agenda microform, and three 1994-1998 items. **IA holds no Minnesota business-magazine back-file 1974-1980** |
| `(title:(minnesota) AND (title:(health) OR title:(hospital) OR title:(medical))) AND mediatype:(texts) AND YEAR:[1970 TO 1982]` | 17 | **EMPTY of anything usable.** ERIC records, a Mayo/Biostor MMPI study, `City of Brainerd v. Minnesota State Board of Health` (1976), two *Minnesota Health Statistics* annuals (`micro_IA40706902_0300` 1978-11, `micro_IA40706909_0213` 1980-01 — the one in-window state statistical series found; **UNTRIED**, microform frames), school-health and health-education directories |
| `creator:("health planning council of minnesota") OR title:("minnesota hospital service") OR creator:("minnesota health planning council")` | **0** | **EMPTY** — the state health-planning agency's own print is not in the IA metadata index under its name |
| carried forward from the 2026-09-24 nightly-harvest run, not repeated here | — | `"charter med"` and `"metropolitan health plans"` were already proven **numFound 0** (queries `IA charter med 1971-1980`, `IA metropolitan health plans`) and UnitedHealth corporate print was **0 on both title- and creator-scoped forms**. Those rows live in `../candidates.csv` and were not re-spent |

## D. UNANSWERED this pass (request failed — recorded, not a null)

| call | outcome |
|---|---|
| `https://archive.org/download/sim_minnesota-medicine_1974_57_index/sim_minnesota-medicine_1974_57_index_djvu.txt` | **HTTP 0 / 0 bytes — `SSL: CERTIFICATE_VERIFY_FAILED: certificate has expired`.** Re-verifies the HARVEST README gotcha from this machine: the `download/` route 302s to a CDN whose certificate does not validate here. The metadata→`<server><dir>` route returned the same file at HTTP 200 / 56,258 B **one request later**. Not retried with verification disabled |
| `https://archive.org/metadata/InterfaceAge197610` and `…/creativecomputing-1977-11` (Apple target) | HTTP 200 but **2-byte body `{}`** — the identifier is in the search index and resolves to no item. State: UNANSWERED, and explicitly **not** evidence that the issue is missing |
| `https://archive.org/metadata/dr_shopping-goods-stores--1963--compiled-from-u-s-bu` (Walmart target) | same 200 / `{}` |

## E. UNTRIED, with the call and why it waited

1. **`Abstracts of Health Care Management Studies` annual indexes 1974-1982** — the serial is proved
   present (vol 10 = 1974 … vol 19 = 1983). Call: `metadata/sim_abstracts-of-health-care-management-studies_197X_YY_index`
   → `<server><dir>/<id>_djvu.txt` → grep `Minnesota`, `HMO`, `prepaid`, `group practice`, `new
   health plan`. At the Minnesota Medicine size class (20-56 KB) this is ~2 requests per year and is
   the **single cheapest remaining route to a named, in-window, independent witness on a Minnesota
   HMO**. Reason it waited: the budget went into proving the Minnesota Medicine seven-year run first.
2. **Medical Economics index volumes 1975-1982** (see §B row 2) — same size class, same reason.
3. **`micro_IA40706902_0300` / `micro_IA40706909_0213` *Minnesota Health Statistics* 1978/1979** —
   UIC microframe items; whether a text layer exists is untested (`metadata/<id>`).
4. **Chronicling America for the Minneapolis/St. Paul dailies** — still the blocked route
   (HTTP 403 Cloudflare, 11 UNANSWERED rows in `../candidates.csv`); this pass deliberately spent
   **zero** requests there, since the nightly runner exists to retry it from unblocked egress.
5. **Google Books / HathiTrust for the same Minnesota print** — untouched (429 / TLS). Family 3 stays
   UNANSWERED for company_003, and must be reported as UNANSWERED, not empty, in any verdict.
