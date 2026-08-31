# PROGRESS — Source of Truth

Last updated: 2026-08-31

## Current phase
R3 PLUMBING ACCEPTED / VISUAL MOTION NOT ACCEPTED.

Previous wording overstated the result. The real-media workflows proved media preservation, schema compatibility, provider routing and MP4 rendering, but did **not** prove a useful automatic motion-design result.

## What is actually verified
- Existing audio/subtitle/emotion prototype preserved.
- Director IR v1 + Perception Result v1 schemas exist.
- `prototype/perception.py` separates observation from cinematic decisions.
- `prototype/semantic_director.py` emits provider-neutral Director IR v1 intent.
- Director→Motion compiler aligns to Motion IR v1.
- Real media can pass through Remotion and HyperFrames providers and produce playable MP4 files with audio.

## Visual inspection correction — 2026-08-31
Manual inspection of the previously cited artifacts shows:
- Remotion artifact: source talking-head video with ordinary caption/lower-third treatment; no convincing automatic explanatory motion-design sequence was demonstrated.
- HyperFrames artifact: predominantly black frames with subtitles; this is not an acceptable visual-motion result.

Therefore the following claims are **NOT ACCEPTED**:
- "automatic motion effects complete"
- "AI director visual rhythm complete"
- "B-roll / explanatory motion workflow complete"
- "Remotion + HyperFrames creative cooperation complete"

The former PASS records remain valid only as **plumbing/runtime compatibility evidence**.

## Current product truth
Verified:
`real human MP4 → analysis → Director IR → Motion IR → {Remotion | HyperFrames} → playable MP4`

Not yet verified:
`narration semantics → visible motion decision → meaningful animated composition/B-roll → clearly improved final video`

## New hard gate — R3.5 Visible Motion Proof
Nothing may be called an "animation/motion demo" until a human can directly inspect the delivered media.

Required acceptance artifact:
1. One 15–30 second narration clip.
2. At least 3 visibly different semantic motion events, not plain subtitles:
   - e.g. kinetic keyword/title motion;
   - explanatory diagram/data/MG animation;
   - B-roll/image/video insert or visual replacement.
3. At least one event rendered by Remotion.
4. At least one event rendered by HyperFrames.
5. Final combined MP4 delivered as a directly inspectable artifact.
6. Contact sheet or GIF preview stored with acceptance evidence.
7. Before/after comparison against a plain-caption baseline.

## Current limitations
- Director Intelligence remains conservative.
- B-roll/Visual Router is not accepted runtime capability.
- Provider execution success is not creative-quality evidence.
- No Blender/Unreal/full NLE work enters the critical path.

## Evidence rule
CI green is necessary but never sufficient for visual features. For animation, B-roll, visual rhythm or directing claims, the actual rendered frames/video are the acceptance source of truth.
