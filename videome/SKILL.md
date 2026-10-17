---
name: videome
description: Build polished short-form reels and videos with a four-agent creative workflow and a 45-technique motion toolkit. Invoke with /videome when planning or building a reel, brainstorming a video goal, researching visual samples, or creating a motion effect.
---

# Videome

Turn a reel brief into a clear, buildable motion treatment. This skill is a grouped library of 45 effect use cases, operated by a four-agent team: goal discovery, sample research, planning/production, and anti-slop review. Each technique includes context, a build recipe, and a scoped build brief for Agent 3.

## Workflow

1. **Run Agent 1 — Goal Grill & Brainstorm.** Discover the user's goal and turn it into an approved creative brief. Agent 1 is user-facing; in runtimes where subagents cannot ask the user, conduct this role in the main conversation.
2. **Start Agent 2 — Sample Scout in parallel.** As soon as a provisional goal/technique exists, gather relevant examples while Agent 1 continues discovery. Use Agent-Reach only if installed and healthy; see [four-agent-team.md](references/four-agent-team.md) for required fallback and truth-in-reporting rules.
3. **Start Agent 4 — Anti-Slop Design & Repo Scout.** Derive project-specific quality constraints and research repositories only when they solve a real implementation need. Have Agent 4 review the plan before final render when practical.
4. **Agent 3 — Planner, Orchestrator & Producer.** Integrate the approved brief, research pack, and design/repo notes; select technique modules from this library; plan, build, and assemble the deliverable.
5. **Judge and revise.** Send the render to Agent 4 for independent evaluation. If it fails, route actionable fixes to Agent 3 and repeat until PASS or a genuine blocker requires user input. Deliver the final product only after PASS.
6. **Verify the handoff.** Check legibility, timing, framing, color, audio, playability, dimensions, duration, frame rate, codecs, and agreed output files.

## Technique library

Read only the relevant file(s):

- **Four-agent team:** [four-agent-team.md](references/four-agent-team.md) — role definitions, copy-ready prompts, parallel workflow, Agent-Reach preflight/fallback, anti-generic design gate, and judge/revision loop. Read this for any production request.
- **Builder contract:** [builder-agent-contract.md](references/builder-agent-contract.md) — detailed build and handoff expectations for Agent 3.

- **Hooks, type & impact:** [01-hooks-type-impact.md](references/01-hooks-type-impact.md) — kinetic hook, gravity drop, giant captions, icon strike, glass type, pop captions, like burst, glitch/VHS hit.
- **UI, product & screen language:** [02-ui-product-screen.md](references/02-ui-product-screen.md) — prompt bar, storyboard deck, film scanner, NLE timeline, playing grid, reel feed, video card, everpresent CTA, comment drop, UI world, phone mockup, screen record + cursor.
- **Cuts, reveals & camera tricks:** [03-cuts-reveals-camera.md](references/03-cuts-reveals-camera.md) — jiggle delete, frame break, digital zoom, zoom-through cut, pull-back reveal, vertigo, whip pan, infinite zoom, parallax 2.5D.
- **Worlds & tactile graphics:** [04-worlds-tactile-graphics.md](references/04-worlds-tactile-graphics.md) — orb, couch wall, green screen, paper cut, doodle roll.
- **Proof, data & structure:** [05-proof-data-structure.md](references/05-proof-data-structure.md) — checklist, headline wall, chart grow, progress bar, counter ticker, comment wall.
- **Grade, film & editorial packaging:** [06-grade-film-packaging.md](references/06-grade-film-packaging.md) — grade slider, eyedropper grade, film look, title card, cover story.

## Build defaults

- Unless the brief says otherwise, treat a short-form reel as vertical 9:16 and design around a 1–2 second opening hook; confirm or adapt to the actual platform and footage.
- Prefer one hero effect per beat; a second effect should clarify cause, result, or proof rather than decorate.
- Preserve actual words, product appearance, UI, logo, and supplied brand colors. For readable text, favor authored type over model-generated lettering.
- Keep text short, high contrast, and inside safe areas. Avoid placing key copy where captions, buttons, or the user's face will be.
- Build with explicit timing and easing, not frame-dependent animation. Use motion with a start, readable hold, and resolved end state.
- Ask only when a missing choice materially changes the outcome. Otherwise make a reversible default and state it in the handoff.

## Output for technique advice

For each chosen effect, provide: **why/where it works**, **beat-by-beat build recipe**, **recommended materials/tools**, **timing/readability notes**, and the **Agent 3 build brief**. For actual production, follow the four-agent team and production contract and return the usable media/project files, not just a concept.
