# A2_periodical_and_filings_settlement.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:28:45Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## EDGAR floor re-set

STATUS: WRITTEN 2026-09-25

**Verdict: the earlier UNANSWERED is resolved and re-set to a documented FLOOR, not a null.** Family (a)
now enumerates completely, and what it proves is that EDGAR cannot answer this company's founding period
at all. The 503-vs-404 contradiction (prior probe §Conflicts C-1) is dead: the fix was on the script side.

**Fix verified in code before use.** `tools/sec_intake.py` line 128-130: older slices are requested as
`"https://data.sec.gov/submissions/%s" % f["name"]`, iterating the `filings.files[]` members read at line
122 — not under `/Archives/edgar/data/<cik>/`, which is what 404/503'd. The comment in the file states the
same. Confirmed live below rather than from the source alone.

**Re-run, this session** (`python tools/sec_intake.py index --cik 789019 --company-dir
founders_playbook/01_companies/company_011_microsoft`):
stdout → `index: 4525 filings from MICROSOFT CORP (MSFT)`.

| check | result |
|---|---|
| rows in `sources/_index/submissions.csv` | 4,525 |
| `source` column counts | `recent` 1,002 · `CIK0000789019-submissions-001.json` 2,002 · `-002.json` 1,521 |
| oldest / newest `filingDate` | **1994-02-14** / 2026-09-17 |
| rows dated before 1994-02-14 | **0** |
| `_INDEX.md` "UNANSWERED slices (never report these as absent)" | **`(none)`** |

The prior probe's truncation is quantified: 3,523 of the 4,525 rows (77.9%) come from the two older slices
that the old build never parsed. The 1,002 `recent` rows are the same set the first probe mistook for the
registrant's whole filing life.

**Earliest filing on the index** (`sources/_index/submissions.csv`, first rows sorted by `filingDate`):

| filed | form | accession | primaryDocument | slice |
|---|---|---|---|---|
| 1994-02-14 | **10-Q** | 0000950109-94-000252 | *(empty in index)* | `-002.json` |
| 1994-05-03 | 10-Q | 0000891020-94-000070 | (empty) | `-002.json` |
| 1994-07-29 | 8-K | 0000891020-94-000114 | (empty) | `-002.json` |
| 1994-09-27 | 10-K | 0000891020-94-000175 | (empty) | `-002.json` |

**The prior probe's open fallback question is now answered from the index, not from expectation.** It asked
whether the registrant's oldest EDGAR-era company-authored text is a 10-K, a 13D/G, or something else.
Answer: **a Form 10-Q filed 1994-02-14** (accession 0000950109-94-000252). The oldest 10-K is 1994-09-27;
the oldest `SC 13G/A` is 1996-02-07 and the oldest `SC 13D` 1996-05-09 — both *later* than the first 10-Q,
and `SC 13D/G` rows are third-party anyway, not company-authored.

**Why the floor is a floor — proved from the index rather than asserted.** Counting the `form` column across
all 4,525 rows: there is **no `S-1` and no `S-1/A` row of any kind** (the exact strings are absent from the
form set, not merely rare). The registration-form families that do appear are `S-3` ×36, `S-3/A` ×21, `S-4` ×7,
`S-4/A` ×6, `S-8` ×16, `S-8 POS` ×10, `S-3MEF` ×1, `S-3ASR` ×8, `D` ×2 — and the *earliest* of any of them is
an S-3 on 1994-10-14, i.e. eight months after the registrant's first EDGAR appearance and long after its
first sale of product. So the IPO registration statement is not on EDGAR, which means there is **no
company-authored registration document and no company-authored financial text of any form before
1994-02-14 on this route**. The window this dossier needs (1975-1980, and to 1986) is entirely below the
floor. This is exactly the shape §14 rule 6 predicts ("EDGAR reaches essentially nothing before ~1994"),
now demonstrated for this CIK rather than inherited.
The 1986 registration date itself remains an **inherited claim from the intake sheet, unverified this
session** — no document seen here prints it.

**Consequence for the tier.** Family (a) is **confirmed zero in-window Tier-1 text for 1975-01-01 →
1990-12-31** and can no longer be scored as "blocked, unknown". It also means the corrected enumeration
does *not* rescue Stage 1 or Stage 2: the oldest filing on disk post-dates the founding window by 19 years
and the 1986 registration by 8 years. Documents downloaded this pass: 0 (index only; no in-window
accession exists to fetch). `sources/sec/_MANIFEST.csv` still carries a header row and no document rows —
now correctly, because the enumeration is complete rather than truncated.

## Family c periodicals

STATUS: WRITTEN 2026-09-25

**Verdict: TIER1_CANDIDATE — the prior LEAD_ONLY is overturned. This family now returns in-window
Tier-1-class text about Microsoft, read off bytes held on disk this session.** Two routes were used:
(i) the shelves already in the repository (Apple's `company_004_apple/sources/` Byte + Homebrew OCR, fetched
2026-09-24, read-only to me and grepped in place), and (ii) fresh fetches into
`company_011_microsoft/sources/periodicals/` with sidecars.

*The route fix that made this possible.* `tools/ia_text.py` is verified as to its **premise** (it classifies
from held bytes, and its own header states that `text:` matches annotations) but its **fetch route is broken
from this egress**: `ocr_url()` assumes `archive.org/download/<id>/<id>_djvu.txt` and returned
`HTTP 404, 0 bytes` for all three identifiers tried (`197503PopularElectronics`,
`byte-magazine-1977-07`, `hcc0201`), with and without `--insecure`. Apple's `_RETRIEVAL_LOG.md` records the
cause and the working form: the `download/` host "302s to a CDN node that returned 404 — use the
metadata→items-server form". Confirmed here: `https://archive.org/metadata/197503PopularElectronics` → HTTP
200, server `ia800609.us.archive.org`, and the text layer is filed as **`197503 Popular Electronics_djvu.txt`**
— the stem is *not* the identifier, so the tool's filename assumption fails independently of the redirect.
A 404 over 0 bytes is **UNANSWERED, never a null**; see §Conflicts C-6 and the FETCH REQUEST at the end.

**What the held bytes actually returned.**

1. **`hcc0201.txt` (Homebrew Computer Club Newsletter, 28,281 B, in Apple's shelf) — the decisive document.**
   Its own masthead line reads `Volume Number 2, Issue 1 January 31, 1976`. Editor's note: "A LETTER FROM
   MITS - Just as the Newsletter was in final preparation a letter arrived from Bill Gates via MITS.
   Reproduced (the only MITS 'software' we have ever reproduced) on page 2, it should be read by every
   computer hobbyist." The reproduced letter, in first person: "**Almost a year ago, Paul Allen and myself,
   expecting the hobby market to expand, hired Monte Davidoff and developed Altair BASIC**"; "the three of
   us have spent most of the last year documenting, improving and adding features to BASIC. Now we have 4K,
   8K, EXTENDED, ROM and DISK BASIC"; "The value of the computer time we have used exceeds $40,000";
   "less than 10% of all Altair owners have bought BASIC"; royalties make the work "worth less than $2 an
   hour"; "We have written 6800 BASIC, and are writing 8080 APL and 6800 APL"; "Nothing would please me
   more than being able to hire ten programmers"; reply address "1180 Alvarado SE, #114, Albuquerque, New
   Mexico, 87108". Signed "**Bill Gates / General Partner, Micro-Soft**". The same issue separately reports
   Altair BASIC availability "set for December 17, 1975. Delivery was then scheduled for January 15, 1976".
   *Tier reading:* §5 puts "original interviews and transcripts" — first-person original text — in Tier 1;
   this is the founder's own words, printed contemporaneously, not a later history. **Tier 1 candidate for
   the founding window, and the earliest such document this project holds for Microsoft.**
2. **`hcc0202.txt` (43,265 B) `Volume Number 2, Issue 2 February 29, 1976`** — carries a reply: "BILL GATES -
   One response to Bill's letter to hobbyists that appeared in our…", signed line "Bill Gates, Micro-Soft",
   and "Regarding your Letter of 3 February 1976 Appearing in Homebrew". **`hcc0204.txt` (30,810 B)
   `Volume Number 2, Issue 4 April 30, 1976`** — the dispute is still being argued in the club: "However,
   since Mr. Bill Gates claims that he did not get payed".
3. **Independent cross-title corroboration of the letter's circulation, from Byte July/September 1976.**
   `byte-1976-07.txt` (487,633 B): "Bill Gates' 'An Open Letter to Hobby-ists' very clearly explained one of
   the chief problems of the hobby computer industry, the low Return on Investment"; and, in the same issue,
   a pointer listing where the text had been printed — "see page 14 of Radio Electronics, May 1976, page 24
   of March-April 1976 PCC … page 3 of February 1976 Computer Notes (published by MITS Inc)".
   `byte-1976-09.txt` (527,921 B): "it now appears that more copies of Altair's BASIC have been pirated than
   have been legally sold. (See the letter by Bill Gates on page 3 of the February 1976 edition of MITS
   Computer Notes, the March April 1976 issue of People's Computer Company and widely published elsewhere…)".
   Two things are established here that no filing can give: the letter's **publication footprint in
   Feb–Apr 1976 across at least four titles**, and a third party's contemporaneous statement of the
   **MITS-licence relationship** ("Altair's BASIC").
4. **Later in-window trade print, from the fresh fetches.**
   `kilobaudmagazine-1977-05_djvu.txt` (672,171 B): in-page counts **MICROSOFT ×1** — "OSI 6502 8K BASIC FOR
   DISK BY MICROSOFT: This powerful…" — with **ALTAIR ×85** and **MITS ×57** in the same issue. The identical
   OSI news line is in Apple's held `byte-1977-05.txt` and `byte-1977-06.txt`, so this is **one syndicated
   news item in two titles, not two independent confirmations** (§Conflicts C-7).
   `1979-Fall-compute-magazine_djvu.txt` (542,112 B, "Compute! Magazine Issue 001", 1979): **in-page** "A
   Convenient Method to List Microsoft BASIC", "versions of Microsoft BASIC (PET, KIM, SYM, etc.)", "Other
   Microsoft BASICs have…". This is the other half of the prior probe's `text:` numFound-2 result and it
   **does** carry the string in the OCR — so `text:` hits are not uniformly fake, they are individually
   unverifiable until opened (§Conflicts C-5).
   `byte-magazine-1980-12` / `byte-magazine-1981-02` (held, 1,669,716 B and 1,617,655 B): 136 and 65
   `Micro-?Soft` hits, including product pricing "MICROSOFT Z-80 SOFTCARD $320", "Thanks to the Z-80
   Softcard by Microsoft", and a trademark line naming "**Microsoft Consumer Products, Inc.**" — the
   corporate-entity name appearing in company-adjacent print at the Stage-1/Stage-2 boundary.

**Nulls inside this family (zeros over held kilobytes, so real nulls):** the twelve Byte 1976 issues
(≈5.3 MB) contain **0** occurrences of `Micro-?Soft`; `hcc0109` (15,563 B, 1975-11-30 per Apple's log) and
`hcc0110` (20,193 B, 1975-12-31) contain **0** occurrences of both `Micro-?Soft` and the two founder names;
`197503PopularElectronics_djvu.txt` (493,273 B) contains **0** occurrences of `micro-soft` while carrying
MITS/Altair 8800 copy ("January's 'Altair 8800' computer project generated an immense reader…", "ALTAIR 8800
PRICES"). The 1975 name-vacuity is itself a finding: **the earliest Microsoft-relevant print is 1976-01-31,
and the founding year 1975 is silent in the four serials sampled.**

## Family d corporate print

STATUS: WRITTEN 2026-09-25

**Verdict: TIER1_CANDIDATE for company-authored in-window print; the annual-report run remains a null
(carried).** This family is no longer decided by the creator-scoped query the prior probe ran — two
company-authored documents have now been opened.

1. **`MSDOS2FuturePlansForMSDOSByPaulAllen_djvu.txt` — 13,639 B, HTTP 200, fetched this session**
   (collection `opensource`, ungated). The document's own face: "MS DOS 2.0 / **by Paul G. Allen** / Future
   plans for MSDOS / or / The Bridge to XENIX", and it is a talk transcript ("**** (slide #1) ****").
   In-page: "**Over the last seven years, Microsoft has ported its software products to over fifty different
   operating system environments.** This, combined with our experience with XENIX, has given us a thorough
   education in what OEMS, end users and programmers want…"; "MSDOS has already been described as
   **Microsoft's** single user, single tasking operating system. It is written in 8086 assembler…"; "Microsoft
   plans to support a standard network protocol"; "Microsoft has a complete in-house mail system right now".
   A named principal speaking as "we" about the company's own product line and installed base — company print
   at Tier-1 class. **Two cautions that cap its confidence:** the text carries **no date on its face** (the
   1982 comes only from the catalogue `year` field, and the string `198x` appears nowhere in the 13,639 B),
   and it describes 2.0 as "the next major release", which sits awkwardly against a 1982 stamp. Recorded as
   §Conflicts C-8; cite at **Medium**, never High, until an internal date or a second source fixes the year.
2. **`1981-microsoft-adventure_djvu.txt` — 3,755 B, HTTP 200.** "Brochure: Microsoft Adventure"
   (collections `readerservice`, `folkscanomy_computer` — ungated). In-page: "The Microsoft Adventure software
   package **for your IBM Personal Computer** includes: Program Diskette, Users' Instruction Booklet…",
   "…by Microsoft", "Playing Adventure, you gain…". Company-issued product print, in-window, and
   **internally dated from below**: it names the IBM Personal Computer, so it cannot pre-date that machine —
   the strongest date anchor this family has. Use as the Stage-2 opener candidate.
3. **Carried null, not re-run:** the creator-scoped annual-report route (§Nulls N-1 in the prior probe;
   JSON held at `sources/corporate_print/ia_q4_creator_microsoft_reports_1977_1998.json`) returned
   `numFound 1`, that row being a 1997 Visual Basic manual. **There is no digitised Microsoft annual-report
   run equivalent to Walmart's FY1972-FY1998 set**, so family (d) cannot supply early financial statements;
   it supplies product and officer print instead. Note this row was *not* re-verified by a second query type
   this session — the title-scoped variant is still untried.
4. **Held but NOT opened, so counted nowhere:** `microsoft-multi-tool-word-brochure` (1983, `opensource`),
   `16-Bit_Operating_Systems_A_Whole_New_Ball_Game_1982-06`, and `multiplanusersgu0000schn` /
   `illustratedmulti0000stul` (1984) which sit in `internetarchivebooks` + `inlibrary` + `printdisabled` —
   borrow-restricted, so §4's legal boundary bites before anyone reads them; treat those two as UNTRIED, not
   as nulls.

**Combined effect on the tier.** Families (c) and (d) each now return in-window Tier-1-class text from bytes
held in this repository. Family (a) is proven silent for the window (§EDGAR floor). So **exactly two families
qualify**, which is the T2 row of §15.2, and the third family can now only come from (b) or (e) — never from
filings.

**FETCH REQUEST (script work, 0 agent web budget) — `tools/ia_text.py` route defect.**
`ocr_url()` must stop assuming `<identifier>_djvu.txt` under `https://archive.org/download/`. Change it to:
`GET https://archive.org/metadata/<id>` → read `server`, `dir`, and the file list; select the entry ending
`_djvu.txt` **by suffix, not by name equality with the identifier**; then
`GET https://<server><dir>/<urlencoded-name>`. Keep the opt-in `--insecure` stamp. Four text layers totalling
1,651,636 B were fetched this way by hand this session and are already in `sources/periodicals/` with
`.meta.json` sidecars recording the route and the UNVERIFIED-TLS flag. Second request: run the corrected tool
over the remaining ~520 unopened items of the numFound-545 shelf, and over `tools/queries.json` once a
`microsoft` task block exists.

## Tier verdict

STATUS: WRITTEN 2026-09-25

**TIER: T2 (core).** Families returning in-window Tier-1-class text: **2 of 5** — (c) periodicals and
(d) corporate print. §15.2's T2 row: "2 families → evidence-bound §A–§U, full registers, records for
load-bearing claims only, **cap 22k words/stage, ≈6-9 agent runs**."

| family | prior probe (2026-09-26, first pass) | this pass | in-window Tier-1 text |
|---|---|---|---|
| (a) filings | UNANSWERED, truncated to 1,002 rows from 2020 | **FLOOR PROVEN** — 4,525 rows, 3/3 slices, oldest 1994-02-14 | **0, permanently**: window ends 8 years before the oldest row |
| (b) web archives | UNANSWERED (CDX 503 ×2) | **carried UNANSWERED** — not re-run this pass | 0 |
| (c) periodicals | LEAD_ONLY | **TIER1_CANDIDATE** | `hcc0201` 1976-01-31 founder letter; Byte/Kilobaud/Compute 1976-1980 |
| (d) corporate print | LEAD_ONLY | **TIER1_CANDIDATE** | Paul G. Allen MSDOS-2.0 talk text; 1981 Microsoft Adventure brochure |
| (e) documentary | UNTRIED | **UNTRIED** | 0 |

**Is the earlier recommendation superseded? Yes — but its direction was right.** The first pass said:
"hold Microsoft ungraded for one scripted re-probe, and plan against **T2 (6-9 agent runs) provisionally,
not T1**." The re-probe has now run and the provisional number is confirmed as the grade, so the *hold* is
superseded while the *plan* survives unchanged. Its two supporting judgments also hold: (i) "Do not fund
15-20 runs on this evidence: T1 needs ≥3 families" — still true, and now stronger, because family (a) has
been positively disqualified for this window rather than merely unmeasured; (ii) "the same error in reverse —
under-grading on an outage and an unconfigured family — is the risk here" — the risk was real and is now
closed, since the corrected count went **up** from 0 qualifying families to 2, not down.

**What would move this to T1, and what would not.** Not filings — nothing on EDGAR predates 1994-02-14 for
this CIK. Only (e) documentary (the Apple precedent is that founding-era paper surfaces at auction and in
museum collections, not in EDGAR) or (b) web archives (a successful CDX re-run, which §14.6 says cannot
reach pre-mid-1990s anyway, so it is a Stage-3-tail corroboration route at best). Realistically **T2 is this
company's ceiling on the current archive**, and the depth should be spent where the documents are: 1975-1985
trade print and company print.

**Budget implication and how to spend it.** 6-9 runs, 22k words/stage, and every tier still emits
`sources.csv`, `conflicts.csv`, `data_gaps.csv` and an UNTRIED list. The corpus is uneven, so the runs
should be: 4-5 against Stage 1 (the Homebrew/Byte/Kilobaud shelf is the richest and least-organised asset),
2-3 against Stage 2 (company print: brochures, the Allen text, then the 1986-1990 tail), **0-1 against
Stage 3 until a 1986-1990 harvest lands** — dispatching a Stage-3 dossier today would produce narrative
with no primary document behind it, which is the failure this whole re-probe exists to prevent. One run of
script-side intake should precede any of them: `sec_intake.py auto --from 1994-01-01 --to 1995-12-31`
(the FY1994 10-K's multi-year selected data is the closest filings will ever come to the founding era) and
the corrected `ia_text.py` over the 545-item shelf.

## Boundaries

STATUS: WRITTEN 2026-09-25

Each date below names the document that carries it. Anything without a document is marked, not deleted.

**Stage 1: 1975-01-01 → 1980-12-31 — now defensible, and it was the emptiest stage before this pass.**
- *Environment, earliest:* `197503PopularElectronics_djvu.txt` (493,273 B) — MITS and the "Altair 8800"
  appear in-page ("ALTAIR 8800 PRICES"; "January's 'Altair 8800' computer project generated an immense
  reader…"). It says **nothing** about Microsoft (0 hits) and may only be used to establish the machine and
  the vendor the first product was written for.
- *Company, earliest document:* **`hcc0201` — Homebrew Computer Club Newsletter Vol 2 No 1, dated on its own
  masthead 1976-01-31.** This is the boundary document: an entity styled **Micro-Soft** exists, with
  **Bill Gates as named "General Partner"**, holding a BASIC product for the Altair, an Albuquerque address,
  and a three-person origin statement ("Almost a year ago, Paul Allen and myself … hired Monte Davidoff and
  developed Altair BASIC"). Consequence for the chronology: the company's own 1976 print places its start
  "almost a year ago", i.e. **≈1975 — but that is the company's retrospective, so every line drawn from it is
  tagged `RETROSPECTIVE SOURCE` per §6.**
- *Corroborating chain (not independent of each other, see C-7):* `hcc0202` 1976-02-29, `hcc0204`
  1976-04-30, `byte-magazine-1976-07` and `-09`, `kilobaudmagazine-1977-05`, `1979-Fall-compute-magazine`.
- *Close:* `byte-magazine-1980-12` (1,669,716 B held) — 136 in-page Microsoft occurrences including priced
  product listings and a trademark line naming **Microsoft Consumer Products, Inc.** A December-1980 boundary
  is therefore documentary, not the arbitrary date the first probe guessed from the absence of 1975-1980
  authored rows (that guess was wrong in mechanism: the first probe's own Q1 window was 1975-1985 and the
  shelf did hold in-window material — it had simply never been opened).

**Stage 2: 1981-01-01 → 1985-12-31 — defensible at its opening, thin at its close.**
- *Open:* `1981-microsoft-adventure` brochure (3,755 B), which names the **IBM Personal Computer** in its own
  text, so it cannot pre-date that machine — an internally-dated company document.
- *Body:* the Paul G. Allen MSDOS-2.0 talk text (catalogue year 1982, **no date on its face**, Medium), and
  the 1983/1984 rows still unopened (`microsoft-multi-tool-word-brochure`; `multiplanusersgu0000schn`,
  `illustratedmulti0000stul` — `inlibrary`/`printdisabled`, so gated under §4).
- *Close (1985):* **no document held.** Stage 2's end date is currently an assumption.

**Stage 3: 1986-01-01 → 1990-12-31 — the binding gap, and filings cannot fill it.** The first probe said
Stage 3 was "the emptiest of the three despite being closest to the era where EDGAR should begin to answer".
Corrected: **EDGAR does not begin to answer until 1994-02-14**, so Stage 3 is not "close to" the filings
era — it is entirely below it. Stage 3 must be built from trade and company print 1986-1990, and the corpus
holds **zero** documents in that span (the 545-item shelf was filtered to 1974-1982; the Q1 shelf to
1975-1985). Two options, both defensible, to be decided by the orchestrator: cut the dossier as **two
stages** (1975-1980 / 1981-1990) with the second stage's tail explicitly marked thinly evidenced, or keep
three stages and let Stage 3 ship as an evidence-pending §A–§U with `data_gaps.csv` carrying a High-importance
row and a named follow-up (§13: a High gap with no follow-up is an open debt, not a finished section).
**Do not let the 1994 filings be pulled backwards to stand in for 1986-1990.**

**Founder pre-history: UNKNOWN — keep it, do not delete it.** Nothing seen this session touches either
founder before 1976-01-31, and the one candidate source class for pre-1975 Microsoft — a **Traf-O-Data**
pattern — was **never searched** (my greps covered `Micro-?Soft`, `MITS`, `Altair`, `Bill Gates`, `Paul
Allen`, `Kilobaud`; Traf-O-Data was not among them). The only pre-window statement in any held document is
the company's own "Almost a year ago, Paul Allen and myself…" line, which reaches back to 1975 and no
further. Any inherited pre-history narrative (school, first joint business, the 1975 New Mexico move) stays
a claim awaiting a source and must not be promoted into §A. The first probe's ruling here is unchanged and
was not tempting: no held byte states a birth, a school, or a pre-1975 company.

## Conflicts

STATUS: WRITTEN 2026-09-25

- **C-5 — the prior probe's C-2 is confirmed, but its reach was overstated.** Confirmed: `text:` matches
  annotations. `197602-modern-data` holds 261,075 B with **0** occurrences of the term, and the match lives
  in the uploader's `description`. New and contrary: the *other* row of the same numFound-2 result,
  `1979-Fall-compute-magazine`, **does** contain "Microsoft BASIC" in its OCR (4+ in-page lines in 542,112 B).
  Adjudication: a `text:` hit is neither evidence nor noise — it is an unopened envelope. The operative rule
  is not "`text:` is blind" but "no `text:` count may be cited for any item until that item's bytes are
  grepped". This keeps the first probe's conclusion intact where it mattered and stops it being used to
  dismiss a hit that turns out to be real.
- **C-6 — `ia_text.py` documentation vs its live behaviour.** The header says the tool downloads the item's
  text layer and greps bytes we hold; in three runs it fetched 0 bytes and returned HTTP 404 for identifiers
  whose text layers demonstrably exist (`hcc0201` and `byte-magazine-1977-07` both have bytes on this
  repository's shelves, and `197503PopularElectronics` was fetched successfully by hand in the same minutes).
  Root causes, both proven this session: (i) `archive.org/download/` 302s to a 404-ing CDN node (Apple's
  `_RETRIEVAL_LOG.md` route note); (ii) the layer's real filename is `"197503 Popular Electronics_djvu.txt"`,
  so the `<identifier>_djvu.txt` assumption fails for any item whose stem differs. Adjudication: the tool is
  sound in method, wrong in route. **Its 404s were recorded here as UNANSWERED, and none of this family's
  nulls rests on them.** Fix requested in the FETCH REQUEST block.
- **C-7 — apparent cross-title corroboration that is one item.** "OSI 6502 8K BASIC FOR DISK BY MICROSOFT"
  appears verbatim in held `byte-1977-05`, `byte-1977-06` and in fetched `kilobaudmagazine-1977-05`
  (672,171 B). Three documents, one news item. Adjudication: it establishes that Microsoft product news was
  in the 1977 trade press — **once**. Any Stage-1 count of "independent mentions" must de-duplicate shared
  copy, exactly as §13's register rules de-duplicate ids.
- **C-8 — the Allen document's date.** Catalogue `year` 1982 vs a text face that carries no year (the
  substring `198`/`197x` is absent from its 13,639 B) while describing "MS DOS 2.0 … the next major release".
  Unresolved. Do not print "1982" as a fact; print "catalogue-dated 1982, undated on its face", Medium.
- **C-9 — superseded by §EDGAR floor, kept so the old file cannot be cited alone.** The first probe's
  "1002 filings … 2020-08-07 → 2026-09-17 … 0 documents" is replaced by 4,525 rows spanning 1994-02-14 →
  2026-09-17 with `UNANSWERED slices: (none)`. Its C-1 503-vs-404 dispute is resolved as a script route
  defect, not as EDGAR behaviour. Both numbers were true of the index each pass held; only one index was
  complete.
- **Carried, not re-adjudicated:** the prior probe's C-3 (`facts` stdout naming a file it did not write) and
  C-4 (`web.archive.org` 503 while sibling archive hosts answered 200) are untouched by this pass — family
  (b) was not re-run, so C-4 remains the live account and `sources/financials/` remains empty.

## Nulls

STATUS: WRITTEN 2026-09-25

Each is a zero over named, held bytes, or an explicit refusal-to-call.

- **N-6** `197503PopularElectronics_djvu.txt`, 493,273 B: 0 occurrences of `micro-soft`. A NULL, and a
  narrow one — one issue of one title, 1975.
- **N-7** Byte 1976, all twelve issues (~5.3 MB held in Apple's shelf): 0 occurrences of `Micro-?Soft`
  anywhere in the year's issues sampled for founder names. NULL for the *name* in 1976 Byte; the *substance*
  arrives in that same year by reference (see `byte-1976-07`, `-09`).
- **N-8** `hcc0109` (15,563 B) and `hcc0110` (20,193 B), the 1975-11-30 and 1975-12-31 Homebrew issues:
  0 hits on `Micro-?Soft` and 0 on both founder names. Notable enough to be a finding: the club's own print
  does not carry the Microsoft origin story in 1975, and the earliest occurrence is 1976-01-31.
- **N-9** `197602-modern-data_djvu.txt`, 261,075 B: 0 — carried from the first pass, still a NULL, now
  re-examined under C-5 (its `text:` hit was annotation-borne).
- **N-10** EDGAR: 0 rows before 1994-02-14 across 4,525; 0 rows of any form 1975-01-01 → 1990-12-31;
  0 `S-1`/`S-1/A` rows. **This one is a true NULL, not a conditional one** — the first pass's N-3 was
  explicitly conditional on a truncated enumeration, and that condition has been removed.
- **N-11** Not nulls, and must not be read as such: every 404 returned by `ia_text.py`; the
  `printdisabled`/`inlibrary` rows never opened; the ~520 unopened items of the 545 shelf; family (b);
  family (e); the 1986-1990 span in all five families.

## Untried

STATUS: WRITTEN 2026-09-25

1. `tools/queries.json` still has no `microsoft` task block — the harvester that owns family (c) in the
   pipeline is still unconfigured for this company (this pass worked around it by hand, not through it).
2. `ia_text.py` after the route fix, over the numFound-545 shelf and the numFound-500 Q1 shelf: ~520 items
   with a text layer never grepped. Priority order: Popular Electronics Sep/Oct/Nov 1975
   (`popularelectroni08unse_1/_2/_3`), `byte-magazine-1977-08` ("Working with APL", the issue next to the
   held July APL letter), `Kilobaud197810`, `kilobaudmagazine-1980-04`, `197811PopularElectronics`.
3. **The `Traf-O-Data` pattern** — never searched on any shelf, and it is the only realistic route to
   pre-1975 founder activity in this corpus. Also untried: `Micro-Soft` hyphenated as a *primary* term
   against 1977-1982 serials (this pass only met it incidentally).
4. Stage 3 at all: **no query with a 1986-1990 window was run in any family.**
5. Family (d) title-scoped corporate-print variants and any Microsoft annual-report sold or deposited as a
   separate item; the four unopened rows named in §Family d (3).
6. Family (b) CDX re-run for microsoft.com's earliest capture; family (e) documentary in full (auction and
   museum routes, per the Apple precedent).
7. EDGAR *contents*: the corrected index enumerates but downloads nothing. Untried: the 1994-02-14 10-Q
   (accession 0000950109-94-000252, `primaryDocument` empty in the index), the 1994-09-27 10-K and its
   multi-year selected-financial table, and EDGAR full-text search 1994-1999 for any later filing that
   *narrates* the 1986 IPO or the 1975-1980 period in a prospectus or 10-K history section.
8. Whether `197503PopularElectronics`'s 493 KB contains the MITS licence/price terms that the Microsoft
   relationship ran through — only the Microsoft/MITS/Altair patterns were run against it, not a licence or
   royalty search.

