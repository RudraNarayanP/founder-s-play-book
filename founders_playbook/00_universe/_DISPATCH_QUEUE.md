# DISPATCH QUEUE — probes held by the 20-concurrent-subagent cap (2026-09-30 01:20)

Every brief here assumes the shared contract in `03_quality_control/PROBE_BRIEF_SHARED.md` (method §15.2 tiers,
§14 defects, §3 independence, the five families, verified tool forms, 0 web calls, append-as-you-go,
release-your-claim, report measured). Dispatch one per free slot; a refused dispatch leaves no trace anywhere
else, so nothing here may be reconstructed from memory later.

## Refused at the cap (dispatch first)

**probe-morganstanley** → `company_039_morganstanley/research/A_chronology_feasibility.md` · budget 85/70
Fleet record: REFUSED, 0 stored, floor 1993-11-08. Measure `sources/_index/` + `sources/sec/_RUN.json`; if no
canonical index exists run `sec_intake index "Morgan Stanley" --company-dir <dir>` once and report which
registrant answered. Thin shelf (2 periodicals, no corporate print).
Traps: the 1924 split from J.P. Morgan & Co. is the origin but partnership-era documents name a **different
firm**, and the modern registrant is a later Delaware continuation — read the JPMorgan and Citigroup dossiers as
the worked examples. `Morgan`/`Stanley` are common surnames and places → entity adjacency only, and test the
OCR "Moran" variant before asserting any zero. An anniversary history is ONE lineage.
Gate: `gates.py --company-dir founders_playbook/01_companies/company_039_morganstanley --checks csv,keys --fail-on substantive --out 03_quality_control/morganstanley_s1_probe_gates.md`

**probe-valero** → `company_040_valero/research/A_chronology_feasibility.md` · budget 85/70
Fleet record: REFUSED/0 stored, **but the post-RD-135 retry stored 30 documents (2.87 MB, 384,391 words)**.
Measure `_RUN.json`, `_index/` and the XBRL facts to see what landed in which window; 1979-01-01→2001-12-31 is
PROPOSED and probably starts too early.
Traps: the operating history was **bought, not built** — today's registrant began as a late-1970s/1980s
holding/lobbying vehicle for a Texas oil family, and the refining business arrived through a 2001 acquisition of
an older company already carrying the name (itself named from a Spanish mission/saint). 1979 / 1980 / 1984 /
2001 are four different legal persons. Deepwater Horizon and the RFCC fires are post-boundary → `(PB)`. Require
entity adjacency for any capacity claim.
Gate: `gates.py --company-dir founders_playbook/01_companies/company_040_valero --checks csv,keys --fail-on substantive --out 03_quality_control/valero_s1_probe_gates.md`

## Tranche 3 (not yet drafted)

`fanniemae, stonex, centene, phillips66, statefarm, freddiemac, exxonmobil, dell, meta`
Two facts to carry into those briefs:
- **State Farm and the two GSEs are structurally outside the registrant set** — a 0-filings result there is a
  real perimeter, not a tool failure, and must be written as such (and the corporate-print/periodical families
  then carry the whole tier).
- **ExxonMobil: the ticker maps to the wrong legal person.** SEC's own `company_tickers.json` answers
  `XOM → CIK 2115436 "ExxonMobil Holdings Corp"`; the historic registrant is **CIK 34088 "EXXON MOBIL CORP"**
  (formerNames `EXXON CORP`, 2 slices), and in-window intake against 2115436 stored **0 documents**. Any probe
  for rank 9 must say which CIK it addressed and re-resolve by name.
- `freddiemac`: ticker `FMCK` is unresolved in SEC's ticker file — resolve by registrant name, never a guess.
- `stonex`: ticker `SNX` answers `TD SYNNEX CORP`, so the guard's refusal was **correct**; find the registrant
  name from a filing cover page rather than from the brand.

## Re-grade wave (after tranche 3) — the 8-slice cap RD-134 removed

These probes ran against an index that read at most 8 archive slices, so each one's **filings-family verdict is
provisional** and their tiers may move up: `jpmorgan, citigroup, gm, chevron, disney, boeing, kroger, jnj,
berkshire, ford`. A re-grade agent re-runs `sec_intake index` (now walking every slice), re-measures the perimeter,
and either confirms the old tier or supersedes it **in place with the original claim struck through** — never by
deleting the first verdict.

## Added 02:20 — probe-centene (refused at the cap; dispatch third)

`company_019_centene/research/A_chronology_feasibility.md` · agent probe-centene · budget 80/65
INTAKE: window 1984-01-01->2002-12-31 PROPOSED; in-window pass stored **30 documents** (20 accessions, floor
2001-10-09, 1 UNANSWERED) - a young company whose filings genuinely reach its origin, so family (a) can carry a
stage here. Shelf otherwise bare: 0 corporate print, 0 periodicals.
TRAPS: 1984 founding vs 1996 Texas IPO - quote what the S-1 prints, not what a later 10-K restates; the business
is government-sponsored managed care, so a "first repeatable validation" is likely a state contract or a
membership figure (distinguish an award from a renewal, and find the dated carrier); Medicaid/premium/PPO
vocabulary matches many firms, require entity adjacency; rapid growth by acquisition means a founding claim and an
acquired-operating-history claim can both be true of different legal persons.
GATE: gates.py --company-dir founders_playbook/01_companies/company_019_centene --checks csv,keys
      --fail-on substantive --out 03_quality_control/centene_s1_probe_gates.md


## Fleet-level gaps the tail probes exposed (orchestrator work, not agent work) — 2026-09-30 02:40

1. **`queries.json` has no web-archive family at all.** Verizon, Elevance and UPS each independently reported
   family (b) as UNTRIED with **0 of 3,802 candidate rows carrying that family** — so the five-family verdict
   is structurally four-family for every company. Needs a per-company CDX task set (`web_archive`) before any
   tier can be argued to be complete.
2. **Corporate print is blind to house organs.** The CP tasks' `report_terms` are `annual|report|member|director`,
   so an employee magazine or a company monthly is invisible by construction (UPS, whose Stage-1 window sits in
   an era when it printed to member-owners). Add `magazine|review|bulletin|news|herald|organ|chronicle|gazette`
   as a second CP term set.
3. **Predecessor vocabulary is missing from the queries.** Elevance's 1944-1960 print is findable only under
   `Mutual Hospital Insurance` / `Blue Cross of Indiana` / `Associated Insurance Companies`; every probe now
   *names* those predecessor spellings in its dossier, so the query block must be rebuilt from the probes' own
   findings, then re-harvested `--facet-free`.
4. **The never-read EDGAR tail.** UPS measured that filings from 2007-09-03 onward were never opened (its
   FR-3). The cheapest test of an alternative founding date is a pass over the recent tail — run per company
   `auto --from 2006-12-31 --to 2026-12-31 --max-docs 25`. (Now safe: `auto` versions its run records instead
   of overwriting them, per the Elevance finding fixed at RD-136.)
5. **The registrant guard tests the wrong thing at item level.** It passed Verizon's shelf while **39 of 45
   corporate-print ids were The Bell Telephone Company of Canada** — a different legal person (third
   occurrence of the Ford-of-Canada shape). The guard compares the *registrant* to the *directory*; nothing
   checks the *item* against the company. `harvest_mine`'s entity-adjacency class is the right place for it:
   a CP item whose naming phrase belongs to a foreign sister should be reported as a decoy, not catalogued.
6. **UPS: 19/19 `TIER1_CANDIDATE` items were bare-word "ups" decoys** (CIA "FOLLOW UPS", NASA SEV-UPS, ERIC,
   "Blow-ups"). The mine's classifier is right; the *tier stamp* in the harvest index is not evidence. Any
   dossier quoting a TIER1_CANDIDATE count as family support is reading a detector's label as a finding.

7. **`sec_intake.py` has no ALIAS map, `harvest_mine.py` does (RD-133).** The BofA probe measured the
   asymmetry precisely: seven name forms all return `NO-MATCH (0 candidates)` for slug `bofa`, while the mine
   holds 12-13 entity-bearing documents for it, because the mine knows `Bank of America`->`bofa` and the
   intake does not know the reverse. EDGAR's only answer is **CIK 0000070858 `BANK OF AMERICA CORP /DE/`**
   (formerNames `BANKAMERICA CORP/DE/`, `NATIONSBANK CORP`) -- i.e. the 1998 NationsBank/MBNA Delaware
   continuation is the registrant, and both the 1904 California line and the 1791/1802 Boston line are
   ancestors. Import `scaffold_company.ALIAS` (reversed) into `resolve_name`, or take `--alias` from the
   command line; every abbreviated slug (`bofa gm jnj rtx att ups`) currently depends on the orchestrator
   remembering to pass a CIK.

## Concrete lead from Cencora's FR-1 (resolved by `tools/legacy_cik.py`, 2026-09-30 03:05)

**CIK 0000011454 = BERGEN BRUNSWIG CORP**, EDGAR perimeter **1994-01-13 -> 2002-02-14**, 190 `recent` rows, and
the form list includes `10-K, 10-K/A, 10-Q, S-4, S-4/A, 424B4, DEF 14A, POS AM`. So Cencora's proposed W-0
window (1985-2000) is **not** a filings silence -- it is a different registrant that files, and the probe could
not reach it because intake only ever addressed the ticker answer (CIK 1140859).

Re-grade brief for `company_010_cencora`: intake CIK 11454 over 1994-01-13->2001-08-28 **into a predecessor
directory** (`company_010_cencora/predecessors/bergen_brunswig/`), not into the registrant's `sources/sec/` --
the no-clobber guard is right to refuse a second CIK in the canonical slot, and the lineage must stay
attributable to its own legal person. Then re-measure family (a) for W-0 and re-issue the tier. Two more CIKs
to look up the same way: AmeriSource Health Corporation (Delaware 1988) and the 1994-2001 AmeriSourceBergen
filer. Also worth knowing: six in-window `Drug Store News`/`Chain Store Age` layers naming Bergen Brunswig
5-35x each are already on **CVS's** shelf, and one 1994 naming sits on **Cardinal's** shelf -- cross-shelf
reading is legitimate, cross-shelf *citing* needs the id to resolve where the bytes live.

## URGENT one-line fix owed, immediately after `registrant-tools` releases tools/sec_intake.py

**D1 — `tools/sec_intake.py:445`**: the legacy `sources/_index/submissions.json` stores `"cik": 354950` as an
**int**, so the `.strip()` call raises an uncaught `AttributeError` and **kills `auto`/`index` for the whole
Sep-25 intake cohort**. Home Depot's probe proved the consequence: a 3,077-row registrant was recorded as
"0 documents stored", its tier was set at T3, and the real cause was our own downloader -- the probe re-graded
it to **T2 core** once it worked around the crash with `grab --file`.

Fix: coerce before stripping (`str(...)` at the read site, and normalise on write), then sweep every
`sources/_index/submissions.json` on disk for an int-typed `cik` and repair the files, and re-run `auto` for the
companies `_FLEET_INTAKE.tsv` recorded as 0-stored-but-indexed (Home Depot, and check Verizon/AT&T/Wells Fargo/
Morgan Stanley/Valero/BofA/ExxonMobil/Fannie Mae/State Farm/Freddie Mac). Prove it with a self-test control that
plants an int `cik` and asserts the run completes. Also sweep the stale records: `_FLEET_INTAKE.tsv` row 38 and
`_IDENTITY_FIX.log` still assert a refusal the disk now contradicts.

Same file, same agent, second half: D2 (`grab` unpacking 2 from a 3-tuple) is already fixed at RD-138 -- do not
re-fix it, but confirm the enumeration path returns candidates for an accession D1 used to crash on.

## Owner defects reported by the Humana + FedEx probes (mine to fix, nobody else's file)

1. **`tools/fleet_intake.py measure()` mis-scrapes `sec_intake`'s printed line.** Humana measured it precisely:
   the dossier records `148 accessions in window` while the Stage-1 window holds **0** rows and the recital window
   holds **1414** -- 148 is what my regex read off sec_intake's own post-dedupe summary. Every tail brief I wrote
   tonight carried that number as fact, so a probe that trusted it would have sized its intake wrong. Fix the
   regex against the exact printed sentence and re-measure the `_FLEET_INTAKE.tsv` column, or delete the column
   and print `inwindow` only from `auto: N accessions in window`.
2. **`resolve_name` cannot reach legacy carriers by name.** FedEx: `sec_intake index "Federal Express Corporation"`
   -> `NO-MATCH, 0 candidates`, because resolution runs through `company_tickers.json` only. Same class as BofA's
   seven name forms. This is the third time tonight; the fix belongs with `registrant-tools`' Defect 1 work --
   fall back to `tools/legacy_cik.py search` before reporting NO-MATCH, and never report a name's absence as a
   registrant's absence.
3. **The auction/museum/manuscript family still has no tool and no query block, and two probes now name it as the
   highest-expected-value route.** FedEx: Yale's archive for the 1965 term paper, the Delaware charter and the CAB
   record behind 1971-73; UPS and Goldman asked for the same. Family (e) is therefore UNTRIED for all 50 companies
   by construction -- which means no tier in this corpus is defensible as complete, and the five-family verdict
   must be reported as four-and-a-half until something exists.
4. **A role-recorded-as-founder trap found sitting in the corpus, not in a book:** FedEx's only `Founder` title
   across 19 filings is `Sheridan Garrison, Chairman and Founder of American Freightways`
   (`0000950103-00-001270 l.250-262`) -- a competitor's founder inside our own shelf. Worth a `gates.py` or
   probe-check pattern: any `Founder` token in a company's filings that attaches to a different corporate name
   should be flagged before it can be copied into a register.
5. **FedEx measured the re-harvest landing mid-pass**: 8 IA layers / 1,377,536 B written into
   `sources/periodicals/` while it was working, which it read and adjudicated rather than ignoring (it surfaced
   two independent third-party carriers and opened a real conflict: 186 packages on day one per the company's own
   1998 advertising vs `a mere seven packages` per a 2009 third party). Keep the sequencing rule: mine AFTER
   harvest, and re-read any A4 within a few lines of quoting it.

## Correction to my own diagnosis in item 1 above (Valero, 2026-09-30)

I wrote that the wrong in-window counts came from `fleet_intake.measure()` mis-scraping a printed line. **That
was only half right, and the half I got wrong is the expensive one.** Valero measured the real mechanism: the
forward recital pass **ran second and rewrote the ledger**, so `sources/sec/_RUN.json` describes
`2001-12-31..2020-12-31` while the shelf holds **57 docs / 27 accessions / 9,680,991 B** of which **27 docs
(16 accessions, 6,808,731 B, filingDate 1997-05-13->2001-05-25) are in-window and appear nowhere in
`_MANIFEST.csv`**. The bytes are on disk; only the accounting describes the wrong pass. Humana's "148 in window"
is the mis-scrape; Valero's "0 in-window docs" is the overwrite. Two defects, one symptom.

So the owner fix is not only a regex: `auto` must key its run records **per pass** (window in the filename, or a
list of pass records inside one `_RUN.json`) so a second window cannot describe the first, and `auto` must
re-count the shelf and report record-vs-shelf disagreement -- which is exactly Defect 2 in the `registrant-tools`
brief. Extend that brief: also re-run the in-window pass for every company whose `_RUN.json` window does not
match the `--from/--to` the fleet record says it used (Valero FR-6 is the worked example).

## `tools/legacy_cik.py search` is unreliable -- my own half-fix, owed now

ExxonMobil's probe ran it on four ancestor names (Vacuum Oil, Humble, Socony, Magnolia) and **all four
parse-failed**, i.e. it reported no candidates for registrants that certainly exist. Its `detail` half is solid
(Mobil = CIK 0000067182, perimeter 1994-02-14->2000-02-09, found rather than assumed) and its no-output-is-a-null
rule held, so nobody was misled into a false absence -- but the search path is not doing its job. Cause is known:
I parse `CIK=(\d{10})` out of the browse-edgar HTML after the ATOM route turned out to carry no names at all
(`title="ARRAY(0x...)"`), and the row markup varies by query shape. Either parse the `action=getcompany` HTML
properly or move to `https://www.sec.gov/cgi-bin/browse-edgar?Company=...&action=getcompany&type=a&output=atom`
variants and assert on a known name (`"vacuum oil"` must return something). Add a self-test control with two
known-positive names and one known-negative, and until it passes, every dossier must treat `search` silence as
UNANSWERED rather than as absence -- the ExxonMobil probe did exactly that, which is the only reason the defect
cost a route and not a conclusion.

## Family (b) now exists -- and a Target trap that must be handled before Target is certified again

`tools/cdx_intake.py` is built, self-tested (37 checks / 0 failures) and verified live: 52 snapshot bodies with
sidecars across centene / cencora / elevance / marathon / microsoft. So **no dossier may write family (b) as
UNTRIED for a slug present in `tools/web_domains.json` any more**, and every slug absent from that file is
demonstrably UNTRIED (a run spent 0 requests and wrote nothing). Re-grade priorities named by the build: Centene
(12 in-window 1999-2002 pages against a purely self-reciting filing lineage), Elevance (anthem.com + wellpoint.com
now supplied; **bcbskc.org is a tested NULL -- stop retrying it**), Microsoft (earliest capture now measurable;
`www.microsoft.com` returned the same captures as the apex, so read one set), Marathon (bytes start 2011-02-07 --
registrant-identity trap), and 8 of 10 enumerations capped at `--limit 500` = a floor, not a census.

**The trap:** `company_042_target/sources/web_archive/cdx_dhc.txt` and `cdx_targetcom.txt` are **byte-identical to
Microsoft's Internet Archive outage banner** (sha256 `e084d52792…`) and carry **no sidecar**. Any Target pass that
counts family (b) from those bytes is counting an outage page -- the same class as the RD-132 error-page-as-source
finding, one shelf over. Whoever owns Target must either retire them with a COR entry or hold family (b) as
UNANSWERED-with-fetch; it must not stand as a second lineage.

## Owed self-test control (Target recert4 found the bug; my fixture control was unfinished)

`gates.py` `_advisory()` now also reads the finding's `subject`, because `gate_quotes` files the ADVISORY
marker there and Target exited 1 on a corpus with **zero substantive findings**. The code fix is verified
live (Target: `Findings 2 | Passes 18`, exit 0, both findings advisory). What is NOT done: a self-test
control that plants an unmatched attributed quote and asserts the advisory classification. My first attempt
made the control report `NOT DETECTED BY ITS OWN GATE` -- the fixture's quote span never reaches `gate_quotes`
finding generation at all -- so I reverted it rather than leave a failing self-test with a green claim.
Someone must find why the planted span is not attributed (min_words? the anchor requirement? sources.csv
mapping?) before writing that control. A fix verified only by hand is a fix that can come back.
