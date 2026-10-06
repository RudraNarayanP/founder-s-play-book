# cdx_intake build report — corpus family (b), web archives, gets a scripted route

Owner: `cdx-intake` (tooling agent). Built 2026-10-06. Files written: `tools/cdx_intake.py`,
`tools/web_domains.json`, `founders_playbook/01_companies/{company_019_centene,
company_010_cencora, company_018_elevance, company_030_marathon, company_011_microsoft}/sources/web_archive/**`,
this report, and `03_quality_control/{centene,cencora,elevance,marathon,microsoft}_cdx_gates.md`.
`tools/queries.json`, `tools/sec_intake.py`, `tools/gates.py`, `tools/periodical_harvest.py`,
registers, volumes and `_parts/` were NOT touched. `harvest_mine.py` / `periodical_harvest.py`
were not run.

## 1. Why this file exists

Method §15.2 sets a tier from how many of five corpus families return in-window Tier-1 text.
`tools/queries.json` carries 427 tasks across `chronicling_america / internet_archive /
corporate_print / hathitrust / google_books` and **nothing for web archives**, so every verdict
in the fleet has been structurally four-family. Microsoft held family-(b) artefacts only because
an agent wrote an ad-hoc curl, and Microsoft's audit NR-1 caught the class that produced: a dead
route written up as if it had been tested (`"http_status": 503, "verdict": "UNANSWERED (service
503, not an empty result)"`, two identical 11,832-byte "Internet Archive: Temporarily Offline"
bodies). Those four files were read first and are now the self-test fixture.

## 2. CLI surface (verbatim from the build)

```
python tools/cdx_intake.py enumerate --domain centene.com --from 1996 --to 2002 [--limit 500]
python tools/cdx_intake.py run --slug centene,cencora [--per-domain 8] [--max-requests 60]
                               [--company-root founders_playbook/01_companies] [--dry-run]
                               [--skip-stored] [--allow-insecure] [--limit 500] [--max-bytes 1500000]
python tools/cdx_intake.py audit --company-dir <dir>      # re-verify bytes against sidecars
python tools/cdx_intake.py selftest                       # or: --self-test   (no network)
```

* `run` reads the domain list from `tools/web_domains.json` (slug → `[{domain, window, why,
  source_line}]`) and resolves `company_0NN_<slug>` dirs itself; `--company-dir` overrides.
* CDX shape used: `https://web.archive.org/cdx/search/cdx?url=<domain>&matchType=domain
  &from=YYYY&to=YYYY&output=text&fl=timestamp,original,mimetype,statuscode,length,digest
  &collapse=timestamp:6&limit=<n>`. Every row records url / timestamp / mimetype / statuscode /
  length (+ digest). Snapshot bytes come from `https://web.archive.org/web/<ts>id_/<original>`
  (`id_` = as captured, no IA toolbar).
* Pacing ≥1 s per host (`POLITE_SECONDS = 1.0`), backoff (10, 20, 40) s on 429/5xx, and a hard
  `--max-requests` cap for the whole process; the cap is armed before any command can reach the
  network so `enumerate` cannot run against an unarmed budget.
* Exit codes: 0 all slots clean, 1 partial (any UNANSWERED / NULL / UNTRIED), 2 identity broken.

## 3. The four states, and how a refusal cannot become a null

`ANSWERED` (bytes stored + sidecar + sha256 verified) · `NULL` (CDX answered and the window holds
no storable capture — a tested emptiness) · `UNANSWERED` (4xx/5xx/timeout/challenge/200-with-
apology-body; a remedy is named in the sidecar/artefact and in `_RUN.json`) · `UNTRIED` (no cited
domain / dry run / budget unspent).

Three structural guarantees, not prose rules:

1. `classify_cdx` **parses first, then looks for a lie**: a status 200 body that yields rows is an
   answer; only a body that yields none is tested against `CDX_LIE_MARKERS`. (The first live run
   inverted this order and mis-classified `centene.com 1996-2002` as UNANSWERED because 159
   genuine rows contain archived URLs matching `robots.txt` / `challenge` — a false negative in
   the safety direction, found and fixed live, and the fix is now self-tested.)
2. An `UNANSWERED` slot carries `captures = None`, never `0`. `_verify_slot()` fails the run if a
   refusal arrives with a count, and `print_slots()` **raises** rather than print one — so "0
   captures" cannot reach a dossier from this tool.
3. NULL is split honestly: `NULL (0 captures in window)` and `NULL (1 capture in window, 0
   fetchable as 200 text)`. The second one exists because `bcbskc.org 1996-2014` measured exactly
   that live — one capture, a `410` robots.txt. Filing it UNANSWERED would send a re-grade agent
   to retry a route that already gave its answer, which is the mirror image of the NR-1 defect.

Per-state artefacts (`<domain>_<window>.NULL.md`, `.UNANSWERED.md`) are written beside the bytes
so a dead route is a filed finding with a date, not an absence.

## 4. Self-test table — `python tools/cdx_intake.py --self-test` → **37 checks, 0 failures, PASS**

| planted defect | result |
|---|---|
| (a) CDX 503 → UNANSWERED, never NULL | FIRED |
| (a) Microsoft 503 fixture found on disk | FIRED |
| (a) IA 'Temporarily Offline' under status 200 → UNANSWERED | FIRED |
| (a) same fixture at its recorded status 503 → UNANSWERED | FIRED |
| (a) UNANSWERED names a remedy | FIRED |
| (a) str marker cannot enter CDX_LIE_MARKERS | FIRED |
| (a) malformed row counted, never silently dropped | FIRED |
| (a) budget exhaustion → UNANSWERED, not NULL | FIRED |
| (a) budget remedy names --max-requests | FIRED |
| (b) CDX 200 + zero bytes → NULL | FIRED |
| (b) CDX 200 + whitespace only → NULL | FIRED |
| (b) unparseable-but-nonempty → UNANSWERED, not NULL | FIRED |
| (b) answered-but-nothing-fetchable → NULL, not UNANSWERED | FIRED |
| (b) an enumeration that hits --limit is labelled a FLOOR, not a census | FIRED |
| (b) the same answer under a generous --limit is not called capped | STAYS CLEAN |
| (b) ranking spreads across the window, not one year | FIRED |
| (b) non-200 and tiny captures are not fetched | FIRED |
| (c) fixture run stores bytes | FIRED |
| (c) clean pair passes audit | STAYS CLEAN |
| (c) planted sha256 mismatch IS caught | FIRED |
| (c) planted orphan body IS caught | FIRED |
| (c) a legacy `.sidecar.json` sibling is a shape note, not an orphan finding | STAYS CLEAN |
| (d) pre-existing bytes untouched | FIRED |
| (d) new capture versioned beside it (`_v2`) | FIRED |
| (d) --skip-stored fetches nothing already on disk, slot stays ANSWERED | FIRED |
| (e) identity holds on a four-state run | FIRED |
| (e) all four states present and distinct | FIRED |
| (e) NULL is not UNANSWERED and vice versa | FIRED |
| (e) identity FIRES when a row goes missing | FIRED |
| (e) identity FIRES on a double-counted slot | FIRED |
| (e) refusal carrying captures=0 is caught | FIRED |
| (e) UNANSWERED lines print no capture count | FIRED |
| (e) the printer RAISES on a refusal carrying captures=0 | FIRED |
| (e) _RUN.json written with the identity | FIRED |
| (e) _RUN.json carries no UNANSWERED-with-count | FIRED |
| (e) dry run → UNTRIED, no bytes claimed | FIRED |
| NEGATIVE CONTROL: clean run produces zero findings | STAYS CLEAN |

The identity is `answered + null + unanswered + untried = raw / unique slots vs attempted`, with
`attempted` taken from the **plan** (the number of cited domains), so a slot that never reaches a
bucket breaks it — the D-3 lesson from sec_intake, where an attempted derived from the rows could
not fail.

## 5. Provenance written

No-clobber: `no_clobber_path()` never overwrites — a colliding capture is written as `_v2` beside
the original and the sidecar records `no_clobber`; run records are versioned aside (`_RUN.prev-
<stamp>.json`, two of them exist from tonight's passes). Sidecar is written **before** the body, so
an interrupted run leaves a detectable sidecar-without-bytes rather than orphan bytes. `_RUN.json`
per company dir carries the identity, per-slot rows, `requests_used` and the policy block.
`audit_dir()` re-hashes everything on disk.

### Sidecar schema, verbatim (`<company>/sources/web_archive/*.html.meta.json`)

```json
{
 "url": "http://www.centene.com:80/accompindex.html",
 "timestamp": "19990903002137",
 "requested_url": "https://web.archive.org/web/19990903002137id_/http://www.centene.com:80/accompindex.html",
 "http_status": 200,
 "bytes": 5429,
 "sha256": "29f084d46a7b6306568f87e9b0eb8dbaeff9e563a1668f36701d0cd1f9e7ab08",
 "transport": "ok",
 "verdict": "ANSWERED",
 "mimetype": "text/html",
 "cdx_length": "2438",
 "cdx_digest": "52JVUSH73GDM7DEONCH3GW3ND7DA4THP",
 "family": "(b) web archives",
 "fetched_utc": "2026-10-06T12:34:53Z",
 "domain": "centene.com",
 "window": "1996-2002",
 "slug": "centene",
 "company_dir": "E:\\founder's playbook\\founders_playbook\\01_companies\\company_019_centene",
 "why": "Stage 1/2 web presence of the registrant itself; the probe called family (b) the cheapest way to open a genuine second in-window Tier-1 family because the filings here are one self-reciting lineage.",
 "source_line": "founders_playbook/01_companies/company_019_centene/research/A_chronology_feasibility.md l.88 and l.97 (FR-1: CDX snapshot set for centene.com + coordinatedcare.com over 1996-01-01..2002-12-31); domain self-declared in sources/sec/0000950109-01-504218_ds1.txt:374 'The address of our Web site is www.centene.com'",
 "cdx_url": "https://web.archive.org/cdx/search/cdx?url=centene.com&matchType=domain&from=1996&to=2002&output=text&fl=timestamp,original,mimetype,statuscode,length,digest&collapse=timestamp%3A6&limit=500",
 "path": "centene.com_19990903002137.html"
}
```

The eight required keys are the first eight; the rest is provenance (why the domain is in the list
and which filing line said so). `transport` is `ok` for every byte stored tonight — no fetch needed
`--allow-insecure`, so nothing on disk is unverified-TLS.

## 6. Measured live, per state (final passes; re-measured after the last write)

10 domains × windows, all enumerated against `web.archive.org`. Pass totals: 23 + 10 + 23 + 15 + 3
+ 3 requests ≈ 77 HTTP calls, every one ≥1 s apart per host, each pass under its own
`--max-requests` cap.

| slug | domain | window | state | http | captures | bodies on disk | earliest stored capture (ts / status / bytes) |
|---|---|---|---|---|---|---|---|
| centene | centene.com | 1996-2002 | ANSWERED | 200 | 159 | 6 | 19990903002137 / 200 / 5,429 |
| centene | coordinatedcare.com | 1996-2002 | ANSWERED | 200 | 500 (capped, floor) | 6 | 20000301174012 / 200 / 6,310 |
| cencora | amerisource.com | 1994-2001 | ANSWERED | 200 | 500 (capped, floor) | 6 | 19961022234939 / 200 / 905 |
| cencora | bergenbrunswig.com | 1994-2001 | ANSWERED | 200 | 500 (capped, floor) | 6 | 19961226045542 / 200 / 3,278 |
| elevance | anthem.com | 1996-2014 | ANSWERED | 200 | 500 (capped, floor) | 6 | 19970530121040 / 200 / 5,764 |
| elevance | wellpoint.com | 1996-2014 | ANSWERED | 200 | 500 (capped, floor) | 6 | 19970708183823 / 200 / 248 |
| elevance | bcbskc.org | 1996-2014 | **NULL** | 200 | **1** (a 410 robots.txt; 0 fetchable) | 0 | — window tested, no bytes |
| microsoft | microsoft.com | 1994-2002 | ANSWERED | 200 | 500 (capped, floor) | 5 | 19961020014044 / 200 / 10,491 |
| microsoft | www.microsoft.com | 1994-2002 | ANSWERED | 200 | 500 (capped, floor) | 5 | 19961020014044 / 200 / 10,491 (same capture as the row above, re-stemmed) |
| marathon | marathonpetroleum.com | 2011-2015 | ANSWERED | 200 | 500 (capped, floor) | 6 | 20110207202905 / 200 / 36,168 |

Fleet state totals across the 10 slots, last pass per company: **ANSWERED 9, NULL 1, UNANSWERED 0,
UNTRIED 0** (identities OK in all five `_RUN.json`: centene 2/2, cencora 2/2, elevance 3/3,
microsoft 2/2, marathon 1/1). Bodies stored on disk: 12 centene, 12 cencora, 12 elevance, 10
microsoft, 6 marathon = **52**, each with a `.meta.json` (`audit` reports 0 findings on centene,
cencora, elevance, marathon; microsoft 0 findings + 2 shape notes for the pre-existing
`.sidecar.json` fixtures, which are not mine and were not touched).

Two UNANSWERED states occurred mid-build and are now closed, both by re-measurement rather than
by editing:
* `centene.com 1996-2002` first pass (marker-order defect, described in §3) → superseded; the
  artefact is preserved as `centene.com_1996_2002.UNANSWERED.superseded-20261006T1805Z.md`.
* `bcbskc.org 1996-2014` first pass (CDX returned 200 with an HTML body) → re-tested and answered,
  so it is now the NULL above; preserved as `bcbskc.org_1996_2014.UNANSWERED.superseded-by-NULL-recheck.md`.

### UNTRIED, left on purpose

* `--slug relevance` (a slug with no cited domain) printed one UNTRIED row, spent **0 requests**
  and wrote nothing: `UNTRIED — supply a cited domain in tools/web_domains.json`. This is the live
  shape of the fleet gap for **ups, comcast, verizon** and every other company not in
  `tools/web_domains.json`. Their windows are *untested*, not empty, and no tier may move on them
  until an agent with a filing or dossier line adds the domain — inventing one is refused by the
  schema (`source_line` is mandatory and copied into every sidecar).
* Pre-1996 coverage was not attempted for any company; per §6, `centene.com` enumerates only 159
  captures for 1996-2002 and its earliest is 1999-09-03, so the 1996-1998 sub-window should be
  enumerated separately before anyone calls it a null.

## 7. Gates

`python tools/gates.py --company-dir <dir> --checks csv,keys --fail-on substantive --out
03_quality_control/<slug>_cdx_gates.md` — run for centene, cencora, elevance, marathon, microsoft.
All five **exit 0**; every finding reported is coverage-only ("a gate had no input yet"), 2 of 2
per company for the four tail dirs and 0 for microsoft's `csv`/`keys` lines
(`channels.csv.source_id all S#### tokens resolve`, `stage_1.md 22 source tokens all resolve`). No
substantive finding is attributable to any file written here — the intake writes only under
`sources/web_archive/`, which those two gates do not read.

## 8. What a re-grade agent should look at (no tier is re-issued here)

Family (b) is now a route with bytes, so the §15.2 count is no longer structurally four for these
five companies. What would move a tier, and what must be checked first:

1. **Are the stored pages Tier-1?** These are company-authored web pages (front pages,
   "accomplishment"/affiliate indexes, IR pages), which is Tier-1 in kind; but 4 of the 52 bodies
   are meta-refresh frames or `<title>`-only stubs (e.g. `amerisource.com_20000301004609.html`,
   187 B; `bergenbrunswig.com_19990117010349.html`, 86 B; `wellpoint.com` earliest 248 B). A tier
   move needs a word count on the stripped text, which this tool does not do — `bytes` and
   `cdx_length` are in every sidecar for that judgment.
2. **Is the capture inside a stage window?** Every stored capture is inside its requested
   year-window, but the windows here were chosen from probe language (Centene 1996-2002 = FR-1;
   Cencora 1994-2001 = the S-4's own pages; Elevance 1996-2014 = FR-6; Marathon 2011-2015 = the
   post-spin domain). A re-grade agent should map each capture to the company's declared stages,
   not to the file name.
3. **Centene** is the strongest candidate: the filings there are one self-reciting lineage, and
   `centene.com` + `coordinatedcare.com` now supply 12 in-window 1999-2002 pages. Evidence to read
   first: `centene.com_19991105102101.html`, `.../20010111053900.html`,
   `coordinatedcare.com_20020401230136.html` (32 KB, the largest).
4. **Cencora**: `amerisource.com` and `bergenbrunswig.com` each give one page per year
   1996-2001; the Bergen Brunswig pages (3-9 KB) are the acquired-party's own words, which is what
   the S-4 lines 850/1855 could not supply.
5. **Elevance**: the dossier's "(b) web archives — entirely. 0 calls" (l.262) and FR-6 (l.308) are
   now superseded for `anthem.com` (6 pages 1997-2014) and `wellpoint.com` (6 pages), and
   `bcbskc.org` is a **tested NULL** — a re-grade may stop treating it as untried, and must not
   retry it.
6. **Microsoft**: 10 fresh 1994-2002 bodies (earliest stored 1996-10-20, 10,491 B) replace the
   "Earliest capture of microsoft.com: NOT ESTABLISHED" line (l.204) as a *measurable* question;
   note `microsoft.com` and `www.microsoft.com` returned the same captures (`matchType=domain` on
   the apex already includes `www`), so read one set, not two.
7. **Marathon**: bytes exist but only from 2011-02-07, i.e. the post-spin registrant. The
   registrant-identity trap applies (the famous 1887/1996 founding belongs to a different legal
   person), so family (b) cannot be in-window for any pre-2011 stage; a null there is a fact about
   the archive.
8. **Target — reported, not touched.** `company_042_target/sources/web_archive/` holds
   `cdx_dhc.txt` and `cdx_targetcom.txt`, 11,832 B each, and both hash to
   `e084d527921708642a79724e9f0210da659bbc0905c6ce9a3a1f416e4628091c` — byte-identical to the
   Microsoft "Internet Archive: Temporarily Offline" outage page. They have no sidecar. If any
   Target pass counts family (b) from those bytes, it is counting an outage page. Target's paths
   belong to another agent tonight, so nothing here was changed; the orchestrator should dispatch
   the owner to re-run `cdx_intake.py run --slug target` after adding a cited `target.com` row to
   `tools/web_domains.json`.

## 9. Every URL hit

* `https://web.archive.org/cdx/search/cdx?url=<D>&matchType=domain&from=<Y1>&to=<Y2>&output=text&fl=timestamp,original,mimetype,statuscode,length,digest&collapse=timestamp:6&limit=500`
  for D = `centene.com`, `coordinatedcare.com`, `amerisource.com`, `bergenbrunswig.com`,
  `anthem.com`, `wellpoint.com`, `bcbskc.org` (×2 passes), `microsoft.com`, `www.microsoft.com`,
  `marathonpetroleum.com` — Y1/Y2 per §6.
* One pre-build shape probe: `http://web.archive.org/cdx/search/cdx?url=centene.com&matchType=domain&from=1996&to=2002&output=text&fl=timestamp,original,mimetype,statuscode,length,digest&collapse=timestamp:6&limit=5`.
* One exact-match diagnostic: `https://web.archive.org/cdx/search/cdx?url=bcbskc.org&matchType=exact&from=1990&to=2024&output=text&fl=timestamp,original,mimetype,statuscode,length&limit=5`.
* 52 snapshot fetches of the form `https://web.archive.org/web/<timestamp>id_/<original>`; each
  URL is recorded verbatim as `requested_url` in the sidecar next to the bytes it produced.
* No search engine was used. `web.archive.org` is the only host contacted.
