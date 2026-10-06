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
