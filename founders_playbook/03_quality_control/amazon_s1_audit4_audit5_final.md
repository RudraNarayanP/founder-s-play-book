# Audit Sheet — Amazon.com (company_001_amazon) · Stage 1 · Run 2026-09-24 (final)
Auditor: **Level-3 Final QA Auditor** — independent of producer: **yes**. This auditor wrote no part of the
dossiers, the merge, the boundary re-base, or any repair pass (numbers round 1/2, hindsight round 1/2, register
sweeps round 1/2), and **edited nothing**: the three target files were read, grepped and measured only, and no
file outside this sheet was created, moved, deleted or tidied.

Two gates, kept separate because a pass in one is not a pass in the other:
**PART 1 = AUDIT 4 confirmation** over the two conditions that failed at the recheck
(`amazon_s1_audit4_recheck.md`, N-01…N-06, RD-035…RD-037);
**PART 2 = AUDIT 5 adversarial verdict** on the reconstruction as finished.

Target as measured this pass: `stage_1.md` **45,878 w / 2,139 ll.** · `context_appendices.md` **10,882 w /
659 ll.** · `stage_1_claim_records.md` **49,309 w / 598 ll.** Boundary **1994 idea formation → 1995-12-31**
(first firm anchor 1994-07-05).
Binding reads: `AUDIT_PROTOCOLS.md` (AUDIT 4 steps 1–5, AUDIT 5 steps 1–5, template);
`00_METHOD_AND_STYLE.md` §2 (firewall + the record-selection null), §3 (classes, confidence, the independence
rule "repeated copying of one origin story is **one** source, not many"), §6, §7 (+ the coda rule from RD-034),
§9.3, §11, §13 (High-importance gaps require a follow-up task); `CORRECTIONS.md` COR-01…COR-14;
`adversarial_review.md` (E-01…E-30, §4 alternatives, §5 hazards, §6 nulls N-1…N-9, §7 residual risks);
`amazon_s1_audit4_hindsight.md`; `amazon_s1_audit4_recheck.md`; `amazon_s1_hindsight_repairs2.md`;
the two register sweeps; `MASTER_RESEARCH_LOG.md` §6 (RD-020…RD-039).

**Method.** A repair log is a claim, not evidence. Every item was re-found **in the file as it stands**, by
string as well as by line, and the causal sweep was run **on constructions rather than on the named list**
(`drove · enabled · allowed · let(s) · meant · caus* · produced · generated · gave · because · since · is why ·
makes/made · made possible · did the work · worked · the only · could not · no one · nobody · key to · thanks to
· led to · positioned`) across both deliverables, plus `validation.csv`, `failures.csv`, `channels.csv` and
`stage_1_claim_records.md` for twins of the same proposition. Negative controls re-run: `8,000,140` = **0 hits**
in all three prose files (`8,000,014` present at `stage_1.md` ll. 68, 608, 862, 1422 area and
`context_appendices.md` ll. 81, 598); `2,300` = absent from the filings trail and carried only as a labelled
founder claim (`stage_1.md` ll. 453–460, 631; `→ U.6`); `did the work`, `drove discovery`, `route worked` =
**0 dataset-voice hits** in either file. Post-sweep edits to `stage_1.md`/`context_appendices.md` were checked
against git (`afb7aac`, `98aa933`): number-register propagation only, no hindsight-relevant sentence altered
after `c92de62`.

| Audit | Result | Items checked | Failures found | Actions taken | Residual risk |
|---|---|---|---|---|---|
| 1 Chronology | not run here — sibling sheets exist (AUDIT 1 PASS with the 1994 re-base; boundary re-check confirmed as condition A8) | boundary strings, endpoint dates, post-stage tagging at the 9 named figures | 0 new (1 carried: stale `→ U.41` pointers, F-5) | logged, not corrected | a reader following the channel-efficacy pointer lands on the Associates conflict |
| 2 Sources | not run here — sibling sheet exists | independence/corroboration discipline at 6 named sites; single-source disclosure at 11 load-bearing claims | **1 internal rule conflict** (A-B1: one-instrument rule vs "two separately-accessioned filings … genuinely corroborated"); 24 `Corroboration: 2` records, several citing a single accession | reported; downgrades proposed, not applied | cross-company comparison could double-count copies of one filing |
| 3 Numbers | not run here — sibling sheets exist | the 9 endpoint figures' bases; `8,000,140` null; `±$1,000`/`±$5` bands; d24 band usage | 0 | none needed | — |
| **4 Hindsight (CONFIRMATION)** | **FAIL** — condition 1 (causal claims) **not met at 5 sites, all in `stage_1.md`/`validation.csv`, none in `context_appendices.md`**; condition 2 (endpoint framing) **PASS**; the outcome-dependent-sentence condition **holds 7/7 with 0 relapses**, and the record-selection null **PASSES** as present, concrete and non-hedging | step 1: 100 causal-construction hit lines plus the exclusivity sweep, adjudicated one by one across both files + the 4 registers; the 7 named outcome-dependent sites re-found; step 2: 9 post-boundary figures traced to every site in both files incl. row titles; step 3: knowability triple + §L grading chain (8 sites) + §N per-cell; step 4: a 20-term trait/inevitability list, re-run this pass and zero-hit in dataset voice; step 5: §M (914 w / 11 entries) and §O (709 w / 6 + note) decoration test; additions: record-selection null tested for concreteness and non-hedging; 1994 re-base re-confirmed at 8 sites | **5** (F-1 High; F-2, F-3 Medium; F-4, F-5 Low) | 5 replacement wordings specified; 3 debts opened RD-040…RD-042; **nothing repaired by this auditor** | **moderate** — the surviving sites are the same proposition the appendices now grade UNKNOWN; one is inside the file's own KNOWABLE ruling |
| **5 Adversarial (VERDICT ON THE FINISHED TEXT)** | **PASS WITH 2 LANDINGS** — the reconstruction survives the ending-independence, founder-state, filing-over-read, decoration and anti-hagiography attacks; **2 attacks land**: the intra-family corroboration double-count (A-B1) and the unadjudicated directory/credibility efficacy question that no canonical `U` block carries (A-B2, with A-B4 on the straddling capital). Neither is fatal to a conclusion; both are fatal to a `COMPLETE` sign-off while open | 30 narrative elements re-behaved against the finished text; 11 single-source claims; 4 filing-over-read probes; 6 §M + 7 §O entries; the boundary attacked from two directions; the 2000 test applied to §A, §D.2, §L, §M, §R read standalone | 2 landed, 2 partly landed, 6 failed (all adjudicated in §12) | decisions recorded per AUDIT 5 step 4: re-tag/append-a-`U`-slot/hold-as-UNKNOWN; **no claim restored, no confidence raised** | low for the narrative; **high for the register**, which is where the two landings sit |

**Headline, and the two parts do not blend.** The appendix repair held: every one of the eight
`context_appendices.md` codas now carries mechanism–alternative–confidence or an honest
`mechanism UNKNOWN`, the §G exclusivity counterfactual that the recheck caught as N-02 is gone (ll. 501–508),
and §E's credibility sentence — the one that failed the recheck — is now the strongest downgrade in the volume
(ll. 352–366: "**Whether credibility borrowed from press substituted for the trust devices above is not
established for Stage 1**", with `RETROSPECTIVE SOURCE`, mechanism "none evidenced", and "**UNKNOWN** that it is
true of 1995 demand"). What did **not** hold is the discipline that repair was supposed to express: *a claim is
repaired everywhere it is made.* The proposition the appendix abandoned is still asserted, in `stage_1.md`, at
§D.1's learning cell and at §H's KNOWABLE list, and in `validation.csv` row 9 — three sites the previous two
swepts named and handed over, and none of which has moved. AUDIT 4's condition 1 therefore still fails, on a
narrower and now precisely-located set. AUDIT 5, run against the finished text, does not break the
reconstruction's argument; it breaks two register conventions the argument depends on.

---

# PART 1 — AUDIT 4 CONFIRMATION (the two conditions that failed)

## 1. Condition 1 — causal claims: mechanism + alternative + confidence, or `mechanism UNKNOWN` — **FAIL**

### 1.1 The sites this brief named

| Named test | Site now | Verdict | Basis |
|---|---|---|---|
| §H directory-placement wording (C-01 / CA-1 / OD-1) | `stage_1.md` ll. 462–476 | **HOLDS as to placement.** KNOWABLE carries only "that discovery in 1995 ran through editorial directories rather than paid media", with three period facts and a named mechanism; the causal half sits in NOT KNOWABLE with three alternatives and the split confidence "High that the channels existed and were claimed, **UNKNOWN (effect of each)** — … matching §D.1, not a demonstrated driver". §D.1 l. 274 and §R l. 1075 were not pulled up to meet it. **But the same list fails one item earlier — F-1.** | ll. 274, 344, 462–476, 619–620, 668, 1075 |
| §D.1 / §D.2 handling of the company's own 50-states/45-countries report (C-02 / C-04) | `stage_1.md` l. 282; ll. 287–291 | ** laundering closed, one residue (F-2).** §D.1 opens "**The company reported**", substitutes the audited $198,000 / $511,000 ≈ 38.7%, and ends "the geographic spread itself is unverified (§L; → U.1)"; §D.2's topic sentence carries "with the company itself reporting … (§L: 'High as claim; **Low as fact**')". §L's chain is consistent across §A l. 147, §D.1 l. 279, §D.2 l. 289, §F.2 l. 373, §L l. 619, §P50 l. 841, §R l. 1065, §U.1 — **zero untagged sites of the geography itself**. The untagged residue is the *channel* clause in the same cell (F-2). | as cited |
| §K personal-guarantee inference (C-08 / C-09 / RD-030) | `stage_1.md` l. 327 (§E.2), ll. 650–654 (§M.5), l. 590 (§K.5), ll. 1781–1800 (§U.24) | **HOLDS, all four.** "the rails are evidenced only **as opened on his signature**; whether a company-only account was available or sought is **UNKNOWN** … Confidence: High that a guarantee was used, **UNKNOWN** that one was required"; §M.5 adds the routine-practice alternative; §U.24 adjudicates the barred counter-claim as UNKNOWN ("the filing evidences that a guarantee was **used**, never that a company-only account was **sought and refused**"). §A l. 126 keeps the observational form ("existed on his personal guarantee, not the company's standing"), which is not a counterfactual. | as cited; RD-030 still OPEN |
| Appendix §E payments coda (N-03) | `context_appendices.md` ll. 371–387 | **HOLDS.** Labels present: mechanism ("the standards bodies' own expectation of a fix at end-1996 … nothing in this section names a mechanism by which the launch design converted that fact into orders"), alternative ("ordinary small-merchant practice rather than trust engineering"), confidence (High no standard in force; Medium design responded; **UNKNOWN that any of it moved demand**). | ll. 371–387 |
| Appendix §F (RD-034 coverage) | `context_appendices.md` ll. 446–461 | **HOLDS, and honestly.** "**Mechanism:** mechanism UNKNOWN, deliberately — none is named and none is owed, because this coda asserts no consequence; it records measurement nulls …". Naming one here would have manufactured it; the alternative (hostnames/counts describe machines and definitions, not audiences) and confidence are present. | ll. 446–461 |
| Appendix §G line ~501 (N-02) | `context_appendices.md` ll. 492–508 | **HOLDS.** "…and by what the exhibit set actually contains"; "**Whether anything else was open … is UNKNOWN in both directions**"; "**Mechanism:** mechanism UNKNOWN — … the exhibit index evidences what was used, never what was available"; SBDC/angel alternative; "High that these are the mechanisms on file, **UNKNOWN** that they were the only ones". The sibling the sweep found (ll. 492–496, "did not yet exist in this form") is also gone, replaced by an unmapped-landscape null. | ll. 492–508 |
| §H "borrowed credibility" family (C-07 / N-01) | appendix ll. 352–366, 558–569; `stage_1.md` l. 378, l. 669 | **HOLDS at all four sites, and the family is now uniformly down-tagged.** §E and §H both print "Whether borrowed credibility moved demand is UNKNOWN inside Stage 1"; §F.2 l. 378 keeps its Medium cap with "claimed 1995-10-04; no independent dated listing survives" and reports the 1997 quotation rather than asserting it; §M.9 l. 669 keeps the Washington Post mechanism as "rejected, documented null". Grep of the family (`credibility`, `borrowed`, `did the work`, `precondition for card entry`) returns no surviving assertion of effect anywhere in the corpus deliverables. `_parts/s1_p2.md` l. 78 is the mirror (RD-038, low). | as cited |

### 1.2 What the construction-sweep returned (100 causal hit lines + the exclusivity sweep, every line adjudicated)

Legitimate classes, as at the recheck: quotation, negation, folklore label, open question, documented null,
method directive. Concretely: `drove` survives only at l. 240 (literal driving, RETRO, folklore-labelled),
l. 708 (an *Unknowns* cell asking "Whether incorporation drove or followed"), ll. 1317/1920/1932 (U.6 and U.31
CLAIM A / residual, one of them "none is load-bearing"); `worked because` survives once, at appendix l. 417, on
the 1996 Associates Program with the mechanism quoted from the filing and no Stage-1 proposition attached
(accepted, as the recheck accepted it); `the only …` constructions are everywhere record-scoped ("the only filed
date", "the only observed mechanism", "evidenced only as opened on his signature", "the only contemporaneous
Stage-1 discount disclosure"), which is the compliant form; `obviously` = l. 61 inside the firewall's own
prohibition list; `inevitable` = appendix l. 79 "near-inevitable", scoped to the shape of the financing and
negated at ll. 83–84. **No dataset-voice sentence survives whose force is supplied by the ending.**

**Five live failures, in the same class RD-034 exists to close:**

**F-1 · High — `stage_1.md` §H l. 463, inside the file's own KNOWABLE ruling.**
"…that no shelf held more than ~10% of the in-print universe; **that card entry frightened buyers**; 1995 postal
rates…". A psycho-economic state asserted as in-period knowledge with no mechanism, no alternative and no
confidence at the site (the block's closing Confidence line answers only the channel bullet). Its support is
(i) the company's own risk text about buyers "reluctant to enter their credit card numbers" and (ii) Dial-A-Book's
founder on **1996-09-18** about a rival [D-52]. The same volume contradicts it twice: §F.2 l. 376 grades the
identical item "**High 1996 / UNKNOWN 1995 incidence**", and appendix §B's coda l. 173 says "**Low** that
consumer distrust produced them". This is precisely the OD-1 shape — the knowability section asserting as period
knowledge what the evidence sections grade UNKNOWN — cured at one bullet and surviving at its neighbour.
Registered as RD-036 in `MASTER_RESEARCH_LOG.md` l. 499, `OPEN — next repair pass`, and not done.
**Required:** "that the filing and a 1996 competitor *described* buyers as reluctant to type a card number
(company-stated; the competitor item is 1996-09-18 and about a rival); **Low as a measured 1995 condition, and
1995 incidence is UNKNOWN** (§F.2 objections row; appendix §B coda; no 1995 refusal or chargeback rate exists,
§J.5)". Move the measured half to NOT KNOWABLE, leaving KNOWABLE only what a 1995 reader could observe.

**F-2 · Medium — `stage_1.md` §D.1 l. 282, third clause (the recheck's N-04, still standing).** "the
directory-era route **placed the store in the period's principal discovery channels**". The efficacy verdict
("worked") is correctly gone and the quad is present, but the *existence* half states the company's own
1995-10-04 listing claim as learned fact, untagged, two clauses after the same cell was repaired to say "The
company reported" — the laundering C-02 was written to close, inside the same cell. §H l. 470 and §F.2 l. 378
both grade that listing "claimed / no independent dated listing survives".
**Required:** "…is **claimed, by the company's own 1995-10-04 release,** to have placed the store in the
period's principal discovery channels — no independent dated listing survives (§F.2, capped Medium on that
ground; RD-029) — and that it converted there is not knowable inside the boundary".

**F-3 · Medium — `validation.csv` row 9 (`1995-10-04 · Netscape/Yahoo placement`), `what_it_demonstrated`:**
"That a two-person firm **could earn editorial distribution** inside its first quarter of trading". The row's own
did-NOT cell and confidence ("UNKNOWN effect") disarm it, and `channels.csv` carries the same item as
self-report-only, so the register now reads two ways about one claim. "earn" adds a merit-and-effect reading
that no source carries. Registered as RD-037 (log), OPEN.
**Required cell:** "That the company *claimed* editorial placement within its first quarter of trading; no
independent dated listing survives; effect UNKNOWN (S1701, self-report)".

**F-4 · Low — `stage_1.md` §O.7 ll. 770–775 (N-05, still standing).** "The Stage-1 differentiator **the evidence
supports** is aggregation and discoverability — **directory placement**, licensed catalogue data, e-mail
notification, **tiered discounting** — not chronology." An unmeasured channel inside a phrase that says the
evidence supports it, in the section a reader quotes; and "tiered discounting" reads forward toward the
March-1997 "Amazon.com 500" that U.18 bars. **Required:** name the evidenced items (a licensed catalogue
searchable over ~400,000 sourceable titles against a superstore's ~130,000; a published telephone number; the
advertised 10–40% band), and add "directory placement is listed among the channels the store used, not among the
effects it can claim (effect of each UNKNOWN)".

**F-5 · Low — traceability defect on the same null (N-06, still standing).** `stage_1.md` ll. **274, 469, 1075**
each route the channel-efficacy question to "**→ U.41**", but canonical U.41 (l. 2086) is "The Associates
Program: 1996 technology mislabelled as Stage-1". Grep of the 42 canonical blocks confirms **no U block carries
the directory-placement or credibility efficacy conflict at all**. The pointer therefore lands a reader on a
closed question and implies the open one was adjudicated. Fix by **appending** a slot (U.43) or by re-pointing to
RD-029/RD-040 at the claim site; **do not renumber** — the file's own convention (`U_CONCORDANCE.md`, and
l. 2112 "this is the precedent that licenses the same treatment in U.1–U.41") makes the spine load-bearing.

**Condition 1 = FAIL** — 5 sites, 0 of them in `context_appendices.md`, 4 of them previously named by the audit
they failed and left undone by the pass that inherited them.

## 2. Condition 2 — endpoint framing: the 1996-97 figures as consequences only — **PASS**

All nine figures named in this brief, traced to **every** occurrence in both files, and separately tested
against the second half of the condition (none framed as the point of Stage 1).

| Figure | Sites (both files) | Status |
|---|---|---|
| FY1996 net sales $15.7M / 15,746 | firewall l. 66; §P59 in the explicit "context only, NOT Stage-1 metrics" block (l. 854 header, l. 859 row); U.19's version-safety list l. 1690 | fenced |
| 151 / 158 / 256 employees | l. 66; §P61 ("post-boundary; **none enters a Stage-1 cell**"); §R Employees l. 1062; U.17 ll. 1619–1647 ("151, 158 and 256 are all post-boundary … may appear only in the consequence column"); appendix l. 595 (inside the 1995-12-31 row, as the *explanation of why* 11 is filed there) | fenced; exemplary |
| ~180,000 accounts | l. 67; §L l. 623 under a `*POST-STAGE-1*` heading; §P60; §R Customers l. 1065 ("≈180,000 is a 1996-12-31 figure, post-boundary"); `validation.csv` row kept out of the Stage-1 snapshot by the `stage2-consequence` field | fenced |
| >40% repeat | l. 67; §L l. 623; §F.2 l. 379 "All post-boundary"; §M.8 ll. 663–665; U.12 l. 1513; appendix l. 650 "must not be back-projected" | fenced |
| Ingram 59% | l. 67; §A l. 131; §B.2 l. 204; §G.1 l. 392; §G.4 l. 426; §M.7 l. 662; §R l. 1067; P55; U.40; appendix ll. 274, 299, 610 — **every one** carrying "1996 basis / 1995 share UNKNOWN" | fenced |
| Series A $8,000,014 | firewall l. 68; §K(j) ll. 608–610 "**1996, post-boundary**, and appear here only to warn against collapsing them"; P62; appendix l. 81 ("June 1996, outside Stage 1, and so forms no part of any Stage-1 capital figure"); appendix l. 598 row headed "First institutional preferred — post-boundary, **not** Stage-1 capital" | fenced; **C-17 holds** (`8,000,140` = 0 hits) |
| March-1997 discounting | §E.3 ll. 346–348; U.18 ll. 1652–1670 ("may not be back-projected"); §I l. 507 (B&N/AOL as "a firewall against retro-fitting a moat"); appendix ll. 271, 300, 612, 651 — l. 300 uses it *anti*-rhetorically to bar discounting from the Stage-1 verdict | fenced |
| $1,007,000 program incl. its 1996 leg | firewall l. 68; §B.2 l. 203 ("so **most of it is post-boundary**"); §K l. 555 + reconciliation l. 556; §K.4 l. 580; P51/P70; §P.2 d22/d25 (candidate ≈$921,000 "RECORDED AND **NOT ADOPTED**", three reasons); §R Capital l. 1072; §S l. 1099; U.8; appendix preamble ll. 67–76 ("counted separately … so most of that program is post-boundary"); appendix l. 596 row "Capital raised **inside** Stage 1" + l. 597 separate row "straddles the boundary — **not Stage-1 capital**; in-window amount UNKNOWN" | fenced at the **row title**, which is the site AUDIT 4 called most-copied |
| 2.5M titles / 40% art captions | §E.1 l. 315 "All are **1997 marketing numbers** and may not be back-projected"; §E.3 l. 340; §M.3 ll. 641–643; P57/P58; U.3; appendix l. 611 | fenced |

No sentence in either file frames a 1995 decision as wise because of what a 1996 number did; the pressure runs
the other way (§N's pricing row answers its own 1995 decision with marketing > gross profit and a rival undercut
the typical discount; §L's 1996 row is headed `*POST-STAGE-1*` before it is headed "Signal"). **Condition 2 =
PASS.** Two notes carried, not counted as failures: (a) appendix §F l. 417's "worked because" is 1996-dated,
mechanism-quoted and unattached to Stage 1 — accepted, but it is the nearest surviving approach to the barred
construction and the next auditor will look at it; (b) appendix §A l. 93–94 says the plan assumed "a consumer
rush into a channel **a quarter of households could reach**" — 24.1% is *PC ownership*, and §H l. 446 / §B
ll. 114–120 are explicit that 1995 household *access* is not comparably reportable; the proxy label is missing at
that one site. Wording, not evidence.

## 3. Condition 3 (regression) — the seven outcome-dependent sentences, and the record-selection null

**Regression check: 7 / 7 still hold; 0 relapses; 0 cosmetic.** OD-1 → §H ll. 462–476 ("drove discovery" =
0 hits); OD-2 → l. 282 "The company reported"; OD-3 → l. 282 ("worked" = 0 dataset-voice hits); OD-4 →
ll. 287–291; OD-5 → §N l. 709 "*Expected result* = **None evidenced** — no 1994 source states an expected result
for the rename (→ U.4)"; OD-6 → l. 711 "An order system live **before a first sale was possible** … asserted
without any priority claim (→ U.11)"; OD-7 → appendix ll. 558–569. §A read standalone still cannot make a reader
expect success (ll. 106–171), and the null now sits *above* "Failure remained entirely plausible." rather than
displacing it.

**Record-selection null: PASS — present, concrete, not a hedge.** §A ll. 137–150 enumerates the four §2 losses
each tied to a live site in this volume — §N deliberations (no founder-state document, COR-06/N-1), the rejected
options that never surface (~20-category screen at §C.2 rung 3), the unprinted failures (§M.9, §M.10), and the
absent independent count behind each self-report ("the ~2,200 visits, the 50-states/45-countries reach and every
repeat share originate with the seller"), closing on "this file's density of evidence is itself an outcome of
survival, **not a measure of the period**". §S l. 1090 is the first data row, four-column, importance **High**,
confidence "High (that the selection operates); **UNKNOWN** (what the lost record would have shown)". It is not
portable to another company's file unaltered, which is the test for a null rather than a hedge. Propagated
beyond the two required sites: §M note ll. 683–688, §O warning ll. 721–725, `adversarial_review.md` §5 hazard
(i). **Register-side caveats, reported not repaired:** `data_gaps.csv` has **no** survivorship row and no
RD-035/RD-036 rows (`grep -c "RD-03" data_gaps.csv` = 0), and `MASTER_RESEARCH_LOG.md` ll. 498–501 **re-uses**
ids RD-035/036/037 for three different items than the recheck opened under those ids (the recheck's RD-035 is the
1995 credibility-conversion chase, **High**, and RD-036 the institutional-mechanisms chase) — the second
collision in this register, and it leaves a High-importance retrieval debt with no clean id and no
machine-readable row, which method §13 treats as an open research-debt violation.

## 4. PART 1 verdict

| AUDIT 4 pass condition | Result |
|---|---|
| Zero outcome-dependent sentences surviving | **PASS** (7/7 hold; the fresh sweep adds none) |
| Every causal claim with mechanism + alternative + confidence, or `mechanism UNKNOWN` | **FAIL — 5 sites** (F-1 §H l. 463, with a direct contradiction of §F.2 l. 376; F-2 §D.1 l. 282; F-3 `validation.csv` r9; F-4 §O.7; F-5 the three stale `→ U.41` pointers and the absent U slot) |
| Endpoint framing: 1996-97 figures as consequences only, none as the point of Stage 1 | **PASS** — all nine figures fenced at every site in both files, including the row titles |
| Knowability split; record-selection null; negative-signal sections substantive; survivorship language | **PASS** (conditions 3–6 and 7 of AUDIT 4 unchanged from the recheck, re-confirmed at the sites above) |

**AUDIT 4 (confirmation): FAIL, on one condition.** The appendix is clean; the residue is in the stage file and
the validation register, and it is the identical proposition the appendix has already abandoned.

---

# PART 2 — AUDIT 5: ADVERSARIAL VERDICT ON THE FINISHED RECONSTRUCTION

Brief followed: try to prove the dominant narrative wrong, citing only evidence; do not invent objections; do not
sneer at actors who lacked the ending. The 30 graded elements of `adversarial_review.md` were re-tested
behaviourally against the delivered text.

## 5. Does any conclusion still depend on knowing Amazon succeeded?

Only at the five sites catalogued as F-1…F-5, and none of them is a *conclusion* of the volume: they are
untagged residue inside sections whose own tables grade the same item UNKNOWN. The load-bearing conclusions are
outcome-free and checkable: §A (a firm with 5.5–6.0 months of trading, $(304,000) on $511,000, no profitable
order size, card rails on a personal signature, failure plausible); §D.2 ("**It did not show a business.**");
§M.2 (the $(0.19) derivation); §I ("Amazon was **not** the first online bookseller"); §K/§P (the round is a
filed program that mostly post-dates the boundary, in-window amount UNKNOWN). Two sentences that would otherwise
be the risk — §O.7's "differentiator the evidence supports" and §H's "card entry frightened buyers" — are
residuals of wording, not premises for anything downstream: no §R cell, §P row or CSV metric is built on either.
**Verdict: no surviving conclusion depends on the ending.** The stronger honest statement is that the
*selection* does — which the file now says itself at §A l. 149–150 and §S l. 1090 instead of concealing.

## 6. Which load-bearing claims rest on a single source, and does the text say so?

| Load-bearing claim | Sole source | Does the text say so? |
|---|---|---|
| >1M titles; 10–40% band; 50 states/45+ countries; Netscape/Yahoo listings; phone number; Eyes & Editors; the Bezos quotation; "first four weeks" | press release dated **1995-10-04**, one document | **Yes, in three registers.** §T l. 1130 ("Ancestor of … — one self-reported source"); `validation.csv` r3 note ("Nine claims in one document are ONE source"); §L l. 619, §P46/P47/P50, U.1, U.16. **Plus the sharper caveat: §T marks the release `restoration pending` — "only a summarised extract was captured; HTML never saved."** The volume's most load-bearing in-window document is not on disk (RD-027, OPEN) |
| Six-week beta, ~300 invited testers, ten-book minimum, "a book a day", forgone bonus, garage-with-four, 15-July e-mail, "50 phone books", "illegal to do commerce in spring 1994" | Sheff — **interviewed 1999, published 2000** | **Yes.** §T l. 1143 lists the lineage and fixes the tier ("**T4 as evidence for 1994**"); §N ll. 694–701; U.14 (which also records that the "1994" label was the orchestrator's own cache error, caught by the agent reading the file) |
| Soft-launch ~May 1995; Bellevue→SODO move; Relentless/Cadabra naming sequence; the C/NCSA/Oracle stack; "a lot of non-authoritative sources" | Kaphan, GeekWire **2011** | **Yes — explicitly.** §T l. 1147: "**single source** for soft-launch timing, the Bellevue→SODO move and the Relentless/Cadabra naming sequence (Stone corroborates only 'Cadabra')"; §J l. 530 caps the stack at Medium and keeps "Whether Bezos wrote any of the site software" UNKNOWN |
| The **only** dated outside 1995 evidence of the live store (search returned "within seconds"; ordering by web/toll-free/fax; $3.00 + $0.95) | Tallahassee Democrat 1995-10-22 and Knight Ridder Nov 1995, **both via a 2019 aggregator**, print originals not held | **Yes.** §A l. 152–154 "both aggregator-sourced, so the chain is incomplete"; §D.1 l. 280; §E.2 l. 331; §T l. 1155; RD-011 OPEN; and §D.2 l. 295 draws the *weak* conclusion the chain supports ("the only independent 1995 evidence shows a journalist testing a search, **not** a delivered order") |
| The curated Web at launch = 3,084 entries; the payments-vendor bounding null; "the only Amazon in it is the river" | **one** August-1995 NCSA Mosaic "What's New" mirror, retrieved 2026 from a third-party site | **Partly.** §T l. 1160 names it a mirror and the tier ruling is honest (COR-07, one of the few genuinely in-window artifacts); `claim_records` F-71 is `Corroboration: 1`; F-74's null is classed INFERENCE/Medium with "Absence in one curated directory is not absence in the market". **But** the mirror's own completeness is never tested, and §H's KNOWABLE channel bullet leans on its count. See A-B3 |
| 11 employees at 1995-12-31; $511,000; the guarantees; Ingram 59%; the §4(2) program | the 1997 filing family — **one instrument** | **Yes at the top** (ll. 30–31: "All SEC passages derive from that one filing family and count as **one** instrument for independence purposes") — **and no further down: see A-B1** |
| Rename date Cadabra→Amazon.com; catalog licensor; 1995 distributor share; 1995 order counts/AOV; guarantee amounts; the ~$976,000 identities; any 1995 valuation | none | **Yes** — printed as UNKNOWN in §B.2, §S, §J, §K and `data_gaps.csv`, with follow-ups |

**A-B1 (LANDS) — the one-instrument rule is contradicted inside the volume, in the direction of inflated
corroboration.** Four sites count copies of the same registration statement as independent evidence: §G.3 l. 417
("in **two** separately-accessioned filings, so genuinely corroborated"); §J l. 532 and appendix §F ll. 406–407
(restated in a second accession — "corroboration 2"); §U l. 1202 ("appears in two separately-accessioned filings,
and controls"); and §T l. 1126, which states the rule as doctrine ("disclosures repeated in both gain
independence"). The claim-record appendix carries **24** records with `Corroboration: 2` on S-1 + S-1/A pairs, and
at least one (K02) names a single accession in its Source cell while asserting two corroborations. That is the
false-corroboration pattern AUDIT 2 step 3 exists to collapse and method §3 forbids. The volume demonstrably
knows the correct rule — §K l. 555 refuses independence for the No. 5-only decomposition ("an amendment-stage
addition absent from the original, so it **is not** corroboration"). **Materiality:** low for the verdicts,
because §3 gives High on a primary document alone, so no confidence level actually moves. **Damage:** real and
cross-company — the `independence_note` column and any future count of "sources per claim" inherit the double
count. **Decision: re-search not required; a ruling is.** Either the header governs (then drop the four phrases
and set those records to `Corroboration: 1, same-instrument duplicate`), or the accession rule governs (then
amend the header and say what independence an amendment can add — counsel and auditor are the same, the issuer is
the same, and the amendment is a later draft of one document). Recommended: header governs; amendments count as
version evidence, which is already how COR-02 uses them.

**A-B2 (LANDS) — the question the whole stage turns on is not adjudicated anywhere in §U.** Directory and press
efficacy in 1995 is the single most-cited mechanism in the field, it is graded UNKNOWN at §D.1/§F.2/§H/§R, and
three routing pointers send the reader to U.41 — which is about the Associates Program. Of 42 canonical blocks,
none carries it. AUDIT 5's own logic (F-5 above; RD-040 below) is that an unresolved conflict is a finding and
must have a slot, not a dangling pointer.

## 7. Does it survive the absence of a contemporaneous founder-state interview?

**Yes — and this is the strongest part of the file.** The absence is treated as a property of the record, not a
licence to infer: §N opens with the ceiling before its first row (ll. 694–701: Sheff "Tier 1 as an artifact of
1999/2000, **Tier 4 as evidence for 1994**"; the 1995-10-04 quotation is "company-issued publicity about the
firm's own performance, not independent reporting of his reasoning"; "That is a data gap about **the record**,
not a gap in the history → U.14"); U.14 adjudicates it; `data_gaps.csv` carries it with a follow-up (RD-013).
The decision rows obey it: motives are tagged `RETROSPECTIVE (RETRO)` in the *Actual result* column (ll. 705,
706, 710), the rename row answers with "**Motive UNKNOWN in-window**", the *Expected result* cells for the rename
read "**None evidenced**", the location row concedes that Tier 1 corroborates only the *condition* (no sales tax
collected outside Washington) and not the motive, the year-end row prints "none stated", and l. 707 refuses to
count three tellings as three sources. §C.2 puts the planning document at **rung 3** with rungs 1 and 2 empty and
closes "that silence is the strongest evidence of its historical weight". Where an inference is drawn, it is
labelled one and held narrow (ll. 255–256 "**INFERENCE, narrowly held**"; l. 590 "only observed mechanism";
l. 1548 "multi-causal and unproven in its weighting"). Two cells still read as motive-supply rather than
motive-record: §N l. 712's *Rationale* "Get the payment channel at personal cost" (an inference from the act, not
a stated rationale — the row is otherwise clean) and §O.1's *Considered* resting on the twenty-category list
whose own §N row says no 1994 document survives. Both are tag-the-gap items, not conclusions.

## 8. Does it over-read the audited filings as contemporaneous 1995 observation? Is October 1995 separated from verification?

**Mostly no, and the separation of the release is exemplary.** The filings are handled as what they are: §Q
l. 1048 tags the endpoint row "FACT (audited, filed 1997 — a retrospective filing describing an in-window
state)"; U.19 keeps the method caution that the S-1 "was filed two years after Stage 1 and after a successful
IPO, so even it is a **post-outcome document**"; §C.2 l. 253 calls it "written under securities-law liability by
an issuer describing its own origins"; the IDC and Euromonitor figures are quoted-but-not-adopted with RETRO
tags; the 1997 B&N 10-K is barred from the 1995 shelf benchmark (l. 393); the art-plan captions are 1997 numbers
(l. 315).

**A-B4 (partly lands) — one systematic exception.** The section whose whole job is the founders' starting
proposition, §C.1 l. 223 "**Problem and mechanism**", is populated from the 1997 filing's teleology — "'founded
to capitalize on the opportunity for online book retailing'" — at `[T1 · FACT]` / **High**, with **no RETRO tag at
the site**, and §H l. 450's market-dollar row does the same job for Euromonitor with one. The claim as written is
true (the filing says it), and the subsection is titled "as the record states it", so this is a tag the volume
already applies elsewhere and not a belief the file holds wrongly. But "founded to…" is the issuer's 1997 account
of 1994 intent, and it is the single sentence that lets a reader reconstruct a purpose from a prospectus. Fix:
append "`RETRO` for the founding motive: what the filing evidences in-period is the **condition** (a licensed
catalogue over distributor files), not the **intention**."

On the release: the separation is real and enforced at eight sites (§L l. 619 "a company self-report, not
verified demand"; §D.1 l. 279/282; §D.2 l. 289; §R l. 1065 "as claimed by the company"; §P50 "MARKETS-SERVED
COUNTS, not customers, orders or accounts"; U.1's note that the tension is "between two statements by the same
author, not between a claim and a measurement"; COR-13 barring the release from the mailboxes/toll-free/fax/e-mail
claims, applied at §F.2 l. 377, §J l. 535, §Q l. 1039). **A-B5 (fails):** the claim that the volume over-reads the
release is refuted by l. 1039's explicit "What the release does NOT say (COR-13)" block — the file is narrower
than its own best source, which is the opposite defect.

## 9. Is anything in §M / §O decorative?

**§M: no.** 11 entries, 914 words, against §A's 922. Entries 1–8 and 11 each *is* a load-bearing argument: M.2
derives $(0.19)/$1 and the ≥~79% break-even and closes "Evidenced arithmetic, not hindsight"; M.3 converts the
400,000-of-2.5M qualifier into a month-one advertised-vs-obtainable gap; M.4 sets the slogan against the
four-to-six-week and "may not be available at all" concessions; M.5 removes the guarantee counterfactual; M.7
turns the supplier into the fact that armed rivals; M.8 removes retention from Stage 1 entirely; M.11 prices the
scale (0.16% of 1995 Web purchases) with the basis warning attached. M.9/M.10 are prohibition entries — radio/TV,
gifts, print ads, search engines, the Post mechanism, the Slate test on Stephen Glass's fabrication record, the
Bulgarian order, and the file's own untraceable artifacts. Two of M.9's sub-items (gifts, radio/TV) police claims
no source **in this corpus** makes, so they are defensive rather than load-bearing — but they are cheap, and the
dataset is designed for re-use, so listing them is right. **One real gap:** the incumbent-reproduction risk —
which §H l. 478 itself lists as NOT KNOWABLE ("whether the incumbent's catalogue and database assets would simply
reproduce the offer") and §I l. 506 documents (B&N buying the largest online front door from March 1997) — never
appears as a negative signal in §M, even though the filing's own risk factors name incumbents (l. 488). §M's
survivorship note partly excuses this (a filing discloses what it must, not what it fears), and U.11 carries the
competitive facts, so it is a placement defect, not a suppression. Recommend one M entry pointing at
l. 478/l. 506.

**§O: no, with two wording inconsistencies.** 6 counterfactuals plus the boundary note, 709 words, each with
Visible / For / Against / Considered / Others, and no scores. O.2 (CD-ROM) is the anti-decorative move in its
purest form: "**Recorded as UNKNOWN, not as a rejected alternative, and must not be written as one**" — a
counterfactual kept precisely in order to refuse it. The §O preamble warning ll. 721–725 propagates hazard (i)
and bars the "options that successful companies took" reading. **But** the header defines "*Considered* = evidence
someone looked at it", and two cells mean something else: O.4's "*Considered:* yes, as the incumbent format being
displaced" is an inference from the launch language, not evidence anyone looked; O.1's rests on the
twenty-category list which §N l. 707 grades FOUNDER CLAIM/RETROSPECTIVE. Both should carry `inferred` or
`retrospective` rather than `yes`. O.7 is F-4 above.

## 10. Attack the boundary: is 1994 → 1995-12-31 defensible?

**The attack (strongest form).** The end is an accounting convention the volume itself disowns — l. 93: "Not that
1995-12-31 is an operational break: it is the audited fiscal cut" — and a boundary that is not a break cannot
close a stage. Three concrete costs follow. (1) It cuts through the financing it has to describe: the $1,007,000
program runs 1995-12-06 → 1996-05-16, the $345,525 tranche includes a 1996-05-03 issuance, and the in-window
amount is permanently UNKNOWN (d25's candidate is recorded and refused on three grounds) — so §R's Capital cell
can never be completed, and no later stage can cross-foot to it. (2) On the method's own stage semantics
(§1: origin → first experiment → **repeatable validation** → scalable formation), nothing inside 1995 is even
arguably a completed test of repeatability: the day of opening is UNKNOWN, quarterly data begin at Q1-1996,
retention has no 1995 datum at all, and the first *full* audited trading year is FY1996. Ending at 1995-12-31
ends Stage 1 on 5.5–6.0 months of a partial year. (3) The alternative end at the program's close, **1996-05-16**,
is contemporaneously marked, resolves the money, and keeps Series A (June 1996) outside.

**Adjudication: the counter-argument does not win, but it is not refuted either — it is answered by a rule the
volume states before the evidence.** The boundary is defended at l. 82 on the only basis the protocol recognises
— "drawn where an **audited number exists**, not where the story is interesting" — and AUDIT 1's pass condition
requires a month-precise, sourced boundary event with a contemporaneous warrant for "Stage N ends here". Moving
the end to 1996-05-16 or FY1996-12-31 would buy capital-comparability by importing precisely the material that
belongs to the next stage's question (first institutional money, 1996 repeat share, Ingram's 59% of a full year),
and the file's own firewall bars using 1996 to explain 1995. Ending at the launch month would be worse: no
audited period closes there. **The residual is real and the volume accepts it:** §R's Capital cell and §S print
in-window amount UNKNOWN as a finding, and d25 records the derivation so a later pass can adopt it without
re-deriving. Cost (2) is answered by §D.2 and §L, which never claim a validated business ("It did not show a
business"; "not a validated business" at l. 50): the stage ends at a *completed first commercial test*, which is
what the audited stub is — not at repeatability, which is Stage 2's claim.

**The start takes the harder hit, and it is one word deep.** "1994 **idea formation**" names the boundary after
the one event in the window that no document attests — the file proves that twice (ll. 52–58; §Q l. 1009's 1993
row at confidence UNKNOWN "for want of any source"; §C.2's rung-3 ladder). Having established that, the honest
label is the anchor it already prints: **1994-07-05 → 1995-12-31, with spring-1994 ideation carried as
retrospective pre-history inside the stage**. As written, both titles and seven §-headers carry an undocumented
event in a boundary name, which is the same error class as the barred 1993 dating that AUDIT 1 re-based — cured
in the appendices' title (C-16) but preserved in the phrase. This is a labelling concession, not an evidentiary
one, and it is the only boundary item I would actually change.

## 11. Anti-hagiography, directly: would this read as plausible if Amazon had failed in 2000?

**Yes.** The deciding sentences, quoted:

- §A l. 164: "**Failure remained entirely plausible.** The measurable audience was low thousands of visits a day
  against 24.1% of U.S. households owning a PC in 1994…" — supported by the registrant's own named barrier, a
  rival's "we haven't sold many books", Newsweek's 1995 no-trustworthy-way-to-move-money line, and the 1997
  "next light bulb or another Edsel", with the last item policed in the same breath as "a 1997 judgment on 1996,
  recorded as evidence about the climate, not about Stage 1" (ll. 170–171).
- §D.2 l. 292: "**It did not show a business.**" and l. 294–295: "The demand signals are self-measured — visits,
  countries and repeat share all originate with the seller".
- §D.2 l. 300–302: "The most consequential fact is that this experiment's best-known datum — the identity, date
  and price of the first sale — **cannot be substantiated from any document made while it was happening.**"
- §M.2 l. 638–640: "**no average order value makes a Stage-1 order profitable** (margin would have needed ≥
  ~79%) … Evidenced arithmetic, not hindsight."
- §A l. 149–150: "this file's density of evidence is itself an outcome of survival, **not a measure of the
  period**."
- §R l. 1079 caption: "Weaknesses (**evidenced, not hindsight**)"; §M l. 686: §M "must not be read backwards as
  'the survivors overcame these'".

A 2000 casualty would leave this file's arithmetic, its nulls and its three "plausible-if-dead" verdicts intact;
what would look odd in hindsight-free terms is only §H's frightened-buyers bullet and §O.7's differentiator
phrase — i.e. the same F-1/F-4 residue. **No investor-fool framing survives** (U.30 "explains a **choice**, not an
outcome … must not be recast as foresight"; U.33 "nor, conversely, to frame the investors as fools"; l. 61;
appendix §G's own bar), and no trait vocabulary: `visionary`, `prescient`, `always intended`, `doomed`, `paid
off`, `vindicated`, `set the stage`, `laid the groundwork`, `watershed`, `destined` = 0 dataset-voice hits across
both files. **AUDIT 5's anti-hagiography question: PASS.**

## 12. Attacks, adjudicated (AUDIT 5 step 4 — decisions recorded)

| # | Attack | Lands? | Decision |
|---|---|---|---|
| A-B1 | Copies of one 1997 filing family counted as independent corroboration in 4 sites + 24 register records, against the volume's own l. 30 rule and method §3 | **YES** | Ruling required, not re-research: header governs; strike the "gain independence / genuinely corroborated" phrasing, re-key those records to `Corroboration: 1 (same-instrument duplicate)`. No confidence change (§3 grants High on a primary document) |
| A-B2 | The directory/credibility efficacy question — the most-cited mechanism of the stage — has no canonical `U` block, and three pointers send it to an unrelated closed conflict | **YES** | Append U.43 (ids by appending only) carrying the conflict with both sides, weight, residual and confidence; re-point ll. 274/469/1075 there or at RD-029/RD-040 |
| A-B3 | The only in-window external census (3,084 Mosaic entries) is one 2026-retrieved third-party mirror, and its *absence* findings bound a channel claim | **Partly** | Survives on the record: `Corroboration: 1` in the register, the null already INFERENCE/Medium with "not absence in the market", and §H l. 442's "evidence about the technology, not the company". Add one clause at §T: completeness of the mirror is untested |
| A-B4 | §C.1 states the founders' problem from a 1997 prospectus's teleology at FACT/High with no RETRO at the site | **Partly** | Tag it. The condition/intention distinction is already drawn at §N l. 710 and U.19 |
| A-B5 | The 1995-10-04 release is over-credited | **NO** | Fails: the volume is *narrower* than the release — COR-13 is applied, and l. 1039 lists what the release does not say |
| A-B6 | Founder reasoning is inferred rather than declared unrecoverable | **NO** | Fails on the record (§7). Two residual cells to re-tag: §N l. 712 *Rationale*; §O.1 *Considered* |
| A-B7 | §M/§O are decorative | **NO** | Fails: word counts, the ≥79% derivation, O.2's refusal. Carried: incumbency absent from §M; two *Considered* cells off-definition |
| A-B8 | The boundary is arbitrary | **NO on the end; yes on the label** | End survives on l. 82's audited-number rule and the firewall. Re-label the start as 1994-07-05 → 1995-12-31 with ideation as retrospective pre-history, or keep the phrase and accept that a boundary is named after an undocumented event |
| A-B9 | Survivorship framing ("successful companies did X") | **NO** | 20-term trait sweep + the construction sweep; the one shared-condition claim is disarmed at §G.1/§M.7 (non-exclusive access) and hazard (i) propagates to five sites |
| A-B10 | The volume launders a barred figure | **NO** | COR-09's 14 items held at every site; `2,300`, `8,000,140`, `95.2`, `871,024`, `Cadabra/Cadamia`, "July 16", `$12,000/$14,000`, first-book variants, WPost stake, "Cadamia" — re-checked, all fenced, retracted or folklore-labelled |

---

## Claims cut or downgraded (proposed; **none applied by this auditor**)

| Ref | Site | Was | **Required** | Why | Evidence applied |
|---|---|---|---|---|---|
| F-1 | `stage_1.md` §H l. 463 | "that card entry frightened buyers" (in KNOWABLE) | "that the filing and a 1996 competitor **described** buyers as reluctant to type a card number (company-stated; the rival item is 1996-09-18); **Low** as a measured condition; 1995 incidence **UNKNOWN**" — measured half to NOT KNOWABLE | causal/state claim inside the file's own knowability ruling, contradicting l. 376 and appendix §B l. 173 | `stage_1.md` ll. 273, 376, 650–654; appendix ll. 148–153, 160–182; §J.5 |
| F-2 | `stage_1.md` §D.1 l. 282 | "the directory-era route **placed the store** in the period's principal discovery channels" | "…**is claimed, by the company's own 1995-10-04 release,** to have placed…; no independent dated listing survives (§F.2, RD-029)…" | self-report stated as learned fact in the learning row, two clauses after the same cell was repaired | ll. 274, 378, 468–476, 619 |
| F-3 | `validation.csv` r9 | "That a two-person firm **could earn** editorial distribution…" | "That the company *claimed* editorial placement…; effect UNKNOWN" | register twin of F-2; contradicts `channels.csv` rows 2–3 | S1701 self-report |
| F-4 | `stage_1.md` §O.7 ll. 770–775 | "…directory placement, … tiered discounting — not chronology" | name the evidenced items; move placement to the channel list; print the advertised 10–40% band | unmeasured channel inside "the evidence supports"; "tiered discounting" reads toward the barred March-1997 program | ll. 274, 346–348, 462–476; U.18 |
| F-5 | `stage_1.md` ll. 274, 469, 1075 | three "→ U.41" pointers | append **U.43** for channel/credibility efficacy, or re-point to RD-029/RD-040; **do not renumber** | no canonical U block adjudicates the question; the pointer implies it is closed | `U_CONCORDANCE.md`; ll. 2086–2100 |
| A-B1 | `stage_1.md` ll. 417, 532, 1126, 1202; appendix ll. 406–407; 24 claim records | "genuinely corroborated" / "corroboration 2" by separate accession | "restated across accessions of **one** filing family — one instrument; version evidence, not corroboration"; `Corroboration: 1 (same-instrument duplicate)` | contradicts l. 30–31 and method §3; the volume already applies the correct rule at l. 555 | ll. 30–31, 555, 852 (P69 "amendment-stage addition, NOT corroboration") |
| A-B4 | `stage_1.md` §C.1 l. 223 | `[T1 · FACT]` / High | add "`RETRO` for the founding motive: the filing evidences the **condition**, not the **intention**" | a 1997 teleology populating §C without the tag the rest of the volume applies | l. 253; U.19; §N ll. 694–701 |
| A8 | Titles/labels, both files | "1994 **idea formation** → 1995-12-31" | "1994-07-05 → 1995-12-31 (spring-1994 ideation carried as retrospective pre-history inside the stage)" — or keep and accept the note at §H l. 434 extended to the title | names the boundary after the one event no document attests | ll. 52–58, 88, 1009; appendix ll. 17–23 |
| minor | appendix §A l. 93 | "a channel a quarter of households could reach" | "a channel only a quarter of households even owned a PC to reach (access share for 1995 is UNKNOWN)" | PC ownership used as an access figure at one site without the proxy label | l. 446; appendix ll. 114–120 |

## Research debt opened by this pass

> **Id continuity, and a collision to fix first.** `MASTER_RESEARCH_LOG.md` l. 490 records that ids are allocated
> by **appending only**, then l. 498–501 itself re-uses RD-035/036/037 for three items other than the recheck's
> RD-035 (1995 credibility conversion, **High**), RD-036 (institutional mechanisms, Medium-High) and RD-037
> (method codas). This sheet therefore numbers from **RD-040** and re-keys nothing: the Company Lead must give the
> recheck's three debts fresh ids, because method §13 makes a High-importance gap without a clean follow-up task
> an open research-debt violation.

| RD id | Section | Debt | Assigned | Status |
|---|---|---|---|---|
| **RD-040** | §H, §D.1, §O.7; `validation.csv`; `stage_1.md` U spine | **Directory- and press-driven conversion in 1995 is unadjudicated and unrouteable.** Close F-1…F-5 in one pass (all five are the same proposition), append U.43, and re-key the three pointers. No new retrieval: every tag needed already exists in §F.2, §M.9, §H and `channels.csv` | Company Lead (edit), Hindsight Auditor (re-confirm) | **OPEN — blocks AUDIT 4 condition 1 and AUDIT 5 sign-off** |
| **RD-041** | `stage_1.md` ll. 30–31/417/532/1126/1202; appendix ll. 406–407; 24 claim records; `sources.csv` `independence_note` | **One accession family must not be double-counted as corroboration.** Decide the rule, apply it to every affected row, and re-state it in `00_METHOD_AND_STYLE.md` §3 as "a restatement of one registration statement is one source". Then re-audit the same pattern in Walmart/Apple/UnitedHealth before any cross-company mechanism count | Method owner + Evidence Registrar | **OPEN — Medium**; recurs across 49 companies |
| **RD-042** | `data_gaps.csv`; `MASTER_RESEARCH_LOG.md` §6; appendix §J | **Register mirror is not closed.** Add the survivorship/record-selection row, add rows for the credibility-conversion and institutional-mechanisms chases under de-collided ids with `follow_up_task`, and reconcile RD-027 (re-save of the 1995 releases — the volume's most load-bearing in-window document, still `restoration pending`) | Orchestrator | **OPEN — High** by method §13 |

## Sign-off

Stage status: **RECONSTRUCTION → ADVERSARIAL REVIEW → QA → COMPLETE.** Currently at **QA.**

| Gate | Result |
|---|---|
| **AUDIT 4 — hindsight (confirmation of the two failed conditions)** | **FAIL.** Condition 1 (causal claims) unmet at **5 sites** — F-1 §H l. 463 (High, and it contradicts the file's own l. 376), F-2 §D.1 l. 282, F-3 `validation.csv` r9, F-4 §O.7, F-5 the `→ U.41` pointers with no U slot. Condition 2 (endpoint framing) **PASS** on all nine figures at every site in both files. Regression: the seven outcome-dependent sentences **still hold 7/7**; the record-selection null **PASS**, concrete and not a hedge; knowability split, §M/§O, survivorship sweep and the 1994 re-base **PASS** |
| **AUDIT 5 — adversarial (verdict on the finished text)** | **PASS WITH 2 LANDINGS.** Survives: outcome-dependence of conclusions; the no-founder-state-interview test; the "not first"/priority reversal; the anti-hagiography 2000 test; the decoration test on §M and §O; the barred-figure laundering test. Lands: **A-B1** (intra-family double-counted corroboration, against the volume's own header rule and method §3) and **A-B2** (the efficacy question with no conflict block and a pointer to an unrelated one); **partly**, **A-B4** (a 1997 prospectus's teleology populating §C.1 untagged) and **A-B8** on the boundary *label* rather than the boundary |

**Recommendation: REOPEN. Stage 1 must not move `QA → COMPLETE`.** COMPLETE requires all five audit rows = PASS,
and the deciding condition is a single one: **AUDIT 4's causal-claims condition is unmet — §H's KNOWABLE list still
asserts "that card entry frightened buyers" as in-period knowledge in the same volume whose §F.2 row grades 1995
incidence UNKNOWN and whose appendix §B coda grades the causal force Low.** That is the exact defect AUDIT 4 was
confirmed to check (a knowability ruling asserting what the evidence tables refuse), and it is the third pass
running in which the borrowed-credibility/directory-efficacy proposition has been repaired at one site and left
standing at its neighbour — the discipline broken is not the wording but *a claim is repaired everywhere it is
made*, which now runs across `stage_1.md`, its `_parts/` mirror and `validation.csv` — while `channels.csv` rows
2–3 already carry the same item right, so the registers read two ways about one claim.

**What reopening costs (nothing more).** F-1…F-5 and A-B1/A-B4 are re-tagging with tags this file already
prints, one appended U.43 slot, one header ruling on accession independence, and three `data_gaps.csv` rows under
de-collided ids — no retrieval, no re-dating, so no AUDIT 1 re-run is triggered. RD-029/RD-030/RD-035/RD-041
carry the retrieval, and RD-027 (the 1995 releases' re-save) is the only item where the answer could change a
verdict. **Rounding up would buy a clean sheet on a volume that still cannot say, in one place, whether a
directory listing produced an order.** No auditor other than this one edited anything, and this one edited
nothing; no corpus file was created, moved, tidied or deleted.
