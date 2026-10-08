# Harvest mining -- exxonmobil

Window applied: 1866-01-01 .. 1999-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

134 candidate rows in the harvest index; 12 items mined; 109 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 2 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 7 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 3 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `exxon mobil corp`, `exxonmobil holdings`; **other quoted terms** (predecessors, siblings, trade titles): `exxon corporation`, `mobil oil`, `standard oil`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `mobrat00unit` | 1976-01-01 | in-window | 121,995 | 200 | 1 | `exxon  corp` | TIER1_CANDIDATE_TEXT |
| `standard-oil-company-of-california-annual-report-1956` | 1957-01-01 / title:1956 | in-window MISMATCH | 68,405 | 0 | 0 | - | VARIANT_TERM_HIT |
| `standard-oil-company-of-california-annual-report-1957` | 1958-01-01 / title:1957 | in-window MISMATCH | 67,323 | 0 | 0 | - | VARIANT_TERM_HIT |
| `pureoiltrustvsst00oilc` | 1901-01-01 | in-window | 3,294,656 | 0 | 0 | - | VARIANT_TERM_HIT |
| `standard-oil-company-of-california-annual-report-1958` | 1959-01-01 / title:1958 | in-window MISMATCH | 75,124 | 0 | 0 | - | VARIANT_TERM_HIT |
| `pureoiltrustvss00derrgoog` | 1901-01-01 | in-window | 3,193,448 | 0 | 0 | - | VARIANT_TERM_HIT |
| `standard-oil-company-of-california-annual-report-1959` | 1960-01-01 / title:1959 | in-window MISMATCH | 69,335 | 0 | 0 | - | VARIANT_TERM_HIT |
| `standard-oil-company-of-california-annual-report-1960` | 1961-01-01 / title:1960 | in-window MISMATCH | 71,360 | 0 | 0 | - | VARIANT_TERM_HIT |
| `micro_IA41153045_0441` | 1975-01-01 | in-window | 5,585 | 4 | 0 | - | BARE_WORD_MATCH |
| `micro_IA41153438_0701` | 1977-01-01 | in-window | 195,001 | 15 | 0 | - | BARE_WORD_MATCH |
| `micro_IA41155163_0728` | 1984-01-01 | in-window | 47,553 | 8 | 1 | `exxon corp` | TIER1_CANDIDATE_TEXT |
| `micro_IA41152954_0005` | 1985-01-01 | in-window | 65,522 | 5 | 0 | - | BARE_WORD_MATCH |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `mobrat00unit` l.2406: minimum  daily  delivery  obligation"  condition.  See.  for  example,  Exxon  Corp..
- `standard-oil-company-of-california-annual-report-1956` l.61: STANDARD OIL COMPANY OF CALIFORNIA < \
- `standard-oil-company-of-california-annual-report-1956` l.102: STANDARD OIL COMPANY OF CALIFORNIA
- `standard-oil-company-of-california-annual-report-1956` l.573: .. In Standard Oil
- `standard-oil-company-of-california-annual-report-1957` l.600: STANDARD OIL COMPANY OF CALIFORNIA
- `standard-oil-company-of-california-annual-report-1957` l.633: their chief areas of interest were Standard Oil
- `standard-oil-company-of-california-annual-report-1957` l.637: Mountain areas; Standard Oil Company of
- `pureoiltrustvsst00oilc` l.50: STANDARD  OIL  COMPANY,
- `pureoiltrustvsst00oilc` l.96: It  soon  became  evident  that  the  Standard  Oil  Company  was  to  be  the  chief
- `pureoiltrustvsst00oilc` l.99: active  competitor  of  the  Standard  Oil  Company,  presided  at  nearly  all  of  the
- `standard-oil-company-of-california-annual-report-1958` l.24: Standard Oil Company of California 1958 Annual Report
- `standard-oil-company-of-california-annual-report-1958` l.62: Standard Oil Company of California
- `standard-oil-company-of-california-annual-report-1958` l.168: Standard Oil Company of California
- `pureoiltrustvss00derrgoog` l.67: STANDARD  OIL  COMPANY,
- `pureoiltrustvss00derrgoog` l.99: It  soon  became  evident  that  the  Standard  Oil  Company  was  to  be  the  chief
- `pureoiltrustvss00derrgoog` l.102: active  competitor  of  the  Standard  Oil  Company,  presided  at  nearly  all  of  the
- `standard-oil-company-of-california-annual-report-1959` l.40: Standard Oil Company of California
- `standard-oil-company-of-california-annual-report-1959` l.560: Standard Oil Company of California
- `standard-oil-company-of-california-annual-report-1959` l.596: Standard Oil Company of California, Western
- `standard-oil-company-of-california-annual-report-1960` l.8: ww STANDARD OIL COMPANY OF CALIFORNIA
- `standard-oil-company-of-california-annual-report-1960` l.38: Standard Oil Company of California
- `standard-oil-company-of-california-annual-report-1960` l.1767: STANDARD OIL COMPANY OF CALI FORNIA, SUR eat eee AND pores ial
- `micro_IA41153045_0441` l.33: Exxon Research and Engineering Co., Linden, N.J.
- `micro_IA41153045_0441` l.49: Exxon Research and Engineering Company
- `micro_IA41153045_0441` l.76: information services at the Exxon Research and Engineering Company
- `micro_IA41153438_0701` l.10: INSTITUTION Exxon Research and Engineering Co., Linden, N.J.
- `micro_IA41153438_0701` l.15: REPORT NO EXXON /GERU.1IDK.77
- `micro_IA41153438_0701` l.103: Exxon Research and Engineering Company
- `micro_IA41155163_0728` l.11: INSTITUTION EXXON Corp., New York, N.Y.
- `micro_IA41152954_0005` l.10: INSTITUTION EXXON Education Foundation, New York, N.Y.
- `micro_IA41152954_0005` l.70: THE EXXON EDUCATION FOUNDATION
- `micro_IA41152954_0005` l.250: addition to the Exxon Education Foundation (EEF); the Rockefeller
