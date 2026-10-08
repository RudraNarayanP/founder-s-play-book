# A_chronology_feasibility.md — RTX Corp (Fortune rank 49) Stage-1 PROBE

Company dir: `founders_playbook/01_companies/company_049_rtx`. Owner: `probe-rtx`
(`scaffold.py claim --path … --agent probe-rtx`, run first, accepted).
**Web budget consumed: 0 WebSearch / 0 WebFetch.** Scripts run: `sec_intake.py` (3 passes, two of them
mine), `ia_text.py` (search ×5, fetch ×1). `harvest_mine.py` / `periodical_harvest.py` were **not** run,
per brief; `A4_harvest_mine.md` was re-read before being quoted (see *Why mined=0*).
Window inherited from the intake state: **1920-01-01 → 1997-12-31, PROPOSED only** — it is the value in
`tools/harvest_mine.py`'s `WINDOWS` table and in `sources/sec/_RUN.json`'s `window` field, i.e. **a search
setting, not a stage window** (RD-112). This probe splits the stages on evidence and says so below.
Every quantifier carries the command that produced it. `## Untried` is a section, not a footnote.

---

## Verdict — Stage 1 = T3 register, PROVISIONAL, and the reason is entity geometry not archive emptiness

**STATUS: WRITTEN**

Three findings, in strength order:

1. **The registrant's own origin sentence exists, is dated, and is 60 years late.** `sources/sec/`
   holds the FY1993 10-K (accession `0000101829-94-000019`, filed **1994-03-31**), L228:
   *"United Technologies Corporation was incorporated in Delaware in 1934."* No document held anywhere
   in this repo has a date inside the 1922-1953 span that states an origin.
2. **The second lineage's founding sentence exists only in a 2019 registration statement.** The S-4
   accession `001140361-19-013079` (as filed 2019-07-17; text offset ~108,831 and ~262,322 of the
   flattened HTML) prints *"Raytheon was founded in 1922 and is incorporated in the state of Delaware"*
   — `founded in 1922` ×2, plain `1922` ×2 in that document. That is **a company-side recital 97 years
   after the year it recites, about the entity the registrant later acquired** — the recital route, and
   it is the only 1922 carrier produced this pass.
3. **The 2020 renaming is proven from held bytes, including legal continuity.** EDGAR's own registry
   record for CIK 0000101829 carries `former_names: ["RAYTHEON TECHNOLOGIES CORP", "UNITED TECHNOLOGIES
   CORP /DE/"]` (`sources/_index/_registrant_CIK0000101829.json`), and the April 2020 filings recite the
   change on the same Commission File Number **001-00812** and the same IRS EIN **06-0570975** as the
   1994-1997 United Technologies filings. So today's RTX Corp **is** the 1994 registrant, renamed — while
   Raytheon Company was the *acquired* Delaware corporation that survived as a **wholly owned subsidiary**
   (8-K `0001140361-20-007906`, date of report 2020-04-03). One registrant, two inherited lineages, and
   the deeper of the two is **not** the registrant's own origin (§3 same-brand-different-legal-person).

**Planning tier for this company = the minimum per-stage tier = T3 register** (≈3-4 agent runs,
8k words/stage; RD-116's convention). Per RD-112 I state which window each tier was measured against:

| stage (probe-proposed) | window measured | tier | families that returned in-window Tier-1 text |
|---|---|---|---|
| **S1 — lineage origins** | **1922-01-01 → 1934-12-31** (PROPOSED) | **T3 register** | **none (0)**. No held document is itself dated in-window. The 1922 and 1934 statements live in carriers dated 1994 and 2019 → retrospective, `RETROSPECTIVE SOURCE` (§6). |
| **S2 — registrant formation → mid-century validation** | **1935-01-01 → 1953-12-31** (PROPOSED) | **T3, PROVISIONAL** | **(c) 1 item, content-verified**: `sources/periodicals/DTIC_ADA320141_djvu.txt` (158,295 B, NRL report dated 20 Jul 1953, equipment received 20 Sep 1951). (d) is TRIED–UNANSWERED, not counted. |
| **S3 — first EDGAR-visible consolidation** | **1994-01-24 → 1997-12-31** (cut on the measured filing floor, not on history) | **T3** | **(a) only**: 78 indexed filings in-window, 7 held SGML documents, entity-naming text present (`Pratt & Whitney` 330, `Sikorsky` 159, `Hamilton Standard` 65 across the 7 held `.txt`). (b) would plausibly count here but is UNTRIED. |
| *(anti-pattern, for the record)* | 1920-01-01 → 1997-12-31 (the inherited **search span**) | *(2 families → "T2")* | **Rejected.** Counting (a) at 1994-97 and (c) at 1951-53 inside one 78-year box manufactures a tier out of a parameter. If a later pass re-grades this company upward, it must name which window moved. |

The honest headline is **not** "the archive is empty before 1994". It is: **this registrant has two
deep lineages and the record supports neither origin contemporaneously in-window; the strongest in-window
primary text this pass produced is a 1953 Naval Research Laboratory engineering evaluation of a
one-off Raytheon sonar unit that "was never put into operation".**

---

## Intake state found, and what this pass added

**STATUS: WRITTEN** (measured 2026-10-06; `python - <<` byte walk over `sources/*`, excluding sidecars)

| folder | files | bytes | what it is |
|---|---|---|---|
| `sources/sec/` | 35 paths = **30 documents** + 5 run artefacts | **15,136,240** | EDGAR, 1994-01-24 → 2020-04-08 |
| `sources/_index/` | 7 | 1,786,983 | submissions enumeration, **2,968 filings** |
| `sources/periodicals/` | **1** (+1 sidecar) | **158,295** | added by this probe (DTIC/NRL 1953) |
| `sources/corporate_print/` | **0** | **0** | directory exists and is **empty** |
| `sources/harvest_mine/` | 1 | 1.0 K | the A4-era mine summary, 8 candidates / mined 0 |
| `sources/web_archive/` | — | — | **does not exist** (no dir; no route in `tools/`) |

Pre-existing state (intake run of `2026-09-29T19:08:12Z`, recorded here verbatim because my two passes
rewrote `_RUN.json` / `_MANIFEST.csv`; **nothing was deleted** — the 8 original SGML documents are still
on disk with their 2026-09-30 mtimes): `stored 8 / 1,449,918 B / 176,852 words`, unanswered 0, skipped 36,
`identity_ok: true`, 36 `UNANSWERED NAMELESS-ROW` entries in `_SKIPPED.csv` (pre-2001 malformed EDGAR
directories, reachable only via the full-submission `<accession>.txt`).

Runs I added:

```
python tools/sec_intake.py auto "RTX Corp" --company-dir founders_playbook/01_companies/company_049_rtx \
  --from 2019-06-01 --to 2021-12-31 --max-docs 14        # -> 14 docs / 8,982,960 B / 348,258 words
python tools/sec_intake.py auto "RTX Corp" --company-dir …/company_049_rtx \
  --from 2020-04-01 --to 2020-04-30 --max-docs 8          # -> 8 docs / 4,697,163 B / 117,460 words
```
Both printed `guard = ok -- slug token(s) ['rtx'] match registrant 'RTX Corp' (CIK 0000101829)` and an
identity check that footed; both **exited 1** because each ended with the `UNANSWERED NOT-ENUMERATED`
advisory (58 and 2 in-window filings never listed once `--max-docs` was reached). That advisory is a
perimeter, not a null: those documents exist and are unknown to this run. Logs kept at
`_probe_rtx_recital_forward.log` and `_probe_rtx_recital_rename2020.log` (repo root, my own run logs).

**Measured filing floor (twice, independently):** `index: 2968 filings … date perimeter 1994-01-24 ->
2026-10-05`; over `sources/_index/submissions_CIK0000101829.csv` (header enumerated first:
`filingDate,form,accession,reportDate,primaryDocument,source`): **rows dated before 1994-01-24 = 0**,
**rows with filingDate ≤ 1997-12-31 = 78**, **S-1-family rows = 0**. EDGAR's own floor, stated as a
measurement, not as "United Technologies filed nothing before 1994".

---

## Why this slug's harvest rows returned `mined=0` — the brief's specific question

**STATUS: WRITTEN.** Answer: **it was not an empty archive, and it was not (only) RD-133's
abbreviation-slug blindness — it was sequencing.** Measurement:

- `stat` gives `research/A4_harvest_mine.md` and `sources/harvest_mine/_index.json` both at
  **2026-09-30 00:14:30 +0530 = 2026-09-29T18:44:30Z**.
- The facet-free reharvest rows for `rtx` in `00_universe/harvest/candidates.csv` carry
  `retrieved_at` **2026-09-29T19:15:07Z / 19:15:12Z / 19:15:17Z** — **30.6 minutes after the mine ran**.
- The 8 rows the mine actually saw are the `retrieved_at 2026-09-29T13:09:40Z` block, every one
  `classification=UNANSWERED`, `http_status` = `SKIPPED: global max-requests cap 600 reached` (2 CA, 2
  corporate_print, 1 Google Books, 1 HathiTrust "hard stop: 5 consecutive failures (host halted)", 2 IA).
  **A4's stated reason was therefore correct on its own bytes** — re-read before quoting, per brief.
- Census now (same file, field-filtered `company=='rtx'`, `csv.DictReader`; **the earlier
  `grep -c rtx` = 54 was a line match, not a census — RD-135's rule, caught on myself**):
  **79 rows**, of which **71 carry an `item_id`**, **47 dated ≤ 1997-12-31**, classification mix
  **TIER1_CANDIDATE 47 / LEAD_ONLY 24 / UNANSWERED 8**, family mix
  **corporate_print 52 / internet_archive 23 / chronicling_america 2 / google_books 1 / hathitrust 1**.
  Max `retrieved_at` in the file for this slug is **2026-10-06T12:04:00Z — the fleet reharvest was still
  landing rows during this probe**, so all three figures are snapshots, not totals.

**The labels are not evidence, and the decoy rate is the proof.** Of the 71 item-bearing rows,
**36 (51%) carry no configured entity token in title *or* identifier** — e.g. *"1977 Teacher Intern
Project. Final Report."*, *"A Pilot data collection effort in the California desert"*, *"Handbook on
grandparenthood"*, *"Super Mario 64 RTX"* class hits, *"arxiv-1104.0849 Nonlinearly-PT-symmetric
systems"*. **43 of 71 are third-party government/judicial/miscellany** (DTIC, NASA NTRS, CIA Reading
Room, PACER, Bitsavers). Exactly **one** row in the whole index is plausibly predecessor corporate print:
`TNM_Cover_-_Ratheon_Company_Anaual_Report_1965` → *Cover — Raytheon Company Annual Report 1965*
(1965-01-01) — a **cover image** from the Ted Nelson junkmail collection, and **its own identifier
misspells the company as "Ratheon"**. So the remedy is a re-mine (fleet task #28), not a re-tier.

---

## Five-family verdict table

**STATUS: WRITTEN.** The three states are TRIED–ANSWERED / TRIED–UNANSWERED (cause + remedy named) /
UNTRIED. An untried family is never reported as a null (§14 r6).

| family | state | what came back, and the count that proves it |
|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED** | 2,968 filings enumerated; floor 1994-01-24; 78 rows ≤ 1997-12-31; 30 documents / 15,136,240 B held; 0 S-1. In-window origin text = the 1934 recital; the 1922/1929/1860s lines are **recital-only** (1994, 2019, 2020 carriers). 2 runs ended on `NOT-ENUMERATED` (58 + 2 filings) → perimeter, not null. |
| **(b) web archives** | **UNTRIED** | `grep -rlni "wayback\|cdx\|web.archive" tools/*.py` → **no file listed**; no `sources/web_archive/` directory exists for this company. §14 r6 puts this family's floor at the mid-1990s, so it bears on S3 (1994-97) and on the 2020 rename coverage — not on 1922. Command in *Untried* #1. |
| **(c) periodical corpora** | **TRIED–PARTLY-ANSWERED** | Internet Archive route: 23 `rtx` rows; I opened **1** and content-verified it (`DTIC_ADA320141`, 158,295 B, "Raytheon Mfg. Co." ×1 line + abstract ×1 line, `raytheon` in **2 lines** of the whole layer). **Chronicling America: TRIED–UNANSWERED** (2 rows, `SKIPPED: global max-requests cap 600 reached`; and `_CA_ENDPOINT_TEST.md` 2026-09-29T18:05:27Z: **7 of 7 endpoint shapes CHALLENGED 403 Cloudflare**). **HathiTrust: TRIED–UNANSWERED** ("hard stop: 5 consecutive failures (host halted)"). **Google Books: TRIED–UNANSWERED** (cap). Remedies: CI egress + `--facet-free` reharvest, then re-mine. |
| **(d) digitised corporate print** | **TRIED–UNANSWERED** | `sources/corporate_print/` = **0 files / 0 B** (empty dir, which is what makes this family *look* null). Index carries **52** corporate_print rows for this slug, **0 bytes fetched**. My own live probes: `"Raytheon Company" annual report` → **numFound 3** (the 1965 cover + a podcast + a city-council video); `"United Aircraft Corporation" annual report` → **numFound 0**; `"United Aircraft Corporation"` bare → numFound 131 (top rows are a 1961 thermodynamics report, TurboTrain press footage, an AFL-CIO case — mixed, metadata-matched); `"Raytheon Manufacturing Company"` → **numFound 4**. Caveat that governs all four: **IA `advancedsearch` matches METADATA, not full text** (Boeing probe finding, re-confirmed here), so every `numFound` above is a lead count, never a naming count. |
| **(e) auction / museum / manuscript** | **UNTRIED** | No such source-family exists in this repo's harvester: `python - <<` walk of `tools/queries.json` → families are exactly `chronicling_america, corporate_print, google_books, hathitrust, internet_archive`. This is the family that holds pre-1930 founder papers, stock certificates and prototype logs — i.e. the 1922 X-ray/rectifier-tube material. Command in *Untried* #2. |

**Families that counted toward a tier: (a) for 1994-1997 only; (c) for 1951-1953 only. None for
1922-1934.** (b) and (e) were never tried and are provisional-by-construction, not nulls.

---

## Carriers for the origin / predecessor question (file + line)

**STATUS: WRITTEN.** Quotations re-read from held bytes this pass. Where the byte is a Windows-1252
smart quote it prints as `` in the raw file; I normalise to `'` and say so (rule 6, OCR/encoding decoys).

| # | carrier (file : locator) | document date | what it carries |
|---|---|---|---|
| K-1 | `sources/sec/0000101829-94-000019_0000101829-94-000019.txt` : **L228** | filed 1994-03-31 (FY1993) | *"United Technologies Corporation was incorporated in Delaware in 1934."* — registrant's own origin recital |
| K-2 | same file : L229-230 | 1994-03-31 | *"Since 1973, growth has been enhanced by the acquisition of several companies…"* — the recital then jumps 39 years; no 1934-1973 narrative |
| K-3 | same file : L254-256 | 1994-03-31 | operating-unit list: *"Pratt & Whitney, Sikorsky, Hamilton Standard, Norden, Carrier, Otis, and UT Automotive units and also the United Technologies Research Center"* — **no Collins, no Raytheon, no United Aircraft, no 1860s** |
| K-4 | same file : **L1470** | 1994-03-31 | *"of an air permit for its Niles, Michigan facility."* — the **only** `Niles` occurrence (count 1) in the 7 held in-window documents; a plant location, **not** a machine-tool lineage claim |
| K-5 | `sources/sec/0001140361-19-013079_nt10003205x1_s4.htm` : flattened-HTML char ~108,831 and ~262,322 | as filed 2019-07-17 | *"Raytheon was founded in 1922 and is incorporated in the state of Delaware"* (×2 in the document; plain `1922` ×2) |
| K-6 | same S-4 : char ~2,100 (letter, "Particulars Regarding Raytheon") | 2019-07-17 | *"On June 9, 2019, United Technologies Corporation, or UTC, Light Merger Sub Corp., … and Raytheon Company, or Raytheon, entered into an Agreement and Plan of Merger"* (`June 9, 2019` ×55) — the two lineages meet on paper |
| K-7 | `sources/sec/0001140361-20-007906_nc10010681x1_8k.htm` (+ `_0001140361-20-007906.txt`, same accession) | date of report **2020-04-03** | cover: `RAYTHEON TECHNOLOGIES CORPORATION`, Delaware, file no. **001-00812**, EIN **06-0570975**; *"In connection with the Merger, the Company's name was changed to Raytheon Technologies Corporation"* |
| K-8 | `sources/sec/0001140361-20-008397_nc10010681x2_8k.htm` | date of report 2020-04-08 | *"United Technologies Corporation (since renamed Raytheon Technologies Corporation, as described below in Item 2.01 of this Current Report on Form 8-K)"* |
| K-9 | `sources/sec/0001140361-20-007906_nc10010681x1_ex99-1.htm` | 2020-04-03 | press release: *"WALTHAM, Mass., April 3, 2020 — Raytheon Technologies Corporation (NYSE: RTX) announced the successful completion of the all-stock merger of equals transaction between Raytheon Company and United Technologies Corporation"* — earliest **ticker** `RTX` carrier held; the later corporate-name change to "RTX Corp" is **not** dated by any held byte |
| K-10 | `sources/_index/_registrant_CIK0000101829.json` : `former_names` | registry, built 2026-10-06 | `["RAYTHEON TECHNOLOGIES CORP", "UNITED TECHNOLOGIES CORP /DE/"]` — EDGAR's own identity chain for one CIK |
| K-11 | `sources/periodicals/DTIC_ADA320141_djvu.txt` : **L102-110**, **L218-222** | report dated 1953-07-20 | NRL Confidential Report #192 by H.H. Elliott, Jr.: *"QHD scaiming [sic] sonar equipment manufactured by Raytheon Mfg. Co., Submarine Signal Division, Waltham, Mass."*; abstract: *"manufactured by the Raytheon Manufacturing Company, Submarine Signal Division, Waltham, Mass., under contract HObsr-42064, was delivered to this laboratory for tests"*; *"Serial No. 1 of Model QHD was the only one built. It was never put into operation."* |

**Independence (§3):** K-1…K-4 are one accession. K-7 and K-9 are one accession (`…-20-007906`) and K-8 is
a different accession of the same registrant — the rename fact is therefore **two accessions, one
registrant-side lineage**, not two independent witnesses. K-5/K-6 are the *joint* proxy of both lineages,
so the 1922 sentence is company-side about the acquired entity. **K-11 is the only third-party carrier in
this table** — the Navy's own laboratory, not the company — and it names the predecessor's **Waltham**
division, which is the same town K-9's press release gives as RTX's office 67 years later: an
independent geographic adjacency, not a founding claim.

---

## Traps, run against the bytes rather than warned about

**STATUS: WRITTEN**

1. **`RTX` is another company's product mark.** Measured live: IA `--q 'RTX'` → **numFound 4,855**;
   `--q 'RTX graphics card'` → **numFound 216**, first item `super-mario-64-rtx` ("Super Mario 64 RTX",
   mediatype `software`). Every graphics/gaming hit is a decoy; the abbreviation alone is worthless as a
   search term, which is exactly why RD-133's `universe_names()` mapping was needed — and why it was **not
   sufficient** (see *Why mined=0*).
2. **Surnames and place names need entity adjacency — and here the adjacency is a line wrap.** Counts
   over the **7 held in-window `.txt` documents** (whole-file substring counts): `Pratt & Whitney` **330**,
   `Whitney` **395**, `Hamilton Standard` **65**, `Hamilton` **74**, `Sikorsky` **159**, `Raytheon` **2**
   (both a *competitor's product* mention: FY1993 10-K L572 *"the Raytheon Corporate Jets Hawker 1000 and
   the Learjet"*), `Collins` **0**, `E-Systems` **0**, `Hughes` **0**, `United Aircraft` **0**, `1929` **0**,
   `1922` **0**. The `Whitney` minus `Pratt & Whitney` gap and the `Hamilton` minus `Hamilton Standard` gap
   were then read line by line: **every sampled line is a SGML line-wrap continuation of the corporate
   phrase**, e.g. `sources/sec/0000101829-94-000012_0000101829-94-000012.txt` L912-913 *"…in his current
   position as President of Pratt & / Whitney."* and `…-94-000019…txt` L4098 *"Standard, provides fuel and
   environmental control systems and propellers…"*. **A first reading of mine — "the DEF 14A lists a
   director surnamed Whitney" — is withdrawn on that read**: the bare `Whitney.` line is the wrap, not a
   person. Two adjacency notes survive: the FY1996 10-K/A and FY1996 10-K print an officer line
   *"Raymond P.       President, Hamilton   Executive Vice President, 52"* — **a role, not a founding claim**
   (RD-130's J&J rule) — and that surname `Raymond` sits one character away from the brand `Raytheon`, an
   OCR decoy generator. **Conclusion: no held document promotes Collins / Hamilton / Pratt / Whitney /
   Raytheon to a naming of an origin entity.**
3. **Same brand, different legal person — the 1860s line is asserted by zero held byte, measured over the
   whole corpus.** Command: substring counts over all **36 stored paths** under `sources/sec/` +
   `sources/periodicals/` (1994 → 2020, both my forward passes included): `1860` **0**, `1866` **0**,
   `Rentschler` **0**, `machine tool` **0**, `United Aircraft` **0**, `1929` **0**, `Pratt & Whitney
   Aircraft` **0**. The brief's warning — a machine-tool company whose aircraft-engine division came later,
   i.e. the same brand across two legal persons — is therefore **untested by every document this repo
   holds**, and the one candidate trace (`Niles, Michigan`, K-4) is a single air-permit sentence (`Niles`
   **1** occurrence corpus-wide). So the 1860s/1929 strata are **UNKNOWN** here, not absent from the world.
   Any Stage-1 volume that writes "since 1860", "1929" or "United Aircraft Corporation" would be importing
   a brand story the corpus does not contain (§14 r8), and would repeat Boeing's exact error in reverse
   (RD-130: "since 1916" attached to a different legal person).
4. **Repeatable validation for a defence contractor — which kind of record, with which carrier.**
   Recorded, and it is a **government contract plus acceptance testing**, not a test flight: K-11 names a
   Bureau-of-Ships contract number, a delivery date (**equipment received 20 September 1951**, engineering
   evaluation started 12 December 1951, report 20 July 1953) and a third-party test programme. The same
   carrier also supplies the **negative signal**: the unit was a one-off that never entered service.
   **A test-flight-type validation is UNKNOWN** (no held carrier of any family), and for the 1922 origin
   window **no validation record of any kind is held**.

---

## Load-bearing open questions, and what I refused to claim

**STATUS: WRITTEN**

1. **Founding date and founding act of the registrant: 1934 (Delaware) at medium confidence** — one
   accession, company-authored, 60 years after the fact. **I refused to state 1929 or "United Aircraft
   Corporation" as the registrant's origin**: zero held byte names it, and the folk date attaches to a
   predecessor legal person (the K-3 unit list is the registrant's own, and does not contain it).
2. **Founding date of the Raytheon lineage: 1922, Low confidence, and NOT the registrant's origin.**
   I refused to write "RTX was founded in 1922": the only carrier is a 2019 joint-proxy sentence about the
   acquired entity. I also refused to give a founding **month, instrument, town or founder name** — the
   held bytes say only *"Raytheon was founded in 1922 and is incorporated in the state of Delaware"* (the
   contiguous sentence, quoted in full at R05) and, third-party, *"Raytheon Mfg. Co., Submarine Signal
   Division, Waltham, Mass."* in 1953.
3. **`Collins` as a lineage: absent from the origin window, present only as a 2020 segment label.**
   Measured: `Collins` **0** occurrences in each of the 7 held in-window (1994-1997) documents, but **137**
   occurrences across the 36 stored paths (10 of them), the earliest being the 2019-2020 carriers — e.g.
   `sources/sec/0001140361-20-008397_nc10010681x2_8k.htm`: *"and its Collins Aerospace Systems segment
   prior to the Separation, which provides technologically advanced aerospace products…"*. `Rockwell`
   likewise **87** occurrences in 9 paths, all 2019-2020. **So the Collins line enters this registrant's
   own voice only as a segment name in 2019-2020 separation language — no held document says when or how
   the registrant came to hold it.** Any chronology that dates the Collins acquisition rests on a source
   not in this repo; I refused to supply the year from memory. (Counts are occurrences across stored
   *paths*, several of which are different documents or SGML/HTML variants **of one accession** — they are
   not independent witnesses, §3.) `Rockwell` needs the same care: **86** occurrences in the 2019-2020
   paths but exactly **1** in-window, and that one is a **different Rockwell** — FY1993 10-K L600-604,
   *"Pratt & Whitney is a team member with Rockwell, Rocketdyne, McDonnell Douglas and Lockheed under
   contract with the U.S. Air Force"*, the NASP/X-30 research team. It is a useful carrier (a second
   government-contract validation record, in-window) and a warning (a brand name in the same accession
   can belong to another company entirely).
4. **The date of the second rename (Raytheon Technologies → RTX Corporation): UNKNOWN.** EDGAR's
   `former_names` proves it happened; no held document dates it. K-9 gives the **ticker** RTX from
   2020-04-03, which is **not** the corporate name — a ticker is not a renaming (RD-116's CSV-column error
   in a new costume). FETCH REQUEST F-2.
5. **First experiment / first customer / first failure (1922-1934): UNKNOWN for all three.** The corpus
   cannot reach them, and the single in-window mid-century record (K-11) is a 1951-53 production test.
6. **Do not read the 8 `UNANSWERED` harvest rows, the `0 B` corporate_print directory, the `NOT-ENUMERATED`
   advisories or the `403`s as nulls about the world.** Each is reported with its cause and remedy above.

## Conflicts the registers must carry (named here, not resolved here)

- **C-1 (blocking for Stage 1 §B):** registrant-self 1934 (K-1) vs brand-folk 1929/United Aircraft
  (0 held bytes) vs Raytheon-lineage 1922 (K-5). Three dates, two legal persons, **one registrant**.
  Do not resolve by picking the oldest.
- **C-2:** "all-stock **merger of equals**" (K-9, company press release) vs the instrument's own shape —
  *Merger Sub merged with and into Raytheon, with Raytheon surviving as a wholly owned subsidiary of the
  Company* (K-7) — i.e. the surviving registrant is UTC's. The press language is a framing, the 8-K is
  the structure.
- **C-3:** `numFound` figures (4,855 / 216 / 168 / 131 / 4 / 3 / 0) are **metadata** matches; the only
  naming counts are from read bytes. Never book one as the other.

---

## FETCH REQUEST / RE-RUN REQUEST (no web budget on this pass; these are script routes)

**STATUS: WRITTEN**

```
FETCH REQUEST 1 — re-mine the enlarged index for this slug (the binding remedy for mined=0)
  tool: harvest_mine.py (NOT run by this probe, per brief)
  cmd:  python tools/harvest_mine.py --company rtx --limit 12 --max-mb 25
  why:  71 item-bearing rows exist now vs 8 UNANSWERED rows when the mine ran (2026-09-29T18:44:30Z,
        30.6 min before the facet-free rows landed). Expect a decoy purge too: 36/71 titles+ids carry
        no entity token.
FETCH REQUEST 2 — the second renaming
  tool: sec_intake.py auto "RTX Corp" --company-dir …/company_049_rtx --from 2022-01-01 --to 2024-06-30 --max-docs 8
  doc:  the 8-K / 10-K Item 1 that recites the name change to "RTX Corporation" and its effective date
  claim it would settle: item 4 of *Load-bearing open questions* (currently UNKNOWN).
FETCH REQUEST 3 — the OTHER registrant's own early filings
  tool: sec_intake.py index "Raytheon Company" --company-dir …/company_049_rtx   [name, not this CIK]
  why:  CIK 101829 is UTC's line. Raytheon Company is a different registrant; its 1992-1997 filings are
        the nearest thing to predecessor-own voice the EDGAR family can give. RD-133's "CIK is not the
        brand" applies in reverse here.
FETCH REQUEST 4 — the 60 NOT-ENUMERATED filings from my own two forward passes
  58 in 2019-06-01..2021-12-31 and 2 in 2020-04-01..2020-04-30; raise --max-docs or narrow the window.
FETCH REQUEST 5 — chronicling_america / hathitrust / google_books for this slug
  cmd:  python tools/periodical_harvest.py --company rtx --facet-free   [run from CI egress]
  why:  2 CA + 1 HT + 1 GB rows are UNANSWERED at a global request cap and a host halt; CA is separately
        403 on all 7 endpoint shapes from this machine (`_CA_ENDPOINT_TEST.md`, 2026-09-29T18:05:27Z).
FETCH REQUEST 6 — the 46 unopened in-window IA/periodical items
  cmd:  python tools/ia_text.py mine --insecure --q '"Raytheon Manufacturing Company" OR "United Aircraft
        Corporation"' --pattern "Raytheon Manufacturing|United Aircraft|Submarine Signal" \
        --company-dir founders_playbook/01_companies/company_049_rtx --max-mb 25
```

## Untried (searches never run — not nulls)

**STATUS: WRITTEN**

1. **Family (b) web archives.** No route exists in `tools/` (`grep -rlni "wayback|cdx|web.archive"
   tools/*.py` → 0 files). Command once one exists:
   `curl -s "http://web.archive.org/cdx/search/cdx?url=utc.com&from=1996&to=1999&output=json&limit=5"`
   and the same for `raytheon.com`. Bears on S3 (1994-1997) and on the 2020/2023 renamings.
2. **Family (e) auction / museum / manuscript records.** No source-family key exists in
   `tools/queries.json` (enumerated: 5 families, none of them this). Needs a new family before it can be
   tried; targets the 1922 X-ray / rectifier-tube paper class.
3. **HathiTrust / Google Books direct** (beyond the fleet rows): no per-company route was run from this
   pass; the 403/`numFound 0` question RD-130 raised was not re-tested for `rtx`.
4. **The 23 `internet_archive` rows and 52 `corporate_print` rows never fetched** — 1 of 71 item-bearing
   rows was opened by this probe. The perimeter of family (c)/(d) evidence is **one document**.
5. **The `raytheon.com` / predecessor home-town press class** (Waltham, Massachusetts: *Waltham News
   Tribune*, *Telegram & Gazette*) — never queried by any tool in this repo for this slug; this is where a
   1922-1940 naming of "Raytheon Manufacturing Company" would physically live.
6. **The 1,904 filings of this registrant after 1997-12-31** (2,968 total − 78 in-window) were sampled at
   22 documents over two narrow windows; the FY1997-FY2019 10-Ks — which are the likeliest carriers of a
   fuller "History of Business" than FY1993's two sentences — are entirely unread.

---

## One sentence naming the route most likely to change this verdict

**Re-mine this slug against the now-enlarged index and open the `corporate_print`/`internet_archive`
rows it has never fetched (FETCH REQUESTs 1 and 6):** if any item in the 47 in-window rows is a
pre-1953 Raytheon Manufacturing Company or United Aircraft Corporation **annual report, prospectus or
house organ** rather than a third-party DTIC/NTRS file, family (d) flips from UNANSWERED to ANSWERED and
S1/S2 move from T3 to T2 — the same move Boeing, Walmart, Target and Kroger made, and the reason this
probe refuses to call the origin window thin on one opened document.

## Defects observed on this pass (recorded, not routed around)

**STATUS: WRITTEN**

- **D-1 (mine/harvest sequencing).** A mine that runs while the reharvest is still writing produces a
  `mined=0` dossier that stays on disk as if final. `A4_harvest_mine.md` is now **superseded as to the
  world, not as to its bytes**; nothing was deleted. Fix belongs to the tool: stamp the index snapshot
  time into the dossier, or refuse to write a verdict when `max(retrieved_at) > mine_time`.
- **D-2 (`ia_text.py search`, console encoding).** The bare-`RTX` query crashed printing non-ASCII
  titles and left a **6,001-character truncated file that is not valid JSON** — a reader parsing it gets
  an exception, and a reader skimming it gets silence where the answer was 4,855 hits. Workaround used:
  `PYTHONIOENCODING=utf-8` + regex extraction. The tool should escape/validate on write.
- **D-3 (`sec_intake.py auto` exit code).** Both of my recital passes stored everything they planned
  (`identity … -> OK`) and still **exit 1** on the `NOT-ENUMERATED` advisory. In a fleet runner, exit 1
  reads as failure and the 22 stored documents become invisible. Advisory ≠ failure (§15.6).
- **D-4 (`_MANIFEST.csv` / `_RUN.json` rewritten by each run).** The prior run's held-list was replaced,
  not appended, so the record of the first intake now survives only in this dossier and in `_SKIPPED.csv`.
  Manifests should be dated/append-only like `sources.csv` (§13). **Pre-state preserved here verbatim**
  (8 docs / 1,449,918 B / 176,852 words, built 2026-09-29T19:08:12Z).
- **D-5 (empty `sources/corporate_print/`).** A 0-byte directory created by intake is indistinguishable
  from "searched and empty"; it should not exist before a family is tried, or should carry a
  `NOT_FETCHED` sidecar.
- **D-6 (RD-133 still live).** Rows with no `item_id` are skipped without being counted — the reason the
  2026-09-29T13:09 block could print `mined=0 / unans=0`. The count for this slug is now measurable
  (8 → 79 rows, 71 with ids) and is recorded above rather than left as a silent drop.

## Gate run at close

**STATUS: WRITTEN**

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_049_rtx \
  --checks csv,keys --fail-on substantive --out founders_playbook/03_quality_control/rtx_s1_probe_gates.md
```

Result: **Findings 2 | Passes 0**, exit code **0**, and both findings are coverage-only — `coverage/
registers` ("no register CSVs at root or research/ -- csv/anchors gates DID NOT RUN") and
`coverage/narrative` ("no stage_*.md volumes found"). The gate's own footer says these are "expected for
a freshly probed company, and NOT failing the exit code unless --fail-on all". **This is not a passing
gate and must not be reported as one** — it is the pre-authoring state, and the substantive csv/keys
gates did not run because this probe writes no registers (correct at tier-setting stage, §13).
It counted **31 source documents**, which reconciles exactly with this probe's tally (30 SEC documents +
1 periodical layer = 31), so the intake is fully enumerated.

**One instrument note (RD-131's class — a wrong checker needs a narrower claim, not a rewritten corpus):**
run twice (before and after this dossier's corrections), the gate printed `tier: T3 (a stated-verdict line)
from A_chronology_feasibility.md -- T2/T3 all mentioned in research/ (14 mentions, 2 on a verdict line); if
the dossier's own text names a different tier, trust the dossier and tell me, because this reader is not the
authority on your finding`. The `T2` strings it counted are this dossier's **counterfactual** rows (the
rejected 1920-1997 search-span grade, and the "route most likely to change this verdict" sentence), each
labelled as such in place. **The operative verdict is T3, PROVISIONAL for S2/S3**, and no re-grade is being
requested by this pass. Both runs reported the same 2 coverage-only findings and the same 31 documents.

---

## Claim records (dossier-local ids; registers are minted at merge, §13)

**STATUS: WRITTEN**

R01 Claim: The registrant behind ticker RTX states its own incorporation as Delaware 1934 — Date: 1934
— Source: FY1993 Form 10-K, United Technologies Corporation, accession 0000101829-94-000019 — Source
date: 1994-03-31 — URL: https://www.sec.gov/Archives/edgar/data/0000101829/000010182994000019/0000101829-94-000019.txt
— Archived: not archived (held under `sources/sec/`) — Tier: 1 — Class: FOUNDER CLAIM (retrospective
memory; corporate self-narrative) — Passage: "United Technologies Corporation was incorporated in
Delaware in 1934." — Conf: Medium — Corroboration: 0 independent (one accession) — Conflicts: C-1

R02 Claim: That 1994 10-K carries no 1929, no United Aircraft, no 1860s machine-tool sentence — Date:
1994-03-31 — Source: same accession, byte counts — Source date: 1994-03-31 — URL: same — Archived: — —
Tier: 1 — Class: FACT (measurement) — Passage: "NO_VERBATIM_PASSAGE_RECORDED" — Conf: High — Corrobora-
tion: measured by count (`United Aircraft` 0, `1929` 0, `machine tool` 0 across the 7 held in-window
`.txt`) — Conflicts: None

R03 Claim: RTX Corp (CIK 101829) is the renamed United Technologies Corporation, not the renamed Raytheon
Company — Date: 2020-04-03 — Source: Form 8-K accession 0001140361-20-007906 — Source date: 2020-04-03 —
URL: https://www.sec.gov/Archives/edgar/data/0000101829/000114036120007906/nc10010681x1_8k.htm — Archived:
— — Tier: 1 — Class: FACT — Passage: "In connection with the Merger, the Company's name was changed to
Raytheon Technologies Corporation" — Conf: High — Corroboration: 2 accessions + EDGAR `former_names`
registry (same registrant lineage, so capped at Medium-High for independence) — Conflicts: None

R04 Claim: Raytheon Company was the surviving subsidiary of a merger into a UTC shell, i.e. UTC's
registrant line is the continuous one — Date: 2020-04-03 — Source: 8-K 0001140361-20-008397 — Source
date: 2020-04-08 — URL: …/0001140361-20-008397/nc10010681x2_8k.htm — Archived: — — Tier: 1 — Class: FACT
— Passage: "United Technologies Corporation (since renamed Raytheon Technologies Corporation, as
described below in Item 2.01 of this Current Report on Form 8-K)" — Conf: High — Corroboration: 1
structure-bearing document, restated in R03's 8-K — Conflicts: C-2

R05 Claim: The Raytheon lineage's 1922 founding sentence exists only in a 2019 registration statement —
Date: 1922 (recited); carrier 2019-07-17 — Source: Form S-4 accession 0001140361-19-013079 — Source date:
2019-07-17 — URL: https://www.sec.gov/Archives/edgar/data/0000101829/000114036119013079/nt10003205x1_s4.htm
— Archived: — — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION (company-side about another legal person) —
Passage: "Raytheon was founded in 1922 and is incorporated in the state of Delaware" — Conf: Low — Corrob-
oration: 0 independent — Conflicts: C-1

R06 Claim: The merger agreement between the two lineages is dated June 9, 2019 — Date: 2019-06-09 —
Source: S-4 joint proxy letter — Source date: 2019-07-17 — URL: as R05 — Archived: — — Tier: 1 — Class:
FACT — Passage: "On June 9, 2019, United Technologies Corporation, or UTC, Light Merger Sub Corp., a
wholly owned subsidiary of UTC, or Merger Sub, and Raytheon Company, or Raytheon, entered into an
Agreement and Plan of Merger" — Conf: High — Corroboration: 1 accession, phrase occurs 55× in-document —
Conflicts: None

R07 Claim: The registrant's own in-window (1994-1997) voice names five legacy operating units and no
Collins — Date: 1994-03-31 — Source: FY1993 10-K L254-256 — Source date: 1994-03-31 — URL: as R01 —
Archived: — — Tier: 1 — Class: FACT — Passage: "The Corporation conducts its business principally through
its Pratt & Whitney, Sikorsky, Hamilton Standard, Norden, Carrier, Otis, and UT Automotive units" —
Conf: High — Corroboration: 1 accession — Conflicts: None (but see *Open questions* 3: `Collins` = 0
count, a perimeter statement, not a historical null)

R08 Claim: `Raytheon` in the 1994-95 10-Ks names a competitor's products, not the registrant — Date:
1994-03-31 — Source: FY1993 10-K L572 — Source date: 1994-03-31 — URL: as R01 — Archived: — — Tier: 1 —
Class: FACT — Passage: "powers two applications, the Raytheon Corporate Jets Hawker 1000 and the Learjet"
— Conf: High — Corroboration: 2 documents (1994, 1995) — Conflicts: None. **This is the trap (1) class
inverted: the right brand in the wrong company's mouth.**

R09 Claim: A third-party 1953 Navy laboratory evaluation names Raytheon Manufacturing Company's Submarine
Signal Division at Waltham, Mass. — Date: 1953-07-20 — Source: DTIC ADA320141 (NRL Confidential Report
#192, H. H. Elliott Jr.), held at `sources/periodicals/DTIC_ADA320141_djvu.txt` — Source date: 1953 —
URL: https://archive.org/details/DTIC_ADA320141 — Archived: local bytes 158,295 B, sidecar notes UNVERIFIED
TLS — Tier: 1 (third-party government record) — Class: CONTEMPORARY OBSERVATION — Passage: "QHD
scaiming [sic] sonar equipment manufactured by Raytheon Mfg. Co., Submarine Signal Division, Waltham,
Mass." — Conf: Medium (OCR; TLS unverified) — Corroboration: 1 third-party document — Conflicts: None

R10 Claim: The earliest held repeatable-validation-shaped signal is a contract-and-acceptance-test record,
not a test flight — Date: 1951-09-20 (delivery) / 1951-12-12 (tests begun) — Source: DTIC ADA320141
abstract — Source date: 1953 — URL: as R09 — Archived: local — Tier: 1 — Class: FACT — Passage: "Serial
Humber [sic] 1 of the Model QHD Scajining [sic] Sonar Equipment manufactured by the Raytheon Manufacturing
Company, Submarine Signal Division, Waltham, Mass., under contract HObsr-42064, was delivered to this
laboratory for tests" — Conf: Medium (contract number is OCR-garbled; not quoted to registers at High) —
Corroboration: 1 — Conflicts: None

R11 Claim: The same record carries the earliest held negative signal — Date: 1953 — Source: DTIC ADA320141
L110 — Source date: 1953 — URL: as R09 — Archived: local — Tier: 1 — Class: FACT — Passage: "Serial No. 1
of Model QHD was the only one built. It was never put into operation. The technology of this equipment has
long been superseded." — Conf: High — Corroboration: 1 third-party — Conflicts: None

R12 Claim: The `RTX` token is a decoy-dominant search term — Date: measured 2026-10-06 — Source: Internet
Archive `advancedsearch` via `tools/ia_text.py` — Source date: 2026-10-06 — URL: archive.org metadata API
— Archived: raw outputs left in `_tmp_rtx_q*.json` at repo root (mine, scratch, add-only) — Tier: 3 —
Class: FACT (measurement) — Passage: "NO_VERBATIM_PASSAGE_RECORDED" — Conf: High — Corroboration: two
queries (`RTX` numFound 4,855; `RTX graphics card` numFound 216, first item "Super Mario 64 RTX") —
Conflicts: C-3

R13 Claim: `mined=0` for this slug was a sequencing artefact, not an empty archive — Date: 2026-09-29 —
Source: `stat` on `research/A4_harvest_mine.md` + `sources/harvest_mine/_index.json` vs
`00_universe/harvest/candidates.csv` `retrieved_at` column — Source date: 2026-10-06 — URL: — — Tier: 1
(own tool state) — Class: FACT (measurement) — Passage: "NO_VERBATIM_PASSAGE_RECORDED" — Conf: High —
Corroboration: file mtimes and row stamps agree (18:44:30Z mine vs 19:15:07Z+ rows) — Conflicts: None

R14 Claim: EDGAR cannot reach the origin window for this registrant at all — Date: floor 1994-01-24 —
Source: `sources/_index/submissions_CIK0000101829.csv` — Source date: 2026-10-06 — URL: SEC submissions
JSON — Archived: local — Tier: 1 — Class: FACT (measurement) — Passage: "NO_VERBATIM_PASSAGE_RECORDED"
(rows < 1994-01-24: 0 of 2,968; S-1-family rows: 0) — Conf: High — Corroboration: measured twice (the
2026-09-29 intake and this pass's re-walk, 2,966 → 2,968 rows) — Conflicts: None. **Reported as a
perimeter with dates, never as "filed nothing".**

R15 Claim: The date of the second renaming (to RTX Corporation) is not established — Date: UNKNOWN —
Source: EDGAR `former_names` registry record only — Source date: 2026-10-06 — URL: — — Tier: 1 — Class:
UNKNOWN — Passage: "NO_VERBATIM_PASSAGE_RECORDED" — Conf: UNKNOWN — Corroboration: 0 — Conflicts: None
(FETCH REQUEST 2 assigned).

R16 Claim: A second in-window government-contract validation record exists — Pratt & Whitney on the
NASP/X-30 Air Force team — Date: FY1993 (carrier filed 1994-03-31) — Source: accession
0000101829-94-000019, L600-604 — Source date: 1994-03-31 — URL: as R01 — Archived: local — Tier: 1 —
Class: FACT — Passage: "Pratt & Whitney is a participant in the National Aero-space Plane (NASP) team with
Rockwell, Rocketdyne, McDonnell Douglas and Lockheed under contract with the U.S. Air Force" — Conf:
Medium (the passage is at L601-602 with a line-wrap between "Pratt &" and "Whitney"; verified in bytes) —
Corroboration: 1 accession — Conflicts: None. **Usable for trap (3)'s "which kind of record" answer; NOT
usable as an origin or Collins-lineage claim — this `Rockwell` is Rockwell International, a team partner.**

R17 Claim: The surname-decoy hypothesis for `Whitney` in the FY1993 DEF 14A is withdrawn — Date: measured
2026-10-06 — Source: `sources/sec/0000101829-94-000012_0000101829-94-000012.txt` L912-913 — Source date:
1994-03-11 — URL: https://www.sec.gov/Archives/edgar/data/0000101829/000010182994000012/0000101829-94-000012.txt
— Archived: local — Tier: 1 — Class: FACT (measurement, and a retraction of this probe's own first
reading) — Passage: "Mr. Krapek in his current position as President of Pratt & / Whitney." — Conf: High —
Corroboration: re-read twice (line enumeration, then context read) — Conflicts: None. **Recorded because
§14 r10 requires a retraction to reach the instruction layer, not only the paragraph where it was wrong.**

## Coverage note — what this pass did not examine

**STATUS: WRITTEN.** Did not read the 30 stored SEC documents end to end (counted and line-sampled: the
FY1993 10-K history block, the S-4's Raytheon particulars, three 2020 8-K exhibits). Opened **1 of 71**
item-bearing harvest rows. Did not fetch any `corporate_print` byte. Did not re-run `harvest_mine.py` /
`periodical_harvest.py` (forbidden by brief), so the 79-row census is read-only. Did not create
registers, source ids, volumes, or another company's files; wrote nothing under `sources/` except the one
periodical layer and its sidecar, and no file outside `company_049_rtx/` except my two run logs and three
`_tmp_rtx_q*.json` scratch outputs at repo root (add-only, disclosed here).
