# MASTER TASK — AI Director Engine Revival

## Objective
Revive the existing local-first prototype into a semantic director system without rewriting history or faking unfinished acceptance.

## Master Task ID
MT-002 — Perception → Semantic Director → Director IR → Motion Runtime Bridge

## Overall Status
**DONE FOR MVP PLUMBING / DIRECTOR INTELLIGENCE QUALITY IS NEXT**

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
- [x] Render the exact accepted real Motion IR through Remotion with original source video/audio + timed subtitles.
- [x] Render the same accepted real Motion IR through HyperFrames with original source video/audio + timed subtitles.
- [x] Verify both downstream MP4s with media-stream probes.

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
Status: ACCEPTED

Evidence:
- Exact real generated Motion IR is committed downstream at `motion-runtime-os/examples/real-media-director/motion-ir.json`.
- Remotion Director Bridge Acceptance run `32926421757` (run #1): SUCCESS.
  - exact pinned source + exact accepted Motion IR;
  - Motion IR validation PASS;
  - TypeScript PASS;
  - real Remotion render PASS;
  - final MP4 video+audio media probe PASS;
  - artifact ID `9591739910`.
- HyperFrames Real Media Acceptance run `32926669798` (run #2): SUCCESS.
  - exact same pinned source + exact same accepted Motion IR;
  - strict HyperFrames render PASS;
  - final MP4 video+audio media probe PASS;
  - artifact ID `9591815442`.
- Provider semantic parity baseline is independently verified by `motion-runtime-os` Provider Independence run `32926669799` (run #9): SUCCESS including Cross-provider Semantic QA.

## MVP Definition of Done
**SATISFIED.** A real human talking-head video produces Director IR v1, that IR compiles to Motion IR, and the exact accepted Motion IR produces media-probed visible MP4 artifacts through two independent runtime providers.

Verified chain:

`real MP4 → FFmpeg → faster-whisper → Perception → Semantic Director → Director IR v1 → Director Intent QA → Motion IR v1 → {Remotion | HyperFrames} → MP4`

## What is NOT implied by MVP completion
- Deterministic Semantic Director v1 is not yet a high-quality human-equivalent director.
- This acceptance interview was conservatively classified as exposition; it proves execution and contracts more than creative intelligence.
- ChatCut/Edit, Voice Clone, Avatar/Performance, B-roll/Visual generation remain future decision-router/runtime work.

## Phase R4 — Director Intelligence + Decision Routers
Status: NEXT

Next quality frontier:
- build benchmark clips for revelation, contrast/turn, question, emphasis, emotional transition and pacing changes;
- compare before/after outputs and human preference;
- improve Director reasoning while keeping Director IR stable;
- then add Edit/Voice/Avatar/Visual/B-roll routers behind explicit adapter contracts.

## Constraints
- Revival, not rewrite.
- No provider-specific APIs inside Director IR.
- No fabricated real-video acceptance.
- Synthetic media cannot satisfy the real-human acceptance gate.
- No Blender/Unreal/full NLE/avatar runtime in the current accepted MVP.
- Director IR versioning and migration are explicit.
- Repository evidence is Source of Truth.
