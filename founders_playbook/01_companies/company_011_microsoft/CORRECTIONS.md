# Provenance Corrections Register — Microsoft

Standing list of attribution and citation corrections established **after** the dossiers were written, each
verified directly against the bytes held under this company's `sources/` (or a sibling company's shelf,
read-only and grepped in place) rather than accepted from a summary. The consolidation leads are briefed
before several of these land, so their output may still carry the pre-correction form.

**Rule: `stage_1.md` (+ parts), `stage_2.md`, `stage_3.md`, the claim-record appendices and every register CSV
must be emitted with these corrections applied. Reverting one is a defect. A claim whose only support is a
document that must be relabeled to a version which does not contain it is downgraded to `UNKNOWN` until
re-verified — not quietly kept. A superseded entry is marked where it stands, not only where it was retired.**

**Propagation requirement (§14 rule 10, enforced by `gates.py --checks corrections`).** Every `COR-nn` below
must appear (i) in at least one register row and (ii) in at least one stage volume that carried the withdrawn
text. A retraction that reaches prose but not the register is this project's most repeated self-inflicted
injury: the narrative withdraws the claim, `conflicts.csv` keeps asserting it, and the next reader trusts the
register.

---

## COR-01 — the "December 17, 1975" Altair BASIC date is Processor Technology's VDM-1, not a Microsoft event

**Withdrawn:** the statement in `research/A2_periodical_and_filings_settlement.md` §Family c item 1 (l.103-104)
that Homebrew issue `hcc0201` *"separately reports Altair BASIC availability 'set for December 17, 1975.
Delivery was then scheduled for January 15, 1976'."*

**Relying on the bytes** — `company_004_apple/sources/ia_homebrew/hcc0201.txt` **lines 49-55**, read in full
on 2026-09-26:

> *"VDM-1 - Many people are waiting delivery of the VDM-1 Video Display Module from Processor Technology
> Corporation, having placed their order some time ago. Originally availability was set for December 17,
> 1975. Delivery was then scheduled for January 15, 1976 and customers with pending orders were notified. As
> of the end of January, deliveries had not been completed. How does this happen? It turns out that the
> character generator needed is in very limited supply and PTC is awaiting delivery of these parts."*

The sentence's own subject is **the VDM-1** and its vendor is **Processor Technology Corporation**. The word
BASIC does not appear in the passage. The earlier pass attached the dates to Altair BASIC by **textual
proximity inside one issue**, which is method §14 rule 8's exact failure: an inherited figure written down
before the cited line was read.

**Actions, all three of them.**
1. **Altair BASIC has no release, availability or delivery date in any held byte. The value is `UNKNOWN`
   again**, and it is recorded as a `quantitative.csv` row whose value cell reads `UNKNOWN` with the
   superseded value printed only inside the retraction text. **U.1** is the conflict anchor.
2. **No date may be substituted.** The 1976 letter's *"Almost a year ago … developed Altair BASIC"* yields
   only an unquantified span, and the derived window (c. 1975-02 → 1975-07) is printed as
   `derived_arithmetic` at Low. A month-and-day for a 1975 BASIC release is a fill, not a finding.
3. **The withdrawn sentence is not worthless — it moved sections.** The VDM-1 delay is valid **§I competition**
   evidence (a named hobby-market vendor late on deliveries because a character generator was in short
   supply, as of January 1976) and is used with its correct subject in `_parts/s1_p1.md` §I.2.

**Sweep of the string `December 17` across the corpus, run 2026-09-26 before this entry was minted.**
| hit | file | class | state |
|---|---|---|---|
| 1 | `research/A2_periodical_and_filings_settlement.md` l.104 | **stale** — the misattribution, asserted as a Microsoft fact | tagged in place; original text preserved (this register appends, it does not rewrite history) |
| 2 | `research/B1_periodical_records.md` l.309 | retraction marker — the `U.1` conflict row | correct |
| 3 | `research/B1_periodical_records.md` l.436-437 | retraction marker — §Nulls "RETRACTION carried to the instruction layer" | correct |
| 4 | `research/_b1_fix_blocks.py` l.140 | quoted source text — the row-builder that mints the `U.1` `claim_a` cell | correct |
| 5 | `company_004_apple/sources/ia_homebrew/hcc0201.txt` l.51 | quoted source text, correctly about the VDM-1 | correct |
| 6-7 | `company_005_alphabet/sources/sec/…` (Dec 17, **2003** sublease amendments), `company_041_dell/sources/sec/…` (Dec 17, **1993** officer loan) | other companies' filings | unrelated dates; **not defects**, not this company's files |

`1975-12-17` in ISO form: **0 hits anywhere in `founders_playbook/`.** After this entry, the string survives
in the Microsoft directory only inside retraction language or inside the source bytes that carry it with the
right subject.

## COR-02 — the newsletter's publication place is Mountain View; "Menlo Park" in the pending register rows belongs to a different publisher

**Withdrawn:** the `location` value *"Menlo Park, California (place of publication)"* carried by five
Stage-1 `timeline.csv` rows in `research/B1_periodical_records.md` §Register rows (the 1976-01-31 ×2,
1976-02-29, 1976-03-31 and 1976-04-30 rows).

**Relying on the bytes** — `hcc0201.txt` prints its own editorial address twice: masthead l.12
`Robert Reiling, editor □ Post Office Box 626 □ Mountain View, CA 94042` and the editor's note l.21-22
`Send a copy of your correspondence to me at the HOMEBREW COMPUTER CLUB NEWSLETTER, P. O. Box 626, Mountain
View, CA 94042`. **Menlo Park appears in that issue as somebody else's address**: l.36 `Write PCC, Box 310,
Menlo Park, CA 94025` — People's Computer Company, a different organisation — and BYTE July 1976 l.31478
prints the same PCC Menlo Park address. A club meeting location, `the SLAC auditorium` (l.152), is a third
place again and is not a publication place.

**Action.** The merge takes the ten `timeline.csv` rows emitted in `_parts/s1_p1.md` §J's
`>>> REGISTER ROWS FOR MERGE <<<` block, whose five corrected rows carry
`Mountain View, California (place of publication)` or the letter's own `Albuquerque, New Mexico (reply
address printed in the letter)`, and **discards the Menlo Park form**. Two rules follow from it and bind
later passes: (i) **place of publication ≠ where the company was**, and the 1976 register must keep the
Albuquerque reply address and the Mountain View publication place in separate cells; (ii) a location value
inherited from a sibling dossier's prose is a claim, not an address — this defect was introduced by
summarising the club rather than reading its masthead.

## COR-03 — the transport ceiling is a property of these bytes, not of these facts

Every periodical and corporate-print layer under `sources/periodicals/` (and the Apple/Dell shelf layers
grepped in place) carries `"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"` in
its sidecar, because the bytes arrived over `--insecure` TLS against a stale local CA store. **Consequence
binding on every Microsoft stage file: no print fact in this company's volumes carries High confidence**
until a verified retrieval of the same item exists. The EDGAR layer is different — `sources/sec/0000891020-
94-000175_0000891020-94-000175.txt.meta.json` records `http_status: 200`, `bytes: 442763`, a `sha1` and no
transport caveat — so **High is available only for propositions about what that filing says**, which is a
statement about a document, not about 1975. Measurements over bytes held on this disk (grep hit-line counts,
arithmetic sums, index row counts) may be High **as measurements** and are labelled as such; that is not a
route around the ceiling for any print fact.
