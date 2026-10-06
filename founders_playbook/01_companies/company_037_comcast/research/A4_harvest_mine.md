# Harvest mining -- comcast

Window applied: 1963-01-01 .. 1990-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

52 candidate rows in the harvest index; 12 items mined; 39 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 2 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 4 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 6 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `comcast corporation`; **other quoted terms** (predecessors, siblings, trade titles): `cable television`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `bc-1988-01-04` | 1988-01-01 / title:1988 | in-window | 487,203 | 15 | 0 | - | VARIANT_TERM_HIT |
| `bc-1987-11-23` | 1987-01-01 / title:1987 | in-window | 501,915 | 14 | 0 | - | VARIANT_TERM_HIT |
| `bc-1989-01-16` | 1989-01-01 / title:1989 | in-window | 647,970 | 7 | 2 | `comcast corp` | TIER1_CANDIDATE_TEXT |
| `bc-1990-05-28` | 1990-01-01 / title:1990 | in-window | 507,743 | 12 | 0 | - | VARIANT_TERM_HIT |
| `bc-1988-11-14` | 1988-01-01 / title:1988 | in-window | 575,822 | 8 | 2 | `comcast corporation` | TIER1_CANDIDATE_TEXT |
| `bc-1988-11-07` | 1988-01-01 / title:1988 | in-window | 472,585 | 5 | 0 | - | VARIANT_TERM_HIT |
| `F4AUAQAAMAAJ` | 1988-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `-L0gAQAAMAAJ` | 1989-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `-0eTDAAAQBAJ` | 2016-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `nmthncESYIoC` | 2012-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `SVrsDwAAQBAJ` | 2020-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `ooCghX5smGYC` | 2014-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `bc-1988-01-04` l.788: Cable regulation. National Cable Television
- `bc-1988-01-04` l.1572: George Gillett Jr 00.5. Cable Television
- `bc-1988-01-04` l.2075: Jan. 11—/ndiana Cable Television Association annu-
- `bc-1987-11-23` l.321: ranging study of cable television
- `bc-1987-11-23` l.456: invited National Cable Television
- `bc-1987-11-23` l.903: tions barring them Irom entering cable television
- `bc-1989-01-16` l.15650: chief financial officer of Comcast Corp.,
- `bc-1989-01-16` l.16218: lyn along with MSO's Comcast Corp. and
- `bc-1990-05-28` l.80: National Cable Television Association holds its
- `bc-1990-05-28` l.1901: July 15-18—Cable Television Administration
- `bc-1990-05-28` l.1913: Southern Cable Television Association. Washing
- `bc-1988-11-14` l.18769: Comcast Corporation
- `bc-1988-11-07` l.240: Cable television industry remains under fire
- `bc-1988-11-07` l.567: tem operators, Cable Television Laboratories
- `bc-1988-11-07` l.1301: National Cable Television Association re-
