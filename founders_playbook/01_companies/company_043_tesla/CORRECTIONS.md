# Provenance Corrections Register — Tesla (company_043_tesla)

Standing list of attribution, dating and counting corrections established **at or after** the two Stage-1
author passes and verified against the bytes held under this company's `sources/` (read in place; **0 web
calls on every pass that produced these entries**). The Stage-1 merge pass (`tesla-s1-merge`, 2026-09-30)
opened this file; Tesla had none before, because it had no registers and no volume.

**Rule (§14 rule 10, enforced by `gates.py --checks corrections`).** Every `COR-nn` here must appear (i) in at
least one register row and (ii) in at least one stage volume that carried the withdrawn text. Both are
satisfied for COR-01…COR-06: the register homes are named in each entry, and the whole set is propagated in
the "Corrections applied at merge" block at the foot of `stage_1.md`.

**Supersede, don't erase.** No emission was deleted. Where a statement is withdrawn, the superseded wording is
printed inside the correction and inside the surviving register row, tagged `MERGE[…]`.

---

## COR-01 — part 2's supersession of part 1's refundable-reservation figure is declined (it supersedes a different date)

**Withdrawn:** the assertion in `_parts/s1_p2.md`'s quantitative emission that the $26.0m refundable reservation
liability at **2010-03-31** "SUPERSEDES the 2009-09-30 $24.8m figure part 1 carried from the original printing",
together with the derived reading in part 2's channels and decision rows that the liability "holds flat at
$26.0m from **2009-12-31** to 2010-03-31".

**Why.** Both parts print two figures attached to two different period-ends: part 1's $24.8m is a
**2009-09-30** unaudited nine-month balance-sheet date (`S4369`, the 2010-01-29 printing); part 2's $26.0m is a
**2010-03-31** date (`S4372`, 424B4). Neither emission registers a carrier for a **2009-12-31** balance, and
part 2's own §G.4/§P.2 cells use 2009-12-31 as though it were the same datum as its 2010-03-31 figure. A
supersession across two different measurement dates is not a correction, and the merge could not settle it
against the filing because the web budget was **0 calls and 0 were made**.

**Both dated figures stand.** $24.8m at 2009-09-30 and $26.0m at 2010-03-31 are carried; **the 2009-12-31
value is UNKNOWN**, and the "flat liability across the deposit-policy inversion" reading is **not carried as a
finding**.

**Lands in:** `conflicts.csv` row `U.23` (new anchor, minted at merge, declared in `stage_1.md` §U addendum);
`quantitative.csv` row "Refundable reservation liability", 2010-03-31; `stage_1.md` Volume 1 §F.2 against
Volume 2 §G.4, §J.3, §P.2.

**Settling route (FETCH REQUEST, not performed here):** the 424B4 balance-sheet column heads at
`0001193125-10-149105/d424b4.htm` — one read of `sources/sec/0001193125-10-149105_d424b4.htm` for the
reservation-liability line at 2009-12-31 and 2010-03-31 settles it from bytes already on this disk.

---

## COR-02 — accession `0001193125-10-099603` is Amendment No. 2, not "S-1/A No. 3"

**Withdrawn:** part 1's register title for `S4371` ("S-1/A No. 3 primary document ds1a.htm acc
0001193125-10-099603"), repeated from the probe dossier (`research/sources.csv` `S0003`, "third amendment").

**Basis (all held bytes):** the response letter filed **inside** that accession (`filename13.htm`,
`S4382`) is captioned as the response for Amendment No. 2; the PricewaterhouseCoopers consent at `dex231.htm`
(`S4380`) consents to the use of a report "in this **Amendment No. 4**" and the 2010-06-28 accession captions
itself **AMENDMENT NO. 8**. Ordinals taken from listing order among held amendments produce exactly this
error. **RD-126's rule — take an instrument's date from the filing index, never from a filename or listing
order — extends to ordinal instrument identity**, and part 2 adjudicated it as `conflicts.csv` `U.19`.

**Not a dating change:** the filing date 2010-04-29 is unaffected, and so is the load-bearing finding — this is
the printing in which "one of our founders" first appears. The claim record `P1-12`/`P2-54` is re-labelled, not
re-dated.

**Lands in:** `sources.csv` row `S4371` (and its aliased probe row `S0003`, folded here); `conflicts.csv`
`U.19`; `stage_1.md` Volume 1 §B.2 and Volume 2 §N.3.

---

## COR-03 — "nothing EDGAR-dated 2003–2008" is superseded in form by the 2005–2009 REGDEX band

**Withdrawn:** the probe's §Verdict wording, repeated into its `S0006` register row and its claim record `F10`:
"Nothing EDGAR-dated 2003–2008: earliest submission in the 1,750-filing window slice is Form D **2009-04-09**."

**Measured (`research/A3_intake_regrade.md`, §Index, against `sources/_index/submissions.csv`):** the earliest
in-window row is **Form REGDEX, accession `9999999997-05-006484`, filed 2005-02-17**, and the band runs to
**12 REGDEX/REGDEX/A rows from 2005-02-17 to 2009-01-12**, every one a SEC-generated `9999999997-*` paper
accession with a `.paper` primary document, **none held by either pass**.

**Sustained in substance:** 2003 and 2004 are genuinely empty on CIK 1318605, REGDEX entries carry **no
company-authored narrative**, and the earliest **company-authored** document remains the S-1 of 2010-01-29.
The null is about **content**, not about **rows**; "EDGAR is empty for the first five and a half years" must be
restated as "empty of company documents 2003–2004, then SEC paper registration entries 2005–2009". The
founder-attribution conclusion — one documentary voice, two datable layers — is untouched.

**Lands in:** `sources.csv` row `S4377` (EDGAR submissions slice, which absorbs the probe `S0006`, part 1's
`P1S09`, part 2's `P2S13` and `P2S15`); `stage_1.md` Volume 1 §Header record-selection null and §Boundary.

---

## COR-04 — the contemporaneous-instrument count moved from three to nine; the 2003–2004 silence did not

**Withdrawn:** part 1's §E.2 statement, carried into `U.18` as claim A, that "three held exhibits and only three
are contemporaneous documents of the period they describe".

**Measured on the enlarged intake:** **nine** held instruments plus **five** readable letters dated inside the
window and spanning 2005-07-11 → 2010-06-25 — Lotus glider supply (2005-07-11, `S4373`), Hull lease (2006-08-16
"dated for reference purposes only", `S4388`), Taiway (2007-02-12), Polytec Holden (2007-04-13), Chroma ATE
(2007-04-19) (`S4387`), Stanford lease (2009-08-06, `S4373`), DOE Loan Arrangement and the Midland pledge and
security agreement (both 2010-01-20, `S4379`), plus the counsel, company and underwriter letters of
2010-04-29 → 2010-06-25 (`S4382`–`S4385`, `S4383`).

**Survives intact:** **none of the nine is dated 2003 or 2004**, so part 1's substantive finding — the origin
void between the 2003-07-01 incorporation and the 2004-03/04 role dates — is unharmed by the larger intake, and
the four supply agreements carry confidential-treatment redactions on their face, so the in-window cost base is
**EMPTY by design, not by search failure**.

**Lands in:** `sources.csv` row `S4387`; `conflicts.csv` `U.18`; `stage_1.md` Volume 1 §E.2 and Volume 2 §N.1.

---

## COR-05 — the FY2009 full-year figures ARE in the registration lineage (Amendment No. 1, 2010-03-29)

**Withdrawn:** part 1's quantitative note that "the FY2009 full-year figure is NOT in the S-1, which carries
only 9M2009", and the related note on its XBRL row that FY2009 reaches us only from 2011-vintage periodic
reports.

**Correct:** both statements are true of the **2010-01-29 original printing** and false of the **lineage**.
Amendment No. 1 (`0001193125-10-068933`, 2010-03-29, `S4370`) adds the audited FY2009 statements: `111943`
occurs 0 times in the original S-1 and 5 times there, and `55740` 0 → 8. The FY2009 revenue and net loss are
therefore carried in **registration-lineage** instruments as well as in the XBRL series, and the row that said
otherwise is corrected rather than deleted.

**Consequence for independence:** this does **not** create a second voice. The lineage is one registrant
(§3 filing-lineage rule); what changed is the **date of the earliest carrier** for FY2009 money, which moves
from a 2011 periodic report to a 2010-03-29 amendment — 21 days before the offering.

**Lands in:** `quantitative.csv` row "FY2009 revenue and net loss as reprinted post-IPO" (2009-12-31) and
`timeline.csv` row 2010-03-29; `stage_1.md` Volume 1 §A.3/§D.1 and Volume 2 §J.1.

---

## COR-06 — the held-corpus denominator, measured once so three printed counts stop disagreeing

**Withdrawn as printed:** part 1's "76 documents across 24 accessions"; the re-grade's "76 documents,
59,479,299 bytes … across 28 accessions"; part 2's "85 documents / 33 distinct accessions / 59,900,392 B".

**Measured by this merge on the written bytes** (`sources/sec/`, sidecars and `_MANIFEST.csv`/`_UNANSWERED.csv`
excluded): **83 documents across 32 distinct accessions, 59,881,144 B**. `sources/sec/_MANIFEST.csv` carries
**76 rows across 25 accessions** and omits exactly seven items — the **3 corrupted SEC-staff UPLOAD PDFs**
(`0000000000-10-010920/-019954/-027152`, the text-mode-destroyed bytes at `S4386`) and the **4 CORRESP letters**
(`0001193125-10-135111`, `-145972`, `-145981`, `-147594`, i.e. `S4383`–`S4385`) — which is why the regrade's
`auto` run printed **0 UNANSWERED while leaving 269 in-window index rows at 28 fetched accessions**: "0
UNANSWERED" is not coverage and is not a null for the rest.

**Reconciliation:** 85 (part 2) = 83 documents + `_MANIFEST.csv` + `_UNANSWERED.csv`; 76 = the manifest's own
row count; 24/25/28/32/33 are accession counts taken over different inclusion rules, not different corpora. No
claim in the volume depends on which denominator is quoted, and every register row now names the measured one.

**Settlement debt handed on (not fixed here, reported per §14):** `tools/sec_intake.py` writes binary
documents in text mode (the three PDFs carry 23,268 / 13,489 / 10,637 U+FFFD sequences and yield 0 text from
two extractors; they contain no image objects, so only a binary re-fetch can recover them — they are
**UNANSWERED**, not empty) and its `grab --accession` form without `--file` invents `index-headers.txt` and
404s. Also reported, unfixed: `merge_census.py` cannot attribute a `validation.csv`/`failures.csv` pair
(RD-132), and it globs `_parts/*.md` only, so it never saw the probe's 25 rows.
