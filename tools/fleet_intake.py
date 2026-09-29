#!/usr/bin/env python3
"""
fleet_intake.py -- scripted EDGAR intake for every company in the universe, run by the
orchestrator so no dossier agent spends a turn on a download (method s15.1).

Two passes per company, and the second one is the reason this script exists:

  pass 1  in-window  --from <stage-1 lo> --to <stage-1 hi>
  pass 2  recitals   only if pass 1 stored nothing: the same window's END extended forward,
                     because a 1994 10-K or a 1995 S-4 that recites "incorporated in 1903"
                     is the carrier that settles an origin for every pre-EDGAR company here.
                     Ford and Citigroup each produced their founding sentence that way, from
                     bytes neither window could reach.

Older than EDGAR is not empty: pass 1 returning nothing is recorded as
RETURNS-NOTHING-WITH-PERIMETER with the measured floor date, never as a null (s14 r6, RD-128).

Stdlib only, resumable. Usage:
  python tools/fleet_intake.py --dry-run
  python tools/fleet_intake.py --only kroger,disney [--max-docs 30]
  python tools/fleet_intake.py --all
State: founders_playbook/00_universe/_FLEET_INTAKE.tsv  (reruns skip rows marked DONE)
"""
import argparse
import csv
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PLAY = os.path.join(REPO, "founders_playbook")
BASE = os.path.join(PLAY, "01_companies")
STATE = os.path.join(PLAY, "00_universe", "_FLEET_INTAKE.tsv")
sys.path.insert(0, HERE)

from harvest_mine import WINDOWS                       # slug -> (stage-1 lo, hi)
from scaffold_company import universe_rows, assign_slugs   # the pipeline's own name->slug rules


def dirs_by_slug():
    """slug -> company dir, from the directory names actually on disk."""
    out = {}
    for d in sorted(os.listdir(BASE)):
        m = re.match(r"company_\d{3}_(.+)$", d)
        if m:
            out[m.group(1)] = os.path.join(BASE, d)
    return out


def load_state():
    if not os.path.exists(STATE):
        return {}
    with io.open(STATE, encoding="utf-8", newline="") as f:
        return {r["slug"]: r for r in csv.DictReader(f)}


def save_state(row):
    new = not os.path.exists(STATE)
    with io.open(STATE, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t")
        if new:
            w.writeheader()
        w.writerow(row)


FIELDS = ["slug", "company", "dir", "pass1_status", "pass1_docs", "pass2_status", "pass2_docs",
          "filing_floor", "slices_capped", "note", "state"]


def run(cmd):
    """Return (rc, stdout). Never raise: one dead company must not stop the fleet."""
    try:
        p = subprocess.run([sys.executable, os.path.join(HERE, "sec_intake.py")] + cmd,
                           capture_output=True, text=True, timeout=3600)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except Exception as e:                                   # timeout / python missing
        return 9, "SUBPROCESS FAILED: %s: %s" % (type(e).__name__, e)


def measure(out):
    """Parse sec_intake's OWN summary lines -- count what it reports it stored, never assume a shape."""
    d = re.search(r"auto: (\d+) documents stored \((\d+) bytes, (\d+) words\); (\d+) UNANSWERED", out)
    docs = int(d.group(1)) if d else 0
    unans = int(d.group(4)) if d else len(re.findall(r"UNANSWERED", out))
    per = re.search(r"date perimeter (\S+) -> (\S+)", out)
    win = re.search(r"auto: (\d+) accessions in window, (\d+) directories opened", out)
    return docs, unans, (per.group(1) if per else ""), (per.group(2) if per else ""), \
        ("yes" if "walk: CAPPED" in out else "no"), (win.group(1) if win else "0")


def intake(slug, cdir, rank, name, max_docs, dry, recital=True):
    lo, hi = WINDOWS.get(slug, ("1900-01-01", "2000-12-31"))
    # Pass 2 reaches FORWARD to where recitals live, not to "window + a generation": EDGAR's own
    # floor is 1993-1994, so a pre-1960 company's founding sentence can only be in a filing from the
    # 1990s (Ford's 1903/1919 sentence is printed in a 1994 10-K and a 1995 S-4, Citigroup's 1812
    # claim in its 1992 continuation). +25 years alone would have stopped in 1985 and read as empty.
    end2 = str(min(max(int(hi[:4]) + 25, 2006), 2030))
    row = {"slug": slug, "company": name, "dir": os.path.basename(cdir), "pass1_status": "",
           "pass1_docs": "0", "pass2_status": "", "pass2_docs": "0", "filing_floor": "",
           "slices_capped": "", "note": "", "state": "DONE"}
    if dry:
        print("DRY %-14s rank=%-3s %s -> %s  window=%s..%s recital_to=%s"
              % (slug, rank, name, os.path.basename(cdir), lo, hi, end2))
        return row
    rc1, out1 = run(["auto", name, "--company-dir", cdir, "--from", lo, "--to", hi,
                     "--max-docs", str(max_docs)])
    d1, u1, floor1, _t1, capped1, win1 = measure(out1)
    row["pass1_status"] = "rc%s/inwindow%s/UNANS%d" % (rc1, win1, u1)
    row["pass1_docs"] = str(d1)
    row["filing_floor"] = floor1
    row["slices_capped"] = capped1
    if d1 == 0 and recital:
        rc2, out2 = run(["auto", name, "--company-dir", cdir, "--from", hi,
                         "--to", end2 + "-12-31", "--max-docs", str(max_docs)])
        d2, u2, floor2, _t2, capped2, win2 = measure(out2)
        row["pass2_status"] = "rc%s/inwindow%s/UNANS%d" % (rc2, win2, u2)
        row["pass2_docs"] = str(d2)
        row["filing_floor"] = floor2 or floor1
        row["slices_capped"] = capped2 if d2 else capped1
    note = []
    if int(row["pass1_docs"]) + int(row["pass2_docs"]) == 0:
        row["state"] = "EMPTY-PERIMETER"      # not a null: see the module docstring
        note.append("no document stored; probes must cite the measured floor, not a null")
    if row["slices_capped"] == "yes":
        note.append("slice walk capped -- early-filing silence is UNANSWERED")
    if "REFUSED-WRONG-REGISTRANT" in out1 or "not resolved" in out1:
        row["state"] = "REFUSED"
        note.append("identity guard refused the write; resolve the CIK by hand")
    row["note"] = "; ".join(note)
    print("%-14s p1=%s p2=%s floor=%s %s" % (slug, row["pass1_docs"], row["pass2_docs"],
                                             row["filing_floor"], row["note"]))
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--only", default="", help="comma-separated slugs")
    ap.add_argument("--no-recital", dest="recital", action="store_false",
                    help="pass 1 only: use this on a company whose stage-1 window is already "
                         "covered by a merged volume, so a wide recital re-grab cannot overwrite it")
    ap.add_argument("--max-docs", type=int, default=30)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="ignore the resume state")
    a = ap.parse_args()

    ds = dirs_by_slug()
    uni = universe_rows()
    # Match against the dirs that actually exist, with the same vocabulary rules the scaffolder
    # used -- so a company that is named in the universe but has no directory is reported, not guessed.
    slugs, unresolved, _extra = assign_slugs(uni, set(ds))
    want = {s.strip() for s in a.only.split(",") if s.strip()}
    done = {} if a.force else load_state()
    n = 0
    for rank, name in uni:
        slug = slugs.get(rank)
        if not slug:
            print("SKIP rank=%s %r: no matching company dir (unresolved: %s)"
                  % (rank, name, ", ".join("%s" % u[1] for u in unresolved)))
            continue
        if want and slug not in want:
            continue
        cdir = ds.get(slug)
        if not cdir or not os.path.isdir(cdir):
            print("SKIP %-12s no company dir (run tools/scaffold_company.py)" % slug)
            continue
        if slug in done and done[slug].get("state") in ("DONE", "EMPTY-PERIMETER"):
            if not (want and slug in want):
                continue
        save_state(intake(slug, cdir, rank, name, a.max_docs, a.dry_run, a.recital))
        n += 1
    print("fleet_intake: %d companies processed" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
