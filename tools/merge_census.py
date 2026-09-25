#!/usr/bin/env python3
"""
merge_census.py -- count what the parts asked the merge to do, and check it happened.

Assembly agents hand register rows to the merge inside `>>> REGISTER ROWS FOR MERGE <<<`
blocks, because one path has one owner. Nothing enforced that the merge actually applied
them, and the parts' own arithmetic is self-reported. This censuses the REQUEST side by
parsing only structured content -- a fenced block whose header line matches a known register
schema -- and diffs it against the registers by key column.

Design rule taken from this project's own lesson: a block that cannot be attributed is
reported as UNATTRIBUTED, never silently counted as zero and never guessed at. An earlier
build of this tool parsed prose lines as rows and inferred the target register from any
filename mentioned in the block, and it "found" 116 missing rows that did not exist.

  python tools/merge_census.py --company-dir <dir> [--json] [--verbose]

Exit: 0 every attributed row present, 1 rows missing, 2 nothing attributable.
"""

import argparse
import csv
import glob
import io
import json
import os
import re
import sys

BLOCK_MARK = re.compile(r">>>[^<>]*MERGE[^<>]*<<<", re.I)
FENCE = re.compile(r"```([a-zA-Z]*)\n(.*?)```", re.S)
# Canonical schemas, read from Amazon (the assembled reference company) when present.
TARGETS = {
    "conflicts.csv": "conflict_id", "sources.csv": "source_id", "timeline.csv": None,
    "quantitative.csv": None, "data_gaps.csv": None, "validation.csv": None,
    "failures.csv": None, "decisions.csv": None, "channels.csv": None,
}


def headers(company_dir):
    """Column sets per register, from this company or from Amazon as the reference."""
    out = {}
    for fname in TARGETS:
        for d in (company_dir, os.path.join(company_dir, "research"),
                  "founders_playbook/01_companies/company_001_amazon"):
            p = os.path.join(d, fname)
            if os.path.exists(p):
                try:
                    first = next(csv.reader(open(p, encoding="utf-8", errors="replace",
                                                 newline="")))
                except Exception:
                    continue
                if first:
                    out[fname] = [h.strip().lower() for h in first]
                break
    return out


def match_register(hdr_cells, schemas):
    """Attribute a block to a register by column-set overlap only. Ambiguity is a finding."""
    cells = [c.strip().strip('"').lower() for c in hdr_cells]
    scored = []
    for fname, cols in schemas.items():
        if not cols:
            continue
        inter = len(set(cells) & set(cols))
        scored.append((inter / max(1, len(cols)), inter, fname))
    scored.sort(reverse=True)
    if not scored or scored[0][0] < 0.5:
        return None
    tied = [s for s in scored if s[1] == scored[0][1] and s[1] > 0]
    if len(tied) > 1:
        return "AMBIGUOUS:" + ",".join(t[2] for t in tied)
    return scored[0][2]


def existing_keys(path, col):
    if not path or not os.path.exists(path) or not col:
        return set()
    with open(path, encoding="utf-8", errors="replace", newline="") as f:
        rdr = csv.reader(f)
        try:
            hdr = [h.strip().lower() for h in next(rdr)]
        except StopIteration:
            return set()
        key = col if col in hdr else next((h for h in hdr if h.endswith("_id")), None)
        if not key:
            return set()
        i = hdr.index(key)
        return {r[i].strip() for r in rdr if len(r) > i and r[i].strip()}


def census(company_dir, schemas, verbose=False):
    parts = sorted(glob.glob(os.path.join(company_dir, "_parts", "*.md")))
    if not parts:
        return None, "no _parts/ directory -- nothing to census (UNANSWERED, not a pass)"
    requested, unattributed, keyless, bodies, outside = {}, [], [], 0, 0
    for p in parts:
        txt = open(p, encoding="utf-8", errors="replace").read()
        for m in FENCE.finditer(txt):
            lang, body = m.group(1).lower(), m.group(2)
            if not BLOCK_MARK.search(txt[max(0, m.start() - 1200):m.start()]):
                outside += 1      # fenced but not inside a merge request section
                continue
            rows = [r for r in csv.reader(io.StringIO(body)) if any(c.strip() for c in r)]
            if len(rows) < 2:
                continue
            bodies += 1
            fname = match_register(rows[0], schemas)
            if not fname:
                unattributed.append((os.path.basename(p), len(rows) - 1,
                                     "no >=50% column overlap with any register schema"))
                continue
            if str(fname).startswith("AMBIGUOUS"):
                unattributed.append((os.path.basename(p), len(rows) - 1, str(fname)))
                continue
            hdr = [c.strip().lower() for c in rows[0]]
            # Only registers with a real primary key can be censused by key. `timeline`
            # and friends use source_id for the CARRIER, not the row, and keying on it
            # invents "missing rows" out of prose cells -- so they are censused by count.
            key = TARGETS[fname]
            ki = hdr.index(key) if key and key in hdr else None
            data = rows[1:]
            if ki is None:
                keyless.append((fname, os.path.basename(p), len(data)))
                requested.setdefault(fname, []).extend(
                    (os.path.basename(p), "") for _ in data)
            else:
                requested.setdefault(fname, []).extend(
                    (os.path.basename(p), r[ki].strip()) for r in data
                    if len(r) > ki and r[ki].strip())
    if not requested:
        return None, "no attributable merge-request blocks found (UNANSWERED, not a pass)"
    report = []
    for fname, reqs in sorted(requested.items()):
        col = TARGETS[fname]
        have = set()
        for d in ("", "research"):
            have |= existing_keys(os.path.join(company_dir, d, fname), col)
        miss = [(s, k) for s, k in reqs if k and k not in have]
        blanks = [s for s, k in reqs if not k]
        report.append({"register": fname, "requested": len(reqs),
                       "present": len(reqs) - len(miss) - len(blanks), "missing": len(miss),
                       "unkeyed": len(blanks),
                       "examples": ["%s:%s" % (s, k) for s, k in miss[:10]]})
    return {"blocks": bodies, "registers": report, "unattributed": unattributed,
            "keyless": keyless, "fenced_outside_merge": outside}, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company-dir", required=True)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()
    schemas = headers(a.company_dir)
    res, note = census(a.company_dir, schemas, a.verbose)
    if note:
        print("merge_census -- %s: %s" % (os.path.basename(a.company_dir.rstrip("/\\")), note))
        return 2
    total_missing = sum(r["missing"] for r in res["registers"])
    if a.json:
        print(json.dumps({"company": os.path.basename(a.company_dir.rstrip("/\\")),
                          "blocks": res["blocks"], "missing_total": total_missing,
                          "unattributed": res["unattributed"],
                          "registers": res["registers"]}, indent=1))
    else:
        print("# Merge census -- %s\n\n%d structured block(s) parsed; "
              "%d block-group(s) could not be attributed (listed, never counted as zero)."
              % (os.path.basename(a.company_dir.rstrip("/\\")), res["blocks"],
                 len(res["unattributed"])))
        print("\n| register | requested | present | missing | unkeyed | first missing keys |")
        print("|---|---|---|---|---|---|")
        for r in res["registers"]:
            print("| %s | %d | %d | %d | %d | %s |" % (
                r["register"], r["requested"], r["present"], r["missing"], r["unkeyed"],
                ", ".join(r["examples"][:6])))
        print("\nTOTAL missing keyed rows: %d" % total_missing)
        for src, n, why in res["unattributed"]:
            print("  UNATTRIBUTED %s (%d rows): %s" % (src, n, why))
    return 0 if total_missing == 0 else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
