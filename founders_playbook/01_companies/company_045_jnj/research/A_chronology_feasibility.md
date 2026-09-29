# A — Chronology feasibility probe: Johnson & Johnson (company_045_jnj, rank 45)

**Owner:** probe-jnj (Stage-1 PROBE). **Run:** 2026-09-29, web budget 0 WebSearch / 0 WebFetch — every
byte below was reached through `tools/` scripts and read off local disk.
**Scope:** this file is a probe verdict only. It writes **no volume, no registers, no certification**.
**Origin window under test (from `tools/harvest_mine.py` WINDOWS):** `1886-01-01 → 1960-12-31`.
This is a **pure paper-archive verdict**: the window closes 34 years before the EDGAR floor and 36 years
before the first Wayback capture measured below, so nothing in Stage 1 can be settled by the two digital
families that carry every post-1994 company in this corpus.

---

## 1. Headline verdict

**Stage 1 is NOT a null company. It is a print company.** The filing floor is a hard zero for this window,
but two paper families answered, and they answered *inside* the window with company-authored text:

| | result |
|---|---|
| Families returning **in-window Tier-1 text** | **2 of 5** — (c) periodical corpora, (d) digitised corporate print |
| Family with a **documented in-window NULL** | (a) filings (route answered; zero rows in window) |
| Families **UNTRIED** | (b) web archives (measured as floor, see §3), (e) auction/museum documentary |
| Tier issued (RD-112: per stage, against that stage's window) | **Stage 1 = T2 core (PROVISIONAL)**, Stage 2/3 = not yet issuable |
| Entity namings held on disk | **619 lines** across 14 OCR layers / **23,275,060 B** of periodical text |

The single most load-bearing sentence found in this pass is **company-authored, in-window, and it does not
agree with the founding date in the brief** — see §5.1.

---

## 2. What is in-window and held

Final measured state of the protected archive (nothing under `sources/` was deleted or moved):

```
python -c "import os,glob; d='founders_playbook/01_companies/company_045_jnj/sources'; …"
```

* `sources/periodicals/` — **14 OCR text layers, 23,275,060 B** (+ 14 `.meta.json` sidecars).
* `sources/_index/` — 7 EDGAR index artefacts (submissions CSV/JSON/MD × CIK-keyed and generic names).
* **Total 35 files / 25,339,536 B.**
* **SEC document bytes held: 0.** Only the index exists; no accession body was fetched (§3).

Every periodical sidecar carries `"transport": "UNVERIFIED TLS -- re-check before citing at High
confidence"` (fleet default on this machine, whose CA store is stale — `tools/ia_text.py` INSECURE_HOSTS).
**Confidence cap:** no text below may be cited at High confidence on this pass. That is a property of our
transport, not of the record.

---

## 3. Family-by-family verdicts (a)–(e)

### (a) Filings — **documented in-window NULL; route ANSWERED**

```
python tools/sec_intake.py resolve --ticker JNJ
  -> {"ticker": "JNJ", "cik": 200406, "name": "JOHNSON & JOHNSON"}
python tools/sec_intake.py index --cik 200406 --ticker JNJ \
       --company-dir founders_playbook/01_companies/company_045_jnj
  -> index: 3371 filings from registrant 'JOHNSON & JOHNSON' (CIK 0000200406, tickers ['JNJ'])
  -> registrant guard = ok -- slug token(s) ['jnj'] match registrant 'JOHNSON & JOHNSON'
```

Enumerated the header before reading any field by name (RD-124):
`['filingDate','form','accession','reportDate','primaryDocument','source']` — **3,371 rows.**

| measure | value | command |
|---|---|---|
| earliest filing indexed | **1994-03-10** (DEF 14A, acc. 0000950110-94-000059) | `grep '^| DEF 14A' sources/_index/_INDEX_CIK0000200406.md`; earliest-10-K is 1994-04-01 |
| latest | 2026-09-10 | python `min/max` over `filingDate` |
| rows with `filingDate ≤ 1960-12-31` | **0** | python filter on `filingDate` |
| distinct forms | 65 | python `Counter(form)` |
| any form beginning `S-1` | **none — `{}`** | python prefix test on `Counter` |
| rows with no `primaryDocument` | 134 (paper-era shells) | script's own line |
| filing bodies downloaded | 0 — only `index` was run | byte count in §2 |

**Verdict.** This route *answered* (the submissions list returned and enumerated 3,371 filings), so the
zero inside 1886–1960 is a **NULL, not UNANSWERED** — a genuine statement about the record, and exactly the
§14-rule-6 wall ("EDGAR reaches essentially nothing before ~1994"). JNJ is old enough that its pre-1994
paper filings were never converted into this index; no S-1 exists here because JNJ never registered via
S-1 in the electronic era. **The 1886 founding act is not reachable through EDGAR, at any depth.**
The 1994 floor does *not* bound Stage 1 — it post-dates it by 34 years.

### (b) Web archives — **floor measured; in-window NULL by construction**

```
python -c "…urllib web.archive.org/cdx/search/cdx?url=…"
  www.jnj.com            -> earliest capture 19961018041147 (200)
  johnsonandjohnson.com  -> earliest capture 19980126060124 (200)
```

CDX **answered** (returned rows, HTTP 200), so this is not an UNANSWERED slice. Earliest capture is
**1996-10-18**, 36 years past the window's close. **No pre-1961 web-archive evidence is possible for this
company** — the family is a null for Stage 1 and a real (late) carrier for any post-1996 stage. Caveat:
two URLs were probed, not the archive; a 1996 floor for *the registrant's own domains* is not a floor for
every page mentioning JNJ. Not claimed as such.

### (c) Periodical corpora — **IN-WINDOW TIER-1 TEXT RETURNED** (the family that changes the verdict)

The carrier is the trade press the brief predicted. Found by scripted search, then **fetched and grepped as
bytes** (`tools/ia_text.py mine`, which exists precisely because advancedsearch `text:` matches annotations,
not pages — Microsoft's lesson):

```
python tools/ia_text.py mine --q 'title:("American Druggist") AND mediatype:texts AND YEAR:[1890 TO 1905]' \
       --pattern 'Johnson\s*&\s*Johnson|Johnson and Johnson' \
       --company-dir founders_playbook/01_companies/company_045_jnj --rows 6 --max-mb 10 --insecure
  -> 6 items: 6 TIER1_CANDIDATE, 0 NULL/LEAD, 0 UNANSWERED
```

Corpus-level availability of the trade press, from `tools/ia_text.py search` (numFound is *metadata-level*,
i.e. items in the archive, not hits inside them):

| query | numFound | in-window example |
|---|---|---|
| `title:("American Druggist") AND mediatype:texts` | **795** | 1896, 1902, 1904 volumes on disk |
| `title:("Pharmaceutical Era") AND mediatype:texts` | **44** | 1887 volumes exist, **not yet fetched** |
| `title:("Hardware and Sporting Goods") AND mediatype:texts` | **0** — answered zero | the brief's other carrier does not exist in IA |

Held in-window naming lines (verbatim, `sources/periodicals/`):

* `americandruggis29unkngoog` (1904) l.33894 — *"Richards as salesman. In 1887 he engaged with Johnson &"*
  / l.33895 *"Johnson and remained In their service until his death."* — third-party trade press placing
  the firm in existence **by 1887**, and l.33896 *"Johnson & Johnsan find it impossible to express their
  appreciation"*.
* `americandruggis07unkngoog` l.45597 — *"Robert Wood Johnson. The objects of"*
* `americandruggis29` l.36865 — *"in the offices of Johnson & Johnson. It"*
* `americandruggis29` l.25490 — *"of Johnson & Johnson, left here on the"*

**Verdict: family (c) is a live, in-window, externally-witnessed carrier, and it is barely begun** — 795
American Druggist items exist and 5 have been opened; 44 Pharmaceutical Era items (incl. **1887**, the
founding decade itself) are UNTRIED.

### (d) Digitised corporate print / annual reports — **IN-WINDOW TIER-1 TEXT RETURNED (strongest family)**

```
python tools/ia_text.py mine --q '("johnson & johnson" OR "johnson and johnson") AND mediatype:texts \
       AND YEAR:[1886 TO 1920]' --pattern 'Johnson\s*&\s*Johnson|Johnson and Johnson|New Brunswick' \
       --company-dir founders_playbook/01_companies/company_045_jnj --rows 8 --max-mb 10 --insecure
```

**A first attempt at this query returned `0 items` — because my shell-escaped quotes (`\"`) reached the
tool literally and produced a query matching nothing.** That zero was a quoting defect in my own invocation,
not a corpus null; re-run with correct quoting it returned the eight items below. Recorded as a defect (§6).

| item | yr | B held | naming lines | what it is |
|---|---|---|---|---|
| `redcrossnotes00johngoog` | 1900 (masthead: **"1897-1898 and 1899-1900"**, l.72) | 1,306,824 | **246** | company house organ, 99 × "New Brunswick", 69 × surgical dressings |
| `redcrossnotes01johngoog` | 1910 | 831,850 | **258** | same, "New Brunswick, N. J., U. S. A."; "the Johnson & Johnson laboratories" |
| `johnsonsfirstai00unkngoog` | 1903 (l.89); "Copyright, 1901, by Johnson & Johnson" (l.158) | 315,977 | 23 | company first-aid manual |
| `modernmethodsofa00john` | 1888 per metadata, **"1891" in the cover call number** | 131,553 | 16 | "Published by JOHNSON & JOHNSON, New York"; "JOHNSON & JOHNSON, 25 Cedar Street, New York" |
| `belladonnaastud00incgoog` | 1894 | 199,288 | 8 | names RWJ (see §5.2) |
| `asepsissecunduma00john` | 1897 | 59,972 | 10 | **authorship UNESTABLISHED** — title-page OCR is illegible in the first 200 lines |
| `americandruggis01/07/13/26/29`, `bub_gb_A9IAAAAAYAAJ` | 1893–1904 | 3.0–3.6 M each | 1–19 | third-party trade press |
| `alphabetfirstth00goog` | 1897 | 739,027 | **0** | **place-name trap, live**: 126 × "New Brunswick", **0** namings — a Canadian volume |
| `ErnestFairfield` | 1888 | 259,935 | **0** | noise pulled in by the same query |

**619 naming lines total** (`python -c` regex sweep `Johnson\s*&\s*Johnson|Johnson and Johnson`, case-I,
over all 14 layers). Two of the 14 fetched items carry **zero** namings — RD-124 confirmed by measurement:
being returned by a query is not being named by a document.

### (e) Auction / museum documentary records — **UNTRIED, and unimplemented in our tooling**

This is **family 4** in `tools/HARVEST_README.md`, which states it authoritatively:
`| 4 | (not implemented) | auction / museum / special-collections documentary records | **UNQUERIED — no API
verified; remains UNANSWERED, never null** |` and its "Known gaps" line 1: *"no read-only public API was
verified for it."* So there is **no command to run**, and that is a statement about us, not about the record
(§14 r6). Verified before asserting (RD-127):

```
find . -not -path "./.git/*" \( -iname "*auction*" -o -iname "*sotheby*" -o -iname "*christie*" -o -iname "*museum*" \) | wc -l
  -> 1   (company_002_walmart/sources/periodicals/walmart_museum_page.html)
```

**My first draft of this line said "no museum or auction artifact exists in the repository" — false.** A
sibling company holds a museum page, so a museum route has been touched by *some* pass, just never for JNJ
and never through a scripted, repeatable API. **Zero JNJ artifacts on this family; the family is UNTRIED,
not null.** Apple's founding documents survived *only* on this class of record, so for an 1886 company it
remains the highest-value door we cannot presently open.

---

## 4. Per-stage tiers (RD-112: one tier per stage, against that stage's own window)

**RD-116 planning rule applied: a company's planning tier is the minimum across its stages.**

| stage | window | families with in-window Tier-1 text | **tier** | §15.2 run budget | cap |
|---|---|---|---|---|---|
| **Stage 1** | **1886-01-01 → 1960-12-31** (given) | **(c) + (d) = 2** | **T2 core — PROVISIONAL** | **6–9 agent runs** | 22k w/stage |
| **Stage 2** | **NOT SETTABLE BY THIS PROBE** — see below | 1 ((a) only, from 1994-03-10) | **T3 register if placed in 1961–1993; T2 if it touches ≥1994** | 3–4 (1961–93) / 6–9 (≥1994) | 8k / 22k |
| **Stage 3** | **NOT SETTABLE BY THIS PROBE** | 2 ((a)+(b) post-1996; (a) alone 1994–96) | **T3, provisional** | 3–4 | 8k w/stage |

Why **T2 and not T1** for Stage 1, stated exactly: §15.2 needs **≥3 families** returning in-window Tier-1
text. Here (a) is a documented null, (b) is impossible, (e) is untried — so **2 families is 2 families**,
and ambition does not close the gap. Why **not T3**: T3 is ≤1 family, and this window has two, one of them
(*Red Cross Notes* 1897–1900) carrying **494 naming lines in a single pair of company-authored volumes** —
which is more in-window company voice than Walmart or Target has at any date.

Why **PROVISIONAL**, and what would move it: `candidates.csv` carries **8 jnj rows, all 8 UNANSWERED with
empty `http_status` and empty `item_id`** — i.e. *no jnj query was ever answered; every one was skipped*
(`SKIPPED: global max-requests cap` × 7, `SKIPPED: hard stop: 5 consecutive` × 1). Against a fleet holding
1,691 `TIER1_CANDIDATE` rows, JNJ has **zero metadata candidates**. So the two families that returned above
returned on *my ad-hoc scripted probes*, not on a fleet run. The tier is provisional until the block is
executed (§7). **Family (e) untried and family (c) 99% unopened are the two doors; neither is a null.**

---

## 5. Load-bearing open questions

### 5.1 The founding act and date — 1886 vs the incorporation date

**Best in-window document, company-authored, verbatim** (`redcrossnotes00johngoog`, house organ, masthead
"1897-1898 and 1899-1900", l.9283–9285):

> *"In the years previous to 1886-\*87 (the date of the formation of the firm of Johnson & Johnson)
> antisepsis had made but little progress."*

and l.9300–9301, same passage: *"To meet this want Johnson & Johnson devised a system of dressings made to
fill the demand of the best surgical practice."*

**OCR fidelity note (read before quoting this line onward).** The bytes read, exactly:
`In the years previous to 1886-*87 (the` / `date of the formation of the firm of` /
`Johnson & Johnson) antisepsis had made` — l.9283–9285. The `*` is an **OCR artefact standing where an
apostrophe or dash was printed**; where this dossier writes `1886-'87` in prose it is **our reading of the
artefact, not the bytes**. The literal string `1886-'87` occurs **zero** times in held bytes. Quote the
asterisk form or mark the substitution.

This is the strongest founding statement in the corpus and it does three things at once:

1. It **supports 1886** — but as **"1886-'87"**, a *range*, in a document written **11–14 years after the
   event**. It is company self-narrative, retrospective, and not contemporaneous with 1886.
2. It names the **act** as "formation of the **firm**" — a firm, not a corporation.
3. It is **anonymous as to persons**: no founder is named in the formation sentence.

Second witness, different lineage and *nearer* the date, but with a **date conflict**:
`modernmethodsofa00john` prints *"JOHNSON & JOHNSON, 25 Cedar Street, New York"*. The search index says
**1888**; the cover OCR carries **"1 891"** inside the library call number (`RD1 31 J63 1 891`). RD-121 in
live form: **the item's date is UNCONFIRMED** and must not be written as 1888. What it *does* establish,
subject to that conflict, is a **New York imprint address, not New Brunswick** — while `redcrossnotes00`
l.6741 says *"to visit our factory at New Brunswick"*. So the sequence is: New York address in print →
New Brunswick factory in company print, and **the move date is UNKNOWN — no held document dates it.**

**Incorporation:** tested directly and **not found** —
`python -c` pattern `Johnson\s*&\s*Johnson[^.]{0,60}incorporat|incorporat[^.]{0,60}Johnson\s*&\s*Johnson`
over all 14 layers → **0 lines.** The only corporate-form statement held is `belladonnaastud00incgoog`
l.185, *"Johnson & Johnson Corporation"* (1894), which is an *entity form in a printed notice*, not an
incorporation record. **The 1886-vs-incorporation question stays OPEN, and no NJ charter is in the corpus.**

### 5.2 Who is credited as founder, and by which document

**Earle Dickson — 0 lines** in held bytes (`Earle\s+Dickson` sweep, 14 layers / 23.3 MB). A NULL **over
held KB only**, not a finding about the record: 1886–1910 print does not carry the Band-Aid story, and the
sweep covers 5 of 795 Druggist items.
**Band-Aid — 0 lines** (`Band[\s-]*A[\s-]*id`). The product does not exist yet in the held window.
**Miles Stone — 0; James Wood — 0.** **Robert Wood Johnson — 3 lines**, of which the load-bearing one is
`belladonnaastud00incgoog` (1894) l.184–185, verbatim:

> *"Making Belladonna Plasters, ROBERT WOOD JOHNSON, Manufacturing Chemist, President"* / *"Johnson & Johnson Corporation."*

**Read that for exactly what it says.** It is an in-window printed naming of a man with an office against
this company — *a role recorded in a document, which is not a founding claim.* **No document in the corpus
calls anyone a founder.** The three-brothers story in the brief is company self-narrative that this pass
found **no in-window carrier for**; it must not be written as if it did.

### 5.3 First real experiment — the surgical antiseptic product and its first adoption

Best candidate is the *Red Cross Notes* passage itself: dressings devised "to meet this want", against a
background where *"dressings obtainable by the great bulk of practitioners … were for the most part wholly
unreliable"* (l.9288–9294). `redcrossnotes00` carries **69 lines** matching `Surgical (Antiseptic|Dressing*)`.
**What is missing: an adoption event.** No held line names a first hospital, surgeon, or institutional
purchase. The *first* institutional claim held is retrospective and unquantified — see §5.4 (Army and Navy).
**The first real experiment's date, place and first customer are UNKNOWN.**

### 5.4 First repeatable validation — strongest evidence found in the pass

`johnsonsfirstai00unkngoog` (company-authored, l.89 "1903", l.158 "Copyright, 1901, by Johnson & Johnson"):

* l.2371 — dressings *"supplied by Johnson & Johnson to the U. S. Government for the use of the Army and Navy"*
* l.2386 — *"the special endorsement of thousands of railroad, mining and factory surgeons, as well as those connected with fire, police and municipal departments"*
* l.2397–2400 — *"Upwards of seven thousand Johnson's First Aid Cabinets are in use in manufacturing establishments. It has been adopted by several of our chief Railroad Systems as a shop first aid equipment. Boards of Education in many cities have placed this cabinet in the public schools and adopted Johnson's First Aid Manual as a text book"*
* l.2405 — *"Johnson's First Aid Cabinet sells for $6.00"*
* l.2389–2391 — *"universally recognized as the pioneers and leaders in the making of surgical dressings"*
* l.2409 — product lineage: *"the original Johnson's Accident Case"* → First Aid Cabinet

**This is a real, in-window, dated, quantified adoption series — with one fatal qualifier: every line is
one company talking about itself.** *Seven thousand cabinets* is **one lineage**, not a corroborated count
(Walmart's five Kentucky reiterations, RD-097). An independent count of installed cabinets is **UNTRIED**:
the route is the 795-item Druggist corpus plus the 44 Pharmaceutical Era volumes. **Also note the
"plaster bandage" premise in the brief is not satisfied here** — held bytes validate the *First Aid
Cabinet/Manual* system, not a plaster bandage.

### 5.5 The first incurred failure

**None established. UNKNOWN.** No held line records a recall, seizure, refusal, fire, loss or withdrawal.
The nearest thing to a negative in the corpus is a *competitor's* complaint, not ours. Do not let the
absence become a narrative of smooth ascent: §15.2 requires `data_gaps.csv` and an UNTRIED list at every
tier, and failure is precisely the claim class most likely to live in an unopened volume (trade-press
litigation notices, pure-food/drug enforcement reports) rather than in house print.

### 5.6 Listerine — a vocabulary trap, tested explicitly

**Listerine: 13 lines** in held in-window bytes (`americandruggis01/07/29`). Read them: *"Listerine toilet
soap, which sells at $12 a gross to the trade"*, *"Listerine Dermatic Soap"*, *"Peruna, Paine's Celery,
Plnkham's Comp. and Listerine"*. **Zero of those 13 lines names Johnson & Johnson as Listerine's proprietor.**
A product appearing in the trade press is a lead about a product, not a naming of this registrant (RD-124).
**The Listerine-to-J&J link is UNESTABLISHED in held bytes** and stays open.

---

## 6. Defects recorded (not worked around)

1. **The briefed filings command is invalid.** `python tools/sec_intake.py auto "Johnson & Johnson" \
   --company-dir …` → `error: unrecognized arguments: Johnson & Johnson`. `auto` accepts **no positional
   name**; identity is `--cik` or `--ticker` ("need --cik or --ticker", `tools/sec_intake.py` line ~1185).
   The brief's own `--company-dir`-plus-name form cannot run. Used the documented `resolve`/`index` pair.
2. **`sec_intake.py selftest` = 42 checks, 0 failing** — confirmed by count (`grep -c "PASS\|FAIL"` → 42)
   and by its own summary line. No defect in the detector.
3. **`harvest_mine.py --self-test` = 6 checks, 0 failing** — the RD-124 negative controls hold.
4. **`harvest_mine.py --company jnj --limit 10` printed `{}` and exit 0.** Correct behaviour (zero
   mine-able candidates), but it *looks* like a completed mine. A zero-candidate run should say so.
5. **All 8 jnj candidate rows are skips, not answers** — `http_status` empty, `item_id` empty, snippet
   `SKIPPED: global max-requests cap` / `SKIPPED: hard stop: 5 consecutive`. The fleet runner never
   reached JNJ. **JNJ has 0 metadata candidates against a fleet's 1,691.**
6. **`tools/queries.json` DOES have a real jnj block — 8 tasks** (`tasks` list, 427 items, 50 companies).
   The brief's conditional ("if no real jnj block → report family (c) UNTRIED") **does not fire**. The
   correct statement is: *written but never executed*.
7. **The block's own trade-press query returns 0 as answered-zero, and its shape is the cause.**
   `(title:("Pharmaceutical Era") OR …) AND Johnson AND mediatype:texts AND YEAR:[1880 TO 1970]` → **0 of 0**,
   while `title:("Pharmaceutical Era") AND mediatype:texts` alone → **44**. The bare `AND Johnson`
   conjunction kills it. Also **American Druggist — the single richest carrier, 795 items — is not in the
   block at all**, and `Earle Dickson`, `Band-Aid`, `Listerine` appear **0 times** in `queries.json`.
   The block's `company_terms` include bare **`jnj`** — the RD-124 poor-grep term, flagged in the brief.
8. **`ia_text.search` hardcodes `sort[]=downloads desc`**, so `("Johnson & Johnson")` unfiltered returns TV
   commercials and Grateful Dead shows (numFound 28,683) instead of in-window print. Year facets are the
   only defence. Mine-quality defect in the fleet's IA route.
9. **My own quoting defect** — see §3(d): escaped quotes produced a false `0 items`. Kept as a negative
   artefact so the next agent recognises the shape.
10. **`index` wrote both CIK-keyed and generic artefacts** (`submissions.csv` + `submissions_CIK0000200406.csv`,
    both 306,130 B). CIK-keying is the RD-098 fix; the duplicate generic pair is unexplained and is a
    corruption vector if a later pass reads the generic name. **Not deleted** (protected archive).
11. **Transport is UNVERIFIED TLS for every held OCR byte** — see §2 confidence cap.
12. **One of this probe's own absence claims was false, and the RD-127 test caught it.** My first §3(e)
    asserted no auction/museum artifact exists anywhere in the repository; `find` returned **1**
    (`company_002_walmart/sources/periodicals/walmart_museum_page.html`) and `tools/HARVEST_README.md`
    documents family 4 as *"(not implemented) … UNQUERIED … remains UNANSWERED, never null"*. Corrected in
    §3(e) above. **Second occurrence of this exact class in the corpus, and the discipline that catches it
    is the one that says: run the `find` before you write "none".**

---

## Untried (§7)

Per route, with the command that would run it. **No item below is a null.**

1. **Fleet harvest for jnj — the 8 written tasks, never executed.** Highest-value single command:
   `python tools/periodical_harvest.py --company jnj` (then `python tools/harvest_mine.py --company jnj --limit 20`).
2. **The rest of the trade press — 790 unopened American Druggist items, 44 Pharmaceutical Era incl. 1887:**
   `python tools/ia_text.py mine --q 'title:("Pharmaceutical Era") AND mediatype:texts AND YEAR:[1886 TO 1895]' --pattern 'Johnson\s*&\s*Johnson|New Brunswick' --company-dir founders_playbook/01_companies/company_045_jnj --rows 8 --max-mb 10 --insecure`
3. **Earle Dickson / Band-Aid at the item level (metadata answered 0 for the phrase, but full text unsearched):**
   `python tools/ia_text.py search --q '"Dickson" AND "New Brunswick" AND mediatype:texts AND YEAR:[1920 TO 1935]' --insecure`
4. **New Jersey state archives / Secretary of State charter — the incorporation question.** No tool reaches
   it; **UNTRIED, no command in `tools/`.**
5. **HathiTrust for the J&J phrase** — fleet-side precedent (RD-127) is that the first result page returns
   no pre-1990 imprint *for Walmart*; **never measured for jnj**. Body is not in the repo for this slug.
6. **Google Books / corporate print beyond 1920** — the block's `CP jnj annual/shareholder print 1886-1980`
   was skipped; `python tools/periodical_harvest.py --family corporate_print --company jnj`.
7. **Chronicling America — still UNTRIED, and the brief's warning is now MEASURED.**
   `founders_playbook/00_universe/harvest/_CA_ENDPOINT_TEST.md`, verdict 2026-09-29T17:53:03Z: **7 shapes
   tried, 0 ANSWERED, all 7 CHALLENGED (403, Cloudflare, 5,871–6,224 B each)** — including the shape the
   nightly runner 404s on. The probe landed, and it did **not** produce a working path: from CI egress the
   route is now a bot challenge rather than a 404, so RD-128's "wrong-path defect" resolves to *egress
   block on all seven shapes*. Per the probe's own reading key, `CHALLENGED` = "Still UNANSWERED, never a
   null, and it does not mean the path is wrong." **Every CA zero for jnj remains UNANSWERED, and no CA
   count may be cited as a null.** Command when egress changes: `python tools/ca_endpoint_probe.py`.
8. **Auction / museum documentary records (family 4) — no command exists to run.** `tools/HARVEST_README.md`
   records it as *"(not implemented) … no read-only public API was verified"*, and no JNJ artifact is on this
   family (1 repo-wide museum artifact exists, at Walmart). This route needs a tool, not an agent.
9. **XBRL early financial series** — irrelevant to Stage 1 (facts floor 1994) but unrun for Stages 2/3:
   `python tools/sec_intake.py facts --cik 200406 --company-dir founders_playbook/01_companies/company_045_jnj --from 1994-01-01 --to 1999-12-31`
10. **EDGAR document bodies 1994–1999** — `index` only; nothing fetched. Needed for Stage 2/3, not Stage 1:
    `python tools/sec_intake.py auto --cik 200406 --company-dir founders_playbook/01_companies/company_045_jnj --from 1994-01-01 --to 1999-12-31 --max-docs 40`

---

## 8. What this probe refuses to claim

* **Not** that JNJ was founded in 1886. The best held statement says *"1886-'87 (the date of the formation
  of the firm)"* in a **1897–1900 retrospective**. 1886 is the **company's own range**, not a verified date.
* **Not** that any person founded it. One held line gives Robert Wood Johnson a title (1894); **a role in a
  document is not a founding claim**, and no held line makes a founding claim for any of the three brothers.
* **Not** the 1888 date of `modernmethodsofa00john` — metadata and cover disagree (1888 vs "1891").
* **Not** that Listerine, Band-Aid or Earle Dickson belong to this company's in-window story: the first has
  no proprietor naming in held bytes, the other two have **zero** lines.
* **Not** that the 7,000-cabinet figure is corroborated — one lineage, company self-narrative.
* **Not** that any family's zero is a null except where the route *answered*: only (a) filings, (b) web
  archives (floor), and the two answered-zero queries in §3(c)/§6(7) qualify. **(e) is UNTRIED; (c) is 99%
  unopened; CA is UNANSWERED.**
* **Not** a Stage 2 or Stage 3 tier as settled: those windows are not settable from held evidence, and a
  tier against an unset window is not a tier (RD-112).
* **Not** a T1, despite a rich print corpus: §15.2 counts families, and two families is two.

**Route most likely to change this verdict:** executing the existing jnj block (#1) and the **Pharmaceutical
Era 1886–1895 fetch (#2)** — 1887 print sits inside the founding decade and is *unopened*. If either names
the firm at 1886–1889 in a **third-party** carrier, (c) hardens from ad-hoc probe to fleet-documented, a
contemporaneous founding witness exists at last, and the two-lineage test finally has something to test.
