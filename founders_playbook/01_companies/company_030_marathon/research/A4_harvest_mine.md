# Harvest mining -- marathon

Window applied: 1887-01-01 .. 2011-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

71 candidate rows in the harvest index; 12 items mined; 58 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 6 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 1 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 2 | text held, zero hits. |
| `UNANSWERED` | 3 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `marathon oil`, `marathon petroleum`; **other quoted terms** (predecessors, siblings, trade titles): `midwest oil`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `kMeudoDQwpUC` | 2003-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `internationaldir0000unse_o5t3` | 2010-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `cia-readingroom-document-cia-rdp87t00685r000200400003-1` | 1986-01-01 / title:2004 | in-window MISMATCH | 133,241 | 1 | 1 | `marathon petroleum` | TIER1_CANDIDATE_TEXT |
| `PanO0734_1971` | 1971-01-01 / title:1971 | in-window | 53,904 | 0 | 0 | - | NULL |
| `gov.gpo.fdsys.CHRG-107shrg89115` | 2002-01-01 | in-window | 177,615 | 3 | 2 | `marathon oil` | TIER1_CANDIDATE_TEXT |
| `cia-readingroom-document-cia-rdp89-01114r000100020067-1` | 1973-01-01 / title:2006 | in-window MISMATCH | 3,773 | 1 | 0 | - | BARE_WORD_MATCH |
| `gov.gpo.fdsys.CHRG-108shrg95501` | 2004-01-01 | in-window | 2,708,281 | 200 | 39 | `marathon oil` | TIER1_CANDIDATE_TEXT |
| `micro_IA40385601_1436` | 1964-01-01 / title:1964 | in-window | 202,888 | 13 | 9 | `marathon oil` | TIER1_CANDIDATE_TEXT |
| `micro_IA40385018_0456` | 1985-01-01 / title:1985 | in-window | 184,675 | 56 | 24 | `marathon oil` | TIER1_CANDIDATE_TEXT |
| `formermarathonoi00illi` | 2009-01-01 | in-window | 3,661 | 0 | 0 | - | NULL |
| `micro_IA40385605_1089` | 1971-01-01 / title:1971 | in-window | 136,301 | 93 | 16 | `marathon oil` | TIER1_CANDIDATE_TEXT |
| `environmentalris0000vict` | 2004-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp87t00685r000200400003-1` l.3963: Marathon Petroleum pipelines near Munich. | 25X11
- `gov.gpo.fdsys.CHRG-107shrg89115` l.1976: MARATHON OIL COMPANY PROFESSOR OF ENERGY POLICY
- `gov.gpo.fdsys.CHRG-107shrg89115` l.3462: Marathon Oil Company Professor of Energy Policy
- `cia-readingroom-document-cia-rdp89-01114r000100020067-1` l.115: Marathon 071
- `gov.gpo.fdsys.CHRG-108shrg95501` l.299: Steven P. Guidry, Central Africa Business Unit Leader, Marathon Oil Com-
- `gov.gpo.fdsys.CHRG-108shrg95501` l.720: Marathon Oil Company 870
- `gov.gpo.fdsys.CHRG-108shrg95501` l.722: b. Correspondence sent on behalf of Marathon Oil Company, dated Sep-
- `micro_IA40385601_1436` l.32: MARATHON OIL COMPANY;
- `micro_IA40385601_1436` l.213: MARATHON OIL: COMPANY,”
- `micro_IA40385601_1436` l.1169: 1. On Marathon Oil Cempany and The Pardee Com-
- `micro_IA40385018_0456` l.21: MARATHON OIL COMPANY, an Ohio corporation.
- `micro_IA40385018_0456` l.179: Tenneco West, Inc. v. Marathon Oil Co., 564 F.Supp.
- `micro_IA40385018_0456` l.185: Tenneco West, Inc. v. Marathon Oil Co., 756 F.2d 769
- `micro_IA40385605_1089` l.7: MARATHON OIL COMPANY » @ Corporation; and
- `micro_IA40385605_1089` l.28: Marathon Oil Company
- `micro_IA40385605_1089` l.207: MARATHON OIL COMPANY, a corporation; and
