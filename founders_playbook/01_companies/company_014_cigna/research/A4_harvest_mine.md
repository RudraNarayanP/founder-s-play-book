# Harvest mining -- cigna

Window applied: 1979-01-01 .. 1995-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

96 candidate rows in the harvest index; 12 items mined; 81 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 2 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 5 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 3 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 2 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `formerly known as cigna`; **other quoted terms** (predecessors, siblings, trade titles): `connecticut general`, `ina corporation`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `_c-d4kO2SHsC` | 1989-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `RBrmuywAFusC` | 1992-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `INAC2115_1979` | 1979-01-01 / title:1979 | in-window | 111,357 | 0 | 0 | - | VARIANT_TERM_HIT |
| `assessingitperfo00wils` | 1988-01-01 | in-window | 62,186 | 1 | 1 | `cigna  corporation` | TIER1_CANDIDATE_TEXT |
| `cia-readingroom-document-cia-rdp84b00130r000600010246-7` | 1980-01-01 / title:1980 | in-window | 4,428 | 0 | 0 | - | VARIANT_TERM_HIT |
| `cia-readingroom-document-cia-rdp88t00792r000300040001-2` | 1988-01-01 | in-window | 43,176 | 1 | 0 | - | BARE_WORD_MATCH |
| `cia-readingroom-document-cia-rdp91-00929r000200960032-0` | 1983-01-01 / title:2009 | in-window MISMATCH | 24,680 | 1 | 0 | - | BARE_WORD_MATCH |
| `cia-readingroom-document-cia-rdp90g00152r001102380002-3` | 1987-01-01 | in-window | 36,048 | 2 | 0 | - | BARE_WORD_MATCH |
| `micro_IA41153629_0618` | 1992-01-01 | in-window | 54,748 | 0 | 0 | - | VARIANT_TERM_HIT |
| `ERIC_ED460893` | 1995-01-01 | in-window | 125,176 | 0 | 0 | - | VARIANT_TERM_HIT |
| `micro_IA40385019_1642` | 1989-01-01 / title:1989 | in-window | 94,646 | 0 | 0 | - | VARIANT_TERM_HIT |
| `micro_IA40385013_0186` | 1991-01-01 / title:1991 | in-window | 164,349 | 6 | 4 | `cigna companies`, `cigna holdings` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `INAC2115_1979` l.1: INA Corporation/Annual Report 1979
- `INAC2115_1979` l.4: INA Corporation is among the nation’s oldest commercial
- `INAC2115_1979` l.36: INA Corporation Financial Highlights
- `assessingitperfo00wils` l.57: CIGNA  Corporation
- `cia-readingroom-document-cia-rdp84b00130r000600010246-7` l.27: Connecticut General has agreed to a withdrawal of 50 percent
- `cia-readingroom-document-cia-rdp84b00130r000600010246-7` l.30: opined that Connecticut General agreed in order to save the VIP account; he
- `cia-readingroom-document-cia-rdp88t00792r000300040001-2` l.1174: 18 November Economy-Disinvestment. US firm Cigna sells its South African operations to local
- `cia-readingroom-document-cia-rdp91-00929r000200960032-0` l.1071: water-~nitric acid system. CIGNA, Rez DI CAVE, S.ej3
- `cia-readingroom-document-cia-rdp90g00152r001102380002-3` l.1431: CIGNA
- `cia-readingroom-document-cia-rdp90g00152r001102380002-3` l.1436: The CIGNA Consumer Marketing Department offers
- `micro_IA41153629_0618` l.7: Connecticut General Assembly and the Connecticut
- `micro_IA41153629_0618` l.87: Education Committee of the Connecticut General Assembly
- `micro_IA41153629_0618` l.155: Connecticut General Assembly
- `ERIC_ED460893` l.41: The Connecticut General Assembly: Teacher's Manual for
- `ERIC_ED460893` l.80: and seven sections, including: (1) "Introduction to the Connecticut General
- `ERIC_ED460893` l.116: THE CONNECTICUT GENERAL ASSEMBLY
- `micro_IA40385019_1642` l.15: CONNECTICUT GENERAL LIFE INSURANCE COMPANY and
- `micro_IA40385019_1642` l.190: CONNECTICUT GENERAL LIFE INSURANCE COM-
- `micro_IA40385019_1642` l.203: Creative Bath Products, Inc. v. Connecticut General Life
- `micro_IA40385013_0186` l.6067: CIGNA Companies 1050 Connecticut Avenue, N.W.
- `micro_IA40385013_0186` l.6114: Connecticut General Corporation is CIGNA Holdings,
- `micro_IA40385013_0186` l.6115: Inc. The parent of CIGNA Holdings, Inc. is CIGNA
