# target_s1_audit2_sources_independence.md — Stage-1 AUDIT 2, sources & citations

Object: `founders_playbook/01_companies/company_042_target/` — `sources.csv` (21 rows), `stage_1.md`
(37,507 w), the other 8 registers, `CORRECTIONS.md`, `stage_1_index.md`, and the 51 held bytes under
`sources/` (36 non-sidecar files + 15 `.meta.json`).
Owner: `target-s1-audit2`. Method: `00_METHOD_AND_STYLE.md` §3 (independence + filing-lineage), §5
(tiers), §6 (time audit), §13 (schemas), §14.3/14.6/14.8/14.11/14.12, §15.3/15.5/15.6. Read RD-122 and
RD-124 before starting; RD-124's lesson ("a pointer is not a finding") is applied here to the register
itself: a Tier stamp is not a carrier.

Every byte count, hit count and passage verdict below was produced by opening the named file in this
pass. Nothing is cited from another agent's report. Where a claim could not be checked against bytes,
the verdict is **UNVERIFIABLE**, not "wrong".

**Verdict in one line:** the carriers are almost all real — 19 of 21 rows name files that exist at the
claimed byte size, and the corpus's grep counts reproduce exactly (I re-ran six of them). The defects are
concentrated in three places: **two quoted passages that the carrier does not print** (S4203, S4209) and
**one invented quote in a 40-byte file** (S4221); **the merge promoted three negative-artifact rows from
Tier 3 to Tier 1** that a sibling row in the same corpus had already graded correctly; and **four
register rows state a 1962/1967/1968 event as `FACT`/`High` on a carrier that is a recap of that event**,
which is the exact rule the volume itself states at `stage_1.md` L117-119 and applies correctly to the
adjoining rows. Negative-result discipline — the part I expected to be weakest — is **sound**: all five
unread routes named in Target's residue are recorded as UNTRIED/UNANSWERED with a command attached, and
none has become a null.

---

## Carrier check (per source row: verified / mismatch / cannot-open, with bytes)

STATUS: WRITTEN 2026-09-26

Command producing the byte column: `python - <<… os.path.getsize()` over every path token in
`archived_url`, plus `glob` expansion of the two glob-formatted cells. Passage test: read the carrier as
UTF-8, collapse whitespace, casefold, then substring-search each `||`-separated quote.

| row | carrier opened | bytes claimed → actual | quoted passage in the held bytes? | verdict |
|---|---|---|---|---|
| S4201 | `sources/corporate_print/1965_dayton_hudson_djvu.txt` | 48,050 → **48,050** ✓ (sidecar `"bytes": 48050`) | `The Company entered the discount merchandising field in 1962 with Target Stores, Inc., which now has five` — **found** (line-wrap only) | **VERIFIED** |
| S4202 | `…/1966_dayton_hudson_djvu.txt` | 43,364 → **43,364** ✓ | both quotes found verbatim (`$7.50 per visit, excluding groceries. This compares with an industry average of $5.05`; `889,000 square feet`); the row stores the 889,000 sentence **twice**, once wrapped in literal single quotes | **VERIFIED** (duplicated cell content, cosmetic) |
| S4203 | `…/1967_dayton_hudson_djvu.txt` | 45,200 → **45,200** ✓ | **NEITHER quote is in the carrier as printed.** (a) `JOHN F. GEISSE (L1952) / Senior Vice President and General Merchandise Manager` — the layer prints `JOHN F. GEISSE Senior Vice President and General Merchandise Manager`; the token `L1952` occurs in **zero bytes of all 14 held layers** (tested). (b) `Target sales were $86,901,007, an in-crease of 43 percent` — the layer prints `Sales of $86,901,007 in 1967 were 43 percent ahead of 1966 volume of $60,731,468`. The figure is real; the sentence is a paraphrase wearing quote marks, with an unmarked interpolation | **MISMATCH** |
| S4204 | `…/1968_dayton_hudson_djvu.txt` | not claimed → 52,479 ✓ sidecar | `Goods Stores 189,515,025 44 141,824,116 38 33.6` — **exact** | **VERIFIED** |
| S4205 | `…/1969_dayton_hudson_djvu.txt` | not claimed → 55,348 ✓ sidecar | `Low Margin............. 233,532 189,515` — **exact** | **VERIFIED** |
| S4206 | `…/1970_dayton_hudson_djvu.txt` | 53,023 → **53,023** ✓ sidecar agrees (this is the COR-05 byte-count re-base; disk wins, correctly) | `When the Corporation made its first public stock offering in late 1967, it had 23 stores in five states.` — found | **VERIFIED** |
| S4207 | `…/1971_dayton_hudson_djvu.txt` | not claimed → 55,420 ✓ sidecar | passage is the 7 characters `At year` — present, but it cannot carry anything | **VERIFIED-BUT-VACUOUS** |
| S4208 | `…/1972_dayton_hudson_djvu.txt` | not claimed → 75,196 ✓ sidecar | `Target opened 16 new stores within a seven-month period` — found | **VERIFIED** |
| S4209 | `…/1973_dayton_hudson_djvu.txt` | not claimed → **114,193** ✓ sidecar | first quote is **not printed as quoted**. The carrier reads `NamiberF OF StOFES O55 oxen atk veins vie ns. ps 50 50 34 27 19 Total square feet (thousands) anh 5,563 5,518 4,220 3,516 2,390`. The *digits* are all present; the *clean labels* are not — `Number of Stores` is OCR-mangled, and the two rows are joined in the register with `' and '`, a form no carrier prints. Second quote (`Target has grown from 11 stores to 46 stores in five years`) is present verbatim | **MISMATCH** (reconstruction of an OCR-damaged line, unmarked) |
| S4210 | `…/1974_dayton_hudson_djvu.txt` | not claimed → 113,815 ✓ sidecar | passage is the single word `Roseville` — present | **VERIFIED-BUT-VACUOUS** |
| S4211 | `…/1975_dayton_hudson_djvu.txt` | not claimed → 130,295 ✓ sidecar | `Dayton Hudson Corporation Annual Report -- 1975` — exact (masthead) | **VERIFIED** |
| S4212 | `…/1999_annual_report_djvu.txt` | not claimed → 113,428 ✓ sidecar | `George Dayton opens Goodfellows in down` — exact. `1902` occurs exactly once in the layer, inside the interleaved chronology spread (`1902 1946 1954 1969 1978 … Ol 0 EE 0 I 6 …`), i.e. the year and its sentence are **not** adjacent in the bytes. The row's own confidence (`Low`) and `B1S14`'s note ("tick↔blurb pairing unres[olved]") say so, and `stage_1.md` L93/L427 use it only as evidence the company *told* the story in 1999 | **VERIFIED** — correctly capped |
| S4213 | **no carrier** — `archived_url = none` | — | uncheckable: 2013-07-06 obituary never fetched | **CANNOT-OPEN (declared)** — the row itself says `NOT HELD so it cannot be evidence` |
| S4214 | **no carrier** — `archived_url = none` | — | uncheckable | **CANNOT-OPEN (declared)** |
| S4215 | `sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt` | 170,260 → **170,260** ✓ sidecar | passage found modulo one OCR space (`first—␣\nthe shopping-center` in bytes vs `first—the shopping-center` in the cell); the cell's em dashes are genuine U+2014, not corruption (checked raw bytes: 4 × `e2 80 94`, 0 × U+FFFD). Volume's `168,433 chars` reproduces exactly (my `len()` = **168,433**). Its five grep counts reproduce exactly: `Target` 0, `Goodfellow` 0, `Minnesota` 0, `Dayton` 2, `Hudson` 3 — and §H.2 (L734-737) names all five non-company hits (`DAYTON, OHIO`; `J. L. HUDSON REAL ESTATE CO.`; `HUDSON PLAZA`; `Hudson House, Inc.`), so `does not name the company once` is **true and argued**, not assumed | **VERIFIED** |
| S4216 | `sources/ia_search/meta_01-target-archive.json` | not claimed in row; volume cell says 259,567 → **259,567** ✓ | `relevant_passage` = `61 DjVuTXT layers listed with per-file names` + `NO_VERBATIM_PASSAGE_RECORDED` — a description, not a quote. The description checks out: `files` list has **61** entries of format `DjVuTXT`, earliest year-labelled **1965**, latest **2024**, and exactly **17** `Image Container PDF` legs (1965-76, 1985-86, 1990-91, 1994). Caveat the register does not state: one of the 61 (`01 Target Archive_djvu.txt`) carries **no year**, so the run is 60 year-layers + 1 item-level aggregate; and the same item holds 45 `Text PDF` + 17 `Additional Text PDF` + 61 `hOCR` + 61 `chOCR` — `stage_1.md` L2003's "the item's **62** text layers" is **not reproducible** under any single format count I could make (every text-bearing per-page class is 61) | **VERIFIED (file + counts); passage is not a quote** |
| S4217 | `sources/_index/raw_submissions_CIK0000027419.json` | not claimed → **149,561** ✓ | `formerNames: DAYTON HUDSON CORP from 1994-12-09 to 1999-04-12` — reformatted, but the JSON holds exactly one `formerNames` entry with those two ISO timestamps → **substantively verified**. `submissions.csv (2628 rows)` → **2,629 lines = 2,628 data rows** ✓. `and the slice list` → present: `filings.files` = 1 slice, `CIK0000027419-submissions-001.json`, `filingCount 1628`, `1994-02-10 → 2016-04-25`, and `1000 recent + 1628 slice = 2628` ✓, which is why `_INDEX.md`'s `## UNANSWERED slices` = `(none)` is a true statement **about this CIK** | **VERIFIED (summary-form, not verbatim)** |
| S4218 | `sources/name_search/{dayton+hudson,dey+brothers,goodfellow,target+corporation}.atom` | 7,747 each × 4 → **7,747, 7,747, 7,747, 7,747** ✓ | cells are `(no readable passage …)` + `NO_VERBATIM_PASSAGE_RECORDED`, honest. But the row and the volume assert **HTTP 503**; the held bodies are SEC HTML error pages whose visible text contains `500` and `temporarily` and **no `503` token**, and **no sidecar exists for any `name_search/` file** — so the status code is an assertion the carrier cannot show. Status: **the 503-vs-500 question is UNVERIFIABLE from bytes held** (the server response line was never captured). Files exist, sizes match | **VERIFIED-AS-EXISTING / asserted status code UNVERIFIABLE** |
| S4219 | `sources/name_search/fts_%22…%22.json` × 4 | not claimed → 1,021 / 1,021 / 1,019 / 1,018 | zero-hit claim **verified in bytes**: each response carries `"hits":{"total":{"value":0,"relation":"eq"}` | **VERIFIED** |
| S4220 | `sources/web_archive/{cdx_targetcom,cdx_dhc}.txt` | 11,832 each → **11,832, 11,832** ✓ | bodies are an `Internet Archive: Temporarily Offline` HTML page; visible text carries `500`, not `503`; **no sidecars**, so again the status code is unbacked. Row's own `independence_note` — "independent of the company but unreachable" — is the correct characterisation | **VERIFIED-AS-EXISTING / asserted status code UNVERIFIABLE** |
| S4221 | `sources/sec/_MANIFEST.csv` | not claimed → **40 bytes** | **the quoted passage is not in the carrier.** The file is exactly one line: `accession,file,path,bytes,words,status\n` — a header with **no data row**. `0 documents stored,0 skipped/unanswered` is a *statement about* the file, presented inside the `relevant_passage` cell as if it were text *from* it | **MISMATCH (invented quote)** |

**Row totals: 19 rows name a file that exists; 12 fully verified (S4201, S4202, S4204-S4208, S4211,
S4212, S4215, S4216, S4217, S4219 — S4216/S4217 verified via independent re-count because their cells are
descriptions); 3 mismatches (S4203, S4209, S4221); 2 declared cannot-open (S4213, S4214); 2 verified-as-
existing with an unverifiable status assertion (S4218, S4220).** The two status-code rows are also the two
rows whose tier is most inflated — see §Tier inflation: a row that is honest about being a dead route is
not thereby a Tier-1 source.

**Transport-stamp asymmetry (carrier check, sub-finding).** `sources.csv` marks `UNVERIFIED TLS` in
`archived_url` for exactly 2 of the 5 layers whose sidecars carry that stamp. Sidecars reading
`transport: UNVERIFIED TLS` = 1966, 1967, 1971, 1973, 1974 (5 files, read this pass). Rows stating it =
S4202, S4203. Rows silent = **S4207, S4209, S4210** (`held locally: …`, no stamp). A reader of the register
alone — not the sidecars — cannot apply U.037's Medium cap to FY1971/73/74.

---

## Lineage violations

STATUS: WRITTEN 2026-09-26

Target's volume is, on this axis, better than most of the corpus: `stage_1.md` L109-119 states the
single-lineage finding and enforces it ("eleven consecutive stockholder reports FY1965→FY1975 from **one
digitised item**, one uploader, one reporting lineage, plus three later layers (FY1998/99/2000) from the
same item … Repetition across report years is **version evidence, never corroboration**"). The defects are
where the **registers** depart from that rule, not where the prose states it.

1. **S4211 (FY1975 report) claims independence for a company self-report on the ground of who scanned it.**
   `independence_note = "digitised by a third-party backfile service not by the company"`. §3: independence
   means an independent **origin** ("an SEC accession, an auditor's report, a contemporaneous newspaper
   that did not use the filing, a court record, an unrelated third party's data"). A digitisation vendor is
   a conduit, not an origin; the FY1975 layer is the same filer's own report in the same item as S4201-S4210,
   and the volume's own lineage paragraph counts it inside the eleven. **This row asserts corroboration
   weight the document cannot have, and it contradicts `stage_1.md` L111-113 in the same company.** Worst of
   the three lineage defects.
2. **Six of the eleven same-lineage rows carry no lineage caveat.** §3 requires `independence_note` to say
   `same lineage as S00xx` wherever only the lineage exists. Rows that do: S4201, S4202, S4206, S4208, S4212
   (and S4210's "one source however many later reports reprint it"). Rows that **do not** and describe only
   their own OCR condition or masthead: **S4203, S4205, S4207, S4209, S4211** (and S4204's note covers the
   reprint direction only). Consequence: a downstream reader can count FY1967's `86,901,007` (S4203) and
   FY1968's group row (S4204) as two sources for the founding-decade growth story.
3. **The index-plus-body pattern is present but bounded — with one leak.** S4217 correctly bundles the EDGAR
   index JSON, the derived `submissions.csv` and `_INDEX.md` into **one** row. The leak is a *held file with
   no row*: `sources/_index/submissions.json` (576,114 B) — larger than the raw JSON it derives from and
   named by no register cell. And the more serious one: `sources/_index/_INDEX.md` L5-6 reads **"This file is
   the source of truth for what exists. Do not re-search EDGAR for coverage; grep `submissions.csv` and
   report a form as absent only from this list."** Inside a Tier-1-stamped bundle, that instruction turns a
   **1994-02-10 registrant floor** into a global existence statement for the next agent, while U.036 in the
   same register keeps "did any predecessor ever register?" open. Per §14 rule 10, an instruction-layer
   sentence a cold reader trusts is the highest-severity home for an over-reach; the file is true for CIK
   27419 (I verified the arithmetic) and says nothing about predecessor CIKs, which is not what it reads as.
4. **S4216 + the eleven layers: the catalogue counts as a second witness for the corpus's own shape.**
   `evidence_class = CATALOG-LEVEL FACT`, and the folded `P1S06` note is honest ("metadata proves the run is
   1965-2024; it proves nothing about what the company did before 1965"). The merged row keeps a weaker
   version — "the only evidence for the 1965 to 2024 layer run" — so `A04` ("No held byte in any family names
   the company before the FY1965 report … a catalog boundary proven from held metadata") rests its *negative*
   half on an index of the very items it says are silent. §14.6's "zero here is zero" requires the body, not
   the index. The volume's §U.2 wording for U.024 is disciplined; the register cell is not (see
   §Negative-result discipline #2).
5. **One-lineage rule applied twice, differently, inside the same register.** `timeline.csv` row
   `1967-late` (High, `FACT`, S4206) and row `1971-04-16` (High, `RESTATED`, S4206) are the same sentence in
   the same carrier; the second labels the recap, the first does not. See §Tier inflation #6.

---

## Tier inflation

STATUS: WRITTEN 2026-09-26

**The single demonstrable merge-created inflation** — a byte-for-byte comparison against the pre-merge
emissions still on disk (`_parts/s1_p1.md` L776-783, `_parts/s1_p2.md` L1179-1186, and the same rows in
the merged volume's own register-emission block at `stage_1.md` L831-834):

| bytes held | pre-merge tier | merged `sources.csv` tier | what the document is |
|---|---|---|---|
| 4 × `name_search/*.atom` (7,747 B SEC HTML error pages) + 4 × `fts_*.json` + 2 × `cdx_*.txt` | **P1S08 = tier 3**, "Negative artifacts: … an error page is a dead route, never an absence" | **S4218 = 1, S4219 = 1, S4220 = 1** | error pages and a search response with `hits.total.value = 0` |
| `sources/sec/_MANIFEST.csv` (40 B, header only) | P2S07 = 1 | **S4221 = 1** | our own tool's empty manifest |
| `sources/ia_search/meta_01-target-archive.json` | P1S06 = 1 / P2S05 = 1 | **S4216 = 1**, confidence **High** | Internet Archive catalogue metadata |
| `raw_submissions_CIK0000027419.json` | P1S07 = 1 with the note *"the registrant's own index; **it cannot witness anything before its own floor**"* | **S4217 = 1** with the note replaced by **"independent of the company"** | an SEC index (registrant-line facts only) |

1. **S4218 / S4219 / S4220 at Tier 1.** Per §5 and RD-124's rule, these are Tier 3 at best and are evidence
   about a **route**, not the company. The corpus already knew: the sibling row that covered the identical
   bytes at the identical moment was stamped **3**, and the merged volume still prints that `3` at L834, one
   screen above the register's `1`. Whatever the merge's reason, the register and its own audit trail now
   disagree about the tier of the same bytes. The `evidence_class` cells are honest (`UNANSWERED - dead
   route`, `INDEX FLOOR - not a null`); the tier cell is the lie.
2. **S4221 at Tier 1 for a 40-byte, header-only CSV emitted by `tools/sec_intake.py`.** Tier 1 is
   "SEC and other regulatory filings, annual reports, incorporation and court records, patents, archived
   company pages, original interviews, contemporaneous statistics." A tool's own manifest is none of these.
   Compounded by the invented quote (§Carrier check, S4221). Two defects in one 40-byte row.
3. **S4216 at Tier 1 / High.** Catalogue metadata is an index into a corpus; it can prove what the corpus
   contains (`A04`) and nothing about the company. Verified counts make it reliable, not Tier 1.
4. **S4213 Tier 2 and S4214 Tier 4 are tiers on documents never opened.** Both cells say `NOT HELD` and the
   notes refuse evidentiary use, so the rows do no harm *as written* — but §5 tiers are properties of
   carriers. A row with no carrier should read `tier = UNASSIGNED (lead)`. Flagged, low severity, because
   Target uses them correctly (below).
5. **S4217: Tier 1 is arguable, the note is not.** `formerNames` is SEC-attested, so registrant-line facts
   may carry it. What must not survive is the swap of P1S07's self-limiting note for "independent of the
   company": the merged cell teaches that an index whose floor is 1994-02-10 is an independent witness for
   the founding decade.
6. **Confidence the carrier cannot carry — four register rows (the worst defects in this file).**
   The volume's rule, `stage_1.md` L117-119: *"no retrospective recap carries a FACT about a decision in this
   volume. Recaps carry FACT-about-the-printing and RETROSPECTIVE INTERPRETATION-about-the-event, in two
   separate records, always."* `timeline.csv` violates it on rows whose carrier **is** the recap:
   - `1962-early`, "First Target store opens", **`FACT` / High**, S4201 — a FY1965 report narrating 1962.
     The adjoining row `1962` ("Four Target units carry opening year 1962 …") is correctly **`RETROSPECTIVE
     INTERPRETATION at three years' remove` / Medium**, and §6 (L268) says the opening is *"FACT as to the
     printing; RETROSPECTIVE INTERPRETATION as to the act"*. Same fact, three treatments, one register.
   - `1962`, "The Dayton Company enters discount merchandising through Target Stores, Inc.", **`FACT` /
     High**, S4201 — same 1965-dated narration. Its note argues from voice ("narrated in the first person
     plural by the entity that did it"); §6 is a **time** audit, not a voice audit, and FY1999's genealogy
     spread — a *further* 37 years out — is capped at Low for exactly this reason (correctly).
   - `1967-late`, "Corporation first public stock offering with 23 stores in five states", **`FACT` / High**,
     S4206 — note concedes *"printed in the FY1970 Operating Review rather than in a 1967 layer"*.
   - `1968`, "Two new Target stores open in St. Louis and Target ends the year with **eleven** stores",
     **`FACT` / High**, S4204 — the row's own note: *"openings CONTEMPORANEOUS (S4204 L688) but the
     eleven-store total is a **1973 recap** (S4209 L565)"*, and S4209 is an **UNVERIFIED-TLS** layer the
     volume caps at Medium (L546 grades that total *Medium; RESTATED, so never corrobor…*). A High `FACT`
     row therefore contains a restated figure carried by an unverified transport.
   Also `1962` / Brookdale (`FACT`/High, S4201) — same class, but COR-03 already owns that row's trap and
   the note refuses the Target reading, so I record it as consistent with the corpus's own correction.
7. **One row's `source` cell is prose, not a pointer**: `quantitative.csv` — 1 of 61 rows reads
   `source = "no held layer prints a 1963 or 1964 Target opening"` (confidence `UNKNOWN`). Honest content,
   unresolvable address (§13: `source_id`/`source` "points at `sources.csv`"). Four further `source` cells
   carry a duplicated token (`S4209 S4209`) — a visible COR-06 re-join seam, resolvable but not clean.

**What this audit checked and found *clean*, so the list is not read as blanket suspicion:** the UNVERIFIED-
TLS Medium cap is honoured **without one exception** — every register row citing S4202/S4203/S4207/S4209/
S4210 (27 in `quantitative.csv`, 7 in `timeline.csv`, 4 across `validation`/`decisions`/`channels`) is
`Medium` or `Low`; **zero** High. The retrospective FY1999 genealogy is capped at Low and is never used to
date 1902-1961. The masthead assertions behind the genealogy table are real: I tested `DAYTON CORPORATION`
absent from the 1966 layer, present in 1967; `DAYTON HUDSON CORPORATION` absent from 1968, present in 1969 —
so the "first layer under masthead X" claims in S4203/S4205 hold, and the §Boundary filename-vs-masthead
refutation (K3) is correctly argued against the uploader's labels.

---

## Negative-result discipline

STATUS: WRITTEN 2026-09-26

Every route the brief names as "unread" is recorded as UNTRIED/UNANSWERED **with a command attached**, in
both the volume (`§U.4`, L2011-2068) and `data_gaps.csv`. I found **no untried route converted into a null**
in the prose. What I found instead is **two register cells whose wording states a corpus-wide null over a
family the same register admits it never ran.**

| route | where it is recorded as not-done | verdict |
|---|---|---|
| **17 PDF image legs** | `U.030` L2013-2021 — *"this pass ran no PDF leg"*; §H.5 `UNTRIED-1`; cited as the follow-up on U.008, U.009, U.012, U.020, U.021, U.022; count independently **verified as exactly 17** `Image Container PDF` files in `meta_01-target-archive.json` | **UNTRIED, correctly held open.** U.022 says the figures are "absent **from the OCR**, not proven absent from the reports" — model phrasing |
| **Founder-credit obituaries (K1/U.001, S4213/S4214)** | `U.031` L2023-2028, issued as a **`FETCH REQUEST`** with destination path `sources/documentary/` and the reason it cannot be run here ("web budget for this volume is 0 calls"); `data_gaps.csv` U.031; `conflicts.csv` U.001 kept live; §Boundary L136-137 — "One of them (**K1**) is not resolved and is not resolvable from this corpus; it stays live"; L247 the founder question is "carried as a **lead with a named route** … never as a conclusion about why he" | **UNTRIED, and neither unheld row is used as corroboration anywhere.** `failures.csv` has 1 row and it is not this |
| **HathiTrust for the pre-FY1965 leg** | `U.032` L2030-2036 with the literal command (`periodical_harvest.py --query-set target_dayton_print_1955_1964 --use-curl`, `GOOGLE_BOOKS_API_KEY` absent); RD-122 names the same route as the one that could lift T2→T1 | **UNTRIED.** But see defect #2 below — the U.024 wording undercuts it |
| **Predecessor-CIK retries** | `U.036` L2057-2062, with the compliant-UA URL and `sec_intake.py index --cik <n> --from 1930-01-01 --to 1985-12-31`, and the explicit refusal: *"Until this runs, 'one registrant line only' is the limit of the EDGAR record, **not** a proof that no predecessor filed"*; `U.025` = UNANSWERED | **UNTRIED/UNANSWERED, correctly held open.** Risk is in `_INDEX.md` L5-6 (Lineage #3), not in the register |
| **Five UNVERIFIED-TLS layers** | `U.028` = **UNANSWERED (transport)**, "egress/trust-store defect, not an evidence result"; `U.037` = **UNTRIED (re-verification)** with the fix (`--upgrade certifi` / `--use-curl`) and the named consequence set (Q3-Q8, Q16-Q19, §K.3, FY1974 roster) | **Recorded, and — verified — the cap actually binds** (see Tier inflation's last bullet). Only defect: 3 of the 5 rows don't stamp the register cell |

Defects in this section, both in **wording at the register layer**:

1. **U.024 / U.019 stated as corpus-wide nulls over unrun families.** `data_gaps.csv` U.024
   `why_missing = "…and **no family returned** an earlier document"`, and the merged volume's own
   register-emission copy at L915: *"and **no family reached** an earlier document"*. The same register's
   U.032 says book corpora were **never searched**, and the volume's §U.2 prose for U.024 says the opposite
   of the cell: *"WHAT MAY NOT: that no FY1964 report exists anywhere; **no other carrier has been
   searched**"* (L1963). Same for U.019: the gap title is *"**no contemporaneous periodical mention** of
   Target or of the Goodfellow and Dey names"* while its own `why_missing` says "only one periodical leg is
   held" and its follow_up names U.032/U.034. §14.6: "a null from one family is not a null, and an untried
   family is not a null either." The prose is clean; the two cells are the defect a cold reader inherits.
2. **The status codes on U.025/U.026 are asserted beyond their carriers** — "HTTP 503 on all four" /
   "503 twice" with bodies that print `500` and `temporarily`, and **no sidecar** for any `name_search/` or
   `web_archive/` file. §14.9 requires provenance beside the bytes; without it, the *kind* of failure (a
   rate-limit vs a genuine service-down) is unrecoverable, and it changes the retry advice. The **use** is
   correct — both rows refuse to read the failure as absence — so this is a provenance gap, not a null
   error.
3. **N3/U.020's name-presence counts are real, not asserted** — I re-ran them: `GEISSE` = 3 (FY1965, 1966,
   1967, one each), `DOUGLAS J. DAYTON` = 18, `Dey` = 0 across exactly 11 founding-era layers. The volume's
   "not founder evidence either way" framing is the right ceiling on a grep.

---

## Sweep counts

STATUS: WRITTEN 2026-09-26

Each number with the command that produced it (all run this pass, cwd
`founders_playbook/01_companies/company_042_target/`).

| what | command | result |
|---|---|---|
| source rows | `python -c "len(list(csv.DictReader(open('sources.csv'))))"` | **21** × 18 cols (gate agrees) |
| other registers | `csv.DictReader` per file | `quantitative` 61 · `timeline` 24 · `conflicts` 18 · `data_gaps` 22 · `decisions` 3 · `validation` 4 · `failures` **1** · `channels` 3 → **157 rows** total, matching `stage_1_index.md` and RD-122 |
| files held under `sources/` | `glob('sources/**/*',recursive=True)` split on `.meta.json` | **51** total = **36** non-sidecar + **15** sidecars (matches the brief) |
| sidecar coverage | `os.path.exists(f+'.meta.json')` per `.txt` | 15 of 17 text bodies have a sidecar; the 2 without are `web_archive/cdx_*.txt`. **No sidecar exists for any of** `name_search/` (8 files), `ia_search/` (6), `_index/` (4), `sec/` (1) — i.e. **19 held files carry no provenance record**, which is why the 503/500 question above cannot be settled |
| bytes named by a row | path-token extraction from `archived_url` | **12** distinct files resolved and opened; byte claims matched for all 6 rows that state a size (48,050 / 43,364 / 45,200 / 53,023 / 170,260 / 259,567 and 7,747 ×4, 11,832 ×2) |
| **held but named by no row** | basename-in-cited-string test | **8**: `corporate_print/1998_annual_report_djvu.txt` (**118,286 B**, verified-TLS), `corporate_print/2000_annual_report_djvu.txt` (**112,543 B**, verified-TLS), `_index/submissions.json` (**576,114 B**), `ia_search/meta_chain-store-age.json` (7,311 B), `q_corp_title.json` (14,506 B), `q_corp_creator.json` (1,668 B), `q_csa.json` (617 B), `q_dsn.json` (414 B). **The two 1998/2000 layers are used as evidence anyway** — `data_gaps.csv` U.026 `best_available_evidence = "FY1998 layer naming www.dhc.com; FY1999 layer We are Target Corporation …"`. I verified both strings in the bytes: `www.dhc.com` **present in the FY1998 layer** (which prints no `Target Corporation` at all), `We are Target Corporation` **present in the FY1999 layer**, and the FY2000 layer prints `Target Corporation Annual Report 2000` — so the *facts* hold and only the **rows** are missing. §14.11: cite them or record why they don't bear |
| unverified-TLS layers | sidecar `transport` field | **5** (1966, 1967, 1971, 1973, 1974) — matches U.028 exactly; rows stamping it: **2 of 5** |
| CSA grep counts | `re.findall` on the held layer | `Target` 0 · `Goodfellow` 0 · `Minnesota` 0 · `Dayton` 2 · `Hudson` 3 · chars **168,433** — all reproduce the volume's numbers exactly |
| eleven-layer name counts | same, over `corporate_print/19[67]*.txt` (11 files) | `GEISSE` 3 · `DOUGLAS J. DAYTON` 18 · `Dey` 0 |
| metadata counts | `json.load(meta_01-target-archive.json)` | `files` 633 · `DjVuTXT` **61** · `Image Container PDF` **17** · `Additional Text PDF` 17 · `Text PDF` 45 · `hOCR` 61 · `chOCR` 61 — earliest year label **1965**, latest **2024** |
| EDGAR index | `json.load(raw_submissions…)` + `csv.reader(submissions.csv)` | `formerNames` = **1** entry · `filings.recent` = 1,000 · `filings.files` = 1 slice (1,628, 1994-02-10→2016-04-25) · `submissions.csv` = **2,628** data rows = 1,000 + 1,628 ✓ |
| volume size | `len(open('stage_1.md').read().split())` | **37,507** words / 255,104 B (matches RD-122 and the index) |
| citation form | token counts in `stage_1.md` | global `S42xx` appears **2** times (the merge header, L797-799 range statement, and one S4221 mention); the volume cites **dossier-local** ids: `B1Sxx` 276 hits/14 ids, `P1Sxx` 55/8, `FY19xx` 511/17, `U.0xx` 351/38. `stage_1_index.md` mint map carries local→global (`S4201←P1S01+B1S01` … `S4221←P2S07`); registers use global ids **except** `quantitative.csv`, whose §13 column is `source` (10 distinct global ids inside free-text pointers) |

**GATE (run verbatim as briefed):**

```
$ python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target \
    --checks csv,keys,anchors,corrections --fail-on substantive

# Mechanical gate report -- company_042_target

Findings: **0** | Passes: 19

- coverage 9 registers, 2 stage volumes, 17 source documents
- anchors  stage_1.md declares an explicit ANCHORS set (37 ids)
- anchors  stage_1.md declares 37 anchors
- anchors  41 id(s) read as backticked references or range endpoints, not citations (U.0, U.001, …)
- anchors  3 prose mention(s) match no declared entry, ADVISORY only: U.2, U.3, U.4
- corrections 6 retraction ids; register layer reaches 6, volumes 6

## Passing checks
csv … 14 csv lines incl. `csv sources.csv 21 rows x 18 cols` …
keys     stage_1.md  2 source tokens all resolve
keys     stage_1_index.md  21 source tokens all resolve
anchors  citation resolution  every register-cited anchor resolves (44 distinct ids …)
anchors  parity  37 narrative anchors <-> 37 register anchors
corrections propagation  all 6 retraction(s) reach registers and volumes
```

**The gate is green and did not see the defects in this file — and some of that is the check set, not the
corpus.** It reports `17 source documents` while `sources.csv` has 21 rows, 19 of which name a file that
exists on disk, and `sources/` holds 36 non-sidecar files: **I could not reproduce 17 under any definition I
tried**, so the source-document census is opaque (RD-122 met the same unreproducible pass count and called
it a tool problem, not a discrepancy to chase). Within the four checks I was briefed to run there is **no
carrier test** — nothing in `csv`, `keys`, `anchors` or `corrections` opens the file a row names, compares
its bytes, or searches its quoted passage — and no tier-vs-document-class test, so three Tier-1 error pages
pass. §15.6 does list a *verbatim-quote existence* check among `gates.py`'s capabilities, but it is
**ADVISORY**, explicitly not a defect, and it is not in this check set; whether it would have caught S4203,
S4209 and S4221 is therefore **UNKNOWN**, and I did not run it (my brief fixed the four checks). `keys`
checks only that an id *resolves*, never that it points at the **right** carrier — which is how
`timeline.csv`'s `1975-12-31` row can cite **S4201** (the FY1965 layer) for a fact about what the
FY1974/FY1975 reports print, and pass. Per the brief, the budget check is excluded on purpose; RD-122
adjudicates 37,507-vs-22,000.

---

## Untried

STATUS: WRITTEN 2026-09-26

Not examined in this pass — UNKNOWN, not "clean":

1. **S4203's `(L1952)` has no origin I can locate.** It is absent from all 14 held layers, but I did not
   open the 17 PDF image legs (U.030) and ran **0 web calls**, so I cannot say whether it comes from page
   print, another dossier's note, or the author's memory. The carrier-check verdict (not in the cited file)
   stands; the *source of the interpolation* is UNKNOWN.
2. **The HTTP status of S4218/S4220's 19 failures is unrecoverable from bytes on disk.** No sidecars, no
   saved response headers. Only a retry with header capture settles it — that is `U.036`'s and `U.029`'s
   territory, not mine.
3. **`sources/ia_search/q_*.json` and `meta_chain-store-age.json` (16,241 B of search responses) were
   opened for size only, not read.** If any of them is cited in a register cell I did not parse, the
   rowless-artifact finding narrows.
4. **The FY1998/FY2000 layers were opened for three strings each** (`www.dhc.com`, `We are Target
   Corporation`, `Target Corporation`) — I did **not** audit their content, so I cannot say what evidence
   they hold that the missing rows would have to carry.
5. **`_parts/s1_p1.md` and `_parts/s1_p2.md` were read only at their register-emission lines** (tier/id
   comparison). I did not audit part-level prose, so the P1S08 `3`-vs-`1` finding is proven for the tier
   cell only, not for the merge's intent.
6. **6 claim-record fields I could not parse** (the `CLASS:`/`CONFIDENCE:` inline form in §A-§D records
   resisted my regex). The four `timeline.csv` confidence defects are proven from the register cells and
   the volume's own L117-119/L268/L546 rules; whether a **claim record** elsewhere pairs each with the
   correct FACT-about-printing twin is unverified.
7. **The other 9 registers' internal arithmetic** (Q-series footings, `derived_arithmetic` cells) — the
   brief's scope was sources and citations; quantitative integrity belongs to a different audit.
8. **`MASTER_RESEARCH_LOG.md` L1291** still prints the COR-02-retracted `1972-03-22` as a finding — COR-02
   already records it and hands it to the log's owner. I did not edit it (outside my write scope); it is
   listed here so the merge and the orchestrator both see it in the audit's own sweep, per §14 rule 10.

**Repair items this audit hands to a merge/repair agent (it fixed nothing itself, per brief):**
S4203 and S4209 quote cells; S4221's invented quote; tier cells on S4216/S4218/S4219/S4220/S4221; S4211's
independence note; the 6 same-lineage rows lacking a `same lineage as S00xx` note; U.024/U.019
`data_gaps` wording; S4207/S4209/S4210 transport stamps; two rows for FY1998/FY2000 (plus a decision on
`submissions.json`); `timeline.csv`'s 1962/1967-late/1968 classes and confidences and the `1975-12-31`
→ **S4201** pointer; `_INDEX.md` L5-6's "source of truth for what exists"; a `carrier check` in
`gates.py` (§15.5).
