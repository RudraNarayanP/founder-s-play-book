# walmart_s1_audit1_chronology_hindsight.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:30:05Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**PASS-WITH-DEFECTS. High-severity count: 2. Certification withheld from Stage-2 use until two named
repairs are applied — the header block (HDR-1/HDR-2, one edit) and the unwritten merge account (MERGE-1).**

Both highs are the *same physical object* — the `**Company:**` line of the merged volume's header block —
and both are claims the volume refutes twenty lines later in its own body. This is **not** a research
FAIL: the boundary argument, the registers, the independence accounting and the mechanism discipline all
survive adversarial testing, and I could not overturn a single figure, date or anchor. It is the §14-rule-10
defect class (a retraction that never reached the instruction layer), and §14 rule 10 grades that location
as the highest-severity place a stale claim can live. One edit of the front matter by a **repair agent**
(not by me — certifier ≠ repairer) clears both.

| Gate | High | Medium | Low | Suspicions |
|---|---|---|---|---|
| 1 — chronology and causation | 2 (HDR-1, HDR-2) | 2 (CHR-1, CHR-2) | 1 (CHR-3) | 0 |
| 2 — hindsight and mechanism | 0 | 0 | 0 | 1 (HND-1, coverage-limited) |

### MERGE-1 — MEDIUM — outside both gates, found en passant, and it blocks §11 on its own

`stage_1.md`'s front matter sends the reader to the merge account: *"Every row in them was applied,
refused-with-a-reason, or re-pointed at merge, and the account is in
`03_quality_control/walmart_s1_merge.md`."* **That file is an unwritten scaffold** — 476 bytes, every
section still carries the scaffold's unwritten-section placeholder (Row application / Id resolution and collisions / Registers created /
Volume split / Anchor parity / Not applied and why), under a live-owner banner dated 2026-09-25T20:01:36Z.
So the pointer is dangling, and §11's "provenance is closed" cannot be certified: no one has recorded on
paper which of the `>>> REGISTER ROWS FOR MERGE <<<` blocks was applied versus refused. My own spot checks
of `conflicts.csv`/`timeline.csv`/`quantitative.csv` came out clean, which is why this is MEDIUM and not
High — but a clean register with no application account is an **unfalsified** merge, not a verified one.
The `anchors` residue is also unclosed for the same reason: the merge sheet's "Anchor parity" section is
exactly where U.1/U.4 should have been dispositioned.
**Remedy:** the merge agent writes its own sheet (I will not, per certifier ≠ repairer), or the next
certification pass treats Stage 1 as not provenance-closed until it exists.

Mechanical residue (`anchors`): **false positive, no parity damage** — see next section. Named fix, not applied.

## Anchor residue characterisation

**Command run, quoted verbatim:**

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_002_walmart --checks csv,keys,anchors,budget
-> Findings: **1** | Passes: 19
-> anchors | narrative | anchor with no register row: U.1, U.4
-> anchors  stage_1.md declares 82 anchors / stage_1_part_2.md declares 21 anchors
```

**Second scripted run** (I did not hand-parse anything): adding `quotes` to the same command returns
`quotes | ADVISORY | 16 of 33 checked spans unmatched (48%)`. Treated as a triage list per §15.6, then
tested by direct `grep` against `sources/`; see *Passed checks*.
`python tools/gates.py --self-test` → **PASS, 8/8 planted defects caught, clean fixture clean**, so the
`anchors` check that fired is known-working and has **no** must-stay-clean control for this residue shape.

**Ruling: FALSE POSITIVE. Not genuine §U declarations missing register rows.** It is the same *class* seen
on Amazon — a colliding id namespace — but **not** either named Amazon sub-case: `CONFLICT FOR` occurs
**0 times** in `stage_1.md`, `stage_1_part_2.md` and `conflicts.csv`, and no backticked range is involved.
This is a third member of the family: **a line-start markdown heading inside the anchor grammar.**

Mechanism, established rather than inferred:

- `gate_anchors` declares a narrative anchor when a line begins (after `#`/`*`/`-`) with `U\.\d+[a-z]?`
  (`tools/gates.py`, `_anchors_declared`), and collects register anchors with `\bU\.(\d+[a-z]?)\b`
  (`_anchors`). The two patterns are not namespace-scoped.
- §U of `stage_1.md` uses **single-digit editorial subsection labels as headings**: `### U.0 How these
  anchors are minted`, `### U.1 The conflicts no register row covers`, `### U.2 Documented nulls`,
  `### U.3 UNANSWERED and UNTRIED routes`, `### U.4 The finding §U exists to protect`.
- The **real** anchors are zero-padded three-digit: `U.011`–`U.048`, `U.101`–`U.116`, `U.201`–`U.222`, plus
  `U.2x`. All of those carry register rows, and the reverse direction is clean too — the gate raised no
  `anchors | registers` finding, so **no register row cites an anchor absent from the narrative**. Parity on
  the anchor namespace is intact.

**The merge's own disclosure is directionally right but incomplete, and the gap matters.** `stage_1.md`
front matter says: *"§U's own subsection labels (`### U.0`…`### U.4`) collide with the `U.nnn` anchor
grammar … so the gate reports U.1–U.4 as narrative anchors with no register row."* The gate reports
**only U.1 and U.4**. `U.0`, `U.2`, `U.3` pass **by accident**: the registers echo the same labels as prose
references — `grep -o "\bU\.2\b" *.csv` → 64 hits, e.g. `"UNKNOWN - U.2 states the nu…"`, `"from s1_p3.md
U.2 (documented n…"`; `U.3` → 96 hits; and `U.0` matches **inside** the sub-number `U.0.1` ("…per U.0.1:
A2 local k…") because `.` is a word boundary. So three of the five heading labels are "clean" only while an
unrelated note happens to repeat their text. **A future register edit can silently manufacture four
findings here.**

**Named fix — NOT applied (I am the certifier):** (a) volume-side, for a repair agent: retitle the five §U
subsection headings out of the anchor grammar (`### §U-a` … or `### U-i`), which §9.3 forbids me to do to a
part's spine; (b) tool-side, for the gate owner: scope `_anchors_declared` to the anchor shape declared in
`U.0`'s own minting rule (zero-padded `U\.\d{3}`) and add a `--self-test` **must-stay-clean** control that
plants a `### U.1` heading plus a `U.011` anchor and asserts parity still passes.

## Chronology defects

GATE 1. Addressed by stable label; no line numbers used as addresses.

### HDR-1 — HIGH — the retracted Delaware incorporation is the volume's company identification line

- **Text quoted** (`stage_1.md`, header block of merged volume 1, "Company:" line):
  *"**Company:** Wal-Mart Stores, Inc. — a **Delaware corporation**; incorporated **1969-10-01**; the
  operating entity from **1962** was **Wal-Mart, Inc., an Arkansas corporation**"*
- **Document evidence:** my own re-run of the controlling test — `grep -ci delaware sources/periodicals/WALMART_AR_*.txt`
  returns **0 for all nine reports** (and §B.0 records the same). The only day-precision incorporation
  statement anywhere is the company's undated curated page, "1969 — The company officially incorporates as
  Wal-Mart Stores, Inc." (`sources/EXTRACT_corporate_walmart_history_timeline.md`), which is **year only,
  no month, no day, no state**. The corrected reading is in the volume itself at §B.0 ("**State of
  incorporation** — **UNKNOWN — not stated in any of the nine reports**"), §Q and conflicts row
  **U.014**, and it is the row the merge sheet lists as applied.
- **Why this is the worst finding in the volume:** the header is the one place a cold reader looks first
  and does not check. §14 rule 10 exists because of exactly this: *"An instruction file that a cold reader
  trusts without checking is the highest-severity place a stale claim can live."* The volume's own front
  matter half-anticipates it — *"(2) Part 1's header and §D-R03 carried 'a Delaware corporation;
  incorporated 1969-10-01' … the original wording stays visible **in the part's own text**"* — but line 38
  is not part text preserved under `_parts/`: it is the merged volume's identity line, restated **below**
  the disclosure note, in bold, present tense, unrestacted.
- **Proposed remedy (repair agent):** in the header "Company:" line, replace with
  `Wal-Mart Stores, Inc. — state of incorporation UNKNOWN (not stated in any of the nine reports; U.014);
  consolidated registrant group formed by pooling effective 1970-02-01; first Wal-Mart-branded store 1962
  (registrant-retrospective)`. Keep §D-R03 + D-R03c as they are: the correction-beside-the-row pattern
  there is §14-rule-8 compliant and should not be touched.

### HDR-2 — HIGH — the header asserts the entity name the volume classes as Tier-4 folklore

- **Text quoted:** same line, second clause: *"the operating entity from **1962** was **Wal-Mart, Inc., an
  Arkansas corporation**"* — and it points the reader to §B.0 for the "two-issuer question".
- **Document evidence:** `grep -io "wal-mart,  *inc\.\?[^s]" sources/periodicals/WALMART_AR_*.txt` →
  **zero occurrences** across all nine reports. §B.0 states the opposite of what the header asserts:
  *"'Wal-Mart, Inc., incorporated 15 March 1962' — **UNATTESTED in this corpus.** It is Tier-4 folklore"*,
  and **U.013** holds it as CLAIM B, "*unattested anywhere on disk*", with the documented event being the
  1970-02-01 pooling out of **Walton Enterprises, Inc.** (`WALMART_AR_1972.txt` Note 1, S0101).
- **Aggravating:** unlike HDR-1 this clause is **not disclosed anywhere in the merge front matter**, so a
  reader who trusts the disclosure note as the complete list of carried defects will not look for it.
  Register-side the claim is correctly refused — `conflicts.csv` row U.013 and `timeline.csv`'s 1969 row
  carry the year-only, company-asserted form — so the damage is confined to the header.
- **Proposed remedy:** delete the clause with HDR-1's rewrite; add it to the merge sheet's carried-defect
  list as a third item so the disclosure is complete.

### CHR-1 — MEDIUM — "1962 (documented)" in the boundary table outruns the volume's own attestation geometry

- **Text quoted:** `## STAGE BOUNDARY JUSTIFICATION` row 1: *"**1945** *(claimed)* / **1962**
  *(documented)*"*; and §D dated-record **D-R02**: *"1962 | First **Wal-Mart** store opening — the
  documented rival start | FY1972+ store/branch lists (A3/A4) | FACT (single lineage) | Medium"*.
- **What the documents actually say — the brief's live question, answered:** **the 1962 opening is carried
  by the company's own later recap, not by any document of the period.** The earliest text on disk dating
  it is S0103, the FY1974 report dated **1974-03-21** — I verified the sentence in the body, not in the
  intake header: `WALMART_AR_1974.txt` L437-440 *"The Company's first Wal-Mart Discount City store opened in
  Rogers. Arkansas in 1962."* `1962` occurs **exactly once** in that file and **0 times** in
  `WALMART_AR_1972.txt` and `WALMART_AR_1973.txt` (both re-tested). The *month* waits for S0104
  (`WALMART_AR_1975.txt` L653-654 *"…approximately 4700), in / November 1962"*) and S0107 (L375). No
  register, deed, photograph or press item on disk carries either; the volume says so in §C.0.
- **Why still MEDIUM:** §B-1a, §C.0, D-R02c and `conflicts.csv` all state this correctly, and the
  boundary's *close* is properly evidenced (see PASSED list). The exposure is that a later volume lifting
  the summary row inherits "(documented)" as an independence claim it cannot support.
- **Proposed remedy:** qualify the cell — *"1962 (printed by the registrant from 1974; no in-period
  document)"* — and re-point D-R02's Source cell, which currently reads "FY1972+ store/branch lists"
  although FY1972 prints no 1962.

### CHR-2 — MEDIUM — dated-not-dated: the earliest printed "Newport, Arkansas" is FY1974, not FY1975

- **Text quoted** (§B.2 state-of-the-place row, high-confidence cell): *"**Five documents** place the 1945
  start in **Newport, Arkansas**: S0104 … S0106 … S0107 … S0108 … S0109"* → *"High that the registrant placed
  it in Arkansas **from 1975 onward**"*. Same count in `conflicts.csv` U-A2/7→**U.011** ("five registrant
  documents naming Newport, Arkansas"), and §B-1a's "then **five more** dated printings **S0103→S0109**"
  (a seven-document range described as five).
- **Document evidence:** `WALMART_AR_1974.txt` L427-430 prints, in its own body: *"Wal-Mart was founded by
  its President and Chairman, Sam M. Walton, who opened his first Ben Franklin variety store in **Newport,
  Arkansas in 1945**."* So the correct statement is **six documents, from 1974-03-21 onward**. All five
  quoted sentences were individually verified in the body text layer (AR_1975 L643; AR_1977 L660;
  AR_1978 L374; AR_1979 L631; AR_1980 L950), and the count correctly excludes S0105, where Newport appears
  only in a store list — that exclusion is right and should be kept.
- **Direction of the error matters:** it is **safe** — it strengthens the one-lineage finding rather than
  weakening it, and independence stays 0 either way. Hence MEDIUM, not HIGH. But "from 1975 onward" is a
  date-scoped assertion in a High-confidence cell, and it is exactly the kind of boundary a later pass
  would lift as fact.
- **Proposed remedy:** change to "six documents (S0103–S0109 except S0105's list-only mention), from
  **1974-03-21** onward", and repair §B-1a's "five more / S0103→S0109" arithmetic.

### CHR-3 — LOW — the SFAS-13 clause is quoted from the printing that omits its own perimeter

- **Text quoted** (§A.1, total-assets row): *"S0108 prints: 'All financial information has been restated to
  reflect the retroactive application ot [sic] Statement of Financial Accounting Standards No. 13'"*.
- **Evidence:** the `[sic]` is **genuine** — `WALMART_AR_1979.txt` L128-129 prints exactly
  *"…retroactive application / **ot**  Statement  of  Financial  Accounting  Standards  No.  13."*
  (a double-spaced OCR body line, easy to miss). But the same document prints the clause a second time at
  L1485 with the load-bearing qualifier: *"All financial information **prior to 1979** has been restated…"*.
  Quoting only the first omits the restatement perimeter.
- **Proposed remedy:** cite the L1485 form, or print both and note which carries the perimeter. No figure,
  register row or basis flag changes — the row already says "**AS PUBLISHED** 206,691 thousand / **AS
  RESTATED** 251,865,000" and the two-live-bases prohibition is stated.

### Boundary and outcome-before-cause tests — result

- **Nothing in the volume treats the 1945 back-cast as documented origin.** The header labels it
  *"a **CLAIMED ORIGIN, not a documented one**"*, §C.0/§B-1a give it "Low that the event is documented",
  D-R01 carries it as *"a claimed date not a documented one"* with class FOUNDER CLAIM / RETROSPECTIVE
  INTERPRETATION and **independence 0**, and §Q's 1945 row prints *"distance **grows 28 → 35 years** as the
  series runs, which is the wrong direction for evidence"*. That is the §11-requirement met, and it is the
  single strongest thing in the volume. HDR-1/HDR-2 are the only places where the back-cast is upgraded by
  position rather than by evidence.
- **No outcome stated before its cause.** I searched every causal pairing available in the window: the
  1970-10-08 offer is placed after the 1970-02-01 pooling that created the issuer; FY1968–FY1971 rows are
  labelled the company's own *pro forma* caption; the FY1975 SCDigest/PBS distribution-centre dates are
  held as "CONTESTED, four sources, none cited" rather than resolved forwards.
- **No duration contradicts its dates** — five back-casts re-computed independently: 1973−28=1945 ✓;
  1974−29=1945 ✓; 1979−17=1962 ✓; 1975−13=1962 ✓; 1970−8=1962 ✓.

## Hindsight defects

GATE 2. **Result: no High and no Medium hindsight defect established.** This is the strongest of the two
gates on this volume, and I am reporting the boundary of my coverage rather than asserting purity.

- **Outcome leakage — searched, none found.** No sentence in the passages I read states or implies that the
  1970 IPO, the 1979 public-company scale, or the eventual chain was visible at the time. The two places
  leakage is usual both go the other way: §L's NOT KNOWABLE cell says *"**the only witness to every signal
  in §L is the company's own print plus one auditor**"*, and §O/§I's NOT KNOWABLE cells each carry
  *"Whether the 1962 format would scale"* — the outcome is filed under what a contemporaneous reader could
  **not** know. §A.1's own closing line refuses the coda: *"Those silences are the subject of §A.2 and §S
  (part_2); they are not smoothed by the density of the FY1968–FY1980 rows."*
- **The one "so what" coda in the volume passes.** `grep -in "so what"` returns exactly **one** hit
  (§C.1, L387). It does §16/RD-034's full work: it names the absence (*"they never give a mechanism"*),
  declares *"Mechanism therefore is **UNKNOWN**"*, keeps the reconstruction on observable states (*"not
  from intent"*), retains the alternative explanation, and refuses to test what it cannot test (*"that
  alternative cannot be tested on this corpus, and is recorded as UNTRIED at §S"*).
- **Mechanism discipline — `mechanism UNKNOWN` is used correctly and often.** 23 mechanism lines across the
  two volumes; the explicit `UNKNOWN` verdict appears at §C.1, §E.2 (L628), §F (L720/724), §L (L1556), §M
  (L1787), §N (L1887) and §E.3. The mechanism the volume **does** name is licensed by contemporaneous print
  and stays inside it: the 77%-of-mature-volume new-store observation is DERIVED with its arithmetic on the
  page (`153 x (478807000/153) x 1.17 = 560204190; …`) **and still** carries "mechanism UNKNOWN"; §J's
  IBM/Sierra penetration rise is cut down to *"CORRELATION ONLY, and mechanism UNKNOWN"* with alternatives
  retained. I found **no assertion surviving on step one alone** in the passages read.
- **Nothing here is a manufactured mechanism.** Specifically, the volume does not claim the discount format
  worked *because of* small-town siting: the siting language is quoted as the company's published rule
  (FY1978's "average community population 5,000-25,000") and the causal step is left open.

### HND-1 — SUSPICION, coverage-limited, not a finding

I read the header, §A, §B, §C, §D, §P.0, §U in full and the KNOWABLE/coda lines of §§E–§R, but **not** the
prose of §§E–§L, §N–§R line by line within budget. A leakage sentence in an unread cell is possible. This is
labelled a **suspicion**, not a defect, and no remedy is proposed against it; the remedy is the coverage
note itself, carried to *Not testable*.

## Sweep counts

The construction sweep over **both volumes**, run as scripted text search (counts, not a line list).
`grep -io` per term over `stage_1.md` / `stage_1_part_2.md`:

| term | vol 1 | vol 2 | note |
|---|---|---|---|
| `proved` (naive substring) | 3 | 0 | **only 1 is the word** — `grep -o "\bproved\b"`: 2 hits are substring collisions inside *approved*/*improved*. The single real instance is L1050 *"IA proved EMPTY for them"*, about archive yield, not causation |
| `showed that` | 0 | 0 | |
| `drove` | 0 | 0 | |
| `did the work` | 0 | 0 | |
| `clearly` | 0 | 0 | |
| `inevitable` | 0 | 0 | |
| `the reason was` | 0 | 0 | |
| **brief's seven terms, total** | **3** | **0** | of which **1** live token, **0** causal |
| `proves` (extended) | 9 | 1 | 10 hits, all precision statements about **apparatuses or negatives**, e.g. L202/L1007 *"this proves the index did not carry the subject, **not that** the trade ignored the firm"*; L2120 tooling; L2134 an inference I verified to its document (`WALMART_AR_1972.txt` L1073 *"The Company and its subsidiaries file separate in-come tax returns"*, hyphen-wrapped) |
| `shows that` | 1 | 0 | |
| `because it` | 7 | 1 | the only causal-conjunction density; sampled, all document-bound |
| `meant that` / `set the stage` / `foreshadow` | 0 | 0 | |
| `positioned` | 1 | 0 | |

**Read of the sweep:** the hagiography register is essentially absent — a 58,000-word volume with **zero**
`drove`, `clearly`, `inevitable`, `the reason was`, `showed that`, `did the work`, and one non-causal
`proved`. Two cautions for anyone reusing these numbers: (i) a substring sweep over-counts *proved* 3×, so
sweep results here must be word-boundary-gated; (ii) absence of the construction vocabulary is **not** proof
of absence of construction — the residue risk at this company is not adjectives, it is **selection**
(only the winner's nine reports survive), and §A.2/§S name that null explicitly, which is the §2
record-selection requirement being met rather than dodged.

## Independence audit

- **The nine annual reports are one lineage and the volume never lets them be counted twice.** Stated as a
  reading rule before any row (§A.1: *"Nine printings of FY1974 in FY1975/76/77/78/79 remain **one
  lineage** … they are version evidence, not corroboration, and the independent-lineage count for every
  number here is **1**"*) and restated as §P.0 rule 1 for the whole table. I tested whether the text ever
  **claims** corroboration and found three candidates, each correctly self-limited:
  1. *1970-01-01 fleet mix* — FY1980's sentence plus FY1972's President's letter. The volume calls the
     agreement *"an internal check, **not a second source**"* ✓.
  2. *1970-10-08* — labelled *"Its corroborators are **same-lineage**"* with the one genuinely independent
     carrier named as a **negative** ✓.
  3. *FY1975 net sales* — carried as **ESTIMATE/DERIVED** with inversion arithmetic shown, not as four
     corroborations, and the unresolved `226,209 / 236,209` ambiguity left open at **U-A3/1** instead of
     being averaged ✓.
- **Filing-lineage rule / S-1: inapplicable, and correctly recorded as void rather than fudged.** There is
  **no S-1 on disk** — `sources/EDGAR_submissions_CIK0000104169_002_1994-2012.json` puts the electronic
  floor at 1994-02-14, first 10-K 1995-04-27, and §A.2(a) states the consequence: *"the 1970 registration
  statement is **paper at the SEC Reference Room / National Archives, not on disk** — so the stage's
  closing date cannot be read from the filing that created it."* No claim anywhere leans on an S-1/A pair.
- **The independent negative holds up under re-test.** I re-ran it: `grep -c -i "wal-m|wal mart|walmart"`
  over `sources/gov_docs/SEC_SecuritiesTradedOnExchanges_asof-1970-12-31_…txt` → **0**, and the OCR-loss
  control the volume cites is real — **WALGREEN** and **WALWORTH** both print in the same W-block. So A5-04
  ("not exchange-listed at 31-Dec-1970") is correctly the only structurally independent datum in the stage,
  and the volume is careful that it *"corroborates **no dollar, no store and no rate**"*.
- **Third-party retrospectives are not laundered into independence.** PBS (2004) and SCDigest (2012) are
  used only to open a contest, not to settle one: the distribution-centre date is held as *"CONTESTED, four
  sources, none cited"* and the SCDigest supply line as *"Tier-3 trade retrospective, 2012-dated, uncited"*.
- **Self-narrative plus curated page = one corporate record.** §B.2 and **U.115** state it: the page and the
  reports *"cannot be counted twice"*, and the page's silence about pre-1962 is carried as a finding about
  curation, not as evidence that nothing happened. The 1967/1968 calendar-vs-fiscal mislabel on the page is
  caught and quantified rather than adopted.
- **Residual independence risk I could not settle (named, not scored):** `sources/periodicals/` also holds
  `1975-…-hocr.html` and `1976-…-hocr.html`. These are the **same physical artifacts'** second OCR layer, so
  they are one lineage, but I did not verify that no `sources.csv` row treats an `.hocr` file as a separate
  source_id. Carried to *Not testable*.

## Passed checks

Re-run by me against the documents, not accepted from the volume. Every one is **clean**:

| # | Check | Result |
|---|---|---|
| 1 | "Delaware" 0 times in all nine reports | `grep -ci delaware WALMART_AR_1972…1980.txt` → **0/0/0/0/0/0/0/0/0**. The retraction is true; only the header breaches it |
| 2 | "one and only split" did not resurface as fact | Three 2-for-ones carried (§A.1, §K, §P **P47**, §Q, `timeline.csv`); **1971-06-11** and **1972-04-05** verified inside S0101's own capital note (L881 *"Par value of 1,500,000 shares issued in a two-for-one stock split … June 11, 1971 (150,000)"*, L890/898 *"…on April 5, 1972 (300,000)"*). D-R09 survives **only** beside D-R09c, and U.015 closes *"**Do not resurrect it**"* |
| 3 | Newport = **ARKANSAS**; both errors stay dead; no third variant entered | Arkansas adopted on six registrant printings; **Nebraska** appears only inside retraction text (`conflicts.csv` U.011, `data_gaps.csv`); **Kentucky** only as the named A4 error and as the verified BW decoy *"NEWPORT, Ky. — Boycott of Communist-made goods … p38, Dec.15"*; the fourth reading (Missouri) is enumerated as an error, while *Versailles, Missouri* (Bud Walton, 1946) is separately documented in AR_1974/1977/1979 — correct discrimination, no conflation. My own greps: **nebraska/kentucky 0 occurrences in all nine reports** |
| 4 | FY1962–FY1967 empty is carried as the central finding | §A.1, §A.2, §S, §E.1, §P.0 rule 3, §L — six independent statements; §S row 1 *"Every FY1962–FY1967 metric. EMPTY in all nine reports; **not restated later**"*; §E.1 all-UNKNOWN row; **U.102** anchor. Not written around |
| 5 | FY1978/79 total-asset break and the two-live-bases rule | **206,691** verified `WALMART_AR_1978.txt` L2078; **251,865** verified `WALMART_AR_1979.txt` L2177; FY1979's own **324,666,000** L2175. Row prints AS PUBLISHED / AS RESTATED, the capital-lease move 10,904→59,003, and §P.0's forbidden-operation rule *"any asset-turn, debt/assets or total-asset growth figure computed across the break is invalid"* |
| 6 | AS-FILED vs RESTATED basis discipline | The literal token is rare (2×) but the basis is **always** carried, in variant vocabulary: `CONTEMP` / `RESTAT(in S01xx)` / *"pre-split basis"* / *"pre-SFAS-13 basis"* / *"POST-SFAS-13 basis … NOT comparable with any pre-FY1979 asset figure"*. Six rows sampled by targeted search for unlabelled financial rows: **all six carry a basis** (three of the six, e.g. `FY1975,Net sales,236209`, are ESTIMATE/DERIVED with arithmetic and an open ambiguity anchor). No restated figure is offered as corroboration of a contemporary one anywhere I looked |
| 7 | Load-bearing quotations exist **in the document body**, not in our intake headers | Verified independently: 200,000-share/October 8 1970/3,010,467 (AR_1972 L877-879); "twenty-eight year history" (AR_1973 L187); "opened in Rogers. Arkansas in 1962" (AR_1974 L437-440); "November 1962" + "approximately 4700" (AR_1975 L653-654); "until November 1962" (AR_1978 L375); the FY1980 18+14/four-state/$31 million sentence (AR_1980 L376-380); the `[sic] ot` SFAS clause (AR_1979 L128-129); separate tax returns (AR_1972 L1073, hyphen-wrapped) |
| 8 | **The documents' own printed dates**, not headers | AR_1972's 1972-03-22 is printed in the President's message block (L357/L359 *"Sam M. Walton, President / March 22, 1972"*) and again in the stockholders'-approval note (L895); AR_1973's is the auditor's *"Tulsa, Oklahoma / March 20, 1973"* (L742-743). So the corpus's central null — **no company document before 1972-03-22** — rests on print, not on an intake timestamp |
| 9 | A dated artifact was not used as a licence | §C.1's framing rule confines the whole subsection to *"company self-narrative transmitted 13–35 years after the events … quoted because the registrant's stated rationale is itself an in-period document about the 1970s firm, **even where it is not evidence about 1945–1962**"*. The FY1980 report is cited for a 1970 **state** and never for a 1962 **event** |
| 10 | "Not establishable", never "never happened" | Every silence is perimetered: *"UNKNOWN. The commonly cited '6,000 sq ft', '45,000 items' and opening-day price claims have **no witness of any kind** in this corpus"*; *"the record that could describe them was never printed, **or** never kept"* (the §2 record-selection null phrased as a disjunction, not a fact); 22 UNTRIED routes; the company timeline's own pre-1962 silence registered as the finding **U.115** |
| 11 | Registers agree with the narrative on the four contested items | `conflicts.csv` U.011 (Newport), U.013 (founding), U.014 (Delaware), U.015 (splits) each carry the corrected reading; the refuted values appear **only inside retraction language**; `timeline.csv` prints the three splits, not one |

## Not testable

What the scripted gates **structurally cannot see** at this company — the reason a 19/20 green board and a
`--self-test: PASS` are not a certification:

1. **Dated-not-dated.** No check compares a quotation's **subject period** against the citing document's
   printed date. Both my MEDIUM chronology findings (CHR-1, CHR-2) are of that kind, and the gate suite is
   blind to both. This company's whole stage is exposed to it because the evidence is nine reports each
   reprinting a recap 12–35 years late.
2. **Independence / lineage.** `keys` resolves that an `S####` token exists; it cannot tell you that
   S0101–S0109 are one corporate self-narrative. The volume's central methodological claim — independent
   count = 1 for every figure — is unmachineckable by the current suite, and it is precisely where an
   Amazon-style "corroborated in the S-1 **and** the S-1/A" error would live.
3. **Quote fidelity in double-spaced, hyphen-wrapped OCR.** The `quotes` gate is ADVISORY here at 48%
   unmatched, but its own index is 949,517 squashed chars, and three quotations I verified by hand matched
   only after I relaxed whitespace and hyphenation (AR_1972's separate-returns sentence is wrapped
   *"separate in-* / *come tax returns"*; AR_1978's *"Newport, Arkan-"*). So the advisory rate **overstates**
   fabrication risk here, and §15.6's intake-gap excuse does not apply because the bytes **are** on disk.
   A gate whose false-positive rate and false-negative rate are both unknown on this corpus cannot settle
   anything; I settled the load-bearing ones by grep instead.
4. **AS-FILED vs RESTATED.** No check exists. The literal tokens appear 2× in `quantitative.csv` while the
   basis lives in variant prose, so even a string check for "as-filed" would have failed this volume
   **incorrectly**. This is the single most useful gate Walmart needs that Amazon never needed.
5. **The instruction layer.** Every check reads registers and `stage_*.md` **content**; none reads a header
   block for claims the body retracts. HDR-1 and HDR-2 both sat inside a file that reported 19 passes.
6. **The `anchors` gate has no must-stay-clean control for heading labels** (self-test plants only a genuine
   orphan). Per §15.5 that is a bug in the gate, and it is also why my U.1/U.4 ruling had to be made by
   reading `_anchors_declared` rather than by trusting the fire.
7. **Causation and mechanism generally** — `mechanism UNKNOWN` vs a manufactured mechanism is a judgment
   call; no gate sees either.
8. **Tool defect found on my own pass, reported for the gate owner (`tools/scaffold.py`, `cmd_section`):**
   it does `block.replace("STATUS: PENDING", "STATUS: WRITTEN <date>")` over the whole matched block, so it
   **rewrites any quoted occurrence of that string inside an agent's evidence text**. It silently corrupted
   my MERGE-1 finding, turning a quotation about the unwritten merge sheet into a claim that the sheet's
   sections were WRITTEN — i.e. the tool manufactured a false statement in an audit sheet. Fix: anchor the
   replace to the placeholder line only (`re.sub(r"(?m)^STATUS: PENDING$", …)`). Interim guidance for every
   agent using this tool: never put the literal placeholder string in quoted evidence.
   Also observed: of nine `section` calls in one loop only the first reported a match, and the completed
   sheet carries **no** per-section WRITTEN markers — the ledger's `done` record is now the only status
   evidence. Cosmetic against §15.3's WRITE line, but worth knowing before it is relied on as proof that a
   section was written.

## Untried

Stopped at budget (48 tool calls of 60; nothing was skipped for convenience):

- **Line-by-line hindsight read of §§E–§L and §N–§R prose** (only their KNOWABLE/coda cells were read). This
  is HND-1's boundary; a second pass over ~28,000 words would close it.
- **§S and §T in part 2 vs the merged `data_gaps.csv`/`sources.csv` row-for-row equivalence** — the gate
  proves column and key integrity, not that every narrative row was applied. (The missing merge account
  itself is scored above as **MERGE-1**, not left here.)
- **Whether `sources.csv` grants separate source_ids to the `.hocr` OCR layers of AR_1975/AR_1976** (see
  *Independence audit*, residual risk).
- **S0105's printed date.** `WALMART_AR_1976.txt` yields no body month-day for 1976 under my greps, yet the
  register carries publication date 1976-03-26; the audit trail for that one date (auditor report page vs
  intake header) is unestablished. Not scored as a defect — the register could be right via a page I did
  not reach.
- **Whether the refuted FY1980 dividend row (U.026) and the "first SEC-visible registration" label stay
  dead in the registers** — named in §U.4's protected list; I verified the list's other five entries but not
  these two.
- **`budget` check at tier-exemplar vs the tier actually assigned**, and `_MANIFEST.md`'s self-reporting
  against §9.6.
- **Any re-run of `gates.py --checks corrections`** (it exists per `--help`'s default set and the self-test's
  `retraction never reaches the registers` case) and would likely have caught HDR-1's class on its own.
  **Recommend the repair agent run it before re-certifying.**


