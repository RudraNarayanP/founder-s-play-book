# Harvest mining -- freddiemac

Window applied: 1970-01-01 .. 1990-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

44 candidate rows in the harvest index; 12 items mined; 31 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 3 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 5 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 4 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `freddie mac`; **other quoted terms** (predecessors, siblings, trade titles): `federal home loan mortgage`, `federal home loan mortgage corporation`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `cia-readingroom-document-cia-rdp89-00066r000700060001-1` | 1985-01-01 | in-window | 98,700 | 0 | 0 | - | VARIANT_TERM_HIT |
| `DTIC_ADA270234` | 1990-01-01 | in-window | 114,310 | 0 | 98 | `freddie  mac` | TIER1_CANDIDATE_TEXT |
| `cia-readingroom-document-cia-rdp88g01332r001100120011-5` | 1986-01-01 / title:2001 | in-window MISMATCH | 44,177 | 0 | 0 | - | VARIANT_TERM_HIT |
| `micro_IA41152637_1194` | 1988-01-01 | in-window | 260,615 | 0 | 200 | `freddie mac` | TIER1_CANDIDATE_TEXT |
| `cia-readingroom-document-cia-rdp90m00005r001300070026-8` | 1988-01-01 | in-window | 49,418 | 0 | 0 | - | VARIANT_TERM_HIT |
| `cia-readingroom-document-cia-rdp88g01332r000800990016-9` | 1986-01-01 | in-window | 66,176 | 0 | 0 | - | VARIANT_TERM_HIT |
| `micro_IA41152606_0820` | 1982-01-01 / title:1981 | in-window MISMATCH | 32,088 | 0 | 0 | - | VARIANT_TERM_HIT |
| `bEHadqS9X-YC` | 1996-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `iD8-bWporl8C` | 2007-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `LWPrRbiNEo8C` | 2004-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `0UFMAQAAQBAJ` | 2013-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `governmentspons00devegoog` | 1991-01-01 / title:1991 | outside? | 904,005 | 0 | 200 | `freddie mac` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp89-00066r000700060001-1` l.227: . Federal Home Loan Mortgage Corporation, most
- `cia-readingroom-document-cia-rdp89-00066r000700060001-1` l.1044: Federal Home Loan Mortgage Corp. 430 4 102 536 5.0 7.8 (0.8) [6] .
- `cia-readingroom-document-cia-rdp89-00066r000700060001-1` l.1124: Federal Home Loan Mortgage Corp. 7.8 7.2 5.4 4.3
- `DTIC_ADA270234` l.75: Federal  Home  Loan  Mortgage  Corporation  (Freddie  Mac),  which
- `DTIC_ADA270234` l.106: through  June  30,  1989.  Unlike  P'annie  Mae,  Freddie  Mac,  and  in  o.  va
- `DTIC_ADA270234` l.128: Fannie  Mae  and  Freddie  Mac  provide  similar  guidance  to  lenders  from
- `cia-readingroom-document-cia-rdp88g01332r001100120011-5` l.170: Sec. 245, Secondary financing by Federal Home Loan Mortgage Co:
- `micro_IA41152637_1194` l.129: The market value of Freddie Mac Preferred .............-csssssessecssssesseessnneeesenee
- `micro_IA41152637_1194` l.386: IN DECEMBER OCF 1984, FREDDIE MAC WAS GIVEN THE RIGHT TO ISSUE 15
- `micro_IA41152637_1194` l.389: WHICH HAD CAPITALIZED FREDDIE MAC AT ITS ORIGIN IN 1970. THIS STOCK
- `cia-readingroom-document-cia-rdp90m00005r001300070026-8` l.361: FEDERAL HOME LOAN MORTGAGE CORPORATION........ceees ois
- `cia-readingroom-document-cia-rdp90m00005r001300070026-8` l.1281: FEDERAL HOME LOAN MORTGAGE CORPORATION
- `cia-readingroom-document-cia-rdp88g01332r000800990016-9` l.473: Federal Home Loan Mortgage Corporation
- `micro_IA41152606_0820` l.12: REVIEW OF THE FEDERAL HOME LOAN MORTGAGE
- `micro_IA41152606_0820` l.25: A REPORT ON THE AUDIT OF THE FEDERAL HOME LOAN MORTGAGE CORPO-
- `micro_IA41152606_0820` l.53: Federal Home Loan Mortgage Corporation's
- `governmentspons00devegoog` l.530: tutions like Fannie Mae, Freddie Mac, and place them under the
- `governmentspons00devegoog` l.553: stances that cause it to be — I mean, indeed, Freddie Mac and
- `governmentspons00devegoog` l.676: Fannie Mae and Freddie Mac are doing very, very well. I want to
