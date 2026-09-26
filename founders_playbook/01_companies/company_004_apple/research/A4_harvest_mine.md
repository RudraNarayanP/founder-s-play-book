# Harvest mining -- apple

Window applied: 1975-01-01 .. 1980-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

95 candidate rows in the harvest index; 4 items mined; 86 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 1 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 3 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `apple computer`, `apple ii`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `micro_IA41153056_0224` | 1976-01-01 / title:1973 | in-window MISMATCH | 447,400 | 162 | 2 | `apple computer` | TIER1_CANDIDATE_TEXT |
| `reciprocalevalua00prog` | 1976-01-01 | in-window | 84,319 | 6 | 0 | - | BARE_WORD_MATCH |
| `annualcourseconf00spea` | 1976-01-01 | in-window | 47,570 | 20 | 0 | - | BARE_WORD_MATCH |
| `pahukaniluahomes00appl` | 1978-01-01 | in-window | 175,207 | 13 | 0 | - | BARE_WORD_MATCH |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `micro_IA41153056_0224` l.307: use of tt APPLE computer programs, contributed
- `reciprocalevalua00prog` l.31: Loyal  E.  Apple,  Executive  Director
- `reciprocalevalua00prog` l.172: Director,  Mr.  Loyal  E.  Apple,  they  were  shown  some  of  the  aids  and
- `reciprocalevalua00prog` l.206: The  delegation  then  conferred  with  Mr.  Apple  and  the  Department  Directors
- `annualcourseconf00spea` l.27: Speakers/Tutors  - Mr  E Apple,  Executive  Director,  American
- `annualcourseconf00spea` l.28: Foundation  for  the  Blind,  Inc.,  New  York;  Mrs  Marianne  Apple.
- `annualcourseconf00spea` l.53: Mr  cind  Mrs  L Apple,  representing  the  American  Founcition  for  the  *
- `pahukaniluahomes00appl` l.30: Russell  A.  Apple,
- `pahukaniluahomes00appl` l.222: Peg  Apple,  wife  and  my  frequent  collaborator,  has   ridden  herd
- `pahukaniluahomes00appl` l.226: Russell  A.  Apple,
