#!/usr/bin/env python3
"""
id_mint.py -- hand out global `S####` source ids so two merges cannot mint the same one.

The problem is real and current. RD-123 was an id collision: Walmart's merge re-used ids a dossier had
proposed for different documents, so one citation resolved to two files. RD-131 nearly repeated it by
convention instead of carelessness -- Target's merge minted `S4201-S4221`, and Microsoft's merge,
having checked the corpus for free numbers at its own start, continued at `S4222-S4243` immediately
above it. Both checked. Neither held a lock. Two merges running the same evening -- as they are now --
can land on the same free range, and `gates.py` cannot see a collision it was never told about.

What this tool does NOT do is invent a scheme. An audit of the corpus (see --audit) shows the existing
convention is a **single ascending space** -- `S0001` (Amazon) through `S4331` (UnitedHealth), with
316 of 337 issued ids outside any per-rank block. Per-rank blocks would be tidier and would require
re-keying 337 ids plus every citation that points at them (RD-122's 138-site lesson), so they are not
proposed here. The gap is not the layout; it is that allocation is uncoordinated.

So: `--count N` returns the N lowest numbers that are neither present in any `sources.csv` nor already
claimed in `00_universe/_ID_BLOCKS.tsv`, and `--claim` records them against the asking company and
agent. A merge that allocates through this file cannot collide with a merge that did too, and the
registry says who holds what even after the ids leave a company's own files.

  python tools/id_mint.py --audit
  python tools/id_mint.py --count 5 --company company_011_microsoft --claim --agent msft-s1-merge
"""

import argparse
import csv
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(REPO, "founders_playbook", "01_companies")
REGISTRY = os.path.join(REPO, "founders_playbook", "00_universe", "_ID_BLOCKS.tsv")
ID_RE = re.compile(r"\bS(\d{4})\b")
FLOOR = 1
CEIL = 99999
# Why exactly four digits, and why allocation starts above the highest id rather than in the holes:
# the first version of this file used `\bS(\d{3,5})\b` and a lowest-free policy. On the live corpus
# that read the OCR'd BYTE price `S435` as an issued id, and then offered `S0013`-`S0018` as free --
# numbers Amazon holds. A tool that mints collisions is worse than no tool, so: the space is
# four-digit ids only, and the allocator never re-enters a gap.


def scan_issued():
    """id -> set(company dirs) for every S#### cited in any sources.csv."""
    issued = {}
    for d in sorted(os.listdir(BASE)) if os.path.isdir(BASE) else []:
        p = os.path.join(BASE, d, "sources.csv")
        if not os.path.exists(p):
            continue
        for i in {int(x) for x in ID_RE.findall(io.open(p, encoding="utf-8",
                       errors="replace").read())}:
            issued.setdefault(i, set()).add(d)
    return issued


def load_registry():
    out = {}
    if not os.path.exists(REGISTRY):
        return out
    for r in csv.DictReader(io.open(REGISTRY, encoding="utf-8"), delimiter="\t"):
        try:
            out[int(re.sub(r"\D", "", r["id"]))] = (r["company"], r.get("agent") or "")
        except (KeyError, ValueError):
            continue
    return out


def width(i):
    """Print an id the way the corpus prints ids in that range: S0001-style up to 9999."""
    return "S%04d" % i


def audit(issued, reg):
    per = {}
    for i, dirs in issued.items():
        for d in dirs:
            per.setdefault(d, []).append(i)
    print("issued ids: %d distinct, range %s-%s | registry claims: %d"
          % (len(issued), width(min(issued)) if issued else "-",
             width(max(issued)) if issued else "-", len(reg)))
    for d in sorted(per):
        ids = sorted(per[d])
        print("   %-34s n=%-4d %s..%s" % (d, len(ids), width(ids[0]), width(ids[-1])))
    dupes = {i: sorted(v) for i, v in issued.items() if len(v) > 1}
    print("COLLISIONS (one id cited by more than one company): %d" % len(dupes))
    for i, ds in sorted(dupes.items())[:10]:
        print("   %s -> %s" % (width(i), ", ".join(ds)))
    stale = [i for i in reg if i not in issued]
    print("registry ids not present in any sources.csv: %d%s"
          % (len(stale), " (%s)" % ", ".join(width(i) for i in sorted(stale)[:8]) if stale else ""))
    return len(dupes)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true")
    ap.add_argument("--count", type=int, default=0)
    ap.add_argument("--company", default="", help="company dir the ids are for, e.g. company_011_microsoft")
    ap.add_argument("--claim", action="store_true", help="write the allocation into the registry")
    ap.add_argument("--agent", default="")
    ap.add_argument("--above", type=int, default=FLOOR,
                    help="allocate only at or above this number (a merge continuing its own range)")
    a = ap.parse_args()
    issued, reg = scan_issued(), load_registry()

    if a.audit or a.count <= 0:
        n = audit(issued, reg)
        nxt = (max(list(issued) + list(reg)) if (issued or reg) else 0) + 1
        print("\nnext assignable: %s (allocation never re-enters a gap -- see the header note)"
              % width(nxt))
        return 1 if n else 0

    taken = set(issued) | set(reg)
    start = max([a.above] + [max(issued) if issued else 0] + [max(reg) if reg else 0]) + 1
    got = [i for i in range(start, CEIL + 1) if i not in taken][:a.count]
    if len(got) < a.count:
        print("REFUSED: only %d assignable ids above %d; not re-entering a gap to make the number up"
              % (len(got), start - 1))
        return 2
    print("%d id(s): %s" % (len(got), ", ".join(width(i) for i in got)))
    print("   allocated above the highest live id, so no gap is re-entered; %d ids claimed in the "
          "registry, %d appear in a sources.csv" % (len(reg), len(issued)))
    if a.claim:
        if not a.company:
            print("--claim needs --company so a later audit can say who holds the range")
            return 2
        for i in got:
            reg[i] = (a.company, a.agent)
        os.makedirs(os.path.dirname(REGISTRY), exist_ok=True)
        with io.open(REGISTRY, "w", encoding="utf-8", newline="\n") as f:
            w = csv.writer(f, delimiter="\t")
            w.writerow(["id", "company", "agent"])
            for i in sorted(reg):
                w.writerow([width(i), reg[i][0], reg[i][1]])
        print("   claimed for %s (agent %s) -> %s" % (
            a.company, a.agent or "?", os.path.relpath(REGISTRY, REPO)))
    else:
        print("   print-only; pass --claim to reserve before writing")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
