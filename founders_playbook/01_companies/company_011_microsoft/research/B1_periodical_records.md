# B1_periodical_records.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:23:45Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Intake re-run

STATUS: WRITTEN 2026-09-25

## Layers held

STATUS: WRITTEN (msft-s1-records)

Every figure below is a `stat`/`wc -c` of a file on disk this session, not a catalogue count. Three
shelves are in scope; two of them belong to sibling companies and are **read-only to me** (§14 rule 4 —
grepped in place, nothing copied, moved or edited).

| shelf | owner | layers | bytes | span |
|---|---|---|---|---|
| `company_011_microsoft/sources/periodicals/` | this company | 8 OCR text layers | **5,725,436 B** | 1975-03 → 1988-08 |
| `company_004_apple/sources/` (`ia_byte_1976` ×12, `ia_byte_1977` ×4, `ia_byte_1981` ×2, `ia_homebrew` ×13) | Apple dossier | 31 | **12,394,678 B** | 1975-11 → 1981-02 |
| `company_041_dell/sources/periodicals/` (BYTE 1987-04, 1988-03, 1988-10, 1988-12) | Dell dossier | 4 | **7,392,281 B** | 1987 → 1988 |
| **total mined this session** | | **43 layers** | **25,512,395 B** | 1975-03 → 1988-12 |

Microsoft-shelf layers, with size and the date each carries on its own face:

| file | bytes | date on the face | window |
|---|---|---|---|
| `197503PopularElectronics_djvu.txt` | 493,273 | March 1975 (masthead) | Stage 1 |
| `197602-modern-data_djvu.txt` | 261,075 | February 1976 | Stage 1 |
| `kilobaudmagazine-1977-05_djvu.txt` | 672,171 | May 1977 | Stage 1 |
| `1979-Fall-compute-magazine_djvu.txt` | 542,112 | 1979 (issue 001) | Stage 1 |
| `byte-magazine-1986-01_djvu.txt` | 1,850,712 | "JANUARY 1986 VOL. 11, NO. 1" | **Stage 3** |
| `byte-magazine-1988-08_djvu.txt` | 1,888,699 | "AUGUST 1988" | **Stage 3** |
| `MSDOS2FuturePlansForMSDOSByPaulAllen_djvu.txt` | 13,639 | **none on face** (catalogue year 1982) | Stage 2 |
| `1981-microsoft-adventure_djvu.txt` | 3,755 | undated; names the IBM PC | Stage 2 |

Apple-shelf layers used this session (Homebrew is the load-bearing set): `hcc0109` 15,563 B, `hcc0110`
20,193 B, `hcc0201` 28,281 B, `hcc0202` 43,265 B, `hcc0203` 23,686 B, `hcc0204` 30,810 B, `hcc0205`
35,736 B, `hcc0206` 38,832 B, `hcc0207` 37,012 B, `hcc0209` 37,903 B, `hcc0211` 50,597 B, `hcc0213`
35,862 B, `hcccf` 8,071 B; Byte 1976 all twelve issues (360,313–596,030 B each), Byte 1977-04/05/06/07
(681,968 / 727,344 / 796,910 / 751,638 B), `byte-1980-12` 1,669,716 B, `byte-1981-02` 1,617,655 B.
Homebrew issues 0208, 0210, 0212 are **absent from the shelf** — a coverage hole, not a null.

TLS status: the two Stage-3 layers carry `"transport": "UNVERIFIED TLS"` in their `.meta.json` sidecars
(`byte-magazine-1986-01`, `byte-magazine-1988-08`), as do the earlier hand-fetched layers. **Unverified
bytes cap at Medium** regardless of how well they read; the masthead/date checks above are content checks
against those bytes, not corroboration of their transport.

## Origin window

STATUS: WRITTEN (msft-s1-records)

**I do not contest the 1975-1980 window; I narrow what it can be said to contain.**

- **Earliest date any held byte carries about this company: 1976-01-31** — `hcc0201`, Homebrew Computer
  Club Newsletter "Volume Number 2, Issue 1 January 31, 1976", whose page-2 letter signs off
  "Bill Gates / General Partner, Micro-Soft". Verified on disk this session (lines 17-20 editor's note,
  88-111 letter body, 121-129 signature block, at
  `company_004_apple/sources/ia_homebrew/hcc0201.txt`, 28,281 B).
- **1975 is a documented name-vacuity, not an unopened shelf.** Over bytes I grepped myself this session:
  `hcc0109` (15,563 B, masthead "Volume Number 1, Issue 9 November 30, 1975") and `hcc0110` (20,193 B,
  "December 31, 1975") → **0** occurrences of `micro-soft`, **0** of `microsoft`, **0** of the word `gates`,
  **0** of `paul allen`. `197503PopularElectronics_djvu.txt` (493,273 B) → **0** of `micro-soft`.
  All twelve BYTE 1976 issues (360,313-596,030 B, 5,343,636 B total) → **0** occurrences of `micro-?soft`.
- **The stage therefore opens in print on 1976-01-31 and its first-year content is 1976-1980, not
  1975-1980.** 1975 remains inside the stage as the company's *own claimed* starting year, sourced only
  retrospectively: "Almost a year ago, Paul Allen and myself, expecting the hobby market to expand, hired
  Monte Davidoff and developed Altair BASIC" — printed January 1976, i.e. a company self-report reaching
  backwards, so under §6 every line drawn from it is `RETROSPECTIVE SOURCE`. The 1975 MITS/Altair
  *environment* is independently in print (`197503PopularElectronics`), but that document carries no
  Microsoft content and may not be cited for one.
- **Close: 1980-12 is documentary, not arbitrary.** `byte-1980-12` (1,669,716 B) carries **134 matching
  lines** on `micro-?soft` and a company-supplied imprint block: "MICROSOFT Consumer Products, 400 108th
  Ave. N.E., Suite 200, Bellevue, WA 98004. (206) 454-1315." A 1980-12-31 Stage-1 close stands.
- **Stage 3 is no longer empty** (see §Stage 3 attempt): 3,739,411 B of BYTE 1986-01/1988-08 held in this
  company's own `sources/` plus 7,392,278 B of BYTE 1987-04/1988-03/1988-10/1988-12 on the Dell shelf. The
  probe's "zero documents in any family" for 1986-1990 is refuted for family (c).

## 1975-1976 records

STATUS: WRITTEN (msft-s1-records)

Nine records, each built only from bytes read this session. `R`-ids are dossier-local (§13). Passages are
typed exactly as they appear in the held OCR, OCR damage included; where the damage changes a character I
mark it `[sic]` rather than silently repairing it. **One normalisation is applied and disclosed:** BYTE and
Compute! OCR carries doubled inter-word spaces, so quotations from those titles are checked and printed
with single spacing (`re.sub(r'\s+',' ')`); no word is added, removed or reordered. All 28 passages cited
in this dossier were re-verified programmatically against the source files at close-out: **0 misses.**
URLs are the Internet Archive item behind the held
bytes (route recorded in `company_004_apple/sources/_RETRIEVAL_LOG.md` line 25: `metadata/<id>` →
`https://<server><dir>/<name>_djvu.txt`). **All Homebrew/Byte 1976-1981 bytes carry unverified TLS provenance
inherited from their fetching run; §Layers held caps these at Medium.**

```
R01 Claim: An entity styled "Micro-Soft", whose named officer was a "General Partner", existed and put its
own product account into print in January 1976 — Date: 1976-01-31 — Source: "A Letter from MITS" /
newsletter body, Homebrew Computer Club Newsletter Vol. 2 No. 1 — Source date: 1976-01-31 — URL:
https://archive.org/details/hcc0201 (local bytes company_004_apple/sources/ia_homebrew/hcc0201.txt,
28,281 B, lines 121-129) — Archived: — — Tier: 1 — Class: FACT — Passage: "Bill Gates / General Partner,
Micro-Soft" — Conf: Medium — Corroboration: 2 lineages (see R08) — Conflicts: None
```

```
R02 Claim: The company's own 1976 print dates its start to "almost a year ago" and names three people as
the origin — Date: 1976-01-31 (statement about c. 1975) — Source: Gates letter, HCC Newsletter V2N1 —
Source date: 1976-01-31 — URL: https://archive.org/details/hcc0201 (lines 83-88) — Archived: — — Tier: 1 —
Class: FOUNDER CLAIM, retrospective-in-print — Passage: "Almost a year ago, Paul Allen and myself,
expecting the hobby market to expand, hired Monte Davidoff and developed Alt air BASIC [sic: OCR for
"Altair"]" — Conf: Medium — Corroboration: 1 lineage; the 1994 10-K (R08) corroborates the YEAR only, not
the three persons — Conflicts: U-1
```

```
R03 Claim: The same letter reports the product line, the sunk computer time, and the royalty outcome —
Date: 1976-01-31 — Source: Gates letter, HCC Newsletter V2N1 — Source date: 1976-01-31 — URL:
https://archive.org/details/hcc0201 (lines 88, 93, 95) — Archived: — — Tier: 1 — Class: FOUNDER CLAIM
(contemporaneous self-report, unaudited) — Passage: "The value of the computer time we have used exceeds
$40,000." / "less than 10% of all Altair owners have bought BASIC" / "worth less than §2 [sic: $] an hour" —
Conf: Medium — Corroboration: 0 independent — no count, ledger or filing behind any of the three figures
exists in any family this project can reach — Conflicts: None
```

```
R04 Claim: The club printed the letter as an unusual item and reproduced it from a MITS channel — Date:
1976-01-31 — Source: editor's note "A LETTER FROM MITS", HCC Newsletter V2N1 — Source date: 1976-01-31 —
URL: https://archive.org/details/hcc0201 (lines 17-20) — Archived: — — Tier: 3 — Class: CONTEMPORANEOUS
OBSERVATION — Passage: "Just as the Newsletter was in final preparation a letter arrived from Bill Gates
via MITS. Reproduced (the only MITS "software" we have ever reproduced) on page 2" — Conf: Medium —
Corroboration: 1 — Conflicts: None
```

```
R05 Claim: Gates's reply address in the same letter is a New Mexico residential-style PO address, not a
company office — Date: 1976-01-31 — Source: Gates letter, HCC Newsletter V2N1 — Source date: 1976-01-31 —
URL: https://archive.org/details/hcc0201 (lines 121-123) — Archived: — — Tier: 1 — Class: FACT — Passage:
"Just write me at 1180 Alvarado SE, #114, Albuquerque, New Mexico, 87108." — Conf: Medium — Corroboration:
1 (repeated verbatim as the addressee block in hcc0202 = same lineage) — Conflicts: None
```

```
R06 Claim: The club then printed hostile replies, so the 1976 piracy dispute is a two-sided printed
record, not a company monologue — Date: 1976-02-29 and 1976-04-30 — Source: HCC Newsletter V2N2 and V2N4 —
Source date: 1976-02-29 / 1976-04-30 — URL: https://archive.org/details/hcc0202 (lines 87-99),
https://archive.org/details/hcc0204 (line 1863) — Archived: — — Tier: 3 — Class: CONTEMPORANEOUS
OBSERVATION — Passage: "Regarding your Letter of 3 February 1976 Appearing in Homebrew Computer Club
Newsletter Vol. 2 No. 1 … You gave it away; none stole it from you." / "since Mr. Bill Gates claims that he
did not get payed [sic] enough and is in the mood of calling people thieves. (See HBCC newsletter V2-1.)" —
Conf: Medium — Corroboration: 2 independent (unrelated club members) — Conflicts: None
```

```
R07 Claim: A third club member published a paying customer's account that fixes a price and a bundling
condition — Date: 1976-03-31 — Source: "Dear Mr. Gates" reader letter, HCC Newsletter V2N3 — Source date:
1976-03-31 — URL: https://archive.org/details/hcc0203 (line 182 onward) — Archived: — — Tier: 3 — Class:
CONTEMPORANEOUS OBSERVATION — Passage: "I am one of the 10% minority who paid for Altair 8K BASIC." /
"I have no objection to legitimately paying $75 for 8K BASIC, or to being required to purchase suitable
hardware in order to qualify for that price." — Conf: Medium — Corroboration: 1, and the "10%" is
*answering* R03 so it is not an independent count of the paid fraction — Conflicts: U-2
```

```
R08 Claim: Fourteen years later, in a filed document, the registrant states its own origin as a 1975
partnership incorporated in 1981, and names Paul Allen as co-founder — Date: 1994-09-27 (about 1975-1981) —
Source: Microsoft Corporation Form 10-K, accession 0000891020-94-000175 — Source date: 1994-09-27 — URL:
https://www.sec.gov/Archives/edgar/data/0000789019/000089102094000175/0000891020-94-000175.txt (local bytes
442,763 B, lines 181-182 and 975-977) — Archived: — — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION
(company self-report in a filed document, `RETROSPECTIVE SOURCE` per §6) — Passage: "Microsoft Corporation
(the "Company" or "Microsoft") was founded as a partnership in 1975 and was incorporated in 1981." /
"From 1975 to 1981, Mr. Gates was a partner with Paul Allen, Microsoft's other founder, in the predecessor
partnership." — Conf: High — Corroboration: 2 independent lineages (a 1994 SEC accession is not derived
from a 1976 club newsletter; R01's "General Partner" is the contemporary-side match) — Conflicts: U-1
```

```
R09 Claim: The letter's 1976 circulation across other titles is documented by a third party, and it is a
reprinting chain, not nine independent reports — Date: 1976-07 / 1976-09 — Source: BYTE Jul 1976 and Sep
1976 — Source date: 1976-07-01 / 1976-09-01 — URL: https://archive.org/details/byte-1976-07 and
byte-1976-09 (local: company_004_apple/sources/ia_byte_1976/byte-1976-07.txt 487,633 B line 31468;
byte-1976-09.txt 527,921 B line ~2039) — Archived: — — Tier: 3 — Class: CONTEMPORANEOUS OBSERVATION —
Passage: "Bill Gates' "An Open Letter to Hobby-ists" very clearly explained one of the chief problems of
the hobby computer industry, the low Return on Investment" / "it now appears that more copies of Altair's
BASIC have been pirated than have been legally sold." — Conf: Medium — Corroboration: **1** — this is
BYTE restating the same letter; counted as a publication-footprint fact, never as a second source for its
content — Conflicts: None
```

## Circle and partnership form

STATUS: WRITTEN (msft-s1-records)

**What the in-window print establishes.** The only in-window document naming an officer style is R01: the
entity is signed into print as **"Micro-Soft"** with Gates as **"General Partner"**, at an Albuquerque,
New Mexico reply address (R05), describing itself in the first person plural. A second, independent
in-window document — BYTE July 1977, a reader's letter (not company copy) — uses the same hyphenated form
fourteen months later: "While the **Micro-Soft** venture into APL represents a noble undertaking, it
nevertheless embodies the faulty reason-" (`ia_byte_1977/byte-1977-07.txt`, line 27113). So the hyphenated
name is not just a company self-styling; by mid-1977 third-party print carries it too.

**What the 1980 close establishes about entity plurality.** `byte-1980-12` carries a company-supplied
imprint naming a *different* entity: "MICROSOFT Consumer Products, 400 108th Ave. N.E., Suite 200,
Bellevue, WA 98004. (206) 454-1315." with "SoftCard is a trademark of Microsoft." In the same window, the
Windows advertisement in `byte-magazine-1986-01` names **"Microsoft Corporation / Bellevue, Washington
USA"** plus seven further national entities (GmbH/Pty/Ltd/Canada Inc/AB/SARL) and "ONIX Microsoft"
(Seoul). Between 1976 and 1986 the printed entity set goes from one hyphenated general partnership to a
named corporation with a multi-country family — that transition is visible in the corpus and is the
strongest structural spine Stage 1/Stage 3 can offer.

**What these lines do NOT establish — stated narrowly, because this is where folklore enters.**

1. **"General Partner" does not establish that Micro-Soft was a general partnership as a matter of law.**
   No partnership agreement, no certificate of limited partnership, no registry entry and no court record
   is held anywhere in the five families; family (a) is floored at 1994-02-14 and family (e) is UNTRIED.
   The signature block shows a *role title a person chose for his own letter*. The legal form is only
   *consistent with* what a 1994 filing later asserts (R08), and that assertion is itself retrospective.
2. **It does not establish who the other partner(s) were, nor the partnership's terms.** R02 names Paul
   Allen and Monte Davidoff in a sentence about hiring and development, not about ownership; no held byte
   states capital contributions, profit shares, or a formation date. The word "formation" appears in zero
   Microsoft-relevant bytes this session.
3. **It does not establish 1975 as a founding year.** R02's "almost a year ago" is a company
   retrospective, and R08's "founded as a partnership in 1975" is a 1994 retrospective in a different
   lineage — **two retrospectives, both post-dating the event, and zero contemporaneous documents dated
   1975 that mention the company at all** (Byte 1976 ×12, Homebrew 0109/0110, `197503PopularElectronics`:
   all 0 hits, §Origin window).
4. **The Micro-Soft/Microsoft naming line is not evidence of a re-incorporation or a renaming event.** No
   document in this corpus prints a decision to drop the hyphen. What the bytes show is **orthographic
   drift in print**: hyphenated in the company's own 1976 letter and in a 1977 BYTE reader letter, and
   unhyphenated as the dominant form in Byte Dec 1980 (134 matching lines on `micro-?soft`, of which
   **0** carry the literal hyphen) and Feb 1981 (65 lines, **1** hyphenated) — while a third party still
   wrote "Micro-Soft" as late as BYTE April 1987 ("Watch out Micro-Soft.",
   `company_041_dell/sources/periodicals/byte-magazine-1987-04_djvu.txt` line 96074; 1 hyphenated line of
   200). BYTE 1986-01 and 1988-08: 185 and 254 matching lines, **0** hyphenated. Any claim of a dated name change is a fill, not a finding.
5. **"Microsoft Consumer Products" (1980) and "ONIX Microsoft" (1986) must not be read as proven
   subsidiaries.** Both appear inside company-supplied advertising copy, which is self-narrative (§3), and
   the ad gives no corporate relationship. ONIX is a *distributor* name pattern; treating either as a
   filing-grade subsidiary claim is unsupported.
6. **The 1981 incorporation in R08 is a Stage-2-relevant fact from a Stage-3-tailed source.** It may be
   used to date the incorporation *only* as a filed retrospective statement, with confidence High for "the
   registrant says so in 1994" and Medium for "an incorporation occurred in 1981".

**Independence ruling carried forward.** R01/R02/R03/R04/R05 are **one document** — five facts, one
lineage. R09 is BYTE restating R01's content. R06/R07 are genuinely independent club members, but they
*react to* R01, so their testimony about the letter's existence is derivative while their testimony about
their own conduct (paying $75, refusing to) is independent. R08 is the only independent lineage touching
the founding years, and it is 1994 print about 1975.

## Register rows

STATUS: WRITTEN (msft-s1-records) — for the merge pass only; no existing CSV was opened for writing.

`source_id` values below (`D01`…) are **dossier-local** per §13 ("source_id blocks are assigned centrally
at merge"). `claim_ref` maps to the R-ids in §1975-1976 records and the S-ids in §Stage 3.

Two field conventions, so the merge pass does not "repair" them into defects:
- `quantitative.derived_arithmetic` is **empty on non-DERIVED rows** — §13's per-column rule
  ("mandatory whenever `evidence_class` is ESTIMATE/DERIVED, empty otherwise") overrides the general
  no-empty-cell rule there. Every row whose class IS DERIVED carries its arithmetic.
- `sources.archived_url` is `UNKNOWN` for the Internet Archive layers because the IA item **is** the
  archive copy and no separate Wayback capture was checked this session; it is not a missing value.
`data_gaps.follow_up_task` is populated on all eight rows, including the Medium-importance ones.

**55 register rows total: timeline 17 · quantitative 12 · conflicts 5 · sources 13 · data_gaps 8.**
All five blocks were parsed back with `csv.reader` and checked for column count and empty cells.

**timeline.csv** — `company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes`

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Microsoft,stage1,1975,Company later states it was founded as a partnership in this year,Bill Gates; Paul Allen; Monte Davidoff,"Albuquerque, New Mexico",D05,RETROSPECTIVE INTERPRETATION,Medium,U.3,No contemporaneous 1975 document naming the entity exists in any held byte (N-12/N-13/N-14)
Microsoft,stage1,1976-01-31,An entity styled Micro-Soft appears in print with Bill Gates signing as General Partner,Bill Gates,"Menlo Park, California (place of publication)",D01,FACT,Medium,None,Earliest date any held byte carries about this company; masthead read off the file's own face
Microsoft,stage1,1976-01-31,"The company's own letter states its product line, sunk computer time and royalty outcome",Bill Gates,"Albuquerque, New Mexico",D01,FOUNDER CLAIM,Medium,U.2,"One document, one lineage: source of R01-R05"
Microsoft,stage1,1976-02-29,The club prints a hostile reply to the letter,Homebrew Computer Club members,"Menlo Park, California",D02,CONTEMPORANEOUS OBSERVATION,Medium,None,Reply cites the January letter by volume and issue
Microsoft,stage1,1976-03-31,A paying customer's published letter fixes a price and a bundling condition,Homebrew Computer Club reader,"Menlo Park, California",D03,CONTEMPORANEOUS OBSERVATION,Medium,U.2,Only in-window price datum found: 75 USD for 8K BASIC
Microsoft,stage1,1976-04-30,The dispute is still live in club print,Homebrew Computer Club members,"Menlo Park, California",D04,CONTEMPORANEOUS OBSERVATION,Medium,None,"Cites 'HBCC newsletter V2-1', tying the argument back to D01"
Microsoft,stage1,1976-07,"BYTE reports the letter circulating across Radio Electronics, PCC, MITS Computer Notes and club bulletins",BYTE (third party),"Morris Plains, New Jersey",D06,CONTEMPORANEOUS OBSERVATION,Medium,None,"A reprint footprint, not independent corroboration of the letter's content"
Microsoft,stage1,1977-05,Kilobaud carries an in-page Microsoft product news line,Kilobaud,"Peterborough, New Hampshire",D07,CONTEMPORANEOUS OBSERVATION,Medium,None,"Identical syndicated copy in held BYTE 1977-05/06: one item, three documents (A2 C-7)"
Microsoft,stage1,1977-07,A third-party BYTE letter uses the hyphenated Micro-Soft form,BYTE reader,"Morris Plains, New Jersey",D06,CONTEMPORANEOUS OBSERVATION,Medium,None,Not company copy; earliest non-company use of the name form found
Microsoft,stage1,1979,Compute! carries multiple in-page Microsoft BASIC references,Compute!,"Peterborough, New Hampshire",D08,CONTEMPORANEOUS OBSERVATION,Medium,None,"Second half of the probe's text: numFound-2, whose other item was annotation-only"
Microsoft,stage1,1980-12,Company print names Microsoft Consumer Products with a Bellevue address and telephone,Microsoft (ad copy),"Bellevue, Washington",D09,FACT,Medium,U.4,"Stage-1 close document; 134 hit lines, 0 of them hyphenated"
Microsoft,stage2,1981,Company later states it was incorporated in this year,Microsoft Corporation,Washington,D05,RETROSPECTIVE INTERPRETATION,Medium,U.4,Document-boundary candidate for the Stage-1 close
Microsoft,stage2,catalogue-1982,Paul G. Allen talk transcript on future plans for MSDOS 2.0,Paul G. Allen,UNKNOWN,D10,FOUNDER CLAIM,Low,None,No year on its face; house-organ self-narrative; carried from A2 and not re-opened this pass
Microsoft,stage3,1986-01,Company print names Microsoft Corporation at Bellevue plus eight further national entities,Microsoft (ad copy),Bellevue; Munich; Sydney; Berks; Ontario; Sollentuna; Paris; Seoul; Tokyo,D11,FACT,Medium,None,Entity family visible in print at the Stage-3 opening; corporate relationships not established
Microsoft,stage3,1986-01,BYTE reproduces a company-authored house-organ column,Microsoft Languages Newsletter,UNKNOWN,D11,FACT,Medium,None,Self-narrative inside a third-party magazine: one lineage with the ads
Microsoft,stage3,1987-04,Third-party print still uses the hyphenated Micro-Soft form,BYTE contributor,"Morris Plains, New Jersey",D13,CONTEMPORANEOUS OBSERVATION,Medium,None,Read-only on the Dell shelf; 1 hyphenated line of 200 hit lines
Microsoft,stage3,1988-08,Company print names Microsoft Corporation as owner of MS OS/2 and MS Windows/386,Microsoft (ad copy),UNKNOWN,D12,FACT,Medium,None,"254 hit lines over 1,888,699 B"
```

**quantitative.csv** — `company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes`

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Microsoft,stage1,1976-01-31,claimed value of computer time used in development,40000,USD (nominal; company's valuation basis unstated),D01,1976-01-31,FOUNDER CLAIM,Medium,,"Printed as an assertion; no rate, hour count or invoice behind it"
Microsoft,stage1,1976-01-31,claimed paid share of Altair owners,less than 10,percent of Altair owners,D01,1976-01-31,FOUNDER CLAIM,Medium,,The denominator (Altair owners) is itself an uncounted company assertion
Microsoft,stage1,1976-01-31,implied royalty return on development time,less than 2,USD per hour,D01,1976-01-31,DERIVED,Low,printed conclusion only: royalties received / hours spent; BOTH inputs absent from the document so the division cannot be reproduced,"The company's own arithmetic result, not a figure this project can recompute"
Microsoft,stage1,1976-01-31,claimed duration of initial development,2,months,D01,1976-01-31,FOUNDER CLAIM,Medium,,Printed as 'Though the initial work took only two months'
Microsoft,stage1,1976-01-31,persons named in the company's own origin sentence,3,persons (Gates; Allen; Davidoff),D01,1976-01-31,FOUNDER CLAIM,Medium,,3 named in one document; the entity's headcount is NOT established by it
Microsoft,stage1,1976-03-31,listed price of 8K BASIC to a customer,75,USD (nominal),D03,1976-03-31,CONTEMPORANEOUS OBSERVATION,Medium,,Single third-party source; conditional on owning qualifying hardware
Microsoft,stage1,1976-01,start span implied by the company's 'almost a year ago',c. 1975-02 to 1975-07,month span,D01,1976-01-31,DERIVED,Low,1976-01-31 minus 'almost a year' (read as 8-12 months) gives 1975-02 to 1975-06; the phrase is unquantified,Arithmetic on a vague phrase; no single 1975 date may be printed from it
Microsoft,stage1,1976,company-name hit lines across held BYTE 1976,0,hit lines,D06,1976-12-31,DERIVED,High,"sum of grep -ciE 'micro-?soft' over 12 files = 0 (per-file counts all 0); corpus 5,743,636 B","A measurement over held bytes, not a corpus claim"
Microsoft,stage1,1980-12,company-name hit lines in BYTE December 1980,134,hit lines,D09,1980-12-31,DERIVED,High,"grep -ciE 'micro-?soft' byte-1980-12.txt (1,669,716 B) = 134; of these grep -ci 'micro-soft' = 0",A2's '136 hits' counted a different unit: see U.5
Microsoft,stage3,1986-01,company-name hit lines in BYTE January 1986,185,hit lines,D11,1986-01-31,DERIVED,High,"grep -ciE 'Micro-?[Ss]oft' byte-magazine-1986-01_djvu.txt (1,850,712 B) = 185",Unverified TLS
Microsoft,stage3,1988-08,company-name hit lines in BYTE August 1988,254,hit lines,D12,1988-08-31,DERIVED,High,"grep -ciE 'Micro-?[Ss]oft' byte-magazine-1988-08_djvu.txt (1,888,699 B) = 254",Unverified TLS
Microsoft,stage1,1994-02-14,EDGAR index rows dated before the registrant's filing floor,0,filings,D05,1994-09-27,DERIVED,High,"count(filingDate < 1994-02-14) = 0 over 4,525 rows parsed from sources/_index/submissions.csv; minimum 1994-02-14","Establishes family (a) as a NULL for 1975-1990, not a conditional null"
```

**conflicts.csv** — `company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence`

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Microsoft,stage1,U.1,Boundaries,hcc0201 reports Altair BASIC availability set for December 17 1975 with delivery January 15 1976,"A2_periodical_and_filings_settlement.md, Family c item 1",2026-09-25,"Those two dates in hcc0201 belong to Processor Technology's VDM-1 video display module, a different product in a different column",company_004_apple/sources/ia_homebrew/hcc0201.txt lines 48-54,1976-01-31,The earlier dossier attached the dates to Altair BASIC by textual proximity; reading the column shows the subject is the VDM-1 and its character-generator supply,The bytes win: the sentence names VDM-1 and Processor Technology Corporation and never names BASIC,RETRACT. hcc0201 contains no Altair BASIC availability or delivery date; the release date is UNKNOWN again,Whether any 1975-76 print carries an Altair BASIC release date: UNTRIED,High
Microsoft,stage1,U.2,Narrative and quantitative,Company: less than 10 percent of all Altair owners have bought BASIC,company_004_apple/sources/ia_homebrew/hcc0201.txt line 93,1976-01-31,BYTE: more copies of Altair's BASIC have been pirated than have been legally sold,company_004_apple/sources/ia_byte_1976/byte-1976-09.txt line 2039,1976-09,Both describe unpaid copying but imply different paid fractions (under 10 percent versus under 50 percent),"Neither is a measurement, and BYTE is downstream of the company's own claim, so it cannot corroborate it",Treat the paid fraction as a company assertion with no independent denominator; the hcc0203 reader's 'one of the 10 percent minority' adopts the company's number rather than counting it,True paid fraction and the Altair installed base are UNKNOWN and probably unrecoverable,Medium
Microsoft,stage1,U.3,Boundaries,A filed statement says the company was founded as a partnership in 1975,"FY1994 Form 10-K lines 181-182, accession 0000891020-94-000175",1994-09-27,No document dated in 1975 naming the entity exists anywhere in the held bytes,"Homebrew 0109/0110 35,756 B; BYTE 1976 x12 5,743,636 B; Popular Electronics Mar 1975 493,273 B; all 0 hits",2026-09-26,Different evidence classes: one retrospective company self-report versus an absence of contemporary evidence over a bounded sample,"The absence is over named bytes only, so it cannot refute 1975; the filing asserts 1975 nineteen years after the fact","1975 stands as the company's own account, corroborated across two independent lineages (1976 letter, 1994 filing) but never documented contemporaneously","A 1975-dated third-party document may exist in unopened 1975 print (Popular Electronics Jul-Dec 1975, Kilobaud 1975): UNTRIED",Medium
Microsoft,stage1,U.4,Boundaries,Stage 1 closes 1980-12-31,"A2_periodical_and_filings_settlement.md, Boundaries",2026-09-25,The company's own filed statement places incorporation in 1981,FY1994 Form 10-K line 182,1994-09-27,The provisional close was derived from shelf coverage (where the print thins out); the 1981 date is the only in-corpus document naming a legal transition event,The filed statement is the only evidence of an entity-form change; the shelf-derived date is an inference from coverage,"Keep Stage 1 = 1975-1980 for continuity, but record that the transition the company itself reports falls just outside the close; if the orchestrator prefers a document-bound stage, 1981 is the defensible cut","Whether 'incorporated in 1981' means a new corporation, a conversion or a re-domicile is UNKNOWN from this sentence",Medium
Microsoft,stage1,U.5,Measurement,BYTE December 1980 carries 136 Microsoft hits,"A2_periodical_and_filings_settlement.md, Family c item 4",2026-09-25,The same file yields 134 matching lines,"grep -ciE 'micro-?soft' over company_004_apple/sources/ia_byte_1981/byte-1980-12.txt (1,669,716 B)",2026-09-26,Unit definition: occurrences versus matching lines,Both are computed over the same bytes; only one unit may enter the register,"Adopt the matching-line count (134) as this register's unit and label every count 'hit lines', never 'mentions'",Which invocation produced 136 is unknown; the A2 file is not editable from this pass,High
```

**sources.csv** — `source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes`

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
D01,stage1,"R01, R02, R03, R04, R05",Homebrew Computer Club Newsletter Vol. 2 No. 1,Homebrew Computer Club (editorial venue); letter text by Bill Gates,"periodical, club newsletter",primary,1976-01-31,1976-01-31,2026-09-26,"identifier hcc0201; bytes company_004_apple/sources/ia_homebrew/hcc0201.txt 28,281 B",UNKNOWN,1,FOUNDER CLAIM,Medium,"ONE lineage for R01-R05. The club is the publisher; the letter is Gates's own text, so the officer title is company-side and the masthead is club-side","Bill Gates / General Partner, Micro-Soft","Company-authored content inside a third-party venue: cite the venue for the fact of publication, the letter for the content of the claim. Unverified TLS"
D02,stage1,R06,Homebrew Computer Club Newsletter Vol. 2 No. 2,Homebrew Computer Club,"periodical, club newsletter",primary,1976-02-29,1976-02-29,2026-09-26,"identifier hcc0202; bytes company_004_apple/sources/ia_homebrew/hcc0202.txt 43,265 B",UNKNOWN,3,CONTEMPORANEOUS OBSERVATION,Medium,Independent of D01 as to the reply's content; derivative as to the existence of the January letter,Regarding your Letter of 3 February 1976 Appearing in Homebrew Computer Club Newsletter Vol. 2 No. 1 / You gave it away; none stole it from you,Unverified TLS
D03,stage1,R07,Homebrew Computer Club Newsletter Vol. 2 No. 3,Homebrew Computer Club (reader letter addressed to Mr. Gates),"periodical, club newsletter",primary,1976-03-31,1976-03-31,2026-09-26,"identifier hcc0203; bytes company_004_apple/sources/ia_homebrew/hcc0203.txt 23,686 B",UNKNOWN,3,CONTEMPORANEOUS OBSERVATION,Medium,"Third-party author writing in response to D01: the '10 percent minority' phrasing is D01's number, not an independent count","I have no objection to legitimately paying $75 for 8K BASIC, or to being required to purchase suitable hardware in order to qualify for that price",Only in-window price datum found. Unverified TLS
D04,stage1,R06,Homebrew Computer Club Newsletter Vol. 2 No. 4,Homebrew Computer Club,"periodical, club newsletter",primary,1976-04-30,1976-04-30,2026-09-26,"identifier hcc0204; bytes company_004_apple/sources/ia_homebrew/hcc0204.txt 30,810 B",UNKNOWN,3,CONTEMPORANEOUS OBSERVATION,Medium,"Independent club member, explicitly citing 'HBCC newsletter V2-1'",since Mr. Bill Gates claims that he did not get payed [sic] enough and is in the mood of calling people thieves,Unverified TLS
D05,stage1,"R08, U.3, U.4","Form 10-K, Microsoft Corporation, accession 0000891020-94-000175",Microsoft Corporation / SEC EDGAR,regulatory filing,primary,1994-09-27,1994-09-27,2026-09-26,https://www.sec.gov/Archives/edgar/data/0000789019/000089102094000175/0000891020-94-000175.txt,same URL; EDGAR is itself the archive; sha1 recorded in the .meta.json sidecar,1,RETROSPECTIVE INTERPRETATION,High,"Independent lineage from D01: different institution, different date, neither derived from the other","was founded as a partnership in 1975 and was incorporated in 1981 / From 1975 to 1981, Mr. Gates was a partner with Paul Allen, Microsoft's other founder, in the predecessor partnership","TLS certificate-verified; 442,763 B; RETROSPECTIVE SOURCE per section 6"
D06,stage1,"R09, U.2, naming drift","BYTE July 1976, September 1976 and July 1977",BYTE / McGraw-Hill,trade periodical,secondary,1976-07,1976-07 / 1976-09 / 1977-07,2026-09-26,"identifiers byte-1976-07, byte-1976-09, byte-1977-07; bytes company_004_apple/sources/ia_byte_1976 487,633 B and 527,921 B, ia_byte_1977 751,638 B",UNKNOWN,3,CONTEMPORANEOUS OBSERVATION,Medium,"Reprints and references D01's letter: ONE source for the letter's content, an independent source for the fact of its circulation",it now appears that more copies of Altair's BASIC have been pirated than have been legally sold / While the Micro-Soft venture into APL represents a noble undertaking,Unverified TLS
D07,stage1,1977 product news,"Kilobaud, May 1977",Kilobaud,trade periodical,secondary,1977-05,1977-05,2026-09-26,"identifier kilobaudmagazine-1977-05; bytes sources/periodicals/kilobaudmagazine-1977-05_djvu.txt 672,171 B",UNKNOWN,3,CONTEMPORANEOUS OBSERVATION,Medium,"The OSI news line is syndicated: identical copy in held BYTE 1977-05/06, so one item across three documents",OSI 6502 8K BASIC FOR DISK BY MICROSOFT,De-duplicated before counting (A2 C-7)
D08,stage1,1979 breadth of BASIC ports,"Compute! Magazine Issue 001, Fall 1979",Compute!,trade periodical,secondary,1979,1979,2026-09-26,"identifier 1979-Fall-compute-magazine; bytes sources/periodicals/1979-Fall-compute-magazine_djvu.txt 542,112 B",UNKNOWN,3,CONTEMPORANEOUS OBSERVATION,Medium,Independent of MITS and BYTE house copy,"versions of Microsoft BASIC (PET, KIM, SYM, etc.)","Second half of the probe's text: numFound-2; this item's hit is real in-page, the other item's was annotation-only"
D09,stage1,Stage-1 close; entity plurality,"BYTE, December 1980",BYTE / McGraw-Hill carrying Microsoft-supplied advertising,trade periodical carrying company print,primary,1980-12,1980-12,2026-09-26,"identifier byte-magazine-1980-12; bytes company_004_apple/sources/ia_byte_1981/byte-1980-12.txt 1,669,716 B",UNKNOWN,3,FACT,Medium,"Ad copy is company-authored: self-narrative, not third-party observation","MICROSOFT Consumer Products, 400 108th Ave. N.E., Suite 200, Bellevue, WA 98004. (206) 454-1315.","134 hit lines, 0 hyphenated. Unverified TLS"
D10,stage2,Allen product statement,"MS DOS 2.0 / Future plans for MSDOS, by Paul G. Allen",Paul G. Allen,"company print, talk transcript (house organ)",primary,UNKNOWN,1982 (catalogue year only),2026-09-25,"identifier MSDOS2FuturePlansForMSDOSByPaulAllen; bytes sources/periodicals/MSDOS2FuturePlansForMSDOSByPaulAllen_djvu.txt 13,639 B",UNKNOWN,1,FOUNDER CLAIM,Low,"Named principal speaking as 'we' about the company's own products: self-narrative, one lineage","Over the last seven years, Microsoft has ported its software products to over fifty different operating system environments","No year on its face (A2 C-8). Not re-opened this pass: carried, not newly verified"
D11,stage3,"S3-1, S3-2","BYTE, January 1986, Volume 11 Number 1",BYTE / McGraw-Hill carrying Microsoft-supplied advertising and a company column,trade periodical carrying company print,primary,1986-01,1986-01,2026-09-26,"identifier byte-magazine-1986-01; bytes sources/periodicals/byte-magazine-1986-01_djvu.txt 1,850,712 B",UNKNOWN,3,FACT,Medium,The Microsoft Languages Newsletter column is a company house organ reproduced in a third-party magazine: ONE lineage with the advertisements in the same issue,"Microsoft Corporation / Bellevue, Washington USA; The IBM C compiler is a repackaging of the Microsoft C Compiler",Masthead read off the file's face. Unverified TLS
D12,stage3,S3-4,"BYTE, August 1988",BYTE / McGraw-Hill carrying Microsoft-supplied advertising,trade periodical carrying company print,primary,1988-08,1988-08,2026-09-26,"identifier byte-magazine-1988-08; bytes sources/periodicals/byte-magazine-1988-08_djvu.txt 1,888,699 B",UNKNOWN,3,FACT,Medium,Company copy,trademarks of Microsoft Corporation. MS OS/2 and MS Windows/386 are products of Microsoft,254 hit lines. Unverified TLS
D13,stage3,naming drift to 1987,"BYTE, April 1987",BYTE / McGraw-Hill,trade periodical,secondary,1987-04,1987-04,2026-09-26,"identifier byte-magazine-1987-04; bytes company_041_dell/sources/periodicals/byte-magazine-1987-04_djvu.txt 1,769,686 B (read-only on a sibling company's shelf)",UNKNOWN,3,CONTEMPORANEOUS OBSERVATION,Medium,"Third-party venue, third-party author: independent of company print",Watch out Micro-Soft.,1 hyphenated line of 200 hit lines. Nothing copied or moved
```

**data_gaps.csv** — `company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task`

```csv
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
Microsoft,stage1,"Whether Micro-Soft was a partnership as a matter of law, and on what terms","No partnership instrument, registry entry or court record exists in any held byte; family (a) is floored at 1994-02-14 and family (e) is UNTRIED",High,"'General Partner, Micro-Soft' in 1976 company print (D01) plus 'founded as a partnership in 1975' in a 1994 filing (D05)",Medium,"Family (e): search auction and museum holdings for a 1975-1977 Micro-Soft partnership document, licence or cheque; and New Mexico Secretary of State records (0 calls this session)"
Microsoft,stage1,Any document DATED in 1975 that names the company,"Zero hits over 6,272,665 B of bytes dated 1975 or covering it (N-12/N-13/N-14); MITS's own house organ is not held at all",High,"The company's own retrospective statements only (D01, D05)",Low,"Harvest MITS Computer Notes 1975-1976 and People's Computer Company March-April 1976: both are NAMED as carriers of the letter by D06, so their existence is evidenced and their bytes are reachable"
Microsoft,stage1,"Revenue, headcount and customer counts for 1975-1980",No filing exists below 1994-02-14; the creator-scoped annual-report route returned numFound 1 and it is a 1997 manual (N-1); XBRL produced 0 bytes (N-18),High,"Company self-reports in D01: 40,000 USD computer time, under 10 percent paid share, under 2 USD per hour",Low,Search Kilobaud and BYTE 1978-1980 for a software-house revenue survey or a MITS royalty report; Chronicling America for Albuquerque business records
Microsoft,stage1,Altair BASIC release date and the MITS licence terms,The only candidate date in hcc0201 is RETRACTED by U.1 (it belongs to Processor Technology's VDM-1); MITS print is not held,High,D01's 'almost a year ago' and D06's third-party phrasing 'Altair's BASIC',Low,Grep Popular Electronics July-December 1975 and any surviving Computer Notes for licence and royalty language; re-open hcc0201 in full rather than by proximity
Microsoft,stage2,Date of the Allen MSDOS-2.0 talk and what 'over the last seven years' counts,"The 13,639 B layer carries no year on its face; the 1982 is a catalogue field only",Medium,D10 plus A2 conflict C-8,Low,Re-open the layer for a conference name or internal date; cross-check against 1983-1984 product print
Microsoft,stage3,Document coverage for 1982-1985 and 1989-1990,No layer in those spans is held on any shelf this session read,Medium,"BYTE 1986-01 and 1988-08 (D11/D12) plus the Dell-shelf 1987-04, 1988-03, 1988-10 and 1988-12",Medium,"Harvest BYTE, Kilobaud, PC Magazine and InfoWorld for 1982-1985 and 1989-1990; the probe's inventoried-but-unmined 159 BYTE items 1986-89 and 57 PC Magazine items remain UNTRIED"
Microsoft,stage3,Whether anything in 1986-1990 print or filings narrates a public offering,"Zero hits for offering, IPO or shareholder over 3,739,411 B of Stage-3 bytes, and EDGAR's floor post-dates the stage by eight years",High,"D05, filed 1994-09-27, is the earliest company-authored text available on any listing-era subject",Low,Run sec_intake facts for 1994-1999 (0 bytes produced this session) and read the FY1994 10-K financial statements; do NOT pull 1994 text backwards to stand in for 1986-1990
Microsoft,stage1,Founder pre-history before 1976-01-31,"The Traf-O-Data pattern returns 0 hits across every held text layer (N-15), and no byte dated before 1976-01-31 names either founder",Medium,None in-window: only retrospectives,Low,Family (e) plus HathiTrust full-text for Traf-O-Data and 1974-1975 Albuquerque trade print
```

## Stage 3 1986-1990 attempt

STATUS: WRITTEN (msft-s1-records) — **produced.** The probe's named gap ("zero documents in any family for
Stage 3") is **refuted for family (c) by bytes already on disk**: 3,739,411 B in this company's own
`sources/periodicals/` (BYTE 1986-01, 1988-08 — fetched 19:56-19:57 UTC 2026-09-25, **after** the A2
dossier closed, therefore unreported until now) plus **7,392,281 B read-only on the Dell shelf** (BYTE
1987-04, 1988-03, 1988-10, 1988-12).

**S3-1 — the entity family, 1986-01** (`byte-magazine-1986-01_djvu.txt`, 1,850,712 B, masthead "JANUARY
1986 VOL. 11, NO. 1", 185 hit lines). A Microsoft Windows advertisement lists the printed corporate family
by name and place: "Microsoft Corporation / Bellevue, Washington USA", then "Microsoft GmbH / Munich
DEUTSCHLAND", "Microsoft Pty / Sydney NSW AUSTRALIA", "Microsoft Ltd / Berks ENGLAND", "Microsoft Canada
Inc / Ontario CANADA", "Microsoft AB / Sollentuna SWEDEN", "Microsoft SARL / Paris FRANCE", "ONIX
Microsoft / Seoul KOREA", "Microsoft Far East / Tokyo JAPAN". — FACT (Medium, unverified TLS) that
company print at the Stage-3 opening names a corporation at Bellevue plus eight further national entities.
It does **not** establish which were subsidiaries, branches or distributors.

**S3-2 — a house organ inside a third-party magazine, 1986-01.** The same issue carries a column headed
"MICROSOFT LANGUAGES NEWSLETTER / News about the Microsoft Language Family" with product-engineering
statements ("By porting the new Macro Assembler 4.00 release to Microsoft C, it assembles programs from 2
to 3 times faster than the previous Microsoft 3.00 and IBM® 2.00 releases") and an OEM statement ("The IBM
C compiler is a repackaging of the Microsoft C Compiler with a few utilities from the Microsoft Macro
Assembler… IBM also distributes Microsoft BASIC, COBOL, FORTRAN, and Pascal compilers, BASIC interpreter
and Macro Assembler under its own logo"). — **SELF-NARRATIVE, one lineage with S3-1** (same magazine,
company-supplied column). Its independent value is narrow: the IBM repackaging sentence is a company
description of an OEM relationship, useful as Stage-3 channel evidence, not as proof of terms.

**S3-3 — a null that matters.** `gates` matches 12 lines in BYTE 1986-01 and 4 in BYTE 1988-08, and
**every one is electronics usage or a word fragment** ("200 gates per chip", "Unused gates: IC23-B",
"gregates of objects"). `paul allen` → **0** in both. So the founders are **absent from the named pages of
Stage-3 trade print** that this corpus holds: by 1986 the company appears as a trademark and a product
line, not as people. This is a NULL over 3,739,411 B of held bytes and it is the sharpest contrast between
Stage 1 (a first-person letter) and Stage 3 (corporate imprint only).

**S3-4 — 1988-08** (1,888,699 B, masthead "AUGUST 1988", 254 hit lines): "trademarks of Microsoft
Corporation. MS® OS/2 and MS® Windows/386 are products of Microsoft", "versions are fully compatible with
Microsoft Windows", "Microsoft OS/2 Programmer's Toolkit" in dealer price columns. FACT (Medium).

**S3-5 — naming drift reaches 1987** (Dell shelf, read-only): "Watch out Micro-Soft." — the hyphenated form
still in third-party print 11 years after the company stopped using it in its own letters (1 hyphenated
line of 200 in BYTE 1987-04).

**What Stage 3 did NOT produce.** Searching all three held Stage-3 layers: `initial public offering` →
**0**, `public offering` → **0**, `went public` → **0**, `shareholder` → **0**, `IPO` → **0**. Nothing in
1986-1988 print as held narrates a listing or registration, so the intake sheet's inherited "1986
registration" remains **unverified in every family**. And family (a) still cannot reach 1986-1990: its
floor is 1994-02-14, eight years above the stage. The 159 BYTE items 1986-89 / 57 PC Magazine / 26
InfoWorld the probe inventoried but never mined remain **UNTRIED** — I mined 5 issues already on disk,
which is a different act from harvesting the window.

**`mine` route status.** `python tools/ia_text.py mine --q "microsoft" --company-dir <dir> --max-mb 4`
executes without returning field-less rows, but its first stage is an unscoped advancedsearch whose returned
items are annotation-borne noise (the top rows' `collection` fields are `fav--_hindirip9x_watch_despicable_me_3…`
movie-favourite lists, not serials). **I therefore fell back to the explicit `fetch`-already-held + `grep`
route for every figure in this dossier**, which is what §15.1 and the brief prescribe when `mine`
misbehaves. Nothing in this file rests on a `text:` count.

## Nulls and UNANSWERED

STATUS: WRITTEN (msft-s1-records)

NULLS — zeros over bytes I grepped myself this session (each is a real null, bounded to the named bytes):

| # | bytes named | pattern | hits |
|---|---|---|---|
| N-12 | `hcc0109` 15,563 B + `hcc0110` 20,193 B (mastheads 1975-11-30 / 1975-12-31 read off their own faces) | `micro-soft`, `microsoft`, word `gates`, `paul allen` | 0,0,0,0 |
| N-13 | BYTE 1976 ×12, 5,743,636 B | `micro-?soft` | 0 in every issue (per-issue 0) |
| N-14 | `197503PopularElectronics_djvu.txt` 493,273 B | `micro-soft` | 0 |
| **N-15** | **ALL `.txt` under `01_companies/` (25,512,395 B in scope plus the rest of the repo's text layers)** | **`traf-o-data`** | **0** — and the only `traf*` hits in Homebrew are "traffic lights"/"avoid traffic". **Pre-1975 founder activity is absent from every held byte**; this converts the probe's "UNTRIED, never searched" into a searched null over the current shelf. It is NOT a corpus null: the shelf is ~44 of ~545 items |
| N-16 | BYTE 1986-01 + 1988-08, 3,739,411 B | `paul allen`; founder-sense `gates`; `initial public offering`; `shareholder` | 0 / 0 / 0 / 0 |
| N-17 | FY1994 10-K, 442,763 B | `Traf-O-Data`, `New Mexico`, `April 1975` | 0 / 0 / 0 |
| N-18 | `sources/financials/xbrl_early_series.csv` | — | **0 bytes, header row only** (C-3 reproduced; no XBRL series produced) |

UNANSWERED — an infrastructure state, not an absence:

- The 1994-02-14 Form 10-Q (accession 0000950109-94-000252) and 1994-05-03 10-Q (0000891020-94-000070) are
  **UNSTORED**: `auto` reported "118 fetched / 23 stored / 95 unanswered" — the unanswered are index-page
  and 404 fetch targets, not absent filings.
- Family (b) web archives: carried UNANSWERED from the prior probe (CDX 503 ×2), not re-run.
- Homebrew issues 0205/0206/0207/0209/0211/0213 could not be dated from their own faces this session —
  their first date token is a *reference* to a later year. Their dates are known only from
  `company_004_apple/sources/_RETRIEVAL_LOG.md` lines 37-40, which is a sibling dossier's claim. **Not
  UNANSWERED as a fetch, but UNVERIFIED as a date**, so no record here depends on them.
- `sources/sec/_MANIFEST.csv`: header row only, no document rows, despite 3 stored documents — the same
  class of tool defect as C-3. The bytes and their `.meta.json` sidecars are the record.

RETRACTION carried to the instruction layer (§14 rule 10): **A2 §Family c item 1 states that hcc0201
"separately reports Altair BASIC availability 'set for December 17, 1975. Delivery was then scheduled for
January 15, 1976'." The bytes say those dates belong to Processor Technology's VDM-1**
(`hcc0201.txt` lines 48-54). Any later pass that cites A2 for a 1975/76 Altair BASIC delivery date is
citing a misattribution. See conflicts U.1. This note must be applied to `A2_…` and to any stage file that
inherits it; I could not edit A2 (I do not own it).

## Untried

STATUS: WRITTEN (msft-s1-records)

1. **MITS Computer Notes (Feb 1976) and People's Computer Company (Mar-Apr 1976)** — named as carriers of
   the Gates letter by BYTE 1976-07 (D06) and never searched. This is the single highest-value untried
   route in the dossier: a third route for the 1975/76 origin narrative, independent of the Homebrew
   lineage and of MITS's own house organ, and the only realistic source of MITS licence/royalty terms.
2. **`byte-magazine-1977-08`** ("Working with APL", the issue adjacent to the 1977-07 APL letter I read),
   `Kilobaud197810`, `kilobaudmagazine-1980-04`, `197811PopularElectronics`, Popular Electronics
   Jul-Dec 1975, and the remaining ~500 items of the 545 shelf.
3. **A 1982-1985 and 1989-1990 periodical harvest.** I mined only what was already on disk; the window
   between the 1981 brochure and the 1986 BYTE issues is unheld, as is 1989-1990.
4. **The probe's inventoried-but-unmined Stage-3 assets**: 159 BYTE items 1986-89, 57 PC Magazine, 26
   InfoWorld. Byte 1986-01/1987-04/1988-03/1988-08/1988-10/1988-12 were reached only because a sibling
   company happened to hold them.
5. **Family (e) documentary**, unchanged: 0 calls. Now carries a High-importance `data_gaps` follow-up
   (partnership terms, gap 1).
6. **Family (b)**: CDX re-run for microsoft.com's earliest capture; 0 calls.
7. **`sec_intake.py facts` produced an empty file** — whether the SEC company-concept API answers at all
   for this CIK at 1994-1999 is untested; the FY1994 10-K's prose financial statements were also not read.
8. **The 3,468 unfetched 1994-1999 accessions**, including the 1994-10-14 S-3 (oldest registration-form
   row on the index).
9. **Whether any document dated 1975 names Micro-Soft at all** — the N-15/N-12/N-13/N-14 nulls are over a
   bounded sample; the 1975 silence is a strong finding, not a proven absence.
10. **`197602-modern-data` licence/royalty search** and a `Micro-Soft`-as-primary-term search against
    1977-1982 serials.

