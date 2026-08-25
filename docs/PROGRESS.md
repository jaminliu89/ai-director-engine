# PROGRESS — Source of Truth

Last updated: 2026-08-26

## Current phase
Revival R1 — Director IR contract and Motion Runtime bridge.

## Completed
- Existing perception prototype preserved; no rewrite/deletion.
- Director IR v1 schema added at `schemas/director-ir.v1.schema.json`.
- Director IR sample fixture added.
- Provider-neutral `prototype/director_to_motion.py` bridge added.
- Regression test verifies semantic mapping and compiler input immutability.
- Director IR contract GitHub Actions workflow added.
- Architecture upgraded to Perception → Semantic Director → Director IR → Decision Routers.
- Motion execution boundary assigned to independent `motion-runtime-os`.
- AI Video Pipeline 2026 and Video Production OS architecture documents added.
- Revival decision recorded.

## Still not completed
- No real talking-head MP4/MOV acceptance result is checked in.
- Existing perception pipeline has not yet been upgraded to emit Director IR v1 from a real video.
- No repository-level end-to-end proof yet exists for `real video → Director IR → Motion IR → motion-runtime-os render`.
- Edit/Voice/Avatar/Visual routers are architecture seams only, not current runtime capabilities.

## Critical path
1. Make Director IR contract CI green and keep it mandatory for schema/compiler changes.
2. Upgrade the old analyzer output into a normalized Perception Result rather than writing shallow Director JSON directly.
3. Add Semantic Director policy that maps perception + transcript into Director IR v1.
4. Process one legitimate short talking-head fixture and record acceptance evidence.
5. Feed produced Director IR through the bridge and validate the resulting Motion IR against `motion-runtime-os`.
6. Only then claim end-to-end director/runtime integration.

## Risks
- Current emotion logic is heuristic and must remain labeled as such.
- Transcription/model availability may block local real-media acceptance.
- Director reasoning can become prompt-only and non-reproducible unless semantic decisions are schema-bound and evidence-backed.
- Provider-specific concepts must not leak upward from Motion Runtime into Director IR.

## Evidence rule
Contract/fixture/unit-test success proves the Revival bridge design, not real-video product acceptance. These evidence levels stay separate.
