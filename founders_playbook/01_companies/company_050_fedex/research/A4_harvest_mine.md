# Harvest mining -- fedex

Window applied: 1971-01-01 .. 1985-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

55 candidate rows in the harvest index; 12 items mined; 38 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 5 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 3 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 1 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 3 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: none; **other quoted terms** (predecessors, siblings, trade titles): `fdx corporation`, `federal express`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `cia-readingroom-document-cia-rdp96-00788r001500120024-8` | 1984-01-01 / title:2002 | in-window MISMATCH | 2,877 | 0 | 0 | - | VARIANT_TERM_HIT |
| `DTIC_ADA387307` | 1997-01-01 | outside? | 325,525 | 159 | 0 | - | VARIANT_TERM_HIT |
| `airlineindustry0000unse` | 1992-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `DTIC_ADA273978` | 1993-01-01 | outside? | 295,534 | 40 | 1 | `fedex  computer` | TIER1_CANDIDATE_TEXT |
| `overnightsuccess0000trim` | 1993-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `cia-readingroom-document-cia-rdp89-00063r000300260001-6` | 1987-01-01 | outside? | 34,244 | 0 | 0 | - | VARIANT_TERM_HIT |
| `disciplineofmark0000trea` | 1995-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `6292844-FedEx-Re-FedEx-proposal-Kelly-report` | 2019-01-01 | outside? | 2,043 | 7 | 0 | - | BARE_WORD_MATCH |
| `fed-ex-corporation-fdx-annual-report-2016` | 2016-01-01 / title:2016 | outside? | 357,408 | 200 | 4 | `fedex corporation` | TIER1_CANDIDATE_TEXT |
| `fed-ex-corporation-fdx-annual-report-2013` | 2013-01-01 / title:2013 | outside? | 486,237 | 200 | 8 | `fedex corporation`, `fedex shares` | TIER1_CANDIDATE_TEXT |
| `fed-ex-corporation-fdx-proxy-statement-2024-09-23` | 2024-01-01 | outside? | 558,597 | 200 | 8 | `fedex corporation`, `fedex enterprise`, `fedex international` | TIER1_CANDIDATE_TEXT |
| `fed-ex-corporation-fdx-annual-report-2021` | 2021-01-01 | outside? | 543,947 | 200 | 8 | `fedex corporation`, `fedex international` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp96-00788r001500120024-8` l.74: YOUR NOTES/AEFERENCE NUMBERS (FIRST 12 CHARACTERS WILL ALSO APPEAR ON INVOICE) peetes RO FEDERAL EXPRESS USE
- `cia-readingroom-document-cia-rdp96-00788r001500120024-8` l.103: 1 Cl ovenniur pacxaces) (i 0202) "Ty (7) FEDERAL EXPRESS LOCATION SHOWN | a
- `DTIC_ADA387307` l.18: FEDERAL  EXPRESS,  INC.
- `DTIC_ADA387307` l.34: Federal  Express,  Inc.
- `DTIC_ADA387307` l.61: National  Transportation  Safety  Board.  2000.  Crash  During  Landing  Federal  Express,  Inc.  McDonnell
- `DTIC_ADA273978` l.4558: Nearly  anyone  with  a  FedEx  computer  terminal  can  see  load
- `cia-readingroom-document-cia-rdp89-00063r000300260001-6` l.1199: including United Parcel, Federal Express, etc. will be received
- `6292844-FedEx-Re-FedEx-proposal-Kelly-report` l.5: Re: FedEx proposal/Kelly report
- `6292844-FedEx-Re-FedEx-proposal-Kelly-report` l.15: Let me know if you need anything else on the FedEx proposal in addition to what I sent you yesterday.
- `6292844-FedEx-Re-FedEx-proposal-Kelly-report` l.40: Subject: FedEx proposal/Kelly report
- `fed-ex-corporation-fdx-annual-report-2016` l.113: FedEx Corporation will
- `fed-ex-corporation-fdx-annual-report-2016` l.207: collaboratively to achieve overall results for FedEx Corporation.
- `fed-ex-corporation-fdx-annual-report-2016` l.755: FedEx Corporation S&P 500 Dow Jones Transportation Average of $197 million ($133 million, net of tax, or $0.46 per diluted share) in the
- `fed-ex-corporation-fdx-annual-report-2013` l.32: FedEx Corporation
- `fed-ex-corporation-fdx-annual-report-2013` l.340: FedEx Corporation
- `fed-ex-corporation-fdx-annual-report-2013` l.1192: interests with the interests of FedEx’s stockholders, the Board of Directors has established a goal that (i) within four
- `fed-ex-corporation-fdx-proxy-statement-2024-09-23` l.124: President & CEO, FedEx Corporation
- `fed-ex-corporation-fdx-proxy-statement-2024-09-23` l.127: See “Forward-Looking Statements” and “Risk Factors” on pages 24-37 of the FY24 FedEx Corporation Annual Report on Form 10-K,
- `fed-ex-corporation-fdx-proxy-statement-2024-09-23` l.158: FedEx Corporation
- `fed-ex-corporation-fdx-annual-report-2021` l.82: underbelly capacity. And for e-commerce, we’re giving customers even more reasons to choose FedEx — including the addition of
- `fed-ex-corporation-fdx-annual-report-2021` l.83: attractive services like FedEx International Connect Plus — our day-definite e-commerce delivery service rolling out globally this fiscal year.
- `fed-ex-corporation-fdx-annual-report-2021` l.160: See “Forward-Looking Statements” and “Risk Factors” on pages 23-34 of the fiscal 2021 FedEx Corporation Annual Report on
