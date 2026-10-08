# Microsoft Stage 1 audit 2 (numbers + hindsight)

Agent `msft-audit2`, 2026-09-30. Web calls: **0**. Tool calls used to write this: ~45 of 110.
Read in full: `00_METHOD_AND_STYLE.md` §9–§15, `MASTER_RESEARCH_LOG.md` RD-131, `stage_1.md` (2,191 lines),
`stage_1_index.md`, `_MANIFEST.md`, `CORRECTIONS.md`, all nine registers, `research/A2`, `A4`, `A_chronology`,
`B1` (targeted greps), `tools/gates.py`, and the local bytes that `sources.csv` points at — including the
sibling shelves (`company_004_apple`, `company_041_dell`) the register names. Nothing was repaired.

## Verdict

**Not certifiable on numbers/hindsight as it stands, but the volume is not rotten: the arithmetic core holds.**
Every printed sum in the volume and the register reproduces (28+1+8+7+7+1+9+9=70; 11+5+1=17; 134+2=136;
35,756+5,743,636+493,273=6,272,665; 1,850,712+1,888,699=3,739,411; 12+1=13; 148→127→21 folds; 110/6/11 stage
literals; 34,707 words). What fails is **authorship of one 1980 passage** (a reseller's order form is booked as
the company's own print, and the same lines are simultaneously booked as a competitor's ad), **six counts that
do not re-measure**, and **three table fields whose carrier prints a different event's place or date**.

Counts by defect class (26 items):

| class | HIGH | MEDIUM | LOW | total |
|---|---|---|---|---|
| authorship/substitution of a carrier (1) | 2 | 1 | 1 | 4 |
| count/arithmetic that does not re-measure (1,3) | 0 | 6 | 2 | 8 |
| field with no carrier, or a carrier that states another event (3) | 0 | 3 | 3 | 6 |
| false verification assertion (re-measured after writing) (3) | 0 | 3 | 2 | 5 |
| cited row exists but says something else (4) | 0 | 2 | 2 | 4 |
| hindsight / interpretive over-claim (5) | 0 | 2 | 0 | 2 |
| label/basis (2) | 0 | 0 | 2 | 2 |
| **26** | **2** | **14** | **10** | |

Boundary (check 6): **defensible as claimed** — see §Boundary verdict.

---

## Defect rows

Carrier notation: file + line, or stable §/record id. "Prints" = measured on the bytes on disk 2026-09-30.

### HIGH

**H1 — the $320/$365 order form is not Microsoft's; it is a third-party reseller's.**
Claim (register): `quantitative.csv` r23 `Z-80 SoftCard order-form price,320,… FACT … "Company order form
l.11551 reads MICROSOFT Z-80 SOFTCARD(TM) s 320 … company-authored advertising, so self-narrative as to the
claim that this was the price"`; r24 `other SoftCard configuration prices on the same form,365`.
Claim (prose): §Boundary "its order form takes names and addresses directly (`s 320` checkbox, l.11556)";
§O.1 row 3 "Company advertising prints a priced direct-order product"; `timeline.csv` 1980-12 row
`Company advertising prints a priced direct-order product, Z-80 SoftCard at 320 USD`; `decisions.csv` r3
`Company copy prints a 320 USD card`; `channels.csv` `Dealer plus direct-mail order form … 320 and 365 USD on
the order page`; U.13 CLAIM B.
Carrier expected: a Microsoft-authored advertisement/order form in `byte-magazine-1980-12`.
Carrier actually prints (Microsoft-shelf copy, lines measured): the block l.11479–11571 is an advertisement for
**"Insoft Accountant"** — "It was decided one group would retain the 'Peachtree Software' trademark … We are now
ready to market our business software to you under the name of 'Insoft Accountant'" (l.11498–11502), "This fully
Integrated Business Software Package for s 365 includes: GENERAL LEDGER…" (l.11528), order checkboxes
l.11547/11549/11551/11553, vendor terms "At this price software is sold as-is without support … Sale is to end
users only" (l.11559–11561), and the seller's own address "259 Barnett Rd., Unit 2, Medford, Oregon 97501,
503/779-2465" (l.11567–11569). Microsoft's own advertisement is a different block: l.13335–13346
("FORTRAN-80 and COBOL-80…", "your Microsoft dealer today", `MICROSOFT Consumer Products, 400 108th Ave. N.E.,
Suite 200, Bellevue, WA 98004. (206) 454-1315.`), which is a company imprint and verifies.
Severity: HIGH (author substitution feeding a self-narrative/third-party classification, a channel claim, and a
decision row).
Minimal honest repair: re-label r23/r24 as a **third-party reseller's** printed price for the card as a package
option; the numbers 320 and 365 stay (they print), the basis becomes "vendor option price, not company list";
remove "company-authored/self-narrative" from those cells; `channels.csv` direct-mail order-form leg →
**UNKNOWN** (only the dealer line at l.13338 survives as company print); `decisions.csv` r3 actual_result and
`timeline.csv` 1980-12 row re-worded accordingly; U.13 CLAIM B keeps the price but not the "the firm sells"
inference (a reseller pricing the card is not the firm's own price).

**H2 — the same lines are also booked as "Peachtree Software's advertisement".**
Claim: §M.1 1980-12 row "SoftCard's minimum host configuration, printed by an application vendor …
l.11512–11516 (**Peachtree Software's advertisement**)"; M04 "l.11512–11516 (Peachtree Software's advertisement)";
N05/U.12 count "Peachtree's minimum configuration" among four unrelated vendors.
Carrier actually prints: the ad says the **Peachtree trademark was retained by the other group** and these
sellers are marketing under "Insoft Accountant" (l.11498–11502). Part 1 calls the identical lines
"company-supplied advertising" (§E row, §F) — the volume holds two contradictory authorship claims for one
passage, and both are wrong.
Severity: HIGH-MEDIUM (independence *count* survives — it is still a third party — so U.12/N05's "four unrelated
vendors, one magazine" is intact; the named party and the §E/§F label are not).
Minimal honest repair: name the speaker as the vendor printing "Insoft Accountant" (Medford, OR); keep the
independence weight; delete the "company-supplied advertising" label from §E/§F.

### MEDIUM

**M1 — derived start-window does not follow from its own stated rule.**
Claim: `quantitative.csv` r7 `start span implied by the company's 'almost a year ago',c. 1975-02 to 1975-07 …
derived_arithmetic:"1976-01-31 minus 'almost a year' (read as 8-12 months) gives 1975-02 to 1975-06"`.
Also §D "implied start window of roughly 1975-02 → 1975-07", §A table "the derived span 1975-02 → 1975-07",
§S.2 "period c. 1975-02 → 1976-01", and **`CORRECTIONS.md` COR-01 action 2** ("the derived window
(c. 1975-02 → 1975-07)").
What the arithmetic gives: 1976-01-31 − 12 months = 1975-01-31; − 8 months = 1975-05-31 → **1975-01 → 1975-05**.
One row carries three different spans (value, own arithmetic, prose), and the printed upper bound is two months
beyond the stated rule — its only observable effect is that the canonical June-1975 founding falls inside.
Severity: MEDIUM (labelled DERIVED/Low, so no fact is laundered; but the instruction layer repeats it).
Minimal honest repair: print 1975-01 → 1975-05 with the reading stated, or declare the widening as a choice
("read 'almost a year' as 6–12 months") — never leave a bound that only fits the wanted answer.

**M2 — "about a tenth of the room's headcount with any machine at all" (§F, l.695).**
Carrier: `hcc0201` l.138 "At least 300 were on hand"; l.139–141 the eight printed terms summing to 70.
Measured ratio: 70 / ≥300 = **≤23%** (about a quarter). A tenth would need ~30 machines or ~700 attendees.
Severity: MEDIUM (narrative-only; the register correctly carries 70, 28, 40% and no 10% ratio — the "less than
10%" in the same section is the company's different, uncounted figure, which is where the tenth most likely
came from).
Minimal honest repair: "about a quarter of the room (70 counted machines among at least 300 attendees)".

**M3 — the SEC copy count is 12, not fourteen.**
Claims: §K.1 1975-row "14 of 17 held SEC documents"; §R item 7 "Fourteen held SEC documents print the founding
sentence … one lineage with fourteen copies".
Register/prose (correct): `quantitative.csv` r20 "12 documents of 16 stored"; §S.1 "12 of 16"; r21 "13 carriers
(12 filings + FY2017)".
Measured over `sources/sec/*.txt`: **12 files** under every variant tried (whitespace-tolerant phrase, "founded
as a partnership", "partnership in 1975", "founded…1975" within 60 chars); the .html prints none; the largest
reachable denominator is 17 documents (16 .txt + 1 .html) → 12/17 at best.
Severity: MEDIUM — it is the firewall row (§R item 7) whose whole point is that copies are not corroboration;
overstating the copies by two is the wrong direction of error.
Minimal honest repair: 12 of 16 (or 12 of 17 counting the HTML), and "twelve copies".

**M4 — "single-line grep = 6 files" is 4.**
Claims: `quantitative.csv` r20 derived_arithmetic; §S.1 "only 6 of 16 on a single line"; `data_gaps.csv`
GAP-K2 "(6 printing it on one line)".
Measured: literal `founded as a partnership in 1975` within one line = **4** files
(`…95-000018`, `…95-000029`, `…97-002409`, `…97-002537`); whitespace-tolerant per line = 4; the "was/∅ incorporated
in 1981" split gives 3 and 9, neither 6.
Severity: MEDIUM (a High-labelled measurement over held bytes that does not reproduce).
Minimal honest repair: 4, with the four filenames, or restate the method that produced 6.

**M5 — "`1975-12-17` … 0 hits anywhere" is falsified by the files that assert it.**
Claims: `CORRECTIONS.md` l.62 "**0 hits anywhere in `founders_playbook/`**"; `quantitative.csv` r16 notes
"No ISO form of the retracted date appears anywhere in the corpus (0 hits)"; §D l.565 "`1975-12-17` as an ISO
date: **0 hits anywhere**".
Measured: the ISO string occurs in **5 corpus files** repo-wide — `quantitative.csv` r16, `stage_1.md` (l.344,
l.565), `_parts/s1_p1.md` (l.212, l.433, l.878), `CORRECTIONS.md` l.62, and `MASTER_RESEARCH_LOG.md`. Two of those are
the assertion cells themselves (this audit is unavoidably a sixth carrier, which is the point of the repair).
Severity: MEDIUM. The retraction is sound (§14 rule 8 satisfied: the value survives only inside retraction
language); the numeric *verification* is false, and it lives in the instruction layer.
Minimal honest repair: "0 occurrences outside retraction/correction language, in the 5 cells named" — or drop
the count.

**M6 — the "December 17" sweep tally is not a corpus sweep.**
Claims: §D l.557 "7 hit classes, of which 2 are Microsoft-directory prose hits"; `conflicts.csv` U.1 cell
"1 stale prose hit, 4 correct/quoted/retraction hits, 2 hits belonging to other companies".
Measured under `01_companies/`: **52 files** carry the string on re-measurement (45 on the identical pass 25
minutes earlier — the corpus is live and other agents are writing), e.g. Alphabet ×8, Comcast ×8, Goldman ×4,
JPMorgan ×4, J&J ×4, Cardinal ×3, Cencora ×3, BoFa ×2, Dell ×2, Microsoft ×6 + `hcc0201`. The two named
examples (Alphabet 2003 sublease, Dell 1993 loan) exist ✓ but are 2 of ~40 other-company files.
Severity: MEDIUM (the conclusion — no stale Microsoft use — holds; the count presented as a sweep is not one).
Minimal honest repair: re-scope the tally to "the Microsoft directory and the two examples checked", or re-run
and print the count.

**M7 — "Morris Plains, New Jersey (BYTE publication place as printed)" is not printed in that window.**
Claims: `timeline.csv` 1977-07 row `Morris Plains, New Jersey (BYTE publication place as printed)` and the
1976-07 row `Morris Plains, New Jersey`.
Carrier actually prints: `byte-1977-07.txt` l.499 "BYTE is published monthly by BYTE Publications Inc, 70 Main
St, **Peterborough NH 03458**"; `byte-1976-07.txt` l.790–798 same; `byte-1980-12`, `byte-1981-02`,
`byte-1982-03` also print Peterborough NH. `morris plains` = **0 occurrences** in every one of the in-window
files (1976-07, 1976-09, 1977-07, 1980-12); the name does become BYTE's printed place later (`byte-1981-02` and
`byte-1982-03` each print it once, `byte-magazine-1987-04_djvu.txt` l.94970) — which is exactly why the volume's
1987-04 `stage3` row is right and this is a plausible-place substituted backwards from a later year.
Severity: MEDIUM — plausible-place substitution, the invented-date class wearing a location, and it is asserted
"as printed".
Minimal honest repair: Peterborough, New Hampshire 03458 for the 1976/1977 rows; keep Morris Plains only on the
1987 row.

**M8 — the January 7 meeting's venue is the January 21 meeting's venue.**
Claims: `timeline.csv` 1976-01-07 row `location printed as the SLAC auditorium`; §J merge contract item 2
"the location is the club's meeting venue as printed (`SLAC auditorium`, `hcc0201` l.152)"; `CORRECTIONS.md`
COR-02 "A club meeting location, the SLAC auditorium (l.152), is a third place again".
Carrier actually prints: `hcc0201` l.137 "**January 7, 1976** – The first meeting of 1976…" through l.150 names
**no venue**; l.152 opens "**January 21, 1976** – Another well attended meeting filling the SLAC auditorium."
Severity: MEDIUM — textual-proximity coupling inside one issue, i.e. the COR-01 failure mode re-imported into
the register in the same pass that minted COR-01 (and it now sits in the corrections file as a standing rule).
Minimal honest repair: 1976-01-07 `location` → `UNKNOWN (hcc0201 l.137-150 names no venue; SLAC is the Jan 21
venue, l.152)`.

**M9 — the move interval's lower bound predates its own last carrier.**
Claims: §O.1 row 4 and O04 "Date: between **1976-01-30** and 1980-12"; §Q.4 "move lies in 1976-01-30 → 1980-12".
Register (correct): `decisions.csv` r4 and U.14 "between 1976-02-29 and 1980-12".
Carrier: `hcc0202` l.85–88 reprints "1180 Alvarado S.E. No. 114" under the 1976-02-29 masthead (measured) — so
a change of *printed* presence cannot be bounded to begin the day after the January issue.
Severity: MEDIUM (a date bound invented one month early; the volume's own §Boundary keeps the documented
presence at 1976-01-31 → 1980-12 and would not support it).
Minimal honest repair: 1976-02-29 → 1980-12 in §O.1, O04 and §Q.4.

**M10 — Compute! 1979 hit decomposition is off by one and self-contradicting.**
Claims: §S.1 "**11** real + 1 false-positive (`Microsoftware Systems`, l.17602) = 12 on the wide pattern";
§K.1 "11 real hit lines in Compute!" listing **10** lines (7282, 7306, 7316, 7469, 10915, 16106, 16969, 17596,
21051, 21789); §M.1 "(11 real hit lines)" listing 7.
Measured: narrow `micro-?soft` = **11 lines including l.17602** (the false positive is *inside* the narrow set,
because "microsoftware" contains "microsoft"), wide = 12. Real namings = **10**.
Severity: MEDIUM (High-labelled measurement; the enumeration in §K.1 is the right one).
Minimal honest repair: "10 real namings + 1 false-positive = 11 narrow; 12 wide".

**M11 — the EDGAR floor, the volume's hardest load-bearing null, has no register carrier.**
Claim: §Header floor 1 / §A / §G / §K / §Q.1 / GAP-K1/L1/U1 — "`sources/_index/submissions.csv` = 4,525 rows,
oldest `filingDate` 1994-02-14, 0 earlier, no S-1".
Register: `quantitative.csv` r12 (the 0-rows-before-floor measurement) cites `source=S4226` — which is the
**FY1994 10-K**, a document that does not print EDGAR's filing index; r22 (word-boundary namings across 16
filings) also cites S4226. No row in `sources.csv` names `_index/submissions.csv` or the stored-filings corpus
as a carrier.
Measured (the numbers themselves are right): 4,525 rows; min 1994-02-14 = a **10-Q, accession
0000950109-94-000252** exactly as stated; 0 `S-1`/`S-1/A`; word-boundary MITS/Altair/Micro-Soft across the 16
.txt filings = 0 ✓.
Severity: MEDIUM — the figure is verified but its stated carrier does not print it (item-1 class: a number whose
carrier is the wrong document).
Minimal honest repair: mint one `sources.csv` row for the EDGAR index (url/access date/sidecar) and re-point
r12/r22 — merge work, not mine.

**M12 — "the first dollar figure the firm ever printed was a complaint about royalties" (§H coda).**
Carrier: `hcc0201` l.88 "The value of the computer time we have used exceeds **$40,000**." precedes l.94–95
"…worth less than §2 an hour" by six lines in the same letter.
Severity: MEDIUM (a verifiable superlative in interpretive prose, contradicted by its own carrier's ordering).
Minimal honest repair: "the first dollar figures the firm printed are its own sunk-cost valuation and then its
royalty return, in that order".

**M13 — "residential" Albuquerque address has no carrier.**
Claims: §A "a residential PO-box-style Albuquerque address"; §O.1 row 4 `state_before` "Residential reply
address in Albuquerque, NM"; §Boundary "Albuquerque PO address".
Carrier prints only: `hcc0201` l.122–123 "1180 Alvarado SE, #114, Albuquerque, New Mexico, 87108" — a street
address with a unit number. Nothing in any held byte describes the premises, and §B.3 correctly limits itself to
"coincidence of ZIP". The later-folklore reading (a founder's home/dorm) is exactly what §2 forbids importing.
Severity: MEDIUM (interpretive attribute; it is also self-contradicting: "residential" vs "PO-box-style").
Minimal honest repair: "a street address with a unit number in Albuquerque"; occupancy UNKNOWN.

**M14 — a causal clause re-enters through a table cell (§P.1, last row).**
Claim: "Fragmentation itself: no single host dominates the counted room, **which is why a porting programme had
customers**."
Test: evidence (the room count ✓) is present; mechanism is not — no carrier states why anyone bought a port;
§R item 3 refuses "the ports were a strategy" and O05 labels the same reading INFERENCE/Low; §O.1 row 1 already
records "NOT RECORDED — mechanism UNKNOWN".
Severity: MEDIUM (an outcome stated as a cause, in the section whose job is to avoid it).
Minimal honest repair: delete "which is why", or "consistent with demand for ports; mechanism UNKNOWN, Low".

### LOW

**L1 — `decisions.csv` claim_refs point at records that say something else.** Row 1 (1977-05 port placement) →
`O03`, but O03 is the December 1980 self-presentation record (the port row's own record is O05). Row 5
(`stage2,1981,Incorporate the predecessor partnership`) → `O05`, which is the scaling-path record and never
addresses incorporation (K02 does). 2 of 5 rows. Repair: re-point row 1 → O05; row 5 → K02, or mint the record.

**L2 — COR-04 reaches 2 register rows, not the 3 it claims.** `stage_1.md` l.122 "3 rows carry a COR-04 tag";
`CORRECTIONS.md` COR-04 "**Rows tagged: 3**". Measured per row: `conflicts.csv` line 5 (U.1) and
`data_gaps.csv` line 7 (the APL outcome row) only — part 1's MITS-licence row folded into `GAP-L1` and lost its
tag. (COR-05's "3 rows" verifies: `sources.csv` S4243, `timeline.csv` l.26, `channels.csv` l.7 ✓.) Repair: tag
GAP-L1 or restate as 2.

**L3 — §U's lead directs a reader to a row that does not exist.** `stage_1.md` l.1919–1922: "`U.1`-`U.5` are
minted by `research/B1_periodical_records.md` … U.5 the 136-versus-134 measurement". `conflicts.csv` has 14
rows: U.1–U.4, U.6–U.15 (no U.5). Retirement is documented in the merge chrome and the index, not in §U.
Repair: one clause in the §U lead naming U.15 as the kept row.

**L4 — perimeter of the in-window null searches: 11 vs 13 layers.** §K preamble "13 are OCR text layers",
L05/M08/Q.6/GAP-Q1 "13 text layers under sources/periodicals/" vs `stage_1.md` §S.1 "11 layers / 9,763,197 B".
Measured by mtime: `byte-magazine-1981-07` (1,905,830 B) and `byte-magazine-1983-07` (2,165,363 B) arrived
**2026-09-29 23:44**, i.e. three days after the 2026-09-26 pass. So S.1's 11 was right *at the time* (and the
13 of 13,834,390 B is right now), while the nulls written as "searched 13 layers" were run over 11. Both
figures stand unreconciled in one volume. Repair: note the arrival and re-scope the nulls to 11 layers at the
time of writing (§14 rule 11 — the merge took two layers nobody cited).

**L5 — "IPO → 0" over the Stage-3 bytes is a bare-token null.** §Q.7 and `data_gaps.csv` GAP-S1 (B1 §S3-3):
"`initial public offering`, `public offering`, `went public`, `shareholder`, `IPO` all return **0** over
3,739,411 B". Measured: byte total ✓ exact (`byte-1986-01` + `byte-1988-08`); the first four phrases ✓ 0;
`IPO` as a standalone uppercase token = **1** (`byte-magazine-1988-08_djvu.txt` l.1460 "Schematics & IPO
Artwork"), 6 case-insensitively. Full-name founder nulls ✓ (`bill gates` 0, `paul allen` 0; `\bgates\b` 11 are
logic gates). Repair: "1 bare IPO token, 0 offering narrations" — the volume's own RD-124 rule.

**L6 — cited range misses one of its own three values.** `quantitative.csv` r24 "(l.11545–11551)" for the three
365 printings; the third (single-density 8-inch) is at **l.11553**. §S.2's range (l.11545–11556) covers it.

**L7 — one used layer lacks the sidecar the Header says every used layer carries.** Header/§Header: "Every
periodical and corporate-print byte used here … is sidecar-stamped `UNVERIFIED TLS` (verified in
`sources/periodicals/*.meta.json` this pass)". Measured: 12 of 13 layers carry it and their byte fields match
disk exactly; `197602-modern-data_djvu.txt` has a `.sidecar.json` with **no transport and no bytes field** — and
it is searched in §L.3. (FY1994 10-K sidecar ✓ `http_status: 200`, `bytes: 442763` = file size, no caveat.)

**L8 — manifest self-description is stale twice.** `_MANIFEST.md` line 14 lists CORRECTIONS.md as "COR-01 to
COR-04" (COR-05 exists in that file); item 2 cites the core-tier budget finding at "34,665" while its own table
and the gate print 34,707.

**L9 — stage label differs across registers for one fact.** `quantitative.csv` r19 (BYTE March 1982 hit lines)
is `stage1`; `sources.csv` S4239 for the same document is `stage2`, and §K's own table says "NO — Stage 2".
Both literals are legal (§13), but the same measurement is staged two ways.

**L10 — "royalties paid" is a cash gloss on an expense line.** r26 / L06 / §S.2: Schedule X prints "Royalties"
under "Charged to Costs and Expenses / Year Ended June 30", "(In millions)", `$21 $36 $60` (measured at
l.1408–1418 exactly ✓). The volume's out-of-window and fiscal-basis labels are correct; "paid" is not printed.

---

## Gate reconciliation

Command run exactly as briefed:
`python tools/gates.py --company-dir founders_playbook/01_companies/company_011_microsoft --tier exemplar
--out founders_playbook/03_quality_control/microsoft_s1_gates_audit2.md` → exit 1, **1 finding, 21 passes**.
(Note for the tool owner: `--out …md` was created as a **directory**; the report landed at
`03_quality_control/microsoft_s1_gates_audit2.md/gates_company_011_microsoft.md`. This audit's only authored
file is the present one.)

- **Already caught / confirmed by the gate:** register widths (28×11, 26×12, 14×15, 22×18, 13×8, 7×11, 5×11,
  5×11, 7×11), `source_id` resolution (all S#### tokens resolve, 22 in the volume), anchor parity
  **14 ↔ 14**, budget 34,707 < 60,000, corrections propagation "all 5 retractions reach registers and volumes".
  My own re-measurement agrees with every one of these counts, so the gate's passes are real, not vacuous.
- **Where the gate is silent — everything in the MEDIUM/HIGH block.** It checks that a key resolves, never that
  the resolved line says what the prose claims (H1/H2/M7/M8/L1/M11 would pass it); it counts anchors, not the
  §U lead that names a retired one (L3); it checks propagation *presence*, not the *number of tagged rows* (L2);
  it has no arithmetic gate at all, so M1–M6 and M10 pass.
- **ADVISORY treated as coverage, not defect:** "11 of 13 checked spans unmatched (85%)". I verified 24 quoted
  spans directly against bytes and all are present; the gate's misses are explained by this volume's carrier
  shape — 7 of 22 `sources.csv` rows sit on **other companies' shelves** (`company_004_apple`,
  `company_041_dell`) and the two physical copies of BYTE Dec 1980 differ by 5 lines (e.g. the "sibling company"
  sentence is `l.39644–39648` on this shelf, `l.39649–39653` on the Apple shelf; part 2 cites the Apple-shelf
  numbers against the Microsoft-shelf path). That is an intake/indexing gap per §15.6 plus a pointer issue for
  the citation audit, not 11 fabricated citations.

---

## Boundary verdict (check 6)

**Kept: 1975-01-01 → 1980-12-31 is the earliest *defensible* origin, not merely the earliest claimed one, and
the volume says why.** Anchors: `hcc0201` l.83–84 ("Almost a year ago, Paul Allen and myself … hired Monte
Davidoff and developed Altair BASIC"), a retrospective sentence inside a document dated on its own face
(`l.13 Volume Number 2, Issue 1 January 31, 1976`), plus FY1994 10-K `l.181–182` ("founded as a partnership in
1975 and was incorporated in 1981", verified in bytes) — two lineages, both company-side, exactly as §A states.
The volume does not launder the year: it writes "**1975-1980 as a claim about a start, and 1976-01-31 → 1980-12
as a documented presence**" and holds the 1981 filed transition two-sided (U.4). The close is argued from
printed self-presentation (Bellevue imprint + trademark legend + unhyphenated name, all measured on disk), not
from convenience. Caveat recorded separately: the *derived* 1975 sub-span in the register and the corrections
file is wrong (M1), and the 1976-01-07 row's venue is invented (M8) — neither moves the boundary.

## Hindsight verdict (check 5)

This volume earns most of its firewall. §R's twelve refusals all hold against the prose; §C, §D, §F, §G, §I and
§J codas name mechanism **UNKNOWN** rather than manufacture one (only §H's coda overreaches, M12/M14); the
KNOWABLE lists (§B.6, §C, §H) contain nothing beyond their carriers; the A4 mine's "in-window 1975-01-01" index
label is read as an artefact and overturned from the bytes (§K), which is precisely "do not read an index entry
as a fact"; Davidoff's status stays UNKNOWN (U.7) and no role is promoted to founder beyond the registrant's own
wording. The residual hindsight is not in adjectives but in three places: the §P.1 causal clause (M14), the
"residential" premise (M13), and the first-dollar-figure superlative (M12).

## Checks run that found nothing (with counts)

- **20 file-byte claims** — all exact: hcc0201 28,281 · hcc0202 43,265 · hcc0203 23,686 · hcc0204 30,810 ·
  hcc0109 15,563 · hcc0110 20,193 · PE-1975-03 493,273 · BYTE-1980-12 1,669,324 / 1,669,716 ·
  BYTE-1982-03 2,072,713 · BYTE-1986-01 1,850,712 · BYTE-1988-08 1,888,699 · FY2017 report 295,724 ·
  Compute! 542,112 · Kilobaud 672,171 · adventure brochure 3,755 · Allen transcript 13,639 ·
  BYTE-1987-04 1,769,686 · FY1994 10-K 442,763 · BYTE-1981-02 1,617,655 · Modern Data 261,075.
- **11 hit-line measurements** — all reproduce: 134 (both copies), 136 wide (both), 0 hyphenated (both); 139/142
  (1982-03); 185 (1986-01); 254 (1988-08); 107 (FY2017); 1/3 (Kilobaud); 2 with 1 hyphenated (1977-07);
  65/67 with 1 hyphenated (1981-02); 200 with 1 hyphenated (1987-04); 0 across BYTE-1976 ×12 and
  hcc0109/hcc0110/PE-1975-03. Line totals 120,488 and 144,864 ✓.
- **12 arithmetic identities** in §S/§K/§Q/quantitative — all foot (listed in the Verdict).
- **Register arithmetic, 9 registers** — 127 rows, per-register kept/folded/refused exactly as the manifest and
  index print them; 148 = 55+30+63; stage literals 110/6/11; 22 distinct source_ids, 14 distinct conflict_ids,
  0 duplicate keys, 0 empty cells except `derived_arithmetic` on non-DERIVED rows; every High-importance gap
  (7) carries a non-empty `follow_up_task`.
- **24 verbatim spans** re-read from the cited lines (Homebrew letter + replies + mastheads, VDM-1 column,
  Tiny BASIC notice, BYTE 1976-07/-09 pointers, BYTE 1977-07 letter, Kilobaud OSI item, Compute! dealer list,
  PE price/vendor/coupon lines, BYTE 1980-12 imprints and trademark legends, FY2017 l.623, S-3 l.396-397,
  S-4 l.3900, 10-K l.181-182 / l.975-977 / l.566-567 / l.1408-1418) — every one present, all within ±5 lines of
  the cited pointer.
- **Filing-floor null** — 4,525 rows / 1994-02-14 / 10-Q / accession 0000950109-94-000252 / 0 S-1 — five
  numbers, all exact.
- **Word-count chain** — 13,778 + 19,203 = 32,981 − 70 = 32,911 + 1,796 = **34,707**, and `stage_1.md` measures
  34,707; the parts now measure +177 words each, matching the two SUPERSEDED notices the index describes.
- **Contemporaneous/retrospective labelling (check 2)** — all 12 §T.1 carriers re-checked against publication
  and event dates: 1976 letter (contemporaneous print, retrospective content ✓), 1994-1999 filings and FY2017
  report (`RETROSPECTIVE SOURCE` ✓, distance 19–24 yr ✓), Allen transcript (undated on face, catalogue 1982 ✓,
  kept out of Stage 1 ✓), Schedule X (fiscal-year basis, in millions, out-of-window ✓). **No restated or later
  figure is presented as a contemporaneous print anywhere in the volume.**
- **Split-adjusted / per-share vs aggregate:** none of these classes exists to fail — the volume prints nominal
  figures only and §S.3 explicitly refuses inflation-adjusted renderings; no share, EPS or split datum appears
  in Stage 1 or the registers (checked across all 26 quantitative rows).
- **gross/net/face-value substitution:** one found (H1, reseller price as company list); the $439/$621 Altair
  prices ✓ machine/vendor price and labelled "NOT this company's price"; the $89 dealer price ✓ labelled
  dealer's; the $75 ✓ labelled a buyer's statement.

## Coverage notes (not defects)

1. **In-window print the null perimeter never reached.** `company_004_apple/sources/periodicals/` holds six
   1976 hobby-magazine layers (Creative Computing Jan-Feb, Mar-Apr, Sep-Oct, Nov-Dec 1976 + two SIM reprints,
   ~2.0 MB) plus `micro_IA41153056_0224`, none cited by this volume; the "31 layers on the Apple shelf" perimeter
   is the `ia_*` directories (45 .txt files sit on that shelf). Measured: **0** `micro[-. ]{0,2}soft` hits in
   every one of them, so the name-silence and "no byte names a fourth person" nulls **survive** — but each
   carries 6–18 `MITS` and 34–45 `Altair` mentions, i.e. plausible carriers for the price/dealer/licence data the
   volume says exist only in unheld titles (GAP-L1, GAP-N1). Cheapest next step is a script run over the shelf
   already on disk, not a FETCH REQUEST.
2. `1981-microsoft-adventure_djvu.txt` prints **"©1981"** on its face (l.12) — the volume dates it out of window
   only from the IBM-PC naming; the printed copyright line is an unused carrier that would strengthen the `(PB)`
   label. No defect.
3. The non-destruction proof's exact figures (part bodies **91,992 B** and **131,567 B**) could not be
   reproduced from the boundaries the manifest states; four sampled spans per part (5%, 30%, 60%, 90%) are
   present verbatim in `stage_1.md`, so I record the byte figures as *not re-measurable as specified*, not as
   false.
4. `sources/` now holds 82 files (the volume's "78" was right on 2026-09-26); `conflicts.csv` measures 13,887 B
   against the index's 13,886.

## Re-measurement after writing

Every figure asserted above as disk-verified was re-measured from the same paths after this file was written
(hit-line counts 134/136/139/142/185/254/107/11/12; sums 70/17/136/6,272,665/3,739,411/4,037,761; register rows
127 with literals 110/6/11; SEC counts 12 of 16 and 4 single-line; index 4,525 rows and the 1994-02-14 10-Q
accession; the 5 ISO-string carriers excluding this file; the "December 17" file tally, which moved 45→52 between
the two passes because the corpus is live and other agents are writing; the Peterborough/Morris Plains masthead
counts, including the two 1976 BYTE files added to the check on re-measurement (0 Morris Plains, 11 Peterborough
each); and `stage_1.md` at 34,707 words). One figure changed on re-measurement — the December-17 file count, in
the direction that strengthens M6 — and it is corrected above; no other assertion changed.
