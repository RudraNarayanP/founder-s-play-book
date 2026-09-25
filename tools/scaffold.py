#!/usr/bin/env python3
"""
scaffold.py -- claim-before-you-write, for the Founder's Playbook agent fleet.

Why this exists: two failures kept costing this run millions of tokens.
 (1) An agent accumulates a whole document in memory and dies at the turn ceiling with
     nothing on disk, so a completed research pass yields an empty result.
 (2) I judged a pass dead because its output file did not exist yet, dispatched a
     replacement onto the same paths, and both passes finished -- producing duplicate
     record ids and a re-merge.

This makes both impossible to do unnoticed. `claim` creates the file NOW with a
skeleton whose every section is marked PENDING, and records the owner in a ledger with
a heartbeat deadline. A claimed-and-stale file is visible to `ledger` even if the agent
never wrote a word; a claim held by a live agent blocks a second dispatch.

  python tools/scaffold.py claim   --path <file> --agent <name> --sections "A,B,C" [--ttl 90]
  python tools/scaffold.py section --path <file> --section A            # flip PENDING -> WRITTEN
  python tools/scaffold.py touch   --path <file> --agent <name>         # heartbeat
  python tools/scaffold.py release --path <file> [--agent <name>] [--done]
  python tools/scaffold.py ledger                                        # who holds what, age, words
"""

import argparse
import datetime
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(REPO, "founders_playbook", "_OWNER_LEDGER.json")
Q = chr(34)
BANNER = ("<!-- SCAFFOLDED by tools/scaffold.py at {ts}. "
          "STATUS: nothing written yet. Any agent reading this: the owner has a live "
          "claim; do NOT write this path. Every PENDING below is an unwritten section. "
          "-->")


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def iso(t=None):
    return (t or now()).strftime("%Y-%m-%dT%H:%M:%SZ")


def load():
    if os.path.exists(LEDGER):
        try:
            return json.load(open(LEDGER, encoding="utf-8"))
        except ValueError:
            return {}
    return {}


def save(d):
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    tmp = LEDGER + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=1, sort_keys=True)
    os.replace(tmp, LEDGER)


def norm(p):
    ap = os.path.abspath(p)
    try:
        return os.path.relpath(ap, REPO).replace(chr(92), "/")
    except ValueError:
        # Different drive (a temp dir on C: while the repo is on E:) -- relpath raises, which
        # crashed an agent's whole `section` call. Fall back to the absolute path.
        return ap.replace(chr(92), "/")


def words(path):
    try:
        return len(re.findall(r"\S+", open(path, encoding="utf-8", errors="replace").read()))
    except OSError:
        return -1


def age_min(e):
    t = datetime.datetime.strptime(e.get("heartbeat") or e.get("claimed"),
                                   "%Y-%m-%dT%H:%M:%SZ")
    return int((now() - t.replace(tzinfo=datetime.timezone.utc)).total_seconds() // 60)


def cmd_claim(a):
    led = load()
    p = norm(a.path)
    ent = led.get(p)
    if ent and not ent.get("done") and ent.get("agent") != a.agent:
        am = age_min(ent)
        if am < int(ent.get("ttl", 90)):
            print("REFUSED: %s is claimed by '%s' (heartbeat %d min ago, ttl %s min). "
                  "One path, one owner. Wait, or release it explicitly."
                  % (p, ent["agent"], am, ent.get("ttl")))
            return 3
        print("STALE claim by '%s' (%d min) superseded by '%s'" % (ent["agent"], am, a.agent))
    full = os.path.join(REPO, p)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    secs = [s.strip() for s in (a.sections or "").split(",") if s.strip()]
    if not os.path.exists(full) or a.force:
        body = ["# %s" % (a.title or os.path.basename(full)), ""]
        body.append(BANNER.format(ts=iso()))
        body.append("")
        for s in secs:
            body += ["## %s" % s, "", "STATUS: PENDING", ""]
        with open(full, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(body) + "\n")
        created = True
    else:
        created = False
    led[p] = {"agent": a.agent, "claimed": iso(), "heartbeat": iso(),
              "ttl": int(a.ttl), "sections": secs, "done": False,
              "deliverable": a.deliverable or ""}
    save(led)
    print("%s %s (owner=%s ttl=%s min, sections=%d, %d words)"
          % ("CREATED" if created else "ATTACHED", p, a.agent, a.ttl, len(secs), words(full)))
    return 0


def cmd_section(a):
    p = norm(a.path)
    full = os.path.join(REPO, p)
    txt = open(full, encoding="utf-8").read()
    out, hit, fuzzy = [], 0, []
    want = "## " + a.section
    for block in re.split(r"(?m)^(?=## )", txt):
        head = block.split(chr(10), 1)[0].strip() if block else ""
        # EXACT heading match only. Prefix matching let `--section S` stamp a different section
        # WRITTEN and drive the PENDING count to zero, which is the one signal this tool exists to
        # provide -- a false "written" is worse than a missing one.
        if head == want and "STATUS: PENDING" in block:
            block = block.replace("STATUS: PENDING", "STATUS: WRITTEN %s" % iso()[:10])
            hit += 1
        elif head.startswith(want) and head != want:
            fuzzy.append(head)
        out.append(block)
    if not hit:
        print("NOT STAMPED: no section heading equals %s exactly. Existing headings that merely "
              "start with it: %s" % (Q + a.section + Q, ", ".join(fuzzy[:6]) or "none"))
        return 1
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(out))
    touch({"path": a.path, "agent": a.agent})
    print("section %s: marked WRITTEN (%d words on disk)" % (a.section, words(full)))
    return 0


def touch(entry):
    led = load()
    p = norm(entry["path"])
    if p in led:
        led[p]["heartbeat"] = iso()
        if entry.get("agent"):
            led[p]["agent"] = entry["agent"]
        save(led)


def cmd_touch(a):
    touch({"path": a.path, "agent": a.agent})
    print("heartbeat %s" % norm(a.path))
    return 0


def cmd_release(a):
    led = load()
    p = norm(a.path)
    if p not in led:
        print("no claim for %s" % p)
        return 1
    if a.done:
        led[p]["done"] = True
        led[p]["heartbeat"] = iso()
        led[p]["words"] = words(os.path.join(REPO, p))
    else:
        led.pop(p)
    save(led)
    print("%s %s" % ("COMPLETED" if a.done else "RELEASED", p))
    return 0


def cmd_ledger(a):
    led = load()
    rows = []
    for p, e in sorted(led.items()):
        st = "done" if e.get("done") else ("LIVE" if age_min(e) < int(e.get("ttl", 90)) else "STALE")
        rows.append((p, e.get("agent", "?"), st, age_min(e), words(os.path.join(REPO, p)),
                     sum(1 for b in re.split(r"(?m)^(?=## )",
                         open(os.path.join(REPO, p), encoding="utf-8", errors="replace").read())
                         if "STATUS: PENDING" in b) if os.path.exists(os.path.join(REPO, p)) else -1))
    print("%-64s %-22s %-6s %6s %8s %8s" % ("path", "owner", "state", "age", "words", "pending"))
    for r in rows:
        print("%-64s %-22s %-6s %6d %8d %8d" % r)
    live = [r for r in rows if r[2] == "LIVE"]
    print("\n%d claims: %d live, %d stale, %d done"
          % (len(rows), len(live), sum(1 for r in rows if r[2] == "STALE"),
             sum(1 for r in rows if r[2] == "done")))
    return 1 if any(r[2] == "STALE" for r in rows) else 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("claim")
    c.add_argument("--path", required=True); c.add_argument("--agent", required=True)
    c.add_argument("--sections", default=""); c.add_argument("--title")
    c.add_argument("--ttl", default=90); c.add_argument("--deliverable")
    c.add_argument("--force", action="store_true")
    s = sub.add_parser("section")
    s.add_argument("--path", required=True); s.add_argument("--section", required=True)
    s.add_argument("--agent")
    t = sub.add_parser("touch")
    t.add_argument("--path", required=True); t.add_argument("--agent")
    r = sub.add_parser("release")
    r.add_argument("--path", required=True); r.add_argument("--agent")
    r.add_argument("--done", action="store_true")
    sub.add_parser("ledger")
    a = ap.parse_args()
    return {"claim": cmd_claim, "section": cmd_section, "touch": cmd_touch,
            "release": cmd_release, "ledger": cmd_ledger}[a.cmd](a)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
