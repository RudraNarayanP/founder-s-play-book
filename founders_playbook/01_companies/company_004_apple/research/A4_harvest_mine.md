# Harvest mining -- apple

Window applied: 1975-01-01 .. 1980-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

179 candidate rows in the harvest index; 12 items mined; 154 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 6 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 5 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 1 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `apple computer`, `apple ii`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `micro_IA41153056_0224` | 1976-01-01 / title:1973 | in-window MISMATCH | 447,400 | 162 | 2 | `apple computer` | TIER1_CANDIDATE_TEXT |
| `reciprocalevalua00prog` | 1976-01-01 | in-window | 84,319 | 6 | 0 | - | BARE_WORD_MATCH |
| `annualcourseconf00spea` | 1976-01-01 | in-window | 47,570 | 20 | 0 | - | BARE_WORD_MATCH |
| `pahukaniluahomes00appl` | 1978-01-01 | in-window | 175,207 | 13 | 0 | - | BARE_WORD_MATCH |
| `reciprocalevalua00loya` | 1977-01-01 | in-window | 78,742 | 6 | 0 | - | BARE_WORD_MATCH |
| `nD4EAAAAMBAJ` | 1980-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `byte-may-1977` | 1977-01-01 / title:1977 | in-window | 709,824 | 55 | 8 | `apple computer`, `apple-ii` | TIER1_CANDIDATE_TEXT |
| `byte-magazine-1977-04` | 1977-01-01 | in-window | 681,576 | 19 | 0 | - | BARE_WORD_MATCH |
| `byte-magazine-1980-04` | 1980-01-01 | in-window | 1,280,581 | 200 | 88 | `apple computer`, `apple corporation`, `apple ii` | TIER1_CANDIDATE_TEXT |
| `byte-sept-1977` | 1977-01-01 / title:1977 | in-window | 843,147 | 25 | 22 | `apple computer`, `apple ii` | TIER1_CANDIDATE_TEXT |
| `byte-magazine-1979-04` | 1979-01-01 | in-window | 1,186,876 | 113 | 61 | `apple computer`, `apple ii`, `apple inc` | TIER1_CANDIDATE_TEXT |
| `byte-magazine-1980-11` | 1980-01-01 | in-window | 2,421,368 | 200 | 168 | `apple    computer`, `apple    ii`, `apple  computer`, `apple  computers`, `apple  corporation`, `apple  ii`, `apple ii`, `apple. computer` | TIER1_CANDIDATE_TEXT |

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
- `reciprocalevalua00loya` l.28: Loyal  E.  Apple,  Executive  Director
- `reciprocalevalua00loya` l.160: Director,  Mr.  Loyal  E.  Apple,  they  were  shown  some  of  the  aids  and
- `reciprocalevalua00loya` l.189: The  delegation  then  conferred  with  Mr.  Apple  and  the  Department  Directors
- `byte-may-1977` l.455: 34 THE APPLE-II Judith Havey
- `byte-may-1977` l.612: Apple Computer describes the design
- `byte-may-1977` l.5361: Apple Computer Co
- `byte-magazine-1977-04` l.812: A Nybble on the Apple
- `byte-magazine-1977-04` l.2673: A Nybble on the Apple
- `byte-magazine-1977-04` l.2683: Wozniac, designer of the Apple-U computer,
- `byte-magazine-1980-04` l.113: Here is a simple interface you can add to an Apple II to allow audio input and output.
- `byte-magazine-1980-04` l.218: for the Apple II
- `byte-magazine-1980-04` l.546: Apple Computer
- `byte-sept-1977` l.1126: Like Apple Computer,
- `byte-sept-1977` l.2287: Introducing Apple II.
- `byte-sept-1977` l.2304: Apple II* and connect any standard
- `byte-magazine-1979-04` l.384: 20 CROSS-POLLINATING THE APPLE II, by Richard Campbell
- `byte-magazine-1979-04` l.609: Apple II. Richard Campbell gets to the core
- `byte-magazine-1979-04` l.611: Apple II. page 20
- `byte-magazine-1980-11` l.369: 148  THREE-DIMENSIONAL  GRAPHICS  FOR  THE  APPLE  II  by  Dan  Sokol  and  John
- `byte-magazine-1980-11` l.1934: the  Apple  II "computer.
- `byte-magazine-1980-11` l.1997: APPLE™  is  a  registered  trademark  of  APPLE  COMPUTER,  INC.
