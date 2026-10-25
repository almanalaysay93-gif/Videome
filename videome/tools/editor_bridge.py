#!/usr/bin/env python3
"""Non-executing, read-only preflight for optional VideoMe editing providers."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess

def inspect(root=None):
    root = Path(root or os.environ.get("VIDEOME_VENDOR_DIR", "vendors")).expanduser()
    takeoff = root / "claude-shortform-video-editor"
    videocut = root / "chengfeng-videocut-skills"
    if not videocut.exists():
        videocut = root / "videocut-skills"
    checks = {
        "ffmpeg": bool(shutil.which("ffmpeg")),
        "ffprobe": bool(shutil.which("ffprobe")),
        "node": bool(shutil.which("node")),
        "python3": bool(shutil.which("python3")),
    }
    return {
        "schema_version": 1,
        "vendor_dir": str(root),
        "takeoff": {"present": takeoff.is_dir(), "path": str(takeoff), "render_verified": False},
        "videocut": {"present": videocut.is_dir(), "path": str(videocut), "runtime_verified": False, "operations_verified": []},
        "binaries": checks,
        "ready_to_render": False,
        "note": "Presence is not compatibility. This preflight does not execute vendor code or certify rendering."
    }

def verify_media(path):
    if not shutil.which("ffprobe"):
        return {"ok": False, "error": "ffprobe missing"}
    p = Path(path)
    if not p.is_file():
        return {"ok": False, "error": "media file missing"}
    try:
        proc = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_name,width,height",
             "-of", "json", str(p)], capture_output=True, text=True, timeout=30, check=True
        )
        data = json.loads(proc.stdout)
        return {"ok": bool(data.get("streams")), "probe": data}
    except (subprocess.SubprocessError, ValueError) as exc:
        return {"ok": False, "error": str(exc)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["doctor", "verify"])
    parser.add_argument("--vendor-dir")
    parser.add_argument("--file")
    args = parser.parse_args()
    if args.command == "verify" and not args.file:
        parser.error("--file is required for verify")
    result = inspect(args.vendor_dir) if args.command == "doctor" else verify_media(args.file)
    print(json.dumps(result, indent=2))
    if args.command == "verify" and not result["ok"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
