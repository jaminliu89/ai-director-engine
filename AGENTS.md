# AGENTS.md — AI Director Engine Execution Contract

This file is the highest-priority repository-local instruction for coding agents.

## 1. Project mode
Execution project, not strategy-only project.

Required loop:
`Requirement → code/assets → repository update → runnable/testable result → acceptance → next phase`.

## 2. Current objective
Current Master Task: MT-002 — Perception → Semantic Director → Director IR → Motion Runtime Bridge.

Revival means preserve the legacy perception prototype while upgrading the stable seam from shallow Director JSON v0.1 to Director IR v1.

Current evidence boundaries:
- Contract/bridge work may proceed and must be tested.
- Real-video product acceptance is NOT complete until an actual talking-head MP4/MOV produces Director IR v1 with recorded evidence.
- `motion-runtime-os` owns renderer/provider execution; this repository must not import Remotion/HyperFrames APIs.

## 3. Current allowed scope
- local MP4/MOV/audio/script input;
- FFmpeg audio extraction;
- faster-whisper transcription and timestamps;
- deterministic perception signals with explicit limitations;
- Perception Result normalization;
- Semantic Director reasoning/policy;
- Director IR v1 schema/versioning/fixtures;
- Director IR → Motion IR compiler contract;
- tests, CI, acceptance evidence and migration docs.

## 4. Forbidden critical-path expansion
- Blender/Unreal/Unity integration;
- full NLE UI;
- SaaS billing/teams/publishing;
- avatar generation runtime;
- provider-specific renderer APIs inside Director Engine;
- rewriting/removing working legacy prototype without migration evidence.

## 5. Architecture contract
Stable semantic seam: `Director IR v1`.

`Perception → Semantic Director → Director IR` belongs here.
`Motion IR → Remotion/HyperFrames → Render/QA` belongs to `motion-runtime-os`.

Director IR must express intent, not implementation vendor syntax.

## 6. Read-before-write
Before coding, read:
1. `AGENTS.md`
2. `docs/MASTER_TASK.md`
3. `docs/PROGRESS.md`
4. `docs/CONSTRAINTS.md`
5. `docs/REVIVAL_DECISION.md`
6. relevant schema/code/tests.

## 7. Definition of done
A task is not done because code exists. Applicable requirements:
- code committed;
- tests added/updated;
- CI/local checks pass where available;
- output contract/artifact exists;
- `docs/PROGRESS.md` reflects reality;
- unresolved limitations are explicit.

## 8. Truthfulness
Never fabricate test runs, media outputs, model outputs, semantic equivalence or acceptance evidence.

Contract fixture evidence, real-media evidence and downstream render evidence are different levels and must not be conflated.

## 9. Change control
Do not silently change Director IR compatibility, current Master Task, provider boundary or acceptance gates. Record a decision/migration when a change is necessary.

## 10. Multi-agent discipline
Agents use isolated task ownership, preserve working behavior, avoid overlapping writes, add tests for changed behavior and leave explicit handoff/evidence.

Terminal rule: preserve the director brain boundary; prove each new layer before expanding the product surface.
