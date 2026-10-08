# A_chronology_feasibility.md

# A — Chronology-feasibility probe: ExxonMobil (Fortune rank 9)

Owner: `probe-exxonmobil`. Stage-1 PROBE only. No volume, no registers, no ids minted, no certification.
Company dir (absolute): `E:\founder's playbook\founders_playbook\01_companies\company_009_exxonmobil`
All `sources/...` paths below are relative to that directory. Grep/normalisation method is §1a's, stated once.

**CONFIDENCE CAP (binding on every line here).** All **13** Internet-Archive sidecars under
`sources/periodicals/*.meta.json` + `sources/corporate_print/*.meta.json` (counted, not assumed: one
`json.load` pass printing `transport`) read
**`"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"`** — including both scans of
the 1901 Oil City Derrick volume. `sources/sec/*.meta.json` sidecars are EDGAR-transport and are not in that
set. **Nothing in this dossier is stated above Medium**, and nothing above Medium is claimed at all. Line
numbers are printed so a later pass can re-check the bytes, but byte-identity with the live item is asserted
only "as fetched".

**STATUS: WRITTEN** (§0-§11 + `## Untried` + `## Fetch requests`; §5 tiers are PROVISIONAL where flagged, and no
tier below Stage 3 is safe against a route named in `## Untried`).

---

## 0. Counts, each with the command that produced it

| count | value | how measured |
|---|---|---|
| CIKs in this company's tree | **2** — `0000034088` (historic) and `0002115436` (wrong registrant, quarantined) | `ls sources/_index/quarantine/` + `_registrant_*.json` |
| filings enumerated for CIK 34088 | **3,557 rows**; `rows_dropped_no_accession` **0**; **58** rows with no `primaryDocument` | `_registrant_CIK0000034088.json` fields, re-read from the file |
| measured EDGAR perimeter, CIK 34088 | **1994-03-04 → 2026-09-25** | `min/max` of `filingDate` over `submissions_CIK0000034088.csv` (header enumerated first: `filingDate, form, accession, reportDate, primaryDocument, source`) |
| rows dated **before 1994-03-04** | **0** (count, not inference: `len([r for r in rows if r['filingDate']<'1994-03-04'])`) | same CSV |
| SEC documents held after the 34088 intake | **11** files / **2,961,190 B** / **332,653 words** | `sources/sec/_RUN.json` (`stored`, `bytes`, `words`) + `ls sources/sec/*.txt \| wc -l` = 11 |
| intake tally anomaly | `attempted 78`, `stored 11`, `unanswered 0`, `skipped 67`; `identity_ok: false` → **BROKEN** | `_RUN.json`. `duplicate_slots` names the cause exactly: `nameless:0000950103-99-000247:911 in skipped and skipped` and `…:906 in skipped and skipped` — **raw 78 / unique 77**, one accession double-listed in the S-4's own document stream, not a lost document |
| print/periodical text layers held | **13** (`.txt` under `periodicals/` + `corporate_print/`) | `md5sum` pass (see §4a): **12 distinct works**, because `pureoiltrustvsst00oilc_djvu.txt` is **byte-identical** (md5 `242183d1d4100c0755a75bf4cfcc0fd0`) in `corporate_print/` and in `periodicals/` — ONE document, two paths, never two families (hard rule 4) |
| SEC shelf size | `sources/sec/` = **27 files** = 11 `.txt` layers + 11 `.meta.json` sidecars + **5 run artefacts** (`_RUN.json`, `_MANIFEST.csv`, `_PLAN.csv`, `_SKIPPED.csv`, `_UNANSWERED.csv`) — **none of the five is CIK-keyed or run-keyed**, which is §6a's refusal | `ls sources/sec \| wc -l` and `ls sources/sec \| grep -v txt` |
| harvest candidate rows for this slug | **108** in the current A4 (12 mined, **94** left untried at the `--limit`) | `research/A4_harvest_mine.md` L5, snapshot **2026-10-06 17:33:15 +0530**, md5 `cd48afb583465b641be727aeb9d5d566`. The file was **rewritten by the fleet's corporate-print lane mid-run** (it read 63/6/56 at mtime 2026-09-29 23:31:28 when this probe started) — see §11 |
| layers that arrived **during this probe** | **6** — `micro_IA41152954_0005`, `micro_IA41153045_0441`, `micro_IA41153438_0701`, `micro_IA41155163_0728` (mtime 2026-10-06 **17:33**) and SOCal annual reports **1956, 1957** (17:32) | `find sources -type f -newermt '2026-10-06 12:00'`-style mtime listing. The facet-free corporate-print reharvest is writing this tree **while I read it**; §4d reports them and excludes them from every verdict |
| web calls made by this probe | **0** (hard rule 1) | none; `WebSearch`/`WebFetch` unused |

`periodical_harvest.py` and `harvest_mine.py` were **not run** (fleet lanes own them tonight); every route
either owns is reported **UNTRIED with its command** in `## Untried`, never as a null.

---

## 1. The registrant problem, stated as measured

This is the deepest predecessor-chain case in the universe, and it opened with a **wrong-registrant intake**.
Both states are on disk; both are reported here because the orchestrator's quarantine is evidence about the
tool, not about the company.

**CIK 2115436 — the registrant SEC's own ticker file gives you.** `python tools/legacy_cik.py detail 2115436`:

```
CIK 0002115436 ExxonMobil Holdings Corp | recent rows 34, earliest 2026-07-01, latest 2026-09-25 | 0 archive slice(s)
     tickers ['XOM'] | formers []
```

`XOM → 2115436`, filings begin **2026-07-01**, **0 archive slices**, **no former names**. An intake run against
it stored **0 documents for every window** — that result was correct arithmetic about the wrong legal person.
Its artefacts now sit in `sources/_index/quarantine/CIK0002115436/` (`_INDEX_CIK0002115436.md`,
`submissions_CIK0002115436.csv`, and a `dropped_rows_CIK0002115436.csv`). It is a **recent holding company**;
it carries no history of anything before 2026 and must not be used for any stage.

**CIK 34088 — the historic registrant.** `python tools/legacy_cik.py detail 34088`:

```
CIK 0000034088 EXXON MOBIL CORP | recent rows 1001, earliest 2020-01-03, latest 2026-09-25 | 2 archive slice(s)
     tickers [] | formers ['EXXON CORP']
```

`walk: 2 slices` was read in full (RD-134's cap is gone: `--max-slices` defaults to every slice), so the
3,557-row enumeration is the registrant's **whole** EDGAR index, not a truncated head. The guard passed
(`guard: ok — slug token(s) ['exxonmobil'] match registrant 'EXXON MOBIL CORP'`, RD-135's de-spaced matcher).
The 1866-1999 search window stored **11 documents, 0 UNANSWERED, 67 SKIPPED**.

**Two structural facts follow, and they drive everything else in this dossier.**

1. **EDGAR's floor for this registrant is 1994-03-04 — measured, and it postdates the entire origin window.**
   `0` rows before it (command in §0). Standard Oil of New Jersey's 1911–1972 life, the Vacuum/Humble
   acquisitions, and the pre-1999 Mobil line are all **outside** what family (a) can reach. This is not
   "the company filed nothing": 1911-1993 filings, if they exist as SEC records, live in the paper-era
   archives that `sec_intake` does not enumerate for this registrant. **Verdict: measured perimeter, not a
   null.**
2. **EDGAR's live name chain reaches back exactly one rename.** `formers ['EXXON CORP']` — that is all the
   current index carries. But the **archival bytes carry deeper**: the header of the stored 1999 S-4 prints
   `sources/sec/0000950103-99-000247_0000950103-99-000247.txt` **L47-49**:
   ```
   FORMER COMPANY:
   FORMER CONFORMED NAME: STANDARD OIL CO OF NEW JERSEY
   DATE OF NAME CHANGE: 19721123
   ```
   on `CENTRAL INDEX KEY: 0000034088` (L22), `STATE OF INCORPORATION: NJ` (L25), `COMPANY CONFORMED NAME:
   EXXON CORP` (L21). **This is the single most load-bearing carrier in the dossier**: EDGAR's own registrant
   metadata, in a filing, states that the present registrant is the *same legal person* as Standard Oil Co of
   New Jersey, renamed **1972-11-23**. The live submissions index has since dropped that row, so the archive
   beats the index — a 1999 filing byte is the only place in this tree where the 1911-era name is tied to
   CIK 34088 by the SEC rather than by the company's prose.

**STATUS: WRITTEN**

---

## 2. The CIK-by-CIK lineage table this probe could actually build

Each row states the **legal person**, what the reachable record says it *is* to the next row, and the command
that measured its perimeter. "no CIK reachable" is not "no CIK existed" — see the `## Untried` note U-3.

| # | legal person | CIK reachable? | measured perimeter / evidence | relationship to the registrant, and the document that says so |
|---|---|---|---|---|
| 1 | **ExxonMobil Holdings Corp** | **CIK 0002115436** | 34 rows, **2026-07-01 → 2026-09-25**, 0 slices, `formers []`, holds the `XOM` ticker | **NOT an ancestor and not the historic registrant.** A post-2026 holding company that inherited the *ticker*. Reachable, irrelevant to every stage window. Quarantined in `sources/_index/quarantine/CIK0002115436/`. |
| 2 | **EXXON MOBIL CORP** | **CIK 0000034088** | **1994-03-04 → 2026-09-25**, 3,557 rows, 2 slices, `formers ['EXXON CORP']`, SI class 2911, state **NJ**, IRS 13-5409005 | **The registrant.** All tier verdicts in §5 are measured against bytes filed by this person or printed about its ancestors. |
| 3 | **EXXON CORP** | same person as #2 | `_registrant` `formers` row + S-4 header L21-23 | **Name-change stage of the registrant**, not a separate CIK. EDGAR records the change **1972-11-23** out of Standard Oil Co of New Jersey. |
| 4 | **STANDARD OIL CO OF NEW JERSEY** | **no separate CIK — and correctly so**: it is #2 under its old name | S-4 header **L47-49**; the live index no longer carries the row | **Same legal person as the registrant, by SEC metadata.** The name-change date is *the date SEC recorded it*, not an independent corporate act (Citigroup §5 warning applies). |
| 5 | **Standard Oil Company (the 1870/1882 combination)** | **no CIK reachable** | named **1,575** times in the 1901 print (§4b); `standard oil` = **1** occurrence in all 11 held SEC files | Predecessor of the *combination*, not a registrant. Only print reaches it. |
| 6 | **Vacuum Oil Company, of Rochester, N.Y.** | **no CIK reachable** — `legacy_cik search "Vacuum"` → 2 modern registrants (Vacuum Process Technology, 2001/2013), neither related; `search "Vacuum Oil"` **PARSE FAILED** | named at **L18534 / L18541** of the 1901 print, with the explicit statement that Standard Oil owned Vacuum stock but not its management | Mobil-side ancestor. **Unreachable.** No byte in this tree connects Vacuum to any registrant. |
| 7 | **Humble Oil Refining Co / Socony / Magnolia / Socony-Vacuum** | **no CIK reachable** — `search "Humble"` returns 24 unrelated modern filers (David R Humble, Humble Bundle…); `search "Humble Oil"`, `"Socony"`, `"Standard Oil of New Jersey"` all **PARSE FAILED (3500-byte answer, 2 retries)** | **0** occurrences of `humble`, `socony`, `magnolia` in the S-4 **and 0 in all 11 held SEC files**; `socony`/`magnolia`/`humble oil` **0** in the 1901 print | Mobil-side ancestors of the *brand* line. Nothing in the reachable record even names them. |
| 8 | **MOBIL CORP** | **CIK 0000067182 — found, not assumed** | `legacy_cik detail 67182`: **1994-02-14 → 2000-02-09**, 124-125 rows, **0 archive slices**, `formers []`, ends with `15-12B` (deregistration after the merger) | **A separate registrant, and this probe could NOT intake it.** `auto "MOBIL CORP"` → `NO-MATCH (0 candidates)`; `auto "67182"` → resolved `by cik-digits`, then **`*** REFUSED-WRONG-REGISTRANT … Everything went to …quarantine/CIK0000067182`** (log `E:\founder's playbook\_probe_xom_mobil_cik.log`). Its bytes are therefore unread here — see §6 and FETCH REQUEST F-1. |
| 9 | **Mobil Corporation, a Delaware corporation** | the party named in #2's own instrument | S-4 **L13804-13806**: "…between Exxon Corporation, **a New Jersey corporation** ('Exxon'), and **Mobil Corporation, a Delaware corporation** ('Mobil')" | **The merger's second legal person — Delaware.** So Mobil's New York/Texas ancestor chain (rows 6-7) must cross into a Delaware corporation somewhere, and **no held byte says when or how**. `mobil corporation` **82** / `mobil oil corporation` **17** in the S-4 — a naming split a later pass must resolve. |
| 10 | **Standard Oil Company of California** | not sought (belongs to company_021) | 5 annual-report layers 1956-1960 held in *this* tree, `standard oil company` 11-26 hits each, **`of new jersey` 0** | **SIBLING, not ancestor** — the other 1911 successor. It is here only because the harvest query was `standard oil`. Excluded from every verdict (§7.4). |

**What this table proves, and what it does not.** Rows 2-4 + 9 are **documented**: the registrant is the same
legal person as Standard Oil Co of New Jersey (SEC metadata) and as Exxon Corporation (EDGAR `formers`), and
its 1999 merger partner was a **Delaware** corporation named Mobil Corporation. Rows 5-7 are ancestors the
registrant's own filings **never name**: measured across all 11 held SEC files, `standard oil company of new
jersey` = 0 (the only `standard oil` in the corpus is the abbreviated header row at S-4 L48), `vacuum` = 0,
`humble` = 0, `socony` = 0, `1911` = 0, `1870` = 0, `1866` = 0. **The 1999 merger instrument prints no ancestor
story at all** — it is a prospectus about two live companies, not a lineage claim. Every pre-1972 lineage
statement in this tree therefore comes either from the registrant's own 10-K sentence (§3) or from third-party
print (§4), never from the merger filing.

---

## 3. Family (a) — SEC/EDGAR filings: TRIED-ANSWERED, with a hard measured floor

The 11 held documents (`sources/sec/_MANIFEST.csv`, header enumerated before any field was read):

| # | accession | form | filed | bytes | words | what it contributes |
|---|---|---|---|---|---|---|
| 1 | 0000950131-94-000279 | DEF 14A | 1994-03-04 | 100,680 | 12,413 | earliest reachable filing; `exxon corporation` 12 |
| 2 | 0000950131-94-000308 | 10-K | 1994-03-11 | 309,792 | 32,880 | **L130 the founding recital**; cover block L1320 "INCORPORATED IN NEW JERSEY" |
| 3 | 0000034088-94-000006 | 8-K | 1994-09-21 | 6,756 | 831 | nothing lineage-bearing (`new jersey` 2) |
| 4 | 0000950109-95-000647 | 10-K | 1995-03-10 | 242,356 | 23,800 | recital repeated (1882 = 1) |
| 5 | 0000950117-95-000238 | S-3 | 1995-06-28 | 78,365 | 9,589 | 1882 = 1 |
| 6 | 0000930661-96-000138 | 10-K | 1996-03-08 | 262,203 | 26,649 | **L187** recital repeated verbatim |
| 7 | 0000930661-97-000575 | 10-K405 | 1997-03-13 | 358,948 | 39,999 | recital repeated |
| 8 | 0000930661-98-000526 | 10-K405 | 1998-03-18 | 402,757 | 39,491 | recital repeated |
| 9 | 0000950103-98-001093 | SC 13D | 1998-12-11 | 21,528 | 2,692 | the merger notification filing, 1998-12-11 |
| 10 | 0000930661-99-000626 | 10-K | 1999-03-30 | 287,106 | 27,729 | recital repeated |
| 11 | **0000950103-99-000247** | **S-4** | **1999-04-05** | **890,699** | **116,580** | **the merger registration statement — L47-49 SONJ former-name row; L13804-13806 the two constituent corporations** |

**The founding recital, in the registrant's own words** —
`sources/sec/0000950131-94-000308_0000950131-94-000308.txt` **L130**, again at
`sources/sec/0000930661-96-000138_0000930661-96-000138.txt` **L187**:

> "Exxon Corporation was incorporated in the State of New Jersey in 1882."

Six of the eleven files print `1882` exactly once, and each time it is this sentence. **Class: FOUNDER CLAIM /
RETROSPECTIVE INTERPRETATION — company self-narrative at 1994 about 1882** (§3 independence rule: the six
10-K/10-K405/S-3 repetitions are **one lineage, not six witnesses** — the same corporate statement refiled).
It is the only incorporation-date statement for the ancestor anywhere in this tree, and it names the
registrant's *own* incorporation, not the 1911 dissolution and not any acquisition.

**What family (a) cannot do.** Its floor is **1994-03-04** and 0 rows precede it (§0), so **0 held filings in
1866-1993**: filings cannot place a single word inside Stages 1 or 2 as proposed in §5, and they can only
describe the 1999 merger from just outside Stage 3's end. The recital survives here only because the
registrant's *renaming* (1972) and *merger* (1999) are EDGAR-era acts; its *origin* is not.

**Reachable-but-unfetched, from the same enumeration (no new index walk needed).** `_SKIPPED.csv` holds **67
slots**, of which the lineage-relevant ones are: **16 further documents at accession 0000950103-99-000247**
(L15 prints `PUBLIC DOCUMENT COUNT: 17`; only sequence 1 was taken), 8 more FY1999 10-K document slots, and the
index's own earliest-per-form table (`sources/_index/_INDEX_CIK0000034088.md`) names the merger-carrier filings
never stored: **DEFM14A 1999-04-08 (0000950103-99-000260)**, **424B3 1999-12-06 (0000950117-99-002528)**,
**S-8 POS 1999-09-28**, **4 1999-11-30 (0000950103-99-001036)**, **SC 13D/A 1999-02-09**. Those are the
cheapest route to the merger's *completion* mechanics, which no held byte currently prints (the patterns
`expected to be completed`, `consummation is expected`, `third quarter of 1999` return **0 lines** in the stored
S-4 — measured, and narrower than "the S-4 gives no date").

**False-entity control on this family (trap 3).** Oil-industry vocabulary fires constantly and means nothing:
`refinery` = **30** occurrences across the 11 files with zero lineage content, and `chase` = **87** hits in the
S-4 which resolve to **The Chase Manhattan Corporation / Chase Manhattan Bank** as a director's employer
(S-4 L6501-6504) and to **Fox Chase Cancer Center** (L6407) — RD-124's same-sounding-noun class, live in these
bytes. Every adjacency claim here was taken with the entity word hard against an identity word, and is quoted
with its line number.

**STATUS: WRITTEN**

---

## 4. Families (c) and (d) — the print that is on disk, opened and re-grepped

Method, stated once and used for every count below: per-file `re.sub(r'[^a-z0-9]+',' ',text.lower())` then
`re.sub(r'\s+',' ',…)` then `len(re.findall(re.escape(v), norm))`, over `sources/periodicals/*.txt` +
`sources/corporate_print/*.txt` (13 layers). Punctuation becomes a **space**, never deleted (RD-124 defect 2).

### 4a. The shelf is 13 layers = **12 distinct works**

| file | bytes | mtime | what it actually is | lineage value |
|---|---|---|---|---|
| `corporate_print/pureoiltrustvsst00oilc_djvu.txt` **and** `periodicals/pureoiltrustvsst00oilc_djvu.txt` | 3,294,656 each | 09-26 15:32 / 09-29 23:31 | **Byte-identical (md5 `242183d1d4100c0755a75bf4cfcc0fd0`) — ONE document on two shelves.** It cannot be two families (hard rule 4), and the family must be taken from the retrieval route, not the directory a file landed in | see 4b |
| `periodicals/pureoiltrustvss00derrgoog_djvu.txt` | 3,193,448 | 09-29 23:31 | **A second scan of the same 1901 work** (Google-derived copy; different md5, fewer OCR-recoverable hits: `standard oil company of new jersey` **6** vs 8, `pure oil trust` 81 vs 118, `vacuum` 21 vs 28). §3's independence rule: **one lineage, not a second witness** | corroboration count stays **1** |
| `periodicals/mobrat00unit_djvu.txt` | 121,995 | 09-29 23:31 | **U.S. House of Representatives committee print, February 1976** — L13-38 "MOBIL OIL CORPORATION: FAILURE TO DELIVER NATURAL GAS TO THE INTERSTATE MARKET / REPORT BY THE SUBCOMMITTEE ON OVERSIGHT AND INVESTIGATIONS / COMMITTEE ON INTERSTATE AND FOREIGN COMMERCE / NINETY-FOURTH CONGRESS … / U.S. GOVERNMENT PRINTING OFFICE, WASHINGTON: 1976" | **Tier-1 third-party naming of the Mobil side at 1976** — L202 "Isle 95 Field, operated by Mobil Oil Corporation"; 11 hits `mobil oil`. **No incorporation date, no predecessor** (`vacuum`/`humble`/`socony`/`standard oil` = 0) |
| `periodicals/standard-oil-company-of-california-annual-report-{1956,1957,1958,1959,1960}` | 67-75 K each | 09-29 23:30-31 + **10-06 17:32-33** | Corporate print **of a different successor** (Chevron's ancestor, company_021's lineage). `standard oil company` 11-26 hits each, **`of new jersey` 0** | **EXCLUDED from every verdict.** Sibling, not ancestor (trap 1). They are here because the harvest query was the bare trade term `standard oil` |
| `periodicals/micro_IA41152954_0005` (65,522 B), `micro_IA41153438_0701` (195,001 B), `micro_IA41155163_0728` (47,553 B), `micro_IA41153045_0441` (5,585 B) | — | **10-06 17:33 (arrived while this probe ran)** | **ERIC / U.S. Dept-of-Education microfiche reprints**, not company print: `micro_IA41152954_0005` L10 "INSTITUTION **EXXON Education Foundation**, New York, N.Y." (Wingspread Conference report, October 1985); `micro_IA41153438_0701` L10 "INSTITUTION **Exxon Research and Engineering Co.**, Linden, N.J."; `micro_IA41155163_0728` L8 an Exxon Education Foundation science-education meeting; `micro_IA41153045_0441` is a **catalogue skeleton with empty AUTHOR/TITLE fields** | **0 hits on all eight lineage vocabularies.** They name **subsidiaries/foundations**, not the registrant and not an ancestor — the same class as Citigroup's `micro_IA41153428_0048`. Counted in family (c)'s *trial*, **not** in any tier |

### 4b. The one genuine Stage-1 carrier: the 1901 Oil City Derrick volume

Title page read with line numbers (`corporate_print/pureoiltrustvsst00oilc_djvu.txt`; 72,853 lines):

```
L44  | PURE OIL TRUST
L50  | STANDARD OIL COMPANY,
L53  | BEING  The Report of An Investigation
L62  | United States. Industrial Commission,
L65  | Compiled From Private and Official Sources
L67  | By The. Oil City Derrick,
L69  | 1899=1900.
L72  | 1901:
L74  | DERRICK PUBLISHING CO., PRINTERS,   L76 | OIL CITY, PA.
```

Predecessor namings inside it, at line level:

- **L626** — "…New York City, vice-president of **the Standard Oil Company of New Jersey**"
- **L632** — "Mr. John D. Rockefeller, president, and Mr. S. C. T. Dodd, solicitor of **the Standard Oil
  Company of New Jersey**, submitted to the commission in writing replies…"
- **L20649**, **L72656** — two further "Standard Oil Company of New Jersey" namings with officers attached
- **L18534** — "**the Vacuum Oil Company, of Rochester, N.Y.** The executive officers of this company were
  Messrs. H. B. and C. M. Everest, of Rochester…" and **L18539-18541** — "The Messrs. Everest were not at that
  time, nor have they ever been interested in the stock of the Standard Oil Company. **The Standard Oil Company
  were owners in the stock of the Vacuum Oil Company**, but had no direct relation whatever with the management
  of its affairs." (the surrounding year is OCR'd **"ISSl"**, unreadable — **not citable as a date**)
- Phrase counts: `standard oil company` **1,575** · `standard oil company of new jersey` **8** ·
  `pure oil trust` **118** · `vacuum` **28** · `1899` **120** · `1870` **61** · `1882` **25** ·
  `humble` **0** · `socony` **0** · `1911` **0** (this volume was printed a decade before the dissolution).

**What this carrier is, and what it is not.** It is a **trade/industrial-press compilation of a federal
investigation** (U.S. Industrial Commission testimony), published by the Oil City Derrick in **1901** — i.e.
**third-party, contemporaneous, and inside the origin window**, which is the carrier class the Citigroup probe
never found. It establishes that "the Standard Oil Company of New Jersey" existed as a named legal person with
officers at 1901, and that the Vacuum Oil Company was a **separate** legal person whose stock Standard Oil owned
while it disclaimed management control. **It does not carry any founding act.** Read against the adjacency rule
it actively refuses three tempting misattributions:

1. Its `1882` hits are about **the Standard Oil Trust** — L3722 "the formation of the Standard Oil Trust, which
   was formed in 1882", L5409 "…the combination was solely by stock… until 1882". **None** prints an 1882
   *incorporation in New Jersey* (lines containing `1882` **and** `incorporat|organiz|new jersey|charter` →
   **0 shown**). So the 1901 print **does not corroborate the registrant's 1882 recital**; it attests a
   *different* 1882 act, the trust formation. Two 1882s, one year, different legal facts.
2. Its New Jersey incorporation language is about the **opponent**: L4418-4419 "**the Pure Oil Company, a
   corporation organized and existing under the laws of the State of New Jersey**"; L46299-46300 "it has since
   been sought by a reorganization of that concern, which took place about **1897** under the laws of New
   Jersey. **The Pure Oil Trust was reorganized under the laws of New Jersey in 1897**"; L4734 "said company
   was organized in the State of New Jersey, **not to do business in said State**". Attributing any of that to
   Standard Oil is the oil-vocabulary adjacency trap firing exactly as briefed.
3. L620 of the same file lists "…New York City, president **Commercial Travelers'** National League" — RD-124's
   "Travelers can be travellers" decoy class, live in these bytes.

**Family (d) honest verdict: TRIED–ANSWERED, returning nothing for this lineage.** The only corporate-print
items on the shelf are the five Standard Oil **of California** annual reports (a sibling successor) and the
duplicate copy of a trade-press book. **No annual report, house organ, directory or yearbook of Standard Oil of
New Jersey, Humble, Vacuum, Socony or Mobil is held.** A `corporate_print/` shelf holding one file out of thirteen
layers, byte-identical to its `periodicals/` twin, is the clearest statement of that.

**STATUS: WRITTEN**

---

## 5. Proposed stage windows (PROPOSED — the universe CSV has no founding-date column) and per-stage tiers

`00_universe/fortune_top_50_2026.csv` carries no founding date, and `harvest_mine.py`'s window for this slug is
**1866-01-01 → 1999-12-31** (`research/A4_harvest_mine.md` L3), which the harvester's own header admits is a
*search setting* ("deliberately WIDE where the founding date is itself unestablished"). The boundaries below are
taken from **measured bytes** where a byte supplies them, and from assertion where none does — each row says
which. They are PROPOSED and are not applied to any register.

| stage | proposed window | boundary evidence | families returning **in-window Tier-1 text** | tier |
|---|---|---|---|---|
| **Stage 1 — origin of the ancestors** | **1866-01-01 → 1911-12-31** | ends at the 1911 dissolution, the event that made SONJ an operating major. **`1911` = 0 occurrences in every held byte**, so this end boundary is *asserted, not evidenced here* — Stage 1's first open question | **1 — (c)** the 1901 Oil City Derrick volume (SONJ named with officers at L626/L632/L20649/L72656; Vacuum Oil Co of Rochester N.Y. at L18534; printed 1901, third-party, in-window). **(a)** 0 (floor 1994-03-04, measured). **(d)** 0 distinct in-window company print. **(b),(e)** UNTRIED | **T3** |
| **Stage 2 — SONJ as a separate major → renamed Exxon** | **1912-01-01 → 1972-11-23** | end boundary is **SEC's own recorded name-change date**, S-4 **L49** `DATE OF NAME CHANGE: 19721123` — the only stage boundary in this dossier fixed by a registrant-level document | **0.** In-window print on the shelf is Standard Oil *of California* (sibling, excluded); the 1976 House print is out-of-window; the filings floor is 1994. The 1972 rename is carried by **(a)** only as 1999 metadata *about* a 1972 act, which is not a 1972 document | **T3 (PROVISIONAL — the stage most likely to move)** |
| **Stage 3 — Exxon Corp → the 1999 merger** | **1972-11-24 → 1999-11-30 `(PB)`** | start = day after the measured rename. The end **1999-11-30 is the brief's own boundary and is NOT evidenced by any held byte**: patterns `expected to be completed`, `consummation is expected`, `third quarter of 1999` → **0 lines** in the stored S-4. The index's earliest post-merger artefacts are `4 1999-11-30 (0000950103-99-001036)` and `424B3 1999-12-06`; everything past the boundary — the FY1999 10-K, the 8-K/A 2000-02-11, and **the whole post-1999 Valdez litigation history** — is `(PB)` | **2 — (a) 8 in-window filings** (1994-03-04 DEF 14A → 1999-04-05 S-4; the S-4 prints the merger's two constituent legal persons at L13804-13806 and the SONJ former-name row at L47-49) **+ (c) the 1976 House committee print** naming Mobil Oil Corporation as a gas-field operator (L13, L202) | **T2 core (PROVISIONAL)** — 2 families counted, neither provisional in itself; a third family from (d)/(b)/(e) takes it to T1 |

**Planning consequence.** Stage 1 and Stage 2 are **T3 register** work (short narrative + registers; §K, §N, §U
still mandatory; 8k words/stage; ≈3-4 runs). Stage 3 is **T2 core** (22k words/stage, 6-9 runs). Rank 9 does
**not** buy a dense origin: it buys a dense **Stage 3**, because the EDGAR floor (1994-03-04) postdates the whole
origin window and the corporate-print shelf holds a sibling's annual reports. Per RD-112, name the window a
future re-grade moves: a trade-press run moves **Stages 1-2**; the Mobil CIK intake moves **Stage 3** (and
Stage 2 only if a Mobil-era predecessor filing surfaces); neither touches Stage 1's structural emptiness.

**Valdez handling (trap 4).** `valdez` is **not absent** from this corpus: it occurs in six of the eleven held
filings — `sources/sec/0000034088-94-000006…txt` **L115, L128, L146** ("the tanker Exxon Valdez in 1989", "as a
result of the Exxon Valdez grounding", "claims arising from the Exxon Valdez oil spill") and
`sources/sec/0000950131-94-000308…txt` **L2720, L2998, L3845**. Every one of those is a **1994 filing describing
1989**, i.e. `RETROSPECTIVE SOURCE` for Stage 3 and flatly **(PB)** for Stages 1-2. No 1989-dated carrier of the
event exists in this tree, and no Valdez fact may be written into an origin-stage file.

**STATUS: WRITTEN**

---

## 6. Families (b) and (e), and the predecessor-registrant intake gap

**(b) WEB ARCHIVES — UNTRIED.** No command in this brief's verified tool list reaches a capture-timestamp
index, and the probe ran **0** web calls (hard rule 1). Measured tool state: `grep -il "wayback|web.archive|/cdx/"
tools/*.py` returns exactly **one** file, `tools/periodical_harvest.py`, which is **fleet-owned tonight and was
deliberately not run**. So the family has an owner; this probe just was not allowed to use it. Per RD-097/§14(6)
the family floor is ~1996-12-29, so it could only ever bear on Stage 3's last three years and on the post-1999
`(PB)` tail — it cannot touch Stage 1 or Stage 2 at all. **Untried, never a null.**

**(e) AUCTION / MUSEUM / MANUSCRIPT — UNTRIED.** `grep -ric "sotheby|christies|auction|manuscript|sale room"
tools/*.py` (zero-count files suppressed) returns **one** hit, `tools/_tmp_b_dossier_csv_fix.py:1`, which is a
string inside a one-off repair script's prose ("…are auction prose"), **not a retrieval route**. No sale-room or
accession-catalogue command exists for this slug, and no web budget was available. §14(6) and RD-097 make this
family a tier input in its own right (Apple, Walmart, Berkshire all moved on it), and for an oil major the
obvious targets are Standard Oil of New Jersey / Humble / Vacuum manuscript collections and company-archive
finding aids. **Untried.**

**(c) sub-route state, stated precisely.** Chronicling America is **UNTRIED by tool condition, not by policy**:
`tools/ca_endpoint_probe.py` exists to decide which CA URL shape answers, and its own header records that
**from this machine all four candidate shapes returned 403** (Cloudflare bot management), while
`periodical_harvest.py`'s CA path returned 404 for three consecutive nightly runs — **209 CA rows, 0 answers,
122 UNANSWERED**. I did not run the probe: it writes its own output file into the repo, outside the one path I
own. Remedy is the CI lane, named in `## Untried` U-6. HathiTrust is likewise UNTRIED; `tools/ia_text.py` L37
records that this machine's egress is blocked against HathiTrust, which is why the fleet's harvester owns that
route.

### 6a. The intake gap that decides the Mobil question

Mobil's own registrant was found, not assumed: **CIK 0000067182, MOBIL CORP, perimeter 1994-02-14 → 2000-02-09,
0 archive slices, `formers []`**, deregistered via `15-12B`. Two commands then refused to let this probe read
its bytes:

```
python tools/sec_intake.py auto "MOBIL CORP" --company-dir <this dir> --from 1994-01-01 --to 2000-02-09 --max-docs 4
  identity 'MOBIL CORP' not resolved: NO-MATCH name 'MOBIL CORP' (0 candidates); pass --ticker or --cik
python tools/sec_intake.py auto "67182" … (same flags)
  identity: '67182' resolved to CIK 0000067182 (None) by cik-digits
  index: registrant guard = quarantine -- no slug token ['exxonmobil'] appears in registrant name 'MOBIL CORP' …
  *** REFUSED-WRONG-REGISTRANT: EDGAR answered 'MOBIL CORP' for CIK 0000067182 but this directory is
      'company_009_exxonmobil'. Everything went to …sources\_index\quarantine\CIK0000067182; no canonical
      index was touched.  *** Re-run with the legacy registrant's CIK, or --allow-mismatch …
```

Full log: `E:\founder's playbook\_probe_xom_mobil_cik.log`. The guard behaved **correctly** — its artefacts are
CIK-keyed (`_INDEX_CIK0000067182.md`, `submissions_CIK0000067182.csv`, `dropped_rows_CIK0000067182.csv` in
`quarantine/CIK0000067182/`, created 17:37 during this probe) and the canonical 34088 index was not touched.
But the consequence is structural and belongs in the record: **the tree can hold only one registrant's story at
a time**, so no probe can build a two-registrant merger lineage inside a single company directory.

**I did not pass `--allow-mismatch`, and that was a measurement, not timidity.** `sources/sec/_RUN.json`,
`_MANIFEST.csv`, `_SKIPPED.csv`, `_PLAN.csv`, `_UNANSWERED.csv` are **not CIK-keyed and not run-keyed** (the
five files listed by `ls sources/sec | grep -v txt`). A second registrant's `auto` pass through the same
directory would overwrite the run record of the 34088 intake — the exact intake state this brief ordered me to
report, including the `BROKEN` identity tally and the double-listed S-4 slot. Hard rule 2 is "add only". So the
Mobil bytes are requested, not fetched: **FETCH REQUEST F-1**.

Why it matters: Mobil's EDGAR record carries **no former name at all**, so Mobil's own 10-K is the only document
class in this universe that can print the successor's *own* incorporation recital — the analogue of Exxon's
"incorporated in the State of New Jersey in 1882" (§3). Without it the **Mobil side of the 1999 merger has no
registrant-level lineage statement anywhere**, and rows 6-9 of §2 stay disconnected.

**STATUS: WRITTEN**

---

## 7. Five-family verdict table

| family | state | what counted, and the measurement behind it |
|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED** | 11 documents / 2,961,190 B / 332,653 words, registrant CIK 34088, **measured floor 1994-03-04** (0 rows before it). Counts for **Stage 3** (8 in-window filings incl. the 1999 S-4). Contributes the only registrant-level lineage rows in the tree (S-4 L47-49, L13804-13806) and the only founding recital (10-K L130). Contributes **nothing in-window** to Stages 1-2 |
| **(b) web archives** | **UNTRIED** | no authorised command; the only in-repo mention of a wayback/cdx route is inside fleet-owned `tools/periodical_harvest.py`, which was not run. Floor ~1996 → could only reach Stage 3's tail. **Not a null** |
| **(c) periodical corpora** | **TRIED–ANSWERED** on held bytes; live query route **UNTRIED** | 8 works on the `periodicals/` shelf: the **1901 Oil City Derrick** volume (the only Stage-1 in-window Tier-1 carrier, §4b), the **1976 U.S. House committee print** naming Mobil Oil Corporation (the only Stage-3 non-filing carrier), 5 Standard Oil *of California* reports (**excluded**: sibling), 4 ERIC reprints (**excluded**: subsidiary naming). Its live half — `periodical_harvest.py --company exxonmobil --facet-free`, HathiTrust, Google Books, Chronicling America — is **UNTRIED by policy or tool condition** (U-5, U-6) |
| **(d) digitised corporate print** | **TRIED–ANSWERED, answering NOTHING for this lineage** | the shelf holds **1** file and it is byte-identical (md5 `242183d1…`) to a `periodicals/` twin, so distinct company print of this registrant or any ancestor = **0 works**. `ia_text.py list-files --id pureoiltrustvsst00oilc` → **`text_layers: 1`**: no second pamphlet hides behind that identifier. Nothing here counts toward any tier |
| **(e) auction / museum / manuscript** | **UNTRIED** | no route in `tools/` (the single grep hit is a repair script's prose); 0 web budget. **Not a null** |

**Tier arithmetic (§15.2):** Stage 1 = 1 family → **T3**; Stage 2 = 0 families → **T3 PROVISIONAL**;
Stage 3 = 2 families → **T2 core PROVISIONAL**. Families **(b)** and **(e)** are the two that could still move a
tier and have never been tried; **(d)** is tried and empty, and the gap it exposes is not "no digitised print
exists" but **no digitised Standard Oil of New Jersey / Humble / Vacuum / Mobil print was ever queried** —
`research/A4_harvest_mine.md` L21 lists the vocabulary that pass applied (`exxon mobil corp`, `exxonmobil
holdings`, `exxon corporation`, `mobil oil`, `standard oil`), in which **`standard oil company of new jersey`,
`vacuum oil`, `humble oil`, `socony` and `magnolia` appear nowhere**. The trade/industrial-press vocabulary that
produced this dossier's best carrier was never a query at all; it arrived by accident through a `pure oil trust`
title match.

**STATUS: WRITTEN**

---

## 8. Carrier index (file + line), for the origin and predecessor question

Every row below is a byte this probe opened. Paths are relative to the company dir.

| # | carrier | line(s) | what it carries | class / confidence |
|---|---|---|---|---|
| C-1 | `sources/sec/0000950103-99-000247_0000950103-99-000247.txt` | **L47-49** | `FORMER COMPANY: / FORMER CONFORMED NAME: STANDARD OIL CO OF NEW JERSEY / DATE OF NAME CHANGE: 19721123` on `CENTRAL INDEX KEY: 0000034088` (L22), `STATE OF INCORPORATION: NJ` (L25) | **FACT — registrant-level SEC metadata; the strongest lineage statement in the tree.** Medium (EDGAR records the date it *recorded* the change, not the corporate act) |
| C-2 | same S-4 | **L13804-13806** | "STOCK OPTION AGREEMENT dated as of December 1, 1998 … between **Exxon Corporation, a New Jersey corporation** ('Exxon'), and **Mobil Corporation, a Delaware corporation** ('Mobil')" | **FACT — the merger's two constituent legal persons, from the merger instrument itself.** Medium |
| C-3 | same S-4 | **L15400, L15685, L737, L4216, L7986** | Mobil as a named party; "Mobil Oil Corporation" in plan/ESOP and officer captions; `mobil corporation` **82** vs `mobil oil corporation` **17** | FACT for the namings; **the parent/subsidiary naming split is UNRESOLVED** (§9 Q3) |
| C-4 | `sources/sec/0000950131-94-000308_0000950131-94-000308.txt` | **L130** (repeated at `sources/sec/0000930661-96-000138_0000930661-96-000138.txt` **L187**; cover block **L1320** "INCORPORATED IN NEW JERSEY") | "Exxon Corporation was incorporated in the State of New Jersey in 1882." | **FOUNDER CLAIM / RETROSPECTIVE INTERPRETATION** — company self-narrative at 1994 about 1882; **one lineage refiled six times** (§3), corroboration count **1**. Medium |
| C-5 | `sources/corporate_print/pureoiltrustvsst00oilc_djvu.txt` (md5-identical twin at `sources/periodicals/pureoiltrustvsst00oilc_djvu.txt`) | **L44-L76** title page; **L626, L632, L20649, L72656** | 1901 Oil City Derrick printing of the U.S. Industrial Commission investigation, naming "the Standard Oil Company of New Jersey" with its officers (Rogers vp; Rockefeller president; Dodd solicitor) | **CONTEMPORARY OBSERVATION, third party, in-window** — federal-investigation text compiled by trade press. **The only Stage-1 carrier.** Medium (UNVERIFIED TLS sidecar) |
| C-6 | same | **L18534, L18539-18541** | "**the Vacuum Oil Company, of Rochester, N.Y.**"; "The Standard Oil Company were owners in the stock of the Vacuum Oil Company, but had no direct relation whatever with the management of its affairs" | **CONTEMPORARY OBSERVATION** that Vacuum was a **separate** legal person at 1901 — a statement that **distinguishes** it from Standard Oil, not one that joins them. Medium; the adjacent year reads `ISSl` and is **not citable** |
| C-7 | same | **L3722, L5409** (the 1882 Trust) · **L4418-4419, L46299-46300, L4734** (Pure Oil's New Jersey organisation, "about 1897") | What the volume does **not** say: no 1882 New Jersey incorporation of Standard Oil; its NJ-incorporation language belongs to the **opponent** | Negative finding; the counts behind it are in §4b |
| C-8 | `sources/periodicals/mobrat00unit_djvu.txt` | **L13-38, L202** | "MOBIL OIL CORPORATION: FAILURE TO DELIVER NATURAL GAS TO THE INTERSTATE MARKET", Subcommittee on Oversight and Investigations, U.S. GPO, **February 1976**; "Isle 95 Field, operated by Mobil Oil Corporation" | **TIER-1 THIRD-PARTY GOVERNMENT PRINT naming the Mobil-side ancestor in-window (Stage 3).** No founding data. Medium |
| C-9 | `sources/sec/_MANIFEST.csv`, `sources/sec/_RUN.json` | whole files | the intake state: 11 stored / 0 UNANSWERED / 67 SKIPPED, `identity_ok: false`, `duplicate_slots` naming the two nameless S-4 slots | FACT (run record) |
| C-10 | `sources/_index/_INDEX_CIK0000034088.md` (+ `_registrant_CIK0000034088.json`) | earliest-per-form table | the reachable-but-unfetched merger carriers: **DEFM14A 1999-04-08 (…-000260)**, **424B3 1999-12-06 (0000950117-99-002528)**, **4 1999-11-30 (…-001036)**, **S-8 POS 1999-09-28**, **8-K/A 2000-02-11** | **An index row is not a fact about content** (§14) — no bytes read, hence F-2/F-3 |
| C-11 | `sources/_index/quarantine/CIK0002115436/*` | registrant json + index | the wrong-registrant evidence: `XOM → 2115436`, filings from **2026-07-01**, 0 slices, `formers []` | FACT about the tool and SEC's ticker file; **not evidence about the company** |

**STATUS: WRITTEN**

---

## 9. Load-bearing open questions

**Q1 — Which founding act has a carrier, and of what kind?** Three candidate acts exist for this lineage and
they are **not** the same act:
(i) *the registrant's own incorporation* — carried by **one** self-narrative sentence, 10-K L130 (1994),
refiled six times: "incorporated in the State of New Jersey in 1882";
(ii) *the 1882 Standard Oil Trust* — carried by third-party print at 1901 (L3722, L5409), a **different legal
fact** with the same year;
(iii) *the 1911 dissolution that made SONJ an operating major* — carried by **nothing**: `1911` = 0 occurrences
in all 13 print layers and all 11 SEC files (measured, §2/§4b).
So the origin has a self-narrative (Medium), a third-party naming of the *person* (C-5, the strongest thing in
the tree), and **no carrier at all for either founding act or the dissolution act**. State 1882 as
`FOUNDER CLAIM`; state 1911 as `UNKNOWN` until a carrier is opened.

**Q2 — Which legal person does the 1999 merger join, and where does the Mobil line enter it?** Answered
*partly*: S-4 L13804-13806 — a **New Jersey** Exxon and a **Delaware** Mobil. Unanswered: how a New York/Texas
ancestor chain (Vacuum of Rochester N.Y., Socony of New York, Humble of Texas) became a Delaware corporation,
and whether `Mobil Oil Corporation` (17 mentions) is the operating subsidiary or an earlier parent. The answer
lives in CIK 67182's filings — unreachable here (§6a). **This is the single highest-value open question in the
dossier, and the classic founder-claim trap: stitching Vacuum/Socony/Humble into CIK 34088's founding on brand
continuity would be an invented claim.**

**Q3 — First real experiment / first repeatable validation / first incurred failure.** All **UNANSWERED** at
Stages 1-2, and explicitly **not imported from general history**. No held byte describes an acquisition,
refining venture, field, or product attempt by any lineage entity. The nearest held thing is the 1976 House
print's subject — Mobil refusing to accept an FPC certificate and withholding gas (L202-222) — which is a
*Stage-3 regulatory failure of the ancestor*, carried by a third party, and it is not an origin event. The 1901
volume's testimony (patent/brand disputes with the Vacuum Oil people, L18530-18568) is the only in-window
venture-level text, and it belongs to **the opponent's side of the litigation**.

**Q4 — Is there a second, independent witness for the registrant-ancestor link?** Currently **1**: C-1 (the
S-4's former-name row). The live EDGAR index dropped that row, so there is no second EDGAR-era witness, and no
print in this tree says "Standard Oil of New Jersey became Exxon" (the 1901 volume predates the rename by 71
years). Routes that could produce a second: F-2/F-3 (the merger filings' unopened documents and the 1999 proxy,
which normally prints a "History of Exxon" / "History of Mobil" section — the one document class in this
universe most likely to carry *both* ancestor narratives), and U-1's 16 unopened S-4 exhibits.

---

## 10. What this probe refused to claim, and why

1. **Refused to treat CIK 2115436 as the company.** Its filings begin 2026-07-01 and it has no former names; the
   intake that stored 0 documents was correct arithmetic about the wrong registrant. Reported as intake state,
   used for nothing else.
2. **Refused 1882 as a *founding* fact.** Kept as the registrant's own 1994 recital (C-4), one lineage refiled
   six times — not six corroborations, and not a Tier-1 origin document.
3. **Refused to attribute the 1901 volume's New Jersey-incorporation language to Standard Oil.** L4418-4419,
   L46299-46300 and L4734 describe **the Pure Oil Company/Trust**, the adversary (trap 3 firing exactly as
   briefed). Also refused to read its `1882` hits as an 1882 *incorporation*.
4. **Refused to date anything from the Vacuum passage.** The adjacent year is OCR'd `ISSl`; and L18539-18541 is a
   statement **separating** Vacuum Oil from Standard Oil ("owners in the stock … but had no direct relation
   whatever with the management of its affairs"), so it cannot be used to say Vacuum was Standard Oil's
   subsidiary — it says the opposite about control.
5. **Refused to treat the 1911 dissolution as evidenced.** 0 occurrences; it enters Stage 1's boundary as an
   **asserted** date, labelled as such in §5.
6. **Refused the five Standard Oil *of California* annual reports as ancestors.** Sibling successor,
   company_021's lineage; `of new jersey` = 0 in them. Excluded from every family verdict and every tier here —
   and not used as evidence about Chevron in this file either.
7. **Refused the four `micro_IA…` ERIC layers as corporate print or lineage evidence.** They name
   **EXXON Education Foundation** and **Exxon Research and Engineering Co.** — subsidiaries, not the registrant,
   not an ancestor (RD-124 / Ford's-Canadian-layers class).
8. **Refused to count the byte-identical `pureoiltrustvsst00oilc` copy twice** (md5 `242183d1…` on both shelves),
   and refused to count the second scan `pureoiltrustvss00derrgoog` as a second witness — §3 independence rule:
   one work, corroboration count **1**.
9. **Refused the A4 lane's fresh `TIER1_CANDIDATE_TEXT` on `mobrat00unit` as a registrant naming — after
   verifying it in the bytes.** The promoted string is `exxon corp`; measured in that layer: `exxon` **1**,
   `exxon corporation` **0**, and the single hit is **L2406** — "…minimum daily delivery obligation" condition.
   See. for example, Exxon Corp.." — a **`See, for example` footnote cross-reference**, not a statement about the
   entity. The Stage-3 (c) naming I do count is the title page's own **Mobil Oil Corporation** (L13) and its use
   as an operator at L202.
10. **Refused to call pre-1994 EDGAR, Chronicling America, HathiTrust, Google Books, Wayback or auction/manuscript
    "absent".** The first is a measured perimeter (0 rows before 1994-03-04, which is *not* a claim that no
    filings exist); the rest are UNTRIED, each with a command in `## Untried`.
11. **Refused to pass `--allow-mismatch` for the Mobil intake, and refused to run a forward `auto` pass**, because
    both would overwrite the non-CIK-keyed run artefacts in `sources/sec/` (§6a; hard rule 2). Requested instead
    (F-1).
12. **Refused to run `harvest_mine.py` / `periodical_harvest.py` / `ca_endpoint_probe.py`** (fleet lanes own them
    tonight; the third writes outside my path). Every route they own is reported UNTRIED with its command.
13. **Refused a confidence above Medium anywhere in this file** — all 13 IA sidecars read
    `transport: UNVERIFIED TLS`; the EDGAR sidecars are a different transport class, and the cap is applied to
    everything resting on an IA-derived naming as well.
14. **Refused to mint source ids, write registers, or certify depth.** No volume authored; no other company's
    tree read for tier purposes (the Chevron/Citigroup pointers in §7/§10.6 are cross-tree *leads*, never
    counted here).

## Untried

Each entry is a search never run, with the command that would run it. Nothing below is a null.

- **U-1 The 16 unopened documents of the stored S-4 accession** (cheapest, highest value). L15 of the file prints
  `PUBLIC DOCUMENT COUNT: 17` and only sequence 1 was taken; `_SKIPPED.csv` lists 16 more slots at
  `0000950103-99-000247`, plus 8 at the FY1999 10-K and 8 each at FY1997/FY1998. Command (orchestrator, into a
  **run-keyed** directory — see §6a):
  `python tools/sec_intake.py auto "EXXON MOBIL CORP" --company-dir <dir> --from 1999-04-01 --to 1999-12-31 --max-docs 30`.
  Expect exhibits, the joint proxy's history sections, and the completed prospectus text.
- **U-2 The registrant's post-merger recital (RD-134's forward route, deliberately not run here).**
  `python tools/sec_intake.py auto "EXXON MOBIL CORP" --company-dir <dir> --from 2000-01-01 --to 2006-12-31 --max-docs 12`.
  The FY1999/FY2000 10-K and the 2000-2006 proxies are where a *combined* Exxon-Mobil lineage sentence — the
  "successor to Standard Oil of New Jersey" class of statement — would live. **Not run because** `sources/sec/`
  keeps one run record per directory (five non-CIK-keyed files), so a second pass would erase the intake state
  this brief ordered reported.
- **U-3 Predecessor CIK resolution.** `legacy_cik.py search` returned a **3500-byte parse failure** for
  `"Standard Oil of New Jersey"` (2 attempts), `"Humble Oil"` (2), `"Socony"` and `"Standard Oil"` — reported
  **TRIED–UNANSWERED, not zero candidates**, exactly as the tool's own message insists. Remedy: fix the search
  parser, or use EDGAR full-text / the historical company-name tables. Note the asymmetry already measured: the
  index **does** return `MOBIL CORP` (an EDGAR-era filer that deregistered in 2000), so the names missing from it
  are those that left the stage before EDGAR — which is a statement about the index, not about the record.
- **U-4 Chronicling America / HathiTrust / Google Books (family (c)'s live half).** Fleet-owned
  `python tools/periodical_harvest.py --company exxonmobil --facet-free` — `--facet-free` is mandatory
  (RD-130/RD-134: a YEAR-faceted zero is a statement about our parameter). CA's URL shape is still undecided
  (`tools/ca_endpoint_probe.py`: all four candidates returned **403** from this machine); HathiTrust egress is
  blocked from this machine (`tools/ia_text.py` L37). Trade-press targets worth naming because the harvest never
  queried them: **Oil City Derrick**, *Petroleum Engineer*, *Petroleum Week*, *The Oil & Gas Journal*, and the
  house organs of Standard Oil of New Jersey / Humble / Vacuum / Socony.
- **U-5 Digitised corporate print of the actual ancestors (family (d), never queried).** A4's vocabulary (L21:
  `exxon mobil corp`, `exxonmobil holdings`, `exxon corporation`, `mobil oil`, `standard oil`) contains **none**
  of `standard oil company of new jersey`, `socony vacuum`, `vacuum oil company`, `humble oil refining`,
  `magnolia petroleum`. A facet-free title-route re-run with that vocabulary is the single most likely source of
  a Stage-2 carrier; per RD-124 add all of them to the slug's entity list **before** grepping, and per RD-130
  verify every zero is unfaceted.
- **U-6 Web archives (family (b)).** No authorised command; fleet-owned `periodical_harvest.py` is the only file
  in `tools/` that mentions a wayback/cdx route. Floor ~1996 → bears on Stage 3's tail and the `(PB)` post-merger
  period only.
- **U-7 Auction / museum / manuscript (family (e)).** Never searched, no tool, no web budget. For this lineage
  the targets are company-archive finding aids (ExxonMobil / Historical Corporation Records, the Humble and
  Sonj collections at the Texas and New Jersey state archives, Rahway local-history holdings on Standard Oil of
  New Jersey) — named as an **intake gap for the orchestrator**, not attempted.
- **U-8 The quarantined CIK 2115436 artefacts.** Read for registrant identity only (`_registrant_…json`,
  `dropped_rows_…csv`); their filings were not opened and nothing in them bears on any stage.
- **U-9 Bound-run enumeration of every IA item cited here.** Done for the one item that mattered
  (`list-files --id pureoiltrustvsst00oilc` → `text_layers: 1`); **not** done for `mobrat00unit`,
  `pureoiltrustvss00derrgoog` or the SOCal reports. A bound volume can hold one layer per year, so an
  un-enumerated item cannot yet be called a single document.

## Fetch requests

Scripts reach the network; agents do not (§15.1). Each names the identifier/accession and the exact command.

- **F-1 — Mobil Corp's own registrant bytes (blocks Q2, the dossier's worst gap).**
  `python tools/sec_intake.py auto "67182" --company-dir <a directory allowed to hold a second registrant, or with --allow-mismatch into a RUN-KEYED sources/sec> --from 1994-01-01 --to 2000-02-09 --max-docs 8`.
  Wanted: Mobil's FY1994/FY1998 **10-K cover + first business/history page** (its own incorporation state and
  year) and the **`15-12B` of 2000-02-09**. Needed so the Delaware question at §2 row 9 can be answered from a
  filed document instead of from an exhibit recital. **Claim status: UNANSWERED until run.**
- **F-2 — the merger's completed prospectus.** accession **0000950117-99-002528** (`424B3`, 1999-12-06) and
  accession **0000950103-99-000260** (`DEFM14A`, 1999-04-08). Both sit in the stored index and neither was
  fetched. Wanted: the proxy's history sections for **both** constituents, and the **merger completion date and
  exchange ratio**, which no held byte currently prints (§5, Stage 3).
- **F-3 — the 16 unopened S-4 exhibit slots** at accession **0000950103-99-000247** (U-1).
- **F-4 — `list-files` enumeration of `mobrat00unit` and `pureoiltrustvss00derrgoog`** (U-9), to confirm neither
  is a bound run whose extra layers would change family (c)'s count.

## 11. Corrections taken on this pass, and the intake state as I found it

- **A4 is a moving file and I re-read it before quoting it.** Snapshot **2026-10-06 17:33:15 +0530**, md5
  `cd48afb583465b641be727aeb9d5d566`, 74 lines: **108 candidate rows / 12 items mined / 94 left untried**. The
  version this probe first read (mtime 2026-09-29 23:31:28, 53 lines) said **63 / 6 / 56** — the fleet's
  corporate-print reharvest rewrote it **during this run**, at the same minute the six new layers landed (§4a).
  Anyone re-grading from A4 must check its mtime first; **this probe did not run that lane, and the file may
  change again after this dossier closes.** §0's row for A4 is superseded by this one.
- **A4's entity-vocabulary statement still holds in the new version** (L21 unchanged), so §7's conclusion — that
  no query ever contained `standard oil company of new jersey`, `vacuum oil`, `humble oil`, `socony` or
  `magnolia` — is quoted from the 17:33 snapshot, not the 09-29 one.
- **The new A4 promotion was checked rather than inherited.** `mobrat00unit` is now
  `TIER1_CANDIDATE_TEXT` promoted by `exxon corp` (L25). Measured in the bytes: 1 occurrence, at L2406, inside a
  `See, for example` footnote (refusal 9). The label is checkable and the string is real; what it proves is a
  brand-abbreviation in a footnote, which is not a naming of the registrant's origin.
- **The brief's intake figures are confirmed verbatim from `_RUN.json`**, including the `BROKEN` tally's cause:
  `duplicate_slots` = `nameless:0000950103-99-000247:911 in skipped and skipped` and `…:906 …` — two nameless
  document slots in the S-4's own stream listed twice, raw 78 vs unique 77. **Not a lost document**, and it
  affects no claim here; it does mean the S-4's file stream is where U-1/F-3 should look first.
- **`legacy_cik detail 34088` prints `tickers []` while SEC's own ticker file gives `XOM` to 2115436.** Both
  measurements are correct and they do not conflict: **the ticker moved to a new registrant.** Any future brief
  for this company must name the registrant **by CIK**, not by ticker, or the next probe repeats the 0-document
  intake.
- **A brief-form defect worth recording:** the shared brief lists `python tools/ia_text.py list-files
  <identifier>`; the working form is `list-files --id <identifier>` (a positional identifier is rejected with
  `error: unrecognized arguments`). Same class as RD-130's positional-identity fix on `sec_intake`.
- **The earliest reachable filing is not pre-history.** The 1994 8-K and FY1994 10-K carry the Valdez settlement
  language (§5): family (a)'s *oldest* byte is already 22 years past Stage 2's end and 83 years past Stage 1's
  start. Everything in (a) is retrospective for the origin; **only family (c) is contemporaneous**, which is the
  whole reason the Stage-1 tier rests on a trade-press volume rather than on a filing.

**STATUS: WRITTEN** (whole file: §0-§11 + `## Untried` + `## Fetch requests`)
