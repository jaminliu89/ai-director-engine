# PROGRESS — Source of Truth

Last updated: 2026-08-26

## Current phase
Revival R2 — Perception → Semantic Director → Director IR → Motion IR contract verification.

## Completed / implemented
- Existing audio/subtitle/emotion prototype preserved; no rewrite/deletion.
- Director IR v1 schema and sample fixture exist.
- Normalized `prototype/perception.py` separates observation from cinematic decisions.
- `prototype/semantic_director.py` emits provider-neutral Director IR v1 intent.
- `prototype/director_intent_qa.py` adds structural/semantic QA.
- `prototype/legacy_adapter.py` keeps old Director JSON 0.1 consumers explicit and non-authoritative.
- `prototype/analyze.py` now routes MP4 → audio → transcript → Perception → Semantic Director → Director IR; optional Motion IR compilation is exposed.
- Director→Motion compiler is aligned to motion-runtime-os Motion IR field names (`version`, audio cue `time`).
- Semantic pipeline and compiler purity tests are in CI.
- Perception Result v1 schema exists.

## Still not completed
- No legitimate real talking-head MP4/MOV acceptance artifact is checked in.
- Therefore no claim yet that Whisper/FFmpeg/model installation succeeds end-to-end in CI or a clean runtime.
- No repository-level proof yet exists for `real video → Director IR → Motion IR → motion-runtime-os render`.
- Edit/Voice/Avatar/Visual routers remain architecture seams.

## Critical path
1. Keep Director IR + semantic pipeline CI green.
2. Validate a generated Director Motion IR fixture against the current motion-runtime-os schema/validator.
3. Process one legitimate short talking-head fixture and store acceptance evidence.
4. Feed its Motion IR into motion-runtime-os and render through at least Remotion; cross-provider render is a later acceptance level.
5. Only then claim real-media end-to-end integration.

## Evidence rule
Unit/fixture/schema success proves contract integration. It does not prove real-media product acceptance. Synthetic media may test plumbing only and must be labeled synthetic.
