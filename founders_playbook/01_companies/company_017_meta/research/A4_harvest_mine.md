# Harvest mining -- meta

Window applied: 2003-01-01 .. 2012-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

103 candidate rows in the harvest index; 12 items mined; 88 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 6 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 6 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `meta platforms`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `NASA_NTRS_Archive_20120010422` | 2012-01-01 / title:2012 | in-window | 11,766 | 3 | 0 | - | BARE_WORD_MATCH |
| `completeidiotsgu0000aber` | 2010-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `DTIC_ADA563444` | 2011-01-01 | in-window | 29,138 | 98 | 0 | - | BARE_WORD_MATCH |
| `DTIC_ADA500836` | 2009-01-01 | in-window | 37,565 | 117 | 0 | - | BARE_WORD_MATCH |
| `facebookallinone0000nels` | 2012-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `larevanchedunsol0000mezr` | 2009-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `networkednewsoci0000unse` | 2012-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `arxiv-1011.1970` | 2010-01-01 | in-window | 58,425 | 8 | 0 | - | BARE_WORD_MATCH |
| `arxiv-1111.4503` | 2011-01-01 | in-window | 51,587 | 78 | 0 | - | BARE_WORD_MATCH |
| `arxiv-1205.3643` | 2012-01-01 | in-window | 58,816 | 3 | 0 | - | BARE_WORD_MATCH |
| `entrepreneurs0000durm` | 2011-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `aarpfacebooktech0000coll_d2e0` | 2012-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `NASA_NTRS_Archive_20120010422` l.127: @ Space Operations Learning Center Facebook Application
- `NASA_NTRS_Archive_20120010422` l.136: Learning Center (SOLC) Facebook mo-
- `NASA_NTRS_Archive_20120010422` l.145: Spaceville will be a Facebook applica-
- `DTIC_ADA563444` l.3: Overcoming  Facebook  policies  that  put  users  at  risk
- `DTIC_ADA563444` l.8: Facing  the  Facebook
- `DTIC_ADA563444` l.14: Facebook.
- `DTIC_ADA500836` l.1: Harvesting  Ego-Network  Data  from  Facebook
- `DTIC_ADA500836` l.3: Using  the  CEMAP  Facebook  Profile  in  ORA
- `DTIC_ADA500836` l.59: Harvesting  Ego-Network  Data  from  Facebook.  Using  the  CEMAP
- `arxiv-1011.1970` l.24: likely to exist in many social networks, such as Facebook friendship networks. In this
- `arxiv-1011.1970` l.65: Fig. 1 Four communities of a single user (the node in black) of Facebook, as determined by
- `arxiv-1011.1970` l.117: analysis of a Facebook friendship network from five US universities.
- `arxiv-1111.4503` l.9: The Anatomy of the Facebook Social Graph
- `arxiv-1111.4503` l.13: 1 Facebook, Palo Alto, CA, USA
- `arxiv-1111.4503` l.25: ' We study the structure of the social graph of active Facebook users, the largest social network ever
- `arxiv-1205.3643` l.34: Facebook etc) typically do not contain instances of large
- `arxiv-1205.3643` l.898: cial networks (e.g. Twitter, Facebook etc.) do not contain
- `arxiv-1205.3643` l.932: software projects and several meta-data about the users and
