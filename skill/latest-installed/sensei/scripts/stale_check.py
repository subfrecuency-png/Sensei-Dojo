#!/usr/bin/env python3
"""stale_check.py — the stale-on-load check for a live layer (references/live.md in sensei,
mad-scientist-mode, research-engine and command-center; folded in from the retired -live skills 2026-10-01).

Reads the live file, finds the header line `next_review: YYYY-MM-DD` and the
"Dated items" table, and reports every item whose next-event date has passed.
Deterministic: no network, no model judgment (FL-119). The model still decides
what a passed event means; this script only says which items to re-check first.

Usage:
  python3 scripts/stale_check.py --file references/live.md                 # today = system clock
  python3 scripts/stale_check.py --file references/live.md --today 2026-12-03
  python3 scripts/stale_check.py --file references/live.md --json

Table contract: a markdown table under a heading containing "Dated items", with
columns including "ID" and "Next event". The Next event cell starts with an ISO
date (YYYY-MM-DD) or the word "none"/"weekly"/"monthly". Other cells are free text.

Exit codes: 0 = nothing stale · 1 = at least one stale item or next_review passed ·
2 = file missing or unreadable (including non-UTF-8), table not found, or an impossible date — never 1,
so a caller that branches on the code cannot read a broken input as "stale".
Self-test: python3 stale_check.py --selftest (exit 0 = every case passes).
"""
import argparse, datetime as dt, io, json, os, re, sys, tempfile
from contextlib import redirect_stderr, redirect_stdout

ISO = re.compile(r"(\d{4}-\d{2}-\d{2})")


class Malformed(Exception):
    """Input problem that must exit 2, never 1 (1 means 'stale')."""


def parse(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError) as e:
        raise Malformed(f"cannot read {path}: {e}")
    m = re.search(r"next_review:\s*\**\s*(\d{4}-\d{2}-\d{2})", text)
    next_review = m.group(1) if m else None
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith("#") and "Dated items" in l), None)
    if start is None:
        return next_review, None
    rows, header = [], None
    for l in lines[start + 1:]:
        if l.startswith("#"):
            break
        if not l.strip().startswith("|"):
            if header and rows:
                break
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if header is None:
            header = [c.strip("* ").lower() for c in cells]
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(dict(zip(header, cells)))
    return next_review, rows


def iso_date(s, what):
    try:
        return dt.date.fromisoformat(s)
    except ValueError:
        raise Malformed(f"{what} is not a real date: {s}")


def check(path, today):
    next_review, rows = parse(path)
    if rows is None:
        raise Malformed("no 'Dated items' table found")
    key_id = next((k for k in (rows[0] if rows else {}) if k == "id"), None)
    key_ev = next((k for k in (rows[0] if rows else {}) if k.startswith("next event")), None)
    if not rows or not key_id or not key_ev:
        raise Malformed("table needs 'ID' and 'Next event' columns and at least one row")
    stale, undated = [], []
    for r in rows:
        rid = r.get(key_id, "?")
        m = ISO.search(r.get(key_ev, ""))
        if not m:
            undated.append(rid)
            continue
        d = iso_date(m.group(1), f"next event of {rid}")
        if d < today:
            stale.append({"id": rid, "next_event": r[key_ev], "days_past": (today - d).days})
    review_passed = bool(next_review and iso_date(next_review, "next_review") < today)
    return {"today": today.isoformat(), "next_review": next_review, "review_passed": review_passed,
            "items": len(rows), "stale": stale, "no_date": undated}


def run(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", help="path to the live file (-live SKILL.md or a references/*live*.md block)")
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD); default: system clock")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", "--self-test", dest="selftest", action="store_true", help="run the built-in tests (exit 0 = all pass)")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file:
        print("stale_check: --file is required (or --selftest)", file=sys.stderr)
        return 2
    try:
        today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    except ValueError:
        print("stale_check: --today must be YYYY-MM-DD", file=sys.stderr)
        return 2
    try:
        out = check(a.file, today)
    except Malformed as e:
        print(f"stale_check: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        nr = out["next_review"]
        print(f"today {out['today']} · next_review {nr or 'MISSING'}"
              + (" · PASSED — say so before using this layer" if out["review_passed"] else ""))
        print(f"{out['items']} dated items · {len(out['stale'])} past their next event · {len(out['no_date'])} recurring/undated")
        for s in sorted(out["stale"], key=lambda s: -s["days_past"]):
            print(f"  STALE {s['id']}: {s['next_event']} ({s['days_past']} days past)")
    return 1 if (out["stale"] or out["review_passed"] or not out["next_review"]) else 0


def selftest():
    """Exit-code contract: 0 nothing stale · 1 stale · 2 unreadable / missing / malformed (never 1)."""
    d = tempfile.mkdtemp(prefix="stale_check_selftest_")
    good = os.path.join(d, "live.md")
    with open(good, "w", encoding="utf-8") as f:
        f.write("next_review: 2026-11-01\n\n## Dated items\n| ID | Item | Next event |\n|---|---|---|\n"
                "| AA-01 | thing | 2026-10-19 comments due |\n| AA-02 | other | none |\n")
    bad_date = os.path.join(d, "bad-date.md")
    with open(bad_date, "w", encoding="utf-8") as f:
        f.write("next_review: 2026-11-01\n\n## Dated items\n| ID | Next event |\n|---|---|\n| BB-01 | 2026-02-30 |\n")
    no_table = os.path.join(d, "no-table.md")
    with open(no_table, "w", encoding="utf-8") as f:
        f.write("next_review: 2026-11-01\n\n## Something else\n")
    binary = os.path.join(d, "binary.md")
    with open(binary, "wb") as f:
        f.write(b"\xff\xfe\x00\x81 not utf-8 \xc3\x28")

    def code(*argv):
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            return run(list(argv))

    checks = {
        "fresh_exit_0": code("--file", good, "--today", "2026-10-01") == 0,
        "stale_item_exit_1": code("--file", good, "--today", "2026-10-20") == 1,
        "review_passed_exit_1": code("--file", good, "--today", "2026-11-02") == 1,
        # R4 repro: a missing file used to exit 1 via sys.exit(str), which a caller reads as "stale"
        "missing_file_exit_2": code("--file", os.path.join(d, "does-not-exist.md")) == 2,
        "directory_exit_2": code("--file", d) == 2,
        "non_utf8_exit_2": code("--file", binary) == 2,
        "no_table_exit_2": code("--file", no_table) == 2,
        "impossible_date_exit_2": code("--file", bad_date, "--today", "2026-10-01") == 2,
        "bad_today_exit_2": code("--file", good, "--today", "2026-13-01") == 2,
        "no_file_arg_exit_2": code() == 2,
    }
    print(json.dumps(checks, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(run())
