#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tools/_tmp_split_claim_records.py -- mechanical §9.3 budget split of the two Amazon
claim-record volumes that break the 60,000-word hard cap (method §9.2).

Deterministic line-slice only. No prose is regenerated, no record id is re-based, no record's text,
classification, confidence or citation is edited. The script writes nothing unless it can first
PROVE that (volume 1a with its added blocks removed) + (volume 1b with its added header removed)
reconstructs the original bytes exactly, SHA-256.

Usage:  python tools/_tmp_split_claim_records.py --stage 2 [--dry-run]
        python tools/_tmp_split_claim_records.py --stage 3 [--dry-run]
"""
import argparse
import hashlib
import io
import os
import re
import sys

BASE = os.path.join("founders_playbook", "01_companies", "company_001_amazon")
REC = re.compile(r"^((?:[A-T]\d{1,3})|(?:U\.\d{2,3}[a-z]?))\s+Claim:")
HDG = re.compile(r"^([A-U])\.\s.*CLAIM RECORDS")
WORD = re.compile(r"\S+")
CAP = 60000

JOB = {
    "2": {
        "src": "stage_2_claim_records.md",
        "new": "stage_2_claim_records_part_1b.md",
        "next": "stage_2_claim_records_part_2.md",
        "stage": "2",
        "window": "1996-01-01 \u2192 1997-05-15",
        "cut_letter": "Q",
        "head_sections": "\u00a7A\u2013\u00a7P",
        "tail_sections": "\u00a7Q\u2013\u00a7T (plus the \u00a7U carry-forward stub and volume 1's coverage note)",
        "tail_note": ("the \u00a7U carry-forward stub and the `## Coverage note (volume 1 \u2014 this file)` "
                      "block travel with the text they close"),
        "u_range": "U.44 \u2192 U.113",
        "provenance_note": ("The \u00a7U carry-forward stub and the `## Coverage note (volume 1 \u2014 this file)` "
                            "block that closed the pre-split volume travel with the text they close and are "
                            "reproduced here verbatim \u2014 their wording is the pre-split file's own, and their "
                            "self-reported counts and volume labels are superseded by this header and by the "
                            "sheet's `## Proof` (findings F-1, F-3)."),
    },
    "3": {
        "src": "stage_3_claim_records.md",
        "new": "stage_3_claim_records_part_1b.md",
        "next": "stage_3_claim_records_part_2.md",
        "stage": "3",
        "window": "1997-05-16 \u2192 **endpoint under argument**; work carried to 1999-12-31",
        "cut_letter": "M",
        "head_sections": "\u00a7A\u2013\u00a7L",
        "tail_sections": "\u00a7M\u2013\u00a7T (plus the closing `VOLUME 1 ENDS HERE` statement)",
        "tail_note": ("the closing `**VOLUME 1 ENDS HERE \u2026**` statement travels with the text it closes, "
                      "so it now reads at the foot of this volume"),
        "u_range": "U.114 \u2192 U.168",
        "provenance_note": ("The closing `**VOLUME 1 ENDS HERE \u2026**` statement that ended the pre-split "
                            "volume travels with the text it closes and is reproduced here verbatim \u2014 its "
                            "wording, its record count and its volume label are the pre-split file's own and are "
                            "superseded by this header and by the sheet's `## Proof` (findings F-1, F-2, F-3)."),
    },
}


def words(s):
    return len(WORD.findall(s))


def ids_of(text):
    return [m.group(1) for m in (REC.match(l) for l in text.split("\n")) if m]


def section_census(text):
    out, order = {}, []
    for i in ids_of(text):
        k = re.match(r"[A-T]|U\.", i).group(0)
        if k not in out:
            out[k] = [0, i, i]
            order.append(k)
        out[k][0] += 1
        out[k][2] = i
    return out, order


def build_blocks(job, head_ids, tail_ids, head_w, tail_w, n_head, n_tail):
    """The only text this pass adds. Everything else is the original bytes."""
    h_first, h_last = (head_ids[0], head_ids[-1]) if head_ids else ("\u2014", "\u2014")
    t_first, t_last = (tail_ids[0], tail_ids[-1]) if tail_ids else ("\u2014", "\u2014")
    src, new, nxt = job["src"], job["new"], job["next"]
    tail_short = job["tail_sections"].split(" (")[0]

    label_1a = ("> **VOLUME 1a OF 3** (mechanical budget split, 2026-09-26, "
                "`03_quality_control/amz_claim_record_split.md`): this file holds the front matter and "
                "%s \u2014 **%d claim records, %s \u2192 %s**, %d words, under the 60,000-word cap "
                "(method \u00a79.2). It is continued by `%s` (volume 1b, %s) and closes into "
                "`%s` (volume 2, \u00a7U %s). Record ids run continuously across the three volumes and "
                "nothing was re-based, renumbered or reused (method \u00a79.3)."
                % (job["head_sections"], n_head, h_first, h_last, head_w, new,
                   tail_short, nxt, job["u_range"]))

    cut_line = ("\n> **CUT (2026-09-26 budget split, method \u00a79.3): the records after this line were "
                "moved byte-identically into `%s`, which opens at record %s.**\n" % (new, t_first))

    footer = ("""
---

**SUPERSESSION NOTE (mechanical budget split, 2026-09-26; sheet
`03_quality_control/amz_claim_record_split.md`; agent `amz-split-oversize`).** This file is superseded as a
whole-document volume and is now **volume 1a** of the Stage-%s claim-record appendix. Its former content from
%s onward is carried **verbatim** in `%s` (volume 1b, %d records %s \u2192 %s, %d words); %s. \u00a7U (%s)
remains in `%s` (volume 2), whose own header carries one added chain line. The split was
forced by the 60,000-word hard cap in method \u00a79.2 \u2014 this file measured **%d** words before the cut \u2014
and is a file-geometry change only: **nothing was trimmed, condensed, dropped, reworded, re-classed or
re-sequenced** (\u00a79.6), **no record id was re-based or reused** (\u00a79.3), and the union of the three
volumes is byte-identical to the pre-split document except for the added volume labels, the cut
cross-reference and this note, which `tools/_tmp_split_claim_records.py` verifies by SHA-256 before writing.
Word, byte and record counts before and after are in that sheet's `## Proof` section. Self-reported counts
inside this file's front matter and coverage note predate later appends and are superseded by that proof
(findings F-1, F-2, F-3 in the sheet).
""" % (job["stage"], "\u00a7" + job["cut_letter"], new, n_tail, t_first, t_last,
       tail_w, job["tail_note"], job["u_range"], nxt, job["before_words"]))

    header_1b = ("""# AMAZON.COM, INC. \u2014 STAGE %s CLAIM-RECORDS APPENDIX, VOLUME 1b OF 3 (%s) \u2014 CONTINUOUS NUMBERING

**Dataset:** THE FOUNDER'S PLAYBOOK \u00b7 **Company:** Amazon.com, Inc. (company_001) \u00b7 **Stage:** %s
(%s) \u00b7 **Role:** volume 1b of the Stage-%s claim-record appendix, created by the mechanical \u00a79.2/\u00a79.3
budget split of 2026-09-26 (sheet `03_quality_control/amz_claim_record_split.md`), which cut the document at
the section heading \u201c%s\u201d and nowhere else.

**Records held in this volume:** %d claim records, ids **%s \u2192 %s**, sections %s, %d words on disk \u2014
under the 60,000-word cap. **This volume continues** `%s` (**volume 1a**: front matter plus %s, records %s
\u2192 %s, %d words) **and is continued by** `%s` (**volume 2**: \u00a7U conflict spine %s, plus the coverage
note that closes both volumes). Every `U.nnn` key cited in the records below resolves in volume 2; every
record id here is the id it had before the split.

**Invariants of this pass (method \u00a79.3, \u00a79.6, \u00a714 rule 4).** Numbering is continuous across the three
volumes; no id was re-based, renumbered, reused or dropped; **no record's text, classification, confidence or
citation was edited**, and no evidence was trimmed to fit the cap. The bytes below are a verbatim line-slice of
the pre-split volume 1, SHA-256-verified against it before writing. Every field convention of the front matter
\u2014 the `Passage:` taxonomy and its five markers, the filing-lineage rule, the `(PB)`/`(L)`/`(NO LOCAL COPY)`
keys, the retracted-value bar, the RD-078 citation rule and the line-keying declaration \u2014 is in force here
unchanged and is **not restated**; read it at the head of `%s`. %s

---
""" % (job["stage"], tail_short, job["stage"], job["window"], job["stage"],
       job["cut_heading_text"],
       n_tail, t_first, t_last, job["tail_sections"], tail_w, src, job["head_sections"], h_first, h_last,
       head_w, nxt, job["u_range"], src, job["provenance_note"]))

    chain_1b = ("\n> **CUT (2026-09-26 budget split, method \u00a79.3): the records below this line were moved "
                "verbatim from `%s`, whose own foot names this file.**\n" % src)
    chain_next = ("> **CHAIN NOTE (2026-09-26 budget split, method \u00a79.3; sheet "
                  "`03_quality_control/amz_claim_record_split.md`):** this volume continues "
                  "`%s` (volume 1b, %s), whose own volume 1a is `%s`; the three volumes are one document "
                  "with continuous ids, and the only change made to this file by that pass is this line.\n"
                  % (new, tail_short, src))
    return label_1a, cut_line, footer, header_1b, chain_1b, chain_next


def run(stage, dry):
    job = dict(JOB[stage])
    src_p = os.path.join(BASE, job["src"])
    new_p = os.path.join(BASE, job["new"])
    nxt_p = os.path.join(BASE, job["next"])
    if os.path.exists(new_p):
        sys.exit("REFUSE: %s already exists (a split of this volume was already done)" % new_p)

    raw = io.open(src_p, encoding="utf-8", newline="").read()
    original_sha = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    job["before_words"] = words(raw)
    lines = raw.split("\n")

    cut = [i for i, l in enumerate(lines) if HDG.match(l) and HDG.match(l).group(1) == job["cut_letter"]]
    if len(cut) != 1:
        sys.exit("REFUSE: %d heading matches for \u00a7%s, need exactly 1" % (len(cut), job["cut_letter"]))
    k = cut[0]
    job["cut_heading_text"] = re.sub(r"^\w\.\s*", "", lines[k]).replace(" \u2014 CLAIM RECORDS", "").strip()

    head_text = "\n".join(lines[:k])
    tail_text = "\n".join(lines[k:])
    head_ids, tail_ids = ids_of(head_text), ids_of(tail_text)
    head_w, tail_w = words(head_text), words(tail_text)
    assert len(head_ids) + len(tail_ids) == len(ids_of(raw)), "record census lost at the cut"
    assert head_text + "\n" + tail_text == raw, "line-slice does not reconstruct the original"

    label_1a, cut_line, footer, header_1b, chain_1b, chain_next = build_blocks(
        job, head_ids, tail_ids, head_w, tail_w, len(head_ids), len(tail_ids))

    new_1a = (lines[0] + "\n\n" + label_1a + "\n" + "\n".join(lines[1:k]) + cut_line + footer)
    new_1b = header_1b + chain_1b + "\n" + tail_text

    # --- reconstruction proof, computed BEFORE anything is written
    strip_1a = new_1a.replace("\n\n" + label_1a, "", 1)
    strip_1a = strip_1a.replace(cut_line + footer, "", 1)
    strip_1b = new_1b.replace(header_1b + chain_1b + "\n", "", 1)
    assert strip_1a == head_text and strip_1b == tail_text, "added blocks do not reverse out cleanly"
    assert strip_1a + "\n" + strip_1b == raw, "union of parts is not byte-identical to the original"
    for name, w in (("volume 1a", words(new_1a)), ("volume 1b", words(new_1b))):
        if w >= CAP:
            sys.exit("REFUSE: %s would be %d words, still at/over the cap" % (name, w))

    report(stage, job, original_sha, raw, new_1a, new_1b, head_ids, tail_ids, k, lines)
    if dry:
        print("DRY RUN \u2014 nothing written")
        return

    io.open(new_p, "w", encoding="utf-8", newline="").write(new_1b)
    io.open(src_p, "w", encoding="utf-8", newline="").write(new_1a)

    # chain line into volume 2 (one added line under its H1; content otherwise untouched)
    nxt_raw = io.open(nxt_p, encoding="utf-8", newline="").read()
    nlines = nxt_raw.split("\n")
    io.open(nxt_p, "w", encoding="utf-8", newline="").write(
        nlines[0] + "\n\n" + chain_next + "\n".join(nlines[1:]))

    # --- re-read from disk and re-prove
    a = io.open(src_p, encoding="utf-8", newline="").read()
    b = io.open(new_p, encoding="utf-8", newline="").read()
    c = io.open(nxt_p, encoding="utf-8", newline="").read()
    a_r = a.replace("\n\n" + label_1a, "", 1).replace(cut_line + footer, "", 1)
    b_r = b.replace(header_1b + chain_1b + "\n", "", 1)
    ok = hashlib.sha256((a_r + "\n" + b_r).encode("utf-8")).hexdigest() == original_sha
    print("ON-DISK RECONSTRUCTION %s  (%s + %s == original %s)"
          % ("OK" if ok else "FAILED", job["src"], job["new"], original_sha[:12]))
    if not ok:
        sys.exit("FATAL: restore needed \u2014 reconstruction check failed on disk")
    print("volume 2 chain line added: words=%d, ids=%d (record set unchanged)" % (words(c), len(ids_of(c))))


def report(stage, job, sha, raw, new_1a, new_1b, head_ids, tail_ids, k, lines):
    ids_all = ids_of(raw)
    hc, horder = section_census(new_1a)
    tc, torder = section_census(new_1b)
    print("STAGE %s  %s" % (stage, job["src"]))
    print("  original: words=%d bytes=%d ids=%d sha256=%s"
          % (words(raw), len(raw.encode("utf-8")), len(ids_all), sha[:16]))
    print("  cut: line %d (1-based %d)  \u00a7%s heading  %r" % (k, k + 1, job["cut_letter"], lines[k][:58]))
    print("  head slice words=%d ids=%d (%s \u2192 %s)   +added -> %d words" % (
        words("\n".join(lines[:k])), len(head_ids), head_ids[0], head_ids[-1], words(new_1a)))
    print("  tail slice words=%d ids=%d (%s \u2192 %s)   +header -> %d words" % (
        words("\n".join(lines[k:])), len(tail_ids), tail_ids[0], tail_ids[-1], words(new_1b)))
    print("  vol 1a sections: " + " ".join("%s=%d(%s\u2192%s)" % (l, hc[l][0], hc[l][1], hc[l][2]) for l in horder))
    print("  vol 1b sections: " + " ".join("%s=%d(%s\u2192%s)" % (l, tc[l][0], tc[l][1], tc[l][2]) for l in torder))
    print("  ids preserved: %d = %d + %d ; duplicated across parts: %d" % (
        len(ids_all), len(head_ids), len(tail_ids),
        len(set(i for i in head_ids if i in set(tail_ids)))))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True, choices=["2", "3"])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    run(a.stage, a.dry_run)
