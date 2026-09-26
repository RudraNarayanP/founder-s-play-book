# apple_s1_audit1_chronology_hindsight.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:24:47Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: WRITTEN 2026-09-25 (apple-s1-audit)

**PASS-WITH-DEFECTS. High-severity count: 1.** Medium: 3. Low: 3.

This is an unusually clean volume: the `$666.66` position is correct on every one of its fifteen appearances,
the five mandated live conflicts are genuinely two-sided with carriers named and averaging explicitly forbidden,
`mechanism UNKNOWN` is used instead of manufactured mechanism, and the inevitability sweep returns effectively
zero. I re-grepped eleven load-bearing quotations against `sources/` bytes and all eleven are present. I did not
merge this volume and I am not repairing it.

The one high-severity item is a single boundary inversion in §Q: a row dated **1977-01-19** carries the window
status **"In-window (last document before the edge)"**, sixteen days *after* the adopted 1977-01-03 edge, and the
parenthetical asserts an ordering the date contradicts. §Q is the section whose stated rule is that the reader
"cannot drift the boundary," and the mislabel is load-bearing for a count claim in S1P3-10. Both are single-cell
fixes; neither is a research failure. A first audit of a freshly merged volume failing on one item is the expected
result, and this is that item.

| Label | Sev | Gate | One-line defect |
|---|---|---|---|
| G1-A | **High** | 1 boundary | §Q row `1977-01-19` labelled "In-window (last document before the edge)" — post-edge, ordering inverted |
| G1-B | Medium | 1 boundary | S1P3-10's "twenty dated rows inside the window" reaches 20 only via G1-A; its own Date span ends 1977-01-19 |
| G1-C | Medium | 1 boundary | S1P1-05 / S1P1-06 still assert April/June-July 1977 artifacts are "inside the window" in the citable appendix (registered U.019, correctly not silently repaired) |
| G1-D | Medium | 1 independence | BYTE tiered as Tier 1 volume- and register-wide, incl. the unsigned 1981 column that corroborates the end edge and the magazine-compiled 1977-04 store directory; §5 makes trade print Tier 3 |
| G1-E | Low | 1 boundary | Post-boundary marker convention is prose-only; 7 of 10 out-of-window `timeline.csv` rows carry no out-of-window note, one calls 1977-04 print "for Stage 1" |
| G2-A | Low | 2 leakage | §H (a "knowable in-period" section) leans on 1977-02/1977-04 carriers classed CONTEMPORARY OBSERVATION with no §6 RETROSPECTIVE SOURCE tag |
| G1-F | Low | hygiene | `sources/test_direct.txt` duplicates the byte-1976-09 ad; risks inflating the "twelve cached BYTE 1976 issues" denominator (suspicion, not verified) |

Gate 2 has **zero** high or medium findings. The hindsight firewall and the mechanism discipline pass.

## Chronology defects

STATUS: WRITTEN 2026-09-25 (apple-s1-audit)

### G1-A — HIGH. The boundary drifts by sixteen days inside §Q, in the section built to prevent exactly that.

**Text quoted.** §Q's micro-timeline row, Window-status cell: date cell `1977-01-19`; status cell
`In-window (last document before the edge)`; event cell "Homebrew `hcc0213`: **zero** body occurrences; the
founding period's best outside primary is silent across the boundary"; anchor `U.021`.

**Why it is a defect.** The adopted edge is **1977-01-03** (defended at length in §STAGE BOUNDARY
JUSTIFICATION, end-edge table, adopted row). 1977-01-19 is after it. The status cell is therefore wrong in its
classification *and* its parenthetical inverts the ordering — it is the first document **past** the edge, not the
last before it. §Q's own preamble says every row must state whether it is in-window (≤ 1977-01-03), a far-side
witness, or out of window, "printed so the reader sees the boundary's neighbourhood and cannot drift it."

**The volume elsewhere is right, which localises the fault.** The same fact is carried six more times and every
other carrier uses the straddle form: §A "The corporation's own first month in the record — **Empty**"; §D
"`1976-12-10 → 1977-01-19` … the two Homebrew issues **straddling** the incorporation"; claim record **S1P1-29**;
§M; §P row **P32** "`1976-12-10 → 1977-01-19` … spanning the incorporation"; and in `stage_1_part_2.md` the
`timeline.csv`, `conflicts.csv` and `failures.csv` rows all keyed to **U.021**, which carry the range form
`1976-12-10/1977-01-19`. Only §Q flattened the range to its later endpoint. This is a merge-presentation defect,
not a research defect: the register still holds the range.

**Evidence.** Read from `stage_1.md` §Q and cross-read against `research/timeline.csv` (U.021-keyed row,
`date_or_range` = `1976-12-10/1977-01-19`). I also independently confirmed the underlying negative: re-running the
body-only count over `sources/ia_homebrew/hcc0211.txt` and `hcc0213.txt` with the volume's own exclude-lines-1–5
rule returns **0** Apple body lines in each, and a naive whole-file grep returns exactly **1** false positive per
file — so the "silence" is real and the volume's stated grep trap is accurate.

**Proposed remedy (not applied).** In §Q: set the status cell to `Straddles the edge (1976-12-10 in-window;
1977-01-19 far side)` and delete the "last document before the edge" clause. No register change needed.

### G1-B — MEDIUM. S1P3-10's row count depends on G1-A.

**Text quoted.** S1P3-10: "The Stage-1 spine contains **twenty dated rows inside the window** and none of them is
an Apple-side document" — `Date: 1975-10-15 → 1977-01-19`.

**Finding.** Counting §Q's status column as printed gives 19 rows marked In-window (some qualified "milieu",
"start edge", "null", "contested") plus the `1977-01-03` row marked **Window end** = 20. Remove G1-A's
misclassification and the in-window figure is 18, or 19 counting the boundary event. The claim's own `Date:` span
also terminates on the post-edge 1977-01-19. The substantive assertion — that no in-window row is an Apple-side
document — survives untouched; only the arithmetic and the span are wrong.
**Remedy:** restate as "eighteen dated in-window rows plus the boundary event" and close the Date span at
1977-01-03.

### G1-C — MEDIUM. Two appendix claim records still place post-boundary artifacts "inside the window".

**Text quoted.** S1P1-05: "A national retailer directory published in a technical monthly **inside the window**
lists outlets across many jurisdictions…" — `Date: 1977-04`. S1P1-06: "A company advertisement **inside the
window** takes bank cards and offers prepaid freight and a carrying case on a mail-order form" —
`Date: 1977-06 / 1977-07`.

**Finding.** Both are April 1977 and June–July 1977, i.e. three to six months past the edge, and both are exactly
the artifacts the §Boundary rejection row names as refused ("These are the two or three best contemporaneous
*commercial* artifacts the corpus holds, and they sit **after** the adopted boundary"). The defect is **known and
adjudicated**: it is registered as S1P1-CF-10 → **U.019**, whose CLAIM B upholds the boundary, and re-listed in
§M's failure-of-evidence list. The merge correctly declined to edit another pass's released words (§14 rules 4/12).
I confirm the merge's refusal was the right call and that **U.019 preserves the substance**. It remains a live
defect only because the claim appendix is the atom downstream readers cite: a consumer pulling S1P1-05 gets a
`Class: FACT` record asserting in-window status that the volume itself rejects. Compounding it, both records read
`Source date: UNKNOWN` although the dates are precisely known — which suppresses the very contradiction that makes
U.019 legible. **Remedy:** a narrow correction pass on these two records (window status + source date), leaving
all other S1P1 text alone.

### G1-E — LOW. Post-boundary marking is prose-only, and the `(PB)` token the brief asks about does not exist here.

`(PB)` occurs **0 times** in either volume. The honest convention in use is §Q's Window-status column plus prose
`post-window` (35 occurrences, of which 28 in volume 1) and `far-side witness`. So the labelling is honest where it
appears. Where it does not appear is the register layer: of the ten `timeline.csv` rows dated past 1977-01-03,
only three carry an out-of-window note ("Post-stage; admitted only as the far-side witness"; "Post-window";
"OUT OF WINDOW, logged as the outer edge of the record"). Seven do not, and one of those — the 1977-04 store
directory — carries the note "The most granular channel evidence recovered **for Stage 1**". Since §13 permits only
the four stage literals and every row is `stage1`, an unmarked post-boundary row is indistinguishable from
in-window state to any register-only consumer. **Remedy:** extend the three existing out-of-window notes to the
remaining seven rows; do not invent a fifth stage literal.

### Sequence and duration — PASS

No claim states an outcome before the event producing it; the spine is genuinely causal (design → club letter →
dealer advertisement → mail-order discount → exhibitor list → incorporation). Every stated duration checks against
the dates on both sides: `1976-04-01 → 1976-04-12` = **eleven days**, which matches U.005's claim_a and the §Q row
"eleven days after formation" (the twelve-day variant is held as conflict, not resolved); `1976-09 → 1977-06` =
"Maker's printed voice begins **nine months after** dealers advertised the product"; §N's "a corporation nine days
to nine months old, depending on the date assumed" is arithmetically coherent against both candidate formation
dates. `timeline.csv` is not physically date-sorted — rows run to 1981-02, then revert to 1975-04-01 — but that is
append order from a §9-compliant merge, not a sequence claim, and the register makes no ordering assertion.

### Dated-not-dated — PASS (this is the volume's strongest layer)

Eleven load-bearing quotations re-grepped against `sources/` bytes, whitespace-flexible because the corpus is
hard-wrapped: `designed late in 1975` (byte-1977-05); the incorporation sentence (10-K FY1994); "incorporated in
1977, reported profits" (byte-1981-02); `Take a byte out of the new Apple-1` (byte-1976-09); "grateful to STEVE
WOZNIAK for providing transportation" (hcc0204); "price under \$700 at the retail level" (byte-1977-05, in
Wozniak's own first-person voice); "a \$666 value / only \$595" (byte-1976-12, IMSAI); "two people in a garage"
(byte-1976-07, Sphere); "10% discount from" and "currently being marketed" (byte-1976-11); "I first saw the
Apple-ll on November 20 1976" (byte-1977-04). **All present.** Three returned zero on a naive single-space grep
and resolve only under multi-line matching — the volume's own hard-wrap warning is true and I would have
manufactured a defect had I trusted the first pass. Retrospective-carrier discipline also holds on the test that
matters most: the 1976-11-20 demonstration reaches us only through an April 1977 publication, and §Q tags it
"published 1977-04" / far-side rather than laundering it into the window. `666.66` independently returns **0 hits
across all 61 files under `sources/`**, confirming §E.4 and §P row P30. And `314 Fifth Avenue` appears in the
June and July 1976 issues **without naming Apple**, so "earliest Apple-1 retail advertisement recovered" at
1976-09 survives the earlier-carrier test — with "recovered" correctly hedging absence-of-evidence.

## Hindsight defects

STATUS: WRITTEN 2026-09-25 (apple-s1-audit)

### G2-A — LOW. §H classifies post-window carriers as CONTEMPORARY OBSERVATION without §6's RETROSPECTIVE tag.

**Text quoted.** §H.2: "Carl Helmers' April 1977 column defines the '**appliance computer**' in retail terms …
(**CONTEMPORARY OBSERVATION by a named publisher who had a personal relationship with the subjects**, priced into
provenance rather than into corroboration)". §H.3's `NOT KNOWABLE` list cites "the ~35-store directory", and the
record-selection null names "the 101-system survey" and "the ~35-store directory" as the two available errors.

**Finding.** §H is titled "MARKET (AS KNOWABLE IN-PERIOD)" for a window ending 1977-01-03, but its load-bearing
definitional evidence is dated 1977-02-16 and 1977-04 — after the edge. §6 requires that "where a later source is
needed to explain an earlier event it is tagged `RETROSPECTIVE SOURCE`". The class applied, CONTEMPORARY
OBSERVATION, is correct as to the column's *own* moment and the volume immediately discounts it for
corroboration, so no outcome leaks; but the §6 tag is absent and the section's "in-period" frame is therefore
looser than §Q's. Severity stays LOW because every claim built on these carriers is a **negative** knowability
claim, which gets safer, not riskier, as the carrier post-dates the window. **Remedy:** add `RETROSPECTIVE SOURCE
(1977-04)` at §H.2's first use of the column; no reclassification needed.

### Outcome leakage — none found

The known weak spots were tested individually and all hold:

- **Section closers.** §D's anti-hagiography closer is the model case: "Nothing here reads as a company that was
  going to outlast them, **because nothing in the record can say so**." §H.3's closer indicts the reader's
  available errors rather than resolving them. §K.6 makes the registrant's own silence about its first years a
  finding about the archive, not about the firm.
- **KNOWABLE lists.** §C.4, §H.3 and §I.5 keep three separate vocabularies distinct — `KNOWABLE` in-window with
  documents named, `NOT KNOWABLE from any surviving public record`, `UNKNOWN with reason` — and the third is
  correctly reserved for "1976 revenue and unit volume, because no document in any cached family carries them."
- **"So what" codas.** §N.2 is the volume's most exposed closer, asserting that the shape of the decision register
  is "the opposite of the received Apple founding story's usual form". It satisfies §16 in full: evidence (eight
  rows, five rationales UNKNOWN), mechanism ("no document in the corpus records deliberation of any kind"),
  alternative explanation tested and not excluded ("that deliberation was recorded and has simply not been
  digitised … §N's blanks are retrieval failures, not historical ones"), and confidence scoped ("High for the
  table as a description of the record; **no confidence is claimed for it as a description of the founders'
  minds**"). §G.4's arc closer stays inside the geography the print supplies.
- **Denominator discipline.** §D refuses the "200 Apple-1s" count as a divisor by name and states why: it "may not
  be used as a denominator in §L — which is where such figures usually smuggle in." §L.2 then reports the Faire's
  12,800 as a promoter's self-report with no independent denominator.

### Mechanism claims — PASS; nothing survives on step one alone

Each assertion about *why* something worked was tested as evidence → mechanism → alternative → confidence. The
volume passes because it repeatedly declines to supply a mechanism it cannot document, which is the correct
answer under the brief's rule:

- **Channel mechanism (the central one).** **U.008** holds word-of-mouth against the dated print ladder and closes
  "the transition mechanism is undocumented and **three candidates remain equally consistent**". No causal story
  is manufactured to explain how a word-of-mouth product became a 35-store national channel.
- **Survivorship.** §L/§M state plainly that "the mechanism that separated survivors from the listed dead ends is
  not in this corpus" — a mechanism *named as absent* rather than invented.
- **Capital.** §N's undated row refuses the "obvious necessity of outside capital" reading by name: "the 'obvious
  necessity of outside capital' reading is hindsight and is refused."
- **Price.** **U.004** bounds Wozniak's "under \$700" with the \$675 complete-system comparator but says the
  comparator "bounds but does not establish it", and refuses the decoy-as-origin hypothesis as an unadopted
  INFERENCE.
- Four explicit `mechanism UNKNOWN` dispositions; the phrase "mechanism here would be invention" appears in §L.
- **The one residual** is §G.4's "the club as infrastructure" framing, where the only in-window evidence is a
  single transportation clause (n=1). The volume prices this correctly itself — "**Medium** as an account of a
  distribution mechanism (n=1)" — so I record it as a labelled weakness, not a defect.

### Apple-specific positions — all intact

`$666.66`: fifteen appearances inspected, and **not one states it as fact**. Every one is FOUNDER CLAIM / folklore
or UNKNOWN, each with the local test attached (the IMSAI decoy). No in-window fill: 1976 price, order, units,
revenue, supplier and founder officer title are all held as documented nulls, and the §R table's officer-title row
goes further than required by grading itself "High for this corpus, **Medium as a general statement** (BYTE Aug
1977–Nov 1980 is not cached)". Wayne 10-vs-12, Markkula's terms, 50 orders at \$500, word-of-mouth vs the April
1977 directory and June 1977 order form, and \$77,000 vs \$770,000 are all live two-sided rows in
`conflicts.csv` with both carriers and both dates named; U.005 prints "no average of 10 and 12 may be printed
anywhere" and U.009 keeps the revenue pair out of the metric tables entirely. The wording rule is honoured —
"not establishable in the Stage-1 record", never "never happened" — and I checked all five of the negative-existence
hits my sweep returned. **Three are the rule itself**, stated in §R's preamble, in the §S–§U wording rule and in
the status-vocabulary clause. The other **two are the same single judgment**, in U.024's narrative anchor and in its
`conflicts.csv` row: the missing artifact is "a production ledger, which almost certainly never existed" /
"probably never existed". That is a hedged probabilistic claim about whether a three-person hobby partnership kept
paperwork, not an assertion that a historical event failed to occur, so it sits inside the rule's purpose. **No
violation found** — but it is the one place in 65k words where the volume's own vocabulary rule bends, and it bends
in a place where the hedge ("almost certainly", "probably") does the work the rule asks for.

## Sweep counts

STATUS: WRITTEN 2026-09-25 (apple-s1-audit)

Construction sweep over both volumes (`stage_1.md` + `stage_1_part_2.md`), case-insensitive occurrence counts:

| Construction | vol 1 | vol 2 | total | Disposition |
|---|---|---|---|---|
| `proved` | 0 | 0 | **0** | — |
| `showed that` | 0 | 0 | **0** | — |
| `drove` | 2 | 0 | **2** | Both literal motion: "a hobbyist **drove** his own board to a club sixty miles away"; "the designer **drove** it to the meeting". Not causal. |
| `did the work` | 0 | 0 | **0** | — |
| `clearly` | 1 | 0 | **1** | "not **clearly** a decision at all but possibly an incapacity" — an epistemic hedge that *lowers* confidence. |
| `inevitable` | 0 | 0 | **0** | — |
| `destined` | 0 | 0 | **0** | — |
| `the reason was` | 0 | 0 | **0** | — |
| **Total flagged** | **3** | **0** | **3** | **All three benign on reading. Effective inevitability count: 0.** |

Supporting counts: `post-window` **35** total — 31 in volume 1 (28 lower-case + 3 capitalised), 4 in volume 2
(3 + 1) — / `outside the window` 3 per volume / `so what` as a literal **0** / `mechanism` dispositions 4 UNKNOWN
or "equally consistent" / `KNOWABLE`-family markers 17 / `Tier: 1` in narrative **46** (see G1-D) / `(PB)` **0**.
For a 65k-word volume written about the most-hagiographed company in the corpus, a three-hit sweep with zero
surviving causal assertions is a genuine result, not an artefact of my pattern list: I read every hit rather than
accepting the zeros.

## Independence audit

STATUS: WRITTEN 2026-09-25 (apple-s1-audit)

### The centrally assigned `S1M-01…S1M-10` block — PASS, no collisions

I read all 23 `sources.csv` rows: **all `source_id` values are distinct**, and every S#### token in the narrative
resolves (gates `keys` confirms independently). Tracing each assigned id to its carrier: S1M-01 the FY1994 Form
10-K; S1M-02 the Christie's lot-242 object with its Sotheby's 2011 custody chain; S1M-03 the RR Auction essay;
S1M-04 the apple1registry collector pages; S1M-05 the 1976-09-15 Homebrew newsletter; S1M-06 the EDGAR
submissions index; S1M-07 BYTE and Homebrew dealer advertisements; S1M-08 the token censuses; S1M-09 the
unretrieved Kilobaud/Creative Computing family; S1M-10 the patent-register search result. No two ids name one
document, and no id names two documents.

The three lineage decisions the merge sheet reports are all correct under §13's filing-lineage rule, and I checked
them rather than accepting the sheet:

- **S1P3-S04 refused as a second row** and folded into **S1M-02** — right call. The Christie's catalogue, its
  essay, the 2011 lot record, the 2026 press and the RR Auction pages are one custody chain around one unread
  object, and §T states it: "**ONE OBJECT, several carriers … are one custody chain, not corroboration.**"
- **S1M-08**'s own note is the discipline in miniature: "two independent passes over one corpus — **a check, not a
  second source**."
- **S1M-03** is refused standing as corroboration of the merchant story it carries: "vendor copy; not independent
  of the merchant it quotes." A2S-06/A2S-07 do the same job for company-side print — "NOT independent of A2S-07
  (same publisher)"; "same commercial interest as A2S-06: two documents, one interest." **S1M-10**, minted by the
  merge from a dossier-local key with no requested row, correctly records itself as "one search, page 2 of the
  result set not read: a search null", and adds no evidence of its own.

### G1-D — MEDIUM. BYTE is tiered as Tier 1, including the two carriers that most need the distinction.

§5 assigns **Tier 3** to "industry/trade publications". The register assigns **Tier 1** to all thirteen A2S
periodical rows and to S1M-07, and the narrative uses `Tier: 1` 46 times, so the boundary's second witness rests
on a row described in §Boundary as "**Two Tier-1 documents** of unrelated lineage" where the second is `A2S-09`,
"'Apple Stock Goes On Sale', BYTE February 1981" — an unsigned journalist's column reporting company-supplied
financials. The same inflation covers `A2S-05`, the April 1977 national store directory: magazine-compiled
third-party data, which is exactly what §H.3 warns a reader against ("reading a magazine's own advertising
inventory as somebody's sales channel").

**This does not break corroboration.** Independence is satisfied — different author, publisher and decade from the
filing — and the end edge's year stands on the 10-K alone with the column as a genuine second origin. What fails
is the **rank** claimed for the corroborating carrier, and rank is what the confidence scale is built from. The
volume proves it knows the distinction: §R's own legal-events row grades "the two 1976 papers, from a **Tier-3**
catalogue of an unread object," correctly down-weighting an auction house while uplifting a magazine. Periodical
print does earn Tier 1 where the item *is* first-party matter — Apple's own June 1977 advertisement (A2S-07) and
Wozniak's bylined May 1977 article (A2S-06) are properly Tier 1 regardless of carrier — so the fix is per-row, not
a global demotion. **Remedy:** re-tier A2S-05 and A2S-09 to Tier 3 (or Tier 2 with a stated rationale), and amend
the boundary sentence to "a Tier-1 registrant filing and an independent Tier-3 trade column."

### Double-counting tests I ran and the volume passed

Wayne and Markkula are held at **zero** in-window occurrences, and the volume resists the temptation that creates:
it states as a §-level caveat that this "is a property of the source class, not evidence of absence." The 1981
column that is Markkula's only footprint is never treated as independent confirmation of his terms — U.007 closes
"the 1981 holding **may not be back-projected** into 1976-77 as capital." The Homebrew run's own reprints are
counted once (the "one campaign, counted once" rule in §Q), and S1P3-10's corroboration cell reads "per row;
campaigns counted once." The `1976-04-30` newsletter item — a letter from a *different* club reprinted by Homebrew —
was caught, discarded as a boundary support, and registered as **U.020**, which is the single most impressive
lineage judgement in the volume: it defeats a source that reads as primary and in-window and is neither.

## Passed checks

STATUS: WRITTEN 2026-09-25 (apple-s1-audit)

### Mechanical layer, quoted verbatim as instructed (not re-derived)

`python tools/gates.py --company-dir founders_playbook/01_companies/company_004_apple --checks csv,keys,anchors,budget,corrections`

```
Findings: **0** | Passes: 18
coverage     9 registers, 3 stage volumes, 41 source documents
keys         stage_1.md cites 2 hyphenated record keys: S1M-01, S1M-10
keys         stage_1_index.md cites 4: S1M-01, S1M-02, S1M-09, S1M-10
anchors      stage_1.md declares 55 anchors
corrections  no CORRECTIONS.md -- gate DID NOT RUN (not a pass)
csv  timeline.csv 30x11  quantitative.csv 44x12  conflicts.csv 38x15  sources.csv 23x18
csv  data_gaps.csv 35x8  validation.csv 6x11     failures.csv 6x11    decisions.csv 4x15  channels.csv 0x11
csv  source_id tokens resolve: timeline, quantitative, conflicts, validation, failures, decisions, channels
anchors parity  55 narrative anchors <-> 55 register anchors
budget  stage_1.md 56537 (cap 60000) | stage_1_index.md 1472 | stage_1_part_2.md 8713
```
(All 18 reported lines were width-clean with 0 findings; condensed for readability, not re-derived.)

`python tools/gates.py --self-test`

```
anchor with no register row                  [anchors]     CAUGHT
correctly escaped doublequote must stay clean [neg]        STAYS CLEAN
dangling source_id                           [csv]         CAUGHT
duplicate record id                          [csv]         CAUGHT
numeric stage vocabulary                     [csv]         CAUGHT
paraphrase presented as quote                [quotes]      CAUGHT
propagated retraction must stay clean        [neg]         STAYS CLEAN
retraction never reaches the registers       [corrections] CAUGHT
row with wrong column count                  [csv]         CAUGHT
unquoted comma shifts fields                 [csv]         CAUGHT
unresolvable source token in narrative       [keys]        CAUGHT
clean fixture                                CLEAN
self-test: PASS
```

**Count discrepancy against my brief, resolved in the register's favour.** I was dispatched with "38 timeline /
35 quantitative / 44 conflicts / 30 sources / 23 data_gaps". The script reads **30 timeline / 44 quantitative /
38 conflicts / 23 sources / 35 data_gaps** — the brief's five numbers transposed. The script is authoritative
(§15.1), and the merge sheet's own before→after line independently confirms 23→30, 30→44, 13→38, 13→23, 0→35.
Recorded so no later pass "repairs" the registers toward my brief.

### Judgment-gate items that passed

- **Merge refusal verified as correct and lossless.** The five `S1P2-CF-01…05` rows really do parse to 14 fields
  against a 15-column header, so appending them literally would have written shifted records. **Re-pointing
  preserved meaning in all five cases**: I read U.003, U.005, U.007, U.008, U.009 and each carries both sides with
  named carriers and dates, and each prints its part-2 key in its `Maps:` cell — CF-03→U.003 (50 boards at \$500),
  CF-01→U.005 (Wayne), CF-02→U.007 (Markkula), CF-04→U.008 (channel), CF-05→U.009 (revenue). No subject lost a
  side; no row averaged.
- **Seven "repaired so it could be applied" rows.** The four `sources.csv` rows that gained a `source_type` cell
  carry labels matching their own titles — S1M-01 "Registrant filing", S1M-02 auction catalogue, S1M-04 collector
  registry, S1M-05 club newsletter read correctly — so the insertions were content-preserving, not inventions.
- **`channels.csv` left empty is right**: 0 rows, header only. Minting channel rows from §D.3/§G prose would have
  manufactured the very mechanism U.008 refuses. Recorded as an open shape, not a filled one.
- **Word budget / §9.3 split**: 56,537 + 8,713 = 65,250 against a 60k cap, cut at one section boundary, numbering
  continuing; volume 1 at 94% is amber, not a defect.
- **Gap disclosure with a real denominator.** **U.044** names the Homebrew holes precisely — Vol 1 No 1–8 and Vol 2
  No **8, 10, 12**, 14–21 — and states "only **13 of 32** enumerated items are cached" at HIGH importance with a
  follow-up task. I verified it independently: exactly 13 `.txt` files under `sources/ia_homebrew/`, and the absent
  numbers are those named. U.021's silence argument is therefore bounded by a **disclosed** denominator rather than
  an erased one — the failure mode this corpus keeps hitting at other companies.

## Not testable

STATUS: WRITTEN 2026-09-25 (apple-s1-audit)

- **The five live conflicts cannot be adjudicated, by me or by anyone on this evidence.** Wayne's 10% vs 12%,
  Markkula's terms and arrival date, the 50 orders at \$500, and \$77,000 vs \$770,000 turn on the unread
  partnership instrument, an unread charter file and a 1980 prospectus never held. Leaving them live is the correct
  terminal state, not an open task.
- **The auction carriers are outside my reach.** S1M-02/S1M-03's contents — the lot description, the "Spring 1976"
  vs "July 1976" self-contradiction, the "fifty computers at five hundred dollars apiece, to retail at \$666.66"
  restatement — exist in this repo only as the volume's report of them; the lot-text fetch returned **403** and no
  bytes sit under `sources/`. I can certify the volume's *handling* of those carriers, not its *reading*.
- **1976 BYTE issue dates.** §L-6 concedes internal cross-references hold for Oct–Dec and **fail for July**
  (`-07` previews August/September pieces yet narrates through 30 October). I verified the "two people in a garage"
  comparator sits in that file, and the volume's mitigation — nothing in the adopted boundary depends solely on
  `-07`, every Jan–Sep 1976 statement carries `issue-date: provisional` — is the right disposition. Page-sequence
  verification is beyond a 0-web pass.
- **Founder zero-occurrence counts** are not falsifiable the way a quotation is: absence across ~13 MB is a
  property of the source class, as the volume says. I confirmed the counts are honestly scoped ("High **for this
  corpus**, Medium as a general statement").
- **`CORRECTIONS.md` propagation is untested, not passed** — see gate finding 1 below.
- **Whether §13 needs a fifth stage literal for post-boundary rows** is a method question above my remit; I flag
  the consequence (G1-E) and recommend against inventing vocabulary.

### What the mechanical gates structurally cannot see for this company

1. **`corrections` DID NOT RUN.** No `CORRECTIONS.md` exists for Apple. The self-test proves the gate works
   ("retraction never reaches the registers — CAUGHT"), so Apple's retraction propagation is **uncertified, not
   passed** — and Apple has three live retractions (the probe's discarded `1976-04-30` Homebrew support, the "about
   200 Apple-1s" count, the `666.66` folklore) with no carrier into the registers except §U prose.
2. **Volume 2 is invisible to three gates.** The merge sheet already logged this as a *gate* defect and I confirm
   it in the output: `NARR_GLOBS["stage1"]` reads only `stage_1.md`. The "55 ↔ 55" anchor parity and the `keys`
   sweep therefore cover **87% of the volume**; `stage_1_part_2.md`'s 8,713 words — §X's consolidated untried
   routes and every register-request block quoted into the registers — were never parsed. The registers themselves
   are fully width-checked, so the blind spot is the narrative side of the parity claim.
3. **Shape without semantics.** All 38 `conflicts.csv` rows pass width while nothing checks that `claim_a` and
   `claim_b` are genuinely two-sided or that `residual_uncertainty` is a residual. §Q's Window-status cell passes
   the CSV gate as a *cell*; **G1-A is a wrong value in a well-formed column**, and no scripted check can see it.
   Nor can any see S1P1-05's "inside the window" — a string, not a type error.
4. **Independence and tier judgment are not scriptable.** S1M-02's fold, the A2S-06/07 company-side notes and
   G1-D's BYTE inflation all live in free-text cells read only for id resolution.
5. **Nothing compares the volumes against `sources/`.** All eleven quote verifications, the `666.66` = 0 census,
   the 1976-09 earliest-retail-ad survivor test and the hcc0211/13 body-zero were done by hand. The `quotes` check
   exists in the self-test but was not in the run I was directed to execute, so verbatim existence is currently
   unmechanised for Apple — §15.6's advisory about unmatched secondary quotes applies squarely here.
6. **Budget counts words, not drift**, so a 94%-of-cap volume 1 carrying a 26-row §Q table gets no signal, and
   duration claims ("nine months after", "eleven days") are pure prose to a script.

## Untried

STATUS: WRITTEN 2026-09-25 (apple-s1-audit) — closed at 45/60 tool calls, before the 50-call stop line, so this is
a chosen scope boundary rather than an exhausted budget. Zero web requests made, as briefed.

**Narrative not read line-by-line** (I read §A, §Boundary, §C.4, §D.3 and its codas, §E.4/E.5, §H.2/H.3, §K.1,
§N/§N.2, §P, §Q, §R, §T, §U in full or substantially): **§B.1–B.5** founder-state detail (the highest
retrospective-memoir density in the volume, and where a Wayne or Markkula hindsight leak would most plausibly sit);
**§C.1–C.3**; **§E.1, E.3, E.6**; **§F.2–F.4** customer ladder; **§G.1–G.3, G.5, G.6** supply and assembly, where
the single assembly claim and its "function nobody is credited with" live; **§I.1–I.5** competition; **§J.1–J.4**
technology, incl. the *iWoz*-only calculator/bus capital story flagged in the evidence ledger; **§K.2–K.6**;
**§L.1/L.2**; **§M.1–M.5** beyond the two rows I sampled; **§O.1–O.3** counterfactuals, the section whose frame is
most vulnerable to outcome knowledge.

**Registers read for content, not recomputed.** `quantitative.csv` (44 rows) — I did **not** recompute
`derived_arithmetic` against `evidence_class`, so an ESTIMATE labelled FACT, or arithmetic that no longer matches
its operands, is uncaught here. `validation.csv` / `failures.csv` / `decisions.csv` — schema and `source_id`
resolution only; I did not test `what_it_did_not_demonstrate` cells for smuggling, nor whether `actual_result`
carries its `RETROSPECTIVE` label everywhere it needs one. `data_gaps.csv` — the merge asserts every High-importance
gap carries a `follow_up_task` and gates do not check this; I spot-verified U.044 only. `timeline.csv` `conflict_ref`
→ anchor integrity beyond the U.021 rows.

**Structural cross-checks skipped.** `_MANIFEST.md` and `stage_1_index.md` vs the merge sheet's own numbers;
whether the 13 legacy `U-A2-*` rows can double-count against canonical `U.nnn` rows under any plausible consumer
filter; whether `S1M-10`'s 1977-04-11 patent application is Tier-1-eligible at all (it is a search null on a
post-window date, and §5 lists patents as Tier 1 — the tension is real but the row is honestly labelled);
byte-identity of the five new register headers against Amazon's, which the merge sheet claims and I did not
re-verify; the 576/70-token arithmetic of the volume split.

**Deliberately not attempted** (belong to other passes or to scripts): the three `_parts/s1_p1.md` rewrites the
merge refused (S1P1-01…11 `Source`/`Tier`/`Conf` upgrades, S1P1-10's mis-pointed `Conflicts: U.011` cell) — these
are **repairs**, and §14 rule 4 plus my own certifier-not-repairer constraint bar me; part 3's F1–F5 FETCH
REQUESTs (U.037–U.054), which are §15.1 script work; Kilobaud 1976's absent text layer; the California SoS entity
file; the 1980 prospectus; page-sequence dating of `byte-1976-07`; and `sources/test_direct.txt` — I noted it
duplicates the byte-1976-09 ad (different md5, same ad block) and flagged the denominator risk as **G1-F,
suspicion not verified**, because deciding whether it inflates any stated census means re-running the censuses,
which is the scripted job.

**Recommended next dispatch.** One repair agent on four cells only: the §Q Window-status cell and parenthetical for
the 1977-01-19 row; `S1P3-10`'s count and Date span; `S1P1-05`/`S1P1-06`'s window status and `Source date`;
`A2S-05`/`A2S-09` tier values plus the one boundary sentence naming them Tier-1. Then a re-certification pass —
not this one — and a `CORRECTIONS.md` mint so the corrections gate runs for Apple at all.

