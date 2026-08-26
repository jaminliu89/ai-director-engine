# Director Quality Spec v1

## Purpose
R4 evaluates whether director decisions are useful, not merely schema-valid or renderable. Director IR v1 remains stable.

## Quality dimensions
1. Narrative-function accuracy — revelation / turn / question / emphasis / exposition.
2. Attention alignment — high-priority caption/camera/audio choices must target a meaningful phrase rather than decorate every segment.
3. Restraint — exposition should not receive gratuitous cinematic effects.
4. Temporal coherence — pauses, holds and cuts may not destroy speech comprehension.
5. Cross-modal consistency — camera, motion, caption, audio and B-roll decisions should support the same director intent.
6. Preference lift — a directed render must eventually beat a neutral baseline in blinded human preference; machine QA alone cannot close this dimension.

## Gates
### Q0 Contract
Director IR schema + Director Intent QA + Motion consumer contract PASS.

### Q1 Semantic benchmark
`benchmarks/director-intelligence-v1.json` is fail-closed in CI. Any regression blocks R4 progress.

### Q2 Render survival
Chosen intent survives Director IR → Motion IR → runtime execution. Existing Remotion/HyperFrames semantic QA remains the execution gate.

### Q3 Human preference — OPEN
For benchmark clips with revelation, turn, question, emphasis and emotional transition, render neutral and directed variants. Reviewers see unlabeled A/B outputs. Record preference, reason tags and failure modes. R4 quality acceptance requires statistically meaningful preference lift; do not infer it from successful rendering.

## Router policy
Director Engine owns decisions; execution adapters own implementation. Planned routers: Edit, B-roll/Visual, Audio, Voice, Avatar/Performance. Routers consume Director IR and must not redefine narrative intent.

## Non-goals
No Blender/Unreal/full NLE in the current quality loop. No provider-specific fields in Director IR. No claim of human-equivalent directing from keyword classification.
