# Architecture v1.0

```text
Input Video / Audio / Script
        ↓
Perception Layer
  ├─ transcription + word timestamps
  ├─ pauses / rhythm / energy
  ├─ emphasis / emotion signals
  └─ future visual understanding
        ↓
Semantic Director
  ├─ narrative function
  ├─ emotional transition
  ├─ attention target
  ├─ pacing / shot / edit intent
  ├─ camera / caption / audio intent
  └─ performance / B-roll / motion intent
        ↓
Director IR v1
        ↓
Decision Routers
  ├─ Edit Engine adapters
  ├─ Voice/Avatar/Visual providers
  └─ Director→Motion Compiler
               ↓
          Motion Runtime OS
               ↓
        Remotion / HyperFrames
               ↓
          Render + QA Evidence
```

## Stable seams
- Perception does not depend on renderer/provider.
- Director IR is the semantic/editorial contract.
- Motion IR is owned by `motion-runtime-os` and is the timed motion execution contract.
- `prototype/director_to_motion.py` is the first provider-neutral compiler bridge.

## Design principles
1. Understand/reason/decide before provider selection.
2. Director Engine owns why/what should happen; Motion Runtime owns how motion is executed.
3. Unsupported semantics must be explicit.
4. No Remotion/HyperFrames API may leak into Director IR.
5. Real acceptance evidence remains mandatory before claiming end-to-end completion.
