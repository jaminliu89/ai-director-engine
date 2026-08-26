# MASTER TASK — AI Director Engine Revival

## Objective
Revive the existing local-first prototype into a semantic director system without rewriting history or faking unfinished acceptance.

## Master Task ID
MT-002 — Perception → Semantic Director → Director IR → Motion Runtime Bridge

## Completed
- [x] Preserve legacy perception prototype and execution discipline.
- [x] Define Director IR v1 schema.
- [x] Define Video Production OS architecture and repository boundaries.
- [x] Implement provider-neutral Director IR → Motion IR bridge.
- [x] Add compiler immutability + semantic pipeline regression tests.
- [x] Add Director IR + Perception Result schemas and fixtures.
- [x] Add Director IR contract CI gate.
- [x] Add Director Intent QA and explicit legacy 0.1 adapter.
- [x] Archive 2026 AI video pipeline research in repository.
- [x] Process a real public-domain human interview through FFmpeg → faster-whisper → Perception → Semantic Director → Director IR v1.
- [x] Validate the real generated Motion IR against the pinned motion-runtime-os consumer contract.

## Phase R1 — Contract Revival
Status: ACCEPTED

Evidence:
- Director IR Contract CI green.
- Director IR v1 JSON Schema validates emitted fixture output.
- Motion bridge is provider-neutral and does not mutate source IR.

## Phase R2 — Real Video → Perception → Director IR
Status: ACCEPTED

Evidence:
- Real Media Acceptance run `32926244006` (run #7): SUCCESS.
- Fixture: real public-domain U.S. Army interview, 1080×1920, H.264 + AAC, ~28.733s.
- Pinned input SHA-256: `a93869b5712154b990909a3bfb14e2636a5cce59174ecd64854abdbda302fad0`.
- faster-whisper `tiny.en` emitted 4 non-empty segments.
- Director IR v1 JSON Schema: PASS.
- Director Intent QA: PASS, zero errors/warnings.
- Motion Runtime consumer-contract QA: PASS.
- Source footage is preserved into Motion IR as a `video` layer with runtime asset_ref.

## Phase R3 — Director IR → Motion Runtime integration
Status: REAL IR ACCEPTED / FINAL RENDER VERIFICATION IN PROGRESS

Completed evidence:
- Real Director IR compiles to Motion IR.
- Real generated Motion IR passes the pinned `motion-runtime-os` consumer contract.
- Original source video dimensions/FPS/duration and source-video asset reference survive compilation.

Remaining exit gate:
- downstream `motion-runtime-os` renders the exact accepted real Motion IR with the pinned source video;
- resulting MP4 passes video+audio media probe;
- artifact/run evidence is recorded here.

## Phase R4 — Decision Routers
Status: FUTURE AFTER R3

Adapters may include Edit Engine (ChatCut/FFmpeg/NLE), Voice, Avatar/Performance, Visual/B-roll providers. They must consume Director IR decisions and may not redefine the director contract.

## Definition of Done
The revived engine is done for MVP only when a real talking-head video produces Director IR v1, that IR compiles to Motion IR, and the downstream runtime produces a visible artifact whose director intent is verifiably preserved.

## Constraints
- Revival, not rewrite.
- No provider-specific APIs inside Director IR.
- No fabricated real-video acceptance.
- Synthetic media cannot satisfy the real-human acceptance gate.
- No Blender/Unreal/full NLE/avatar runtime in current critical path.
- Director IR versioning and migration are explicit.
- Repository evidence is Source of Truth.
