# NOTES — Boeing Stage-1 part 1 (`_parts/s1_p1.md`), agent `s1-boeing-p1`

Working log for the merge and the orchestrator. Written by the author of the part file; not a dossier volume
and not a register. **Claim/release:** `scaffold.py claim` succeeded at 2026-10-06T21:17:30Z
(`CREATED … owner=s1-boeing-p1 ttl=240 min, sections=4`). Release at close-out (`--done`).

## 1. Every measurement in the part file, with the command that produced it

All over `founders_playbook/01_companies/company_047_boeing/sources/`, python 3 `re`/`csv` one-liners run
through the shell, 2026-10-07. Web calls used: **0**.

1. **Term census over the 25 held non-SEC text files** (7 `corporate_print/*.txt` + 18 `periodicals/*.txt`),
   case-sensitive exact-phrase counts, md5 computed per file. Results carried into §A/§I/§U.011:
   `Boeing Airplane Company` 43 · `Boeing Aircraft Company` 61 · `Boeing Air Transport` 89 ·
   `Boeing Aircraft of Canada` 33 · `Stearman` 27 · `United Aircraft` 34 · `Hubbard` 16 · `Egtvedt` 3 ·
   `W. E. Boeing` 1 (the signature blocks render uppercase, hence 1 not 5) · `The Boeing Company` 25
   (all out of window) · `Boeing` 816.
2. **Zero-counts, re-measured (not inherited):** `Westhoff` 0 · `Pacific Airplane` 0 · `Pacific Aero` 0 ·
   `B & W` 0 · `Montreal` 0 · `C & F` 0 · `since 1916` 1 (FY1934 only) · `July 22` 1 (FY1935 only) ·
   `anniversary` 1 · `22, 1916` 0 · `Sherman Act` 0 · `Public Utility` 0 · `Pujo` 0 · `income protection` 0.
   `antitrust` = 1 occurrence in the whole corpus, in `munitionsindustr1114unit_djvu.txt`, whose `Boeing`
   count is 0. Probe's two negative controls confirmed independently: munitions `Boeing` 0 / `Seattle` 0;
   1916 *Aviation* `Boeing` 0 in 149,286 chars (controls: `August 1, 1916` prints; `William` 7 hits are
   Williams/Somerville/Pusey/Bacon; `Hubbard` 1 hit is `J. F. Hubbard` in a roster).
3. **Noise-resolution reads** (§U.015): `West` 33 (dc_circ) → 105 West Adams Street / Pennsylvania v. West
   Va. / West River Bridge Co. v. Dix / West Virginia ×3; `West` 50 (Edelman) → **Harry R. Weston**, State
   Treasurer of Wyoming, plus public-land meridians; `Green` 6 (dc_circ) → **C. H. GREEN, Secretary of
   PACIFIC AIR TRANSPORT** on a bond form and *Greenhow v. Poindexter*; `Green` 12 (Edelman) →
   **J. A. Greenwood**, Wyo. Attorney General, and the Green River water supply.
4. **Award-date conflict (§U.004):** searched `January 15, 1927` (1 hit), `February 1, 1927` (1),
   `lowest qualified bidder` (7), and found a **third** date, `awarded under date of January 29, 1927`
   (2 places: the court's statement of facts and a brief). The probe quoted only February 1.
5. **SEC origin-recital route run over the held filings** (the probe did not read them):
   33 `.txt`, 7,170,562 B. `Delaware corporation` 60 in 8 files · `Boeing Airplane` 1 hit in each of 26 files
   · `Washington corporation` 4 (a subsidiary list — noise) · `Stearman` 0 · `United Aircraft` 0 ·
   `Westhoff` 0 · `since 1916` 0 · `1916` **2** — both the sentence
   *"Boeing was originally incorporated in Washington in 1916 and was reincorporated in Delaware in 1934"*
   in acc. 0000950123-96-006004 (S-4, 1996-10-29) and acc. 0000891020-98-000905 (S-4/A, 1998-05-13).
   `DATE OF NAME CHANGE` 30 matches, of which **26** carry `19730725` from `BOEING AIRPLANE CO`; the other 4
   belong to co-registrant headers (MCDONNELL CO 19670601, FIRST UNION CORP, CAMERON FINANCIAL CORP).
6. **Post-boundary corporate-print layers measured:** FY1945 (46,004 B) `1916` 0, `since 19` 0,
   `incorporat*` 0, `The Boeing Company` 0, `Boeing Airplane Company` 5. FY1976 (99,175 B) `1916` 0,
   `The Boeing Company` 2, its only `since 19` = "first order from United since 1967", its two `1960` = the
   727 programme. ⇒ the renaming is bounded after FY1945 and at/before FY1976 by held print (§U.009).
7. **md5 census:** 25 files, 25 distinct digests — no byte-identical duplicate across shelves, so no two
   shelves hold one document (§3 check done before any corroboration was counted).
8. **Footing tests** (all pass; the failures are registered instead of fixed): FY1934 P&L and balance sheet;
   FY1935 P&L, surplus roll and balance sheet; FY1940 P&L, both surplus rolls, the two capital-stock fraction
   captions (`1,081,673.75 × 5 = 5,408,368.75` exact), the rights arithmetic
   (`360,496 × 16 − 5,392,547.25 = 375,388.75` = the printed expense), FY1940 Canadian red-figure roll, and
   the FY1940 delivery split footing to gross sales. **Failures registered, not repaired:** FY1935 share pair
   (`491,365½ + 30,517¾ = 521,883¼ ≠ 521,883`) → U.007; FY1939 vs FY1940 1939-backlog basis (872,949 apart)
   → U.006; FY1938's non-verbatim quotation of FY1934 → U.008.
9. **Derived ties published as DERIVED with the arithmetic in §K:** FY1938 "77¢ per share" ⇒ ≈720,725
   shares; register build-up `521,883 + 173,424 + 26,273.5 = 721,580.5` ⇒ `$0.769`; FY1940 one-for-two
   rights on 360,496 ⇒ 720,992 held pre-offering; FY1939 Q4 loss `3,284,073.84 − 2,606,106 = 677,967.84`
   against FY1940's opening deficit `677,966.92` (a 0.92 tie, i.e. cents-rounding).
10. **Disposition searches** on the two court volumes: `decree (is|was) (affirmed|reversed)` 0,
    `judgment affirmed` 0, `289 U.S.` 0 in the Edelman volume ⇒ both outcomes are **UNANSWERED-with-route**,
    not null (§U.016, `P1GAP06`, `FETCH REQUEST` #2).

## 2. Where this pass disagrees with, or corrects, the probe (tier NOT re-graded)

* **Tier inherited unchanged: Stage 1 = T2 core.** The new family-(a) material is post-boundary (1996/1998)
  and therefore cannot count toward Stage 1's in-window family tally. Families (b) and (e) are still untried.
* **Correction 1 — the item is not homogeneous.** "46 text layers, one per year" is a correct *file* census
  and a wrong *document* census: `boeing1934a_djvu.txt` is an undated **Hamilton Metalplane advertisement**
  whose footer reads `DIVISION / BOEING AIRPLANE COMPANY / Division of United Aircraft and Transport Corp. /
  Milwaukee, Wisconsin`. This answers the probe's open question ("did not check whether the 1934a part
  duplicates 1934"): **it does not duplicate — it is a different document type**, and it adds a *fifth*
  referent for the name (§U.001, §U.014). Consequence: **six** in-window company reports, not seven.
* **Correction 2 — the FY1935 anniversary sentence.** The probe's §"Load-bearing open questions" states the
  founding day as UNKNOWN and that nothing names a July date. It prints **"the twentieth anniversary of this
  subsidiary will occur July 22 of this year"**, which yields `1916-07-22` by subtraction from the report's
  1936 sign-off — the day-month *is* in held bytes (the year is not stated beside it). Recorded as DERIVED,
  Medium, single lineage, at §B.1, §C.2, §U.003, `P1QTN20`.
* **Correction 3 — the Edelman volume is not an air-mail record.** It is a **Wyoming gasoline-tax suit**
  (Rock Springs / Cheyenne), in which the co-defendant is **Harry R. Weston** and `Boeing Company` is a
  **defined term of a municipal airport lease**. The probe used it as a carrier of mail-service evidence;
  that use survives (the mail-transfer clerk's testimony is genuinely about the mail), but the framing and
  the name-form needed correcting (§U.016, `P1SRC09`).
* **Correction 4 — the A.M. 18 award date.** The probe quoted "on or about February 1, 1927" as *the* award
  fact and treated it as the strongest load-bearing validation signal. Held bytes print **three** dates for
  one act inside the same volume, so the signal is intact but the date is not quotable as single (§U.004).
* **Addition — `since 1916` has a rival naming in-window.** A federal recital calls the 1927 contract party
  "Boeing Airplane Company, Incorporated, of Seattle, Washington, a corporation duly organized and existing
  under the laws of the **State of Washington**" — the *Airplane* name attaching to a Washington corporation
  in 1927, where the FY1934 report attaches 1916 to a corporation named *Aircraft*. This is the sharpest
  form of the brief's central difficulty and the probe did not record it (§U.001 claim C).
* **Addition — the registrant's own recital exists** in two held accessions (1916 Washington / 1934
  Delaware), and **EDGAR's own header** dates the conformed-name change 1973-07-25 against the brief's 1960
  (§U.001, §U.009).
* **Addition — the reorganisation's stated motive is tax and simplification, printed three times; antitrust
  has 0 witnesses** in the corpus (§U.010). Recorded as UNTRIED, not as a denial.
* **Sub-dissent on family (d) quality:** the probe's 137,518 B figure is right, but the FY1937 layer's
  financial statements are unreadable (column interleaving). The usable in-window corporate print is thinner
  than the byte count implies. This does not move the family verdict — text still returns — but it is why
  no FY1937 row is in `quantitative.csv`.

## 3. Refusals and guardrails applied

* Refused: "founded 1916" as a statement about the registrant; "founded 1934" as a complete origin; July 15
  1916 (unheld — and I did **not** register it as contradicted, only as absent); a 1960 renaming; an
  antitrust motive for the split; a B & W / Westhoff / Pacific Airplane naming of any kind; any reading of
  `West`/`Green`/`C & F`/`Montreal` as namings; "Boeing Company" in the Edelman volume as a corporate naming;
  any FY1937 amount; the FY1935 share-fraction split; a reconciled 1939 backlog figure; a "new management
  saved Boeing" causal claim (§N coda: mechanism UNKNOWN, alternative drivers listed).
* Refused to touch `sources/`: `sources/sec/_MANIFEST.csv` now has 1 line (header) and 0 rows although 33
  `.txt` + 37 sidecars exist. **Reported, not repaired** (§14 rule 4) → defect 5 / `P1GAP18`.
* Declined every fetch rather than spending web budget; five `FETCH REQUEST` blocks emitted (§`## Untried`).

## 4. Known deviations

* **Word count.** `s1_p1.md` is ≈**44.7k words** — over the §15.2 T2 cap of 22k/stage, under the §9.2 hard cap
  of 60k/file. Cause: the tier deliverable was met in full (all of §A–§U, claim records, **211 register rows
  across nine registers**) inside **one** part file, because the dispatch assigned a single path. Evidence was
  not cut to fit (§9.6: the limit governs file geometry, never research depth). **Remedy offered to the
  merge:** split at a §9.3 boundary — parts 1 = Header, boundary, A–O; part 2 = P–U + claim records;
  part 3 = registers; numbering continues, nothing renumbered.
* This part carries claim records for **24** load-bearing claims (T2 rule), not one per claim; §P/§Q figure
  rows are carried by `quantitative.csv`/`timeline.csv` instead.

## 5. What this pass did NOT examine

Did not open the other 31 held SEC `.txt` files beyond the counted greps and the four recitals quoted (all are
`(PB)`); read ~40% of the FY1934-FY1940 corporate-print bytes line by line and counted the rest; did not read
the Edelman volume end to end (493 KB; sampled by pattern, ~30 passages read); opened no new item and fetched
nothing (web 0); did not re-enumerate the IA item's 46-file list (§1 correction is built on the probe's
enumeration plus the 8 layers now on disk); did not verify TLS on any sidecar (all are `ok-INSECURE`); did
not test whether a case-insensitive naming census would surface a naming this one missed; wrote no register
CSV, no other company's file, and nothing outside `company_047_boeing/_parts/` except this NOTES file and my
gate file.

## 5a. Correction to the probe's family-(b) claim (route now exists; still untried here)

The probe reported family (b) web archives as unreachable: "No script in this repository reaches the Wayback
CDX API … `grep -rn "wayback\|cdx\|web.archive" tools/*.py` → the only hit is a *comment*". **That is now
false as a statement about the toolchain**: `tools/cdx_intake.py` exists (63,450 B, mtime **2026-10-06**,
i.e. one week after this company's probe) and its own docstring says it is the "deterministic Internet
Archive CDX intake for corpus family (b)", created because family (b) "had no scripted route whatsoever".
Dispositions for Boeing therefore stand as: family (b) = **UNTRIED but now REACHABLE** — a scripted run is
`python tools/cdx_intake.py …` for the orchestrator, no bespoke web budget needed — and it still cannot bear
on Stage 1, whose floor is 1916-1940 against a mid-1990s archive floor (§14.6). This does not change the
five-family tally or the T2 grade; it changes which of the two untried families is cheap to close.
**Reported rather than fixed** — this pass ran 0 web calls and opened no new item.

## 6. Gate (run at close-out, 2026-10-07)

`python tools/gates.py --company-dir founders_playbook/01_companies/company_047_boeing --tier auto --checks
csv,keys,anchors,corrections --out founders_playbook/03_quality_control/boeing_s1_gates_p1.md`

Result: **Findings 1 | Passes 0**, exit 0. The single finding is `coverage/registers` — "no register CSVs at
root or research/ -- csv/anchors gates DID NOT RUN" — which is the **expected pre-merge state** for an author
pass (the brief forbids me writing the live CSVs), not a defect, and not repaired by inventing files.
Coverage lines: 0 registers, **1 stage volume**, 62 source documents. Anchor lines: my part file declares an
explicit ANCHORS set of **17** ids and they were recognised; `no register anchors found -- UNANSWERED, not
passed`; `corrections` did not run (no `CORRECTIONS.md` on this company). **This is not a passing gate and is
not reported as one** — it is the pre-authoring/merge-pending state, and parity between the 17 §U anchors and
the 17 `conflicts.csv` rows is the merge's to prove after it applies the blocks. `keys` produced no finding:
0 `S###`/legacy source tokens occur in the narrative outside fenced blocks (checked before the run).

**Tool misread recorded, data left alone.** The gate's tier reader stamped **T3** — its own message: "tier T3
from A_chronology_feasibility.md — T1/T2/T3 all mentioned in research/ (7 mentions, 0 on a verdict line); if
the dossier's own text names a different tier, trust the dossier and tell me". The probe's verdict line is
unambiguous ("**Stage 1 … TIER 2 (core)**"), and this dossier names **T2 core** in its Header. Per the gate's
own instruction I report the discrepancy rather than editing anything to silence it: **Stage 1 Boeing is
T2 core**; the `--tier auto` inference is the thing that is wrong here, and it is a `gates.py` reading defect
of the D-3/D-4 class the probe already logged (a stamp derived from mention-counting rather than from the
verdict line).

