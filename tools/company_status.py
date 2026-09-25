#!/usr/bin/env python3
"""
company_status.py -- one-line-per-company fleet status, for routing the wave.

Why: with 46 companies in flight the orchestrator's bottleneck is not compute, it is
answering "what does this company have and what is it blocked on" without reading it.
This derives everything from disk: volumes, words, register rows, gate findings, probe
tier, and the count of sections still marked PENDING by a scaffolded agent.

  python tools/company_status.py                 # table + routing hints
  python tools/company_status.py --json          # machine-readable
  python tools/company_status.py --stale-min 90  # flag claims with no heartbeat
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPANIES = os.path.join(REPO, "founders_playbook", "01_companies")
REGISTERS = ["timeline", "quantitative", "conflicts", "sources", "data_gaps",
             "validation", "failures", "decisions", "channels"]
TIER_RE = re.compile(r"\b(T1|T2|T3)\b[^\n]{0,40}?(exemplar|core|register)?", re.I)


def words(path):
    try:
        return len(re.findall(r"\S+", open(path, encoding="utf-8", errors="replace").read()))
    except OSError:
        return 0


def rows(path):
    try:
        return max(0, sum(1 for _ in open(path, encoding="utf-8", errors="replace")) - 1)
    except OSError:
        return 0


def find(company, name):
    for d in ("", "research"):
        p = os.path.join(company, d, name)
        if os.path.exists(p):
            return p
    return None


def probe_tier(company):
    for p in sorted(glob.glob(os.path.join(company, "research", "A*feasib*.md")) +
                    glob.glob(os.path.join(company, "research", "A*settlement*.md"))):
        t = open(p, encoding="utf-8", errors="replace").read()
        hits = re.findall(r"(?im)^\W*(tier|verdict)[^\n]{0,12}?\b(T[123])\b[^\n]{0,60}", t)
        if hits:
            return hits[-1][1].upper()
        m = re.search(r"\b(T[123])\b", t)
        if m:
            return m.group(1)
    return "?"


def gate_findings(company):
    try:
        r = subprocess.run([sys.executable, os.path.join(REPO, "tools", "gates.py"),
                            "--company-dir", company, "--checks", "csv,keys,anchors,budget"],
                           capture_output=True, text=True, timeout=600)
        m = re.search(r"Findings: \*\*(\d+)\*\*", r.stdout)
        return int(m.group(1)) if m else -1
    except Exception:
        return -1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--gates", action="store_true", help="also run the gate suite per company")
    a = ap.parse_args()
    out = []
    for company in sorted(glob.glob(os.path.join(COMPANIES, "company_*"))):
        vols = ([p for d in ("", "research") for p in
                 glob.glob(os.path.join(company, d, "stage_*.md"))])
        parts = glob.glob(os.path.join(company, "_parts", "s[0-9]_p[0-9]*.md"))
        eff = vols if vols else parts
        pending = sum(len(re.findall(r"STATUS: PENDING",
                                     open(p, encoding="utf-8", errors="replace").read()))
                      for p in eff)
        rec = {
            "company": os.path.basename(company),
            "tier": probe_tier(company),
            "volumes": len(eff),
            "narrative_words": sum(words(p) for p in eff),
            "claim_record_words": sum(words(p) for p in
                                      glob.glob(os.path.join(company, "stage_*claim_records*.md"))),
            "sections_pending": pending,
            "registers": {r: rows(find(company, r + ".csv")) for r in REGISTERS
                          if find(company, r + ".csv")},
            "sources": len([p for pat in ("*.txt", "*.htm*", "*.pdf") for p in
                            glob.glob(os.path.join(company, "sources", "**", pat),
                                      recursive=True)]),
        }
        rec["register_rows"] = sum(rec["registers"].values())
        rec.pop("registers") if not a.json else None
        if a.gates:
            rec["gate_findings"] = gate_findings(company)
        out.append(rec)

    if a.json:
        print(json.dumps(out, indent=1))
        return 0
    hdr = ("%-32s %-4s %5s %9s %9s %6s %8s %7s" %
           ("company", "tier", "vols", "narr_w", "recs_w", "pend", "reg_rows", "sources"))
    print(hdr)
    print("-" * len(hdr))
    for r in out:
        print("%-32s %-4s %5d %9s %9d %6d %8d %7d" % (
            r["company"], r["tier"], r["volumes"], format(r["narrative_words"], ","),
            r["claim_record_words"], r["sections_pending"], r["register_rows"], r["sources"]))
    print("\nRouting hints:")
    for r in out:
        hints = []
        if r["tier"] == "?":
            hints.append("NO TIER -> run probe (a wrong tier routes the wrong number of runs)")
        if r["volumes"] == 0:
            hints.append("NO VOLUME -> assemble")
        if r["sections_pending"]:
            hints.append("%d sections PENDING -> continue pass" % r["sections_pending"])
        if not r["register_rows"]:
            hints.append("no register rows")
        if r["claim_record_words"] and not r["volumes"]:
            hints.append("records without narrative")
        if hints:
            print("  %-32s %s" % (r["company"], "; ".join(hints)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
