# PROGRESS — Source of Truth

Last updated: 2026-08-26

## Current phase
Revival R3 ACCEPTED — real-media Director→Motion Runtime integration complete for MVP plumbing.

## Completed / verified
- Existing audio/subtitle/emotion prototype preserved; no rewrite/deletion.
- Director IR v1 + Perception Result v1 schemas exist.
- `prototype/perception.py` separates observation from cinematic decisions.
- `prototype/semantic_director.py` emits provider-neutral Director IR v1 intent.
- `prototype/director_intent_qa.py` is a fail-closed structural/semantic gate.
- `prototype/legacy_adapter.py` keeps legacy Director JSON 0.1 explicit and non-authoritative.
- `prototype/analyze.py` routes MP4 → FFmpeg audio → faster-whisper → Perception → Semantic Director → Director IR; optional Motion IR compilation is exposed.
- Source media probe preserves real width/height/fps/duration and runtime asset reference.
- Director→Motion compiler aligns to motion-runtime-os Motion IR v1 and preserves source footage as a `video` layer.
- Director IR Contract CI is green.
- Real Media Acceptance run `32926244006` succeeded on a pinned public-domain real human interview: 4 segments, Director Intent QA PASS, Director IR schema PASS, Motion Runtime contract PASS.
- Downstream Remotion Director Bridge Acceptance run `32926421757` succeeded: the exact accepted Motion IR plus pinned source footage rendered to MP4; video+audio media probe PASS.
- Downstream HyperFrames Real Media Acceptance run `32926669798` succeeded using the exact same accepted Motion IR and source SHA; strict render and video+audio media probe PASS.
- Provider Independence Phase 3 run `32926669799` succeeded including Cross-provider Semantic QA.
- Acceptance evidence is recorded in `docs/ACCEPTANCE.md` and downstream `motion-runtime-os/docs/REAL_MEDIA_DIRECTOR_ACCEPTANCE.md`.

## Current product truth
The following path is verified, not hypothetical:

`real human MP4 → FFmpeg → faster-whisper → Perception → Semantic Director → Director IR v1 → Director Intent QA → Motion IR v1 → motion-runtime-os → source video + original audio + timed subtitles → {Remotion | HyperFrames} → MP4`

## Current limitations / not claimed
- Deterministic Semantic Director v1 is conservative; the acceptance interview was classified as exposition rather than demonstrating rich creative decisions.
- Successful execution does not equal superior creative direction.
- Edit/Voice/Avatar/Visual/B-roll routers remain architecture seams, not accepted runtime capabilities.

## Next quality target — R4 Director Intelligence
Move from plumbing correctness to director quality:
- build benchmark clips containing revelation, contrast/turn, question, emphasis, emotional transitions and pacing changes;
- create before/after outputs with controlled variants;
- measure semantic-decision accuracy and human preference;
- improve Director reasoning while keeping Director IR stable;
- only then extend Edit/Voice/Avatar/Visual/B-roll routers.

## Evidence rule
Real-media end-to-end status requires successful runtime artifacts. Synthetic/JSON-only tests remain lower evidence and cannot replace this gate.
