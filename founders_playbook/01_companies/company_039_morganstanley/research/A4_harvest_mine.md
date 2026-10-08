# Harvest mining -- morganstanley

Window applied: 1924-01-01 .. 1960-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

73 candidate rows in the harvest index; 12 items mined; 59 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 3 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 1 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 8 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `morgan stanley`, `morgan stanley co`, `morgan stanley group`; **other quoted terms** (predecessors, siblings, trade titles): `dean witter`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `PvyrwBlrrQUC` | 1940-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `internetadvertis00mary` | 1997-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `rMA25YykAFQC` | 1989-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `sM-9EQAAQBAJ` | 2019-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `AKyGOCZWMJQC` | 1985-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `19890828-robert-baldwin-morgan-stanley-ceo-lodestar-group-chairman` | 1989-01-01 | outside? | 1,901 | 0 | 2 | `morgan stanley` | TIER1_CANDIDATE_TEXT |
| `houseofmorganame0000cher` | 1990-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `painewebberartco0000unse` | 1995-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.gpo.fdsys.CHRG-106hhrg66775` | 1999-01-01 | outside? | 929,463 | 0 | 7 | `morgan stanley` | TIER1_CANDIDATE_TEXT |
| `isbn_9780874208474` | 2000-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `witterunilifeblood00jeanrich` | 1967-01-01 / title:1967 | outside? | 237,480 | 0 | 0 | - | VARIANT_TERM_HIT |
| `micro_IA40386013_1278` | 1997-01-01 / title:1997 | outside? | 107,020 | 200 | 8 | `painewebber inc` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `19890828-robert-baldwin-morgan-stanley-ceo-lodestar-group-chairman` l.16: former Morgan Stanley chair-
- `19890828-robert-baldwin-morgan-stanley-ceo-lodestar-group-chairman` l.63: who built Morgan Stanley intoa
- `gov.gpo.fdsys.CHRG-106hhrg66775` l.170: Morgan Stanley Dean Witter & Co., Harvey B. Mogenson 106
- `gov.gpo.fdsys.CHRG-106hhrg66775` l.4439: Morgan Stanley, Dean
- `gov.gpo.fdsys.CHRG-106hhrg66775` l.8700: TOR, MORGAN STANLEY DEAN WITTER & CO.; ON BEHALF OF
- `witterunilifeblood00jeanrich` l.384: the  administration  office  of  Dean  Witter  &•
- `witterunilifeblood00jeanrich` l.464: Forming  Dean  Witter  &  Co.,  1924   35
- `witterunilifeblood00jeanrich` l.666: with  my  cousin,  Dean  Witter,  these  many  years,
- `micro_IA40386013_1278` l.93: 450 REC. confirming that Painewebber Inc. VIOLATED
- `micro_IA40386013_1278` l.97: Painewebber Inc. for the purpose of defrauding me?
- `micro_IA40386013_1278` l.189: 14. Is the Supreme Court aware that Painewebber Inc.
