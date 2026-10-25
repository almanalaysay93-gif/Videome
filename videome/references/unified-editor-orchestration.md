# Unified editor orchestration (VideoMe-owned)

VideoMe is the **sole user-facing entry point**. Preserve its four-agent workflow and 45-technique library. TakeOff and VideoCut are optional downstream providers, not new agents.

## Stage routing
1. Agent 1: approve brief, inputs, target aspect ratio and deliverable.
2. Agent 2: collect reference examples with provenance.
3. Agent 4: set brand, readability, accessibility and anti-slop criteria.
4. Agent 3: write a versioned storyboard and a provider-neutral edit plan. Obtain approval before expensive rendering where practical.
5. Agent 3: inspect available providers using `python3 videome/tools/editor_bridge.py doctor`. Prefer existing VideoMe tools for motion design, use TakeOff only when its documented storyboard/render workflow is installed, and use VideoCut only for operations explicitly confirmed by its installed runtime.
6. Agent 3: render with a documented, installed provider. Never treat a planning-only bridge as a renderer. If no renderer is available, stop with an actionable installation report.
7. Agent 4: independently inspect render; revise or report a blocker. Validate deliverables with ffprobe when installed.

## Capability policy
- VideoCut: do not infer capability from repository name or count of advertised skills. Require explicit local runtime evidence and operation-level verification. Otherwise mark unavailable.
- TakeOff: do not assume macOS-only dependencies run on Linux/Windows; check installed binaries and source instructions.
- No automatic downloading, running third-party installers, or installing dependencies during a render request.
- Do not silently replace an unsupported operation with a materially different effect. Explain and request approval.
- Use separate directories for inputs, plans, renders and review. Never overwrite input footage.
- Keep source licenses and notices in their original vendor repositories. Link to original sources; do not relicense their code.
- Verify copyright/permissions for external assets.

## Provider-neutral handoff
Create `projects/<slug>/edit-plan.json`:
```json
{
  "schema_version": 1,
  "project": "sample",
  "format": {"width": 1080, "height": 1920, "fps": 30},
  "assets": [],
  "beats": [{"id": "hook", "start_seconds": 0, "duration_seconds": 2, "intent": "attention", "techniques": ["kinetic-hook"]}],
  "provider": "unassigned",
  "approval": "pending"
}
```
The plan is an interchange artifact, **not** proof that a provider supports each technique.

## Failure handling
If TakeOff or VideoCut is missing or incompatible, continue VideoMe's creative planning and available native operations; do not claim a final rendered video. Report missing capability, exact preflight result, and next installation step.
