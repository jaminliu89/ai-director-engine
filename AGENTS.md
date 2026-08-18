# AGENTS.md — AI Director Engine Execution Contract

This file is the highest-priority repository-local instruction for all coding agents (Codex, Claude Code, Gemini, Pi, Hermes, Jules, human contributors, and future agents).

## 1. Project mode
This is an execution project, not a strategy-writing project.

Every phase must produce a verifiable deliverable before the next phase begins.

Required loop:

Requirement -> code/assets -> repository update -> runnable result -> acceptance -> next phase.

Do not substitute architecture, roadmap, vision, or discussion for working software.

## 2. Current frozen objective
Current phase: Phase 1.1 — real MP4/MOV -> audio extraction -> local speech transcription -> rhythm/emphasis analysis -> `director.json`.

The current phase is NOT complete until a real talking-head video has been processed and a real `director.json` has been produced and checked into an acceptance record.

Do not begin Phase 2 renderer integration before Phase 1.1 acceptance passes.

## 3. MVP boundaries
Allowed now:
- Local MP4/MOV input
- FFmpeg audio extraction
- Local faster-whisper transcription
- Word/segment timestamps
- Deterministic rhythm/emphasis/energy analysis
- Director JSON v0.1
- Tests, fixtures, validation, CLI robustness, error handling

Forbidden now:
- Blender integration
- Unreal/Unity/game-engine integration
- 3D world generation
- SaaS accounts/billing/teams
- social publishing
- full NLE timeline editor
- avatar generation
- large future-vision rewrites
- replacing the MVP with a new product direction

Future systems may be documented only as interface constraints; they may not enter runtime code during the current phase.

## 4. Architecture constraint
The stable seam is `Director JSON`.

Input/analyzers must not depend on a specific future renderer.
Future renderers must consume Director JSON rather than forcing analyzer rewrites.

## 5. Multi-agent rule
Agents work asynchronously through isolated task packets and must avoid overlapping file ownership unless explicitly coordinated.

Before coding, every agent must read:
1. `AGENTS.md`
2. `docs/MASTER_TASK.md`
3. `docs/PROGRESS.md`
4. `docs/CONSTRAINTS.md`
5. `docs/ASYNC_AGENT_PROTOCOL.md`
6. the GitHub issue assigned to that agent

Each agent must:
- stay inside its task scope;
- preserve existing working behavior;
- add/update tests for behavior it changes;
- not silently change product direction or schemas;
- record assumptions and unresolved blockers;
- finish with an explicit handoff note in its PR/issue.

## 6. Definition of done for any agent task
A task is not done because code exists.

Done requires all applicable items:
- code committed;
- tests added or updated;
- tests pass locally/CI where available;
- runnable command documented;
- output artifact or acceptance evidence exists;
- `docs/PROGRESS.md` reflects reality;
- no unsupported claim such as 'works' without execution evidence.

## 7. Truthfulness rule
Never fabricate test runs, media outputs, benchmark results, model outputs, or successful execution.

If the environment lacks FFmpeg, model weights, media fixtures, or network access, say exactly what could and could not be verified.

## 8. Change control
Do not edit these without explicit Master Task approval:
- MVP objective
- current phase gate
- Director JSON compatibility guarantees
- forbidden-scope list

If a task reveals a necessary change, open/document a decision instead of silently rewriting the framework.

## 9. Commit/PR discipline
Prefer small, reviewable commits tied to one task.

PR/issue handoff must state:
- files changed;
- commands run;
- tests/results;
- remaining risks;
- whether acceptance criteria passed.

## 10. Product principle
Final architecture can reserve future interfaces, but current implementation must remain deliberately small.

Terminal rule: current phase first; future vision later.
