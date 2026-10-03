# Chronicling America endpoint test -- 2026-10-03T11:53:41Z

Run from the GitHub Actions egress (or any host) to decide which URL shape answers, because
from this project's development machine every shape 403s and a 403 cannot be told apart from
a wrong path. `periodical_harvest.py` currently uses `www.loc.gov/chroniclingamerica` +
`/search/pages/results/?format=json`, which has returned **404** on every nightly run so far
(2026-09-27, -28, -29), so its 209 CA rows carry 0 answers and 122 UNANSWERED.

| shape | verdict | status | bytes | detail |
|---|---|---|---|---|
| `loc-global-chronicling-america` | CHALLENGED | 403 | 5,965 | Cloudflare bot challenge |
| `loc-global-fa-collection` | CHALLENGED | 403 | 5,953 | Cloudflare bot challenge |
| `ca-legacy-pages-results` | NOT-FOUND | 404 | 84,977 | 404 -- the path does not exist (our own defect, not a block) |
| `ca-legacy-newspapers-api` | CHALLENGED | 403 | 5,977 | Cloudflare bot challenge |
| `cronidam-new-api` | NOT-FOUND | 404 | 2,325 | 404 -- the path does not exist (our own defect, not a block) |
| `www-chroniclingamerica-path` | NOT-FOUND | 404 | 84,986 | 404 -- the path does not exist (our own defect, not a block) |
| `www-collections-page-json` | CHALLENGED | 403 | 5,902 | Cloudflare bot challenge |

**Probe query:** `"Wal-Mart" Bentonville` (1960-1969), chosen because the corpus is being mined for exactly this phrase and the collection advertises open OCR full text 1777-2016 -- so a working route should not return zero.

**Reading the verdict:**
- `ANSWERED` -- this shape is the one to use. Open the body, find the total field, and point `CA_BASE` / `ca_search_url` at it; then re-run the CA tasks and re-classify.
- `NOT-FOUND` -- path defect (ours). Not evidence about the corpus.
- `FORBIDDEN`/`CHALLENGED` -- egress block. Still UNANSWERED, never a null, and it does not mean the path is wrong.
- `NOT-JSON` -- right host, wrong format parameter.
- A count from a shape whose schema you have not opened is NOT a null. Read the body first (RD-121/RD-124: three fleet verdicts came from trusting a number nobody had opened).

**ANSWERED shapes:** **none** -- every candidate failed; the route is still UNTRIED and no CA zero may be cited as a null.

