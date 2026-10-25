# VideoMe + TakeOff + VideoCut

This is an **optional orchestration layer inside VideoMe**, not a claim of a working cross-runtime merger.

## Install
Clone this VideoMe branch or copy the `videome` skill directory into your Claude Code skills folder (`~/.claude/skills/videome`). Preserve the existing skill and references.

Optional providers (review their own installation instructions, dependencies, and licenses first):
```bash
mkdir -p vendors
git clone https://github.com/TakeOff-Team/claude-shortform-video-editor.git vendors/claude-shortform-video-editor
git clone https://github.com/Agentchengfeng/chengfeng-videocut-skills.git vendors/chengfeng-videocut-skills
python3 videome/tools/editor_bridge.py doctor --vendor-dir vendors
python3 -m unittest discover -s videome/tests -v
```
Clone only; no upstream installer is automatically run. Consult upstream README and LICENSE for setup and redistribution terms.

## Usage
In Claude Code: `/videome Create a 30-second vertical reel from my footage; plan, review, then render using verified local capabilities.`

The four VideoMe agents remain authoritative. Agent 3 may delegate to installed TakeOff and VideoCut capabilities after checking runtime compatibility. A doctor result of `ready_to_render: false` is expected until a real renderer integration is verified. This tool provides a safe baseline, not an end-to-end renderer.

## Sources
- https://github.com/almanalaysay93-gif/Videome
- https://github.com/TakeOff-Team/claude-shortform-video-editor
- https://github.com/Agentchengfeng/chengfeng-videocut-skills

Preserve original upstream license files and attribution when incorporating upstream source. No upstream code is vendored in this branch.
