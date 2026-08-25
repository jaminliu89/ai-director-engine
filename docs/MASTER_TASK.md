# MASTER TASK — AI Director Engine Revival

## Objective
Revive the existing local-first prototype into a semantic director system without rewriting history or faking unfinished acceptance.

## Master Task ID
MT-002 — Perception → Semantic Director → Director IR → Motion Runtime Bridge

## Completed
- [x] Preserve legacy perception prototype and execution discipline.
- [x] Define Director IR v1 schema.
- [x] Define Video Production OS architecture and repository boundaries.
- [x] Implement first provider-neutral Director IR → Motion IR bridge.
- [x] Add compiler immutability regression test.
- [x] Add Director IR sample fixture.
- [x] Add Director IR contract CI gate.
- [x] Archive 2026 AI video pipeline research in repository.

## Phase R1 — Contract Revival
Status: IMPLEMENTED / CI VERIFICATION IN PROGRESS

Exit gate:
- Director IR v1 exists and is versioned;
- bridge test passes CI;
- no renderer/provider API leaks into Director Engine contracts.

## Phase R2 — Real Video → Perception → Director IR
Status: NOT ACCEPTED

Required evidence:
- real MP4/MOV fixture;
- FFmpeg extraction;
- local transcription with segment/word timestamps;
- perception signals (pause/rhythm/energy/emphasis + explicit limitations);
- Semantic Director converts perception into non-empty Director IR v1;
- acceptance record contains command, environment, output summary and known limitations.

This phase is NOT complete until real media evidence exists.

## Phase R3 — Director IR → Motion Runtime integration
Status: BRIDGE IMPLEMENTED / END-TO-END NOT ACCEPTED

Required evidence:
- Director IR fixture compiles to Motion IR;
- output is accepted by `motion-runtime-os` schema/runtime;
- at least one motion intent, camera intent, caption intent and audio cue survive compilation;
- downstream render evidence proves semantic intent survives execution.

## Phase R4 — Decision Routers
Status: FUTURE AFTER R2/R3

Adapters may include Edit Engine (ChatCut/FFmpeg/NLE), Voice, Avatar/Performance, Visual/B-roll providers. They must consume Director IR decisions and may not redefine the director contract.

## Definition of Done
The revived engine is done for MVP only when a real talking-head video produces Director IR v1, that IR compiles to Motion IR, and the downstream runtime produces a visible artifact whose director intent is verifiably preserved.

## Constraints
- Revival, not rewrite.
- No provider-specific APIs inside Director IR.
- No fabricated real-video acceptance.
- No Blender/Unreal/full NLE/avatar runtime in current critical path.
- Director IR versioning and migration are explicit.
- Repository evidence is Source of Truth.
