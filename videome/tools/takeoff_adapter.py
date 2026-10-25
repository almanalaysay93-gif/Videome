#!/usr/bin/env python3
"""TakeOff adapter. Executes only explicitly requested documented commands."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess

SLUG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,79}$")
ACTIONS = {"doctor", "storyboard", "render", "qa"}

def run(root, action, slug=None, version=None, timeout=3600):
    root = Path(root).expanduser().resolve()
    edit = root / "edit"
    if action not in ACTIONS:
        raise ValueError("Unsupported TakeOff action")
    if not edit.is_file():
        raise FileNotFoundError("TakeOff ./edit missing; install upstream repository first")
    if action != "doctor" and (not slug or not SLUG.fullmatch(slug)):
        raise ValueError("Invalid project slug")
    if version is not None and (action not in {"render", "qa"} or not re.fullmatch(r"v?[0-9]{1,4}", version)):
        raise ValueError("Invalid render version")
    cmd = [str(edit), action]
    if action != "doctor":
        cmd.append(slug)
    if version:
        cmd.append(version)
    try:
        result = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=timeout, check=False)
        return {"provider": "takeoff", "action": action, "ok": result.returncode == 0,
                "exit_code": result.returncode, "stdout": result.stdout[-12000:],
                "stderr": result.stderr[-12000:]}
    except OSError as exc:
        return {"provider": "takeoff", "action": action, "ok": False, "error": str(exc)}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=sorted(ACTIONS))
    p.add_argument("--root", default=os.environ.get("TAKEOFF_ROOT", "vendors/claude-shortform-video-editor"))
    p.add_argument("--slug")
    p.add_argument("--version")
    args = p.parse_args()
    result = run(args.root, args.action, args.slug, args.version)
    print(json.dumps(result, indent=2))
    if not result["ok"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
