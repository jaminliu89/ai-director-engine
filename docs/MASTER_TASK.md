# MASTER TASK — AI Director Engine MVP

## Objective
Build a local-first prototype that converts a real talking-head MP4/MOV into a structured `director.json` that can later drive animation/rendering.

## Master Task ID
MT-001 — Local Video -> Director JSON -> Motion Demo

## Phase gates

### Phase 0 — Repository cold start
Status: COMPLETE

Acceptance:
- repository exists;
- README/PRD/architecture/schema exist;
- project structure exists.

### Phase 1.1 — Real Video -> Director JSON
Status: IN PROGRESS

Required deliverable:
- runnable CLI;
- FFmpeg audio extraction;
- local faster-whisper transcription;
- segment/word timestamps;
- deterministic rhythm/emphasis/energy metadata;
- actual `director.json` from a real talking-head video;
- acceptance record with command + result.

Phase 1.1 acceptance criteria:
- [ ] a real MP4/MOV is processed end-to-end;
- [ ] output JSON is valid and non-empty;
- [ ] at least one segment contains timestamps;
- [ ] at least one segment contains director motion metadata;
- [ ] failure modes are explicit (missing file, missing ffmpeg, missing dependency);
- [ ] tests for deterministic analysis pass;
- [ ] acceptance evidence is recorded in `docs/ACCEPTANCE.md`.

No renderer work enters the critical path before these are checked.

### Phase 2 — Director JSON -> Visible Motion Demo
Status: BLOCKED BY PHASE 1.1

Required deliverable:
- one renderer adapter;
- one 10–30 second visible dynamic-caption demo;
- MP4 output;
- before/after acceptance evidence.

Phase 2 must remain narrow: dynamic typography and visual rhythm only.

### Phase 3 — Product shell
Status: BLOCKED

Only after Phase 2 proves value:
- minimal local desktop UI;
- import -> analyze -> preview -> export.

## Master Definition of Done
MT-001 is complete only when a user can take a short local talking-head video and obtain an exported MP4 whose captions visibly respond to semantic/rhythmic cues.

## Non-goals during MT-001
- Blender
- Unreal/Unity
- avatar generation
- cloud SaaS platform
- complex NLE
- publishing pipeline
- enterprise features

## Governance
`AGENTS.md` is mandatory for every agent. Each subtask must be issued as an isolated GitHub issue/task packet and must not expand the Master Task without a recorded decision.
