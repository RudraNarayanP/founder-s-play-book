# Harvest mining -- disney

Window applied: 1923-01-01 .. 1945-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

100 candidate rows in the harvest index; 12 items mined; 77 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 11 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 1 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `disney brothers studio`, `walt disney`, `walt disney productions`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `001.-walt-disney-company` | 1923-01-01 | in-window | 511,867 | 200 | 71 | `disney company`, `disney international`, `disney retail`, `disney stores`, `walt disney` | TIER1_CANDIDATE_TEXT |
| `Mickey_Mouse_His_Life_And_Art_1930-05` | 1930-01-01 / title:1930 | in-window | 226 | 0 | 0 | - | UNANSWERED |
| `wdp-annual-report-1972` | 1972-01-01 / title:1972 | outside? | 82,852 | 144 | 81 | `disney corporation`, `walt disney` | TIER1_CANDIDATE_TEXT |
| `wdp-annual-report-1974` | 1974-01-01 / title:1974 | outside? | 96,672 | 159 | 85 | `walt disney` | TIER1_CANDIDATE_TEXT |
| `1968-walt-disney-productions-annual-report` | 1968-01-01 / title:1968 | outside? | 57,372 | 78 | 50 | `walt disney`, `walt. disney` | TIER1_CANDIDATE_TEXT |
| `1971-walt-disney-productions-annual-report` | 1971-01-01 / title:1971 | outside? | 41,316 | 89 | 56 | `walt disney` | TIER1_CANDIDATE_TEXT |
| `wdp-annual-report-1967` | 1967-01-01 / title:1967 | outside? | 73,670 | 97 | 57 | `walt disney` | TIER1_CANDIDATE_TEXT |
| `wdp-annual-report-1983` | 1983-01-01 / title:1983 | outside? | 117,520 | 122 | 62 | `disney enterprises`, `walt disney` | TIER1_CANDIDATE_TEXT |
| `wdp-annual-report-1976` | 1976-01-01 / title:1976 | outside? | 62,135 | 58 | 33 | `walt disney` | TIER1_CANDIDATE_TEXT |
| `resort-report-1985-12-v-02-n-04` | 1985-01-01 / title:1985 | outside? | 13,814 | 14 | 9 | `walt disney` | TIER1_CANDIDATE_TEXT |
| `wdp-annual-report-1980` | 1980-01-01 / title:1980 | outside? | 104,942 | 106 | 75 | `disney enterprises`, `walt disney` | TIER1_CANDIDATE_TEXT |
| `wdp-annual-report-1977` | 1977-01-01 / title:1977 | outside? | 94,559 | 101 | 54 | `disney enterprises`, `walt disney` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `001.-walt-disney-company` l.141: THE WALT DISNEY COMPANY AND SUBSIDIARIES
- `001.-walt-disney-company` l.144: Consolidated Financial Information — The Walt Disney Company
- `001.-walt-disney-company` l.162: The Walt Disney Company, together with its subsidiaries, is a diversified worldwide entertainment company with
- `wdp-annual-report-1972` l.10: Look to the name Walt Disney
- `wdp-annual-report-1972` l.47: Walt Disney Productions’
- `wdp-annual-report-1972` l.73: Walt Disney, actress Margie Gay, Rudolf
- `wdp-annual-report-1974` l.36: of Walt Disney Productions are seven of the films which will
- `wdp-annual-report-1974` l.48: © 1974 Walt Disney Productions
- `wdp-annual-report-1974` l.75: ‘ciated with Walt Disney Productions, and this seems
- `1968-walt-disney-productions-annual-report` l.25: Walt Disney Productions
- `1968-walt-disney-productions-annual-report` l.37: Walt Disney
- `1968-walt-disney-productions-annual-report` l.81: Walt Disney World and Mineral King — the
- `1971-walt-disney-productions-annual-report` l.4: WALT DISNEY PRODUCTIONS
- `1971-walt-disney-productions-annual-report` l.10: THE WALT DISNEY WORLD GRAND OPENING SPECTACULAR AND DEDICATION CEREMONY
- `1971-walt-disney-productions-annual-report` l.13: “Walt Disney World is a tribute to the philosophy and life of
- `wdp-annual-report-1967` l.53: Walt Disney
- `wdp-annual-report-1967` l.119: ©1967 Walt Disney Productions
- `wdp-annual-report-1967` l.126: tory of Walt Disney Productions. For the first time since
- `wdp-annual-report-1983` l.89: Walt Disney Productions
- `wdp-annual-report-1983` l.112: place Walt Disney Productions on the
- `wdp-annual-report-1983` l.169: the 60th anniversary of Walt Disney
- `wdp-annual-report-1976` l.1: Annual Report 1976 Walt Disney Productions
- `wdp-annual-report-1976` l.19: tha Walt Disney Educational Media Company.
- `wdp-annual-report-1976` l.21: Walt Disney Archives and tha Studio s expanded
- `resort-report-1985-12-v-02-n-04` l.6: Walt Disney World®
- `resort-report-1985-12-v-02-n-04` l.104: WALT DISNEY WORLD ears Sgt Village:
- `resort-report-1985-12-v-02-n-04` l.225: WALT DISNEY WORLD VILLAGE
- `wdp-annual-report-1980` l.1: Walt Disney Productions 1980 Annual Report
- `wdp-annual-report-1980` l.55: Walt Disney Productions, 500 S. Buena Vista Street,
- `wdp-annual-report-1980` l.62: Suckhiolder Relanons Department, Walt Disney
- `wdp-annual-report-1977` l.2: Annual Report 1977 Walt Disney Productions
- `wdp-annual-report-1977` l.46: Walt Disney Productions continues to maintain the
- `wdp-annual-report-1977` l.54: Reinforced by this financial strength, Walt Disney
