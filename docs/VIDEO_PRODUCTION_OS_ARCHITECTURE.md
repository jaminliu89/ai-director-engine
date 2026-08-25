# Video Production OS Architecture

## System boundary
AI Director Engine is the director brain, not the renderer and not the final editor UI.

```text
Creator / Producer Intent
        ↓
Perception Layer
(video/audio/transcript/energy/pauses/visual context)
        ↓
Semantic Director
(narrative function / emotion transition / attention target)
        ↓
Director IR
        ↓
Decision Routers
 ├─ Edit decisions → ChatCut/FFmpeg/NLE adapters
 ├─ Performance intent → avatar/character providers
 ├─ Voice intent → voice clone/TTS providers
 ├─ Visual/B-roll intent → asset/generative providers
 └─ Motion intent → Director→Motion Compiler
                         ↓
                    Motion Runtime OS
                         ↓
                  Remotion / HyperFrames
                         ↓
                    Render + Motion QA
        ↓
Master QA / Human Review / Distribution / Outcome Feedback
```

## Stable contracts
### Director IR
Owns semantic and editorial intent:
- narrative_function
- emotional_transition
- attention_target
- director_intent
- pacing
- shot_decision
- edit_decision
- camera_intent
- motion_intent
- caption_intent
- audio_intent
- broll_intent
- performance_intent
- confidence / rationale

### Motion IR
Owned by `motion-runtime-os`. It is an execution contract for timed visual layers, camera/motion semantics, subtitle/audio cues and provider-neutral rendering.

## Repository relationship
- `ai-director-engine`: understand, reason, decide.
- `motion-runtime-os`: compile/render/verify motion.
- `skill-hub`: reusable agent/skill/control-plane capabilities.
- `creator-os`: eventual user-facing orchestration/product shell.

## Rules
1. Director Engine must not import Remotion/HyperFrames APIs.
2. Renderer changes must not force Perception rewrites.
3. Director IR and Motion IR have independent schema versions.
4. Provider selection happens after semantic decisions, not before.
5. A deterministic compiler may translate Director IR motion/caption/audio/camera intents into Motion IR.
6. Unsupported semantics must be explicit warnings, never silent drops.
7. `render_success != director_success`; final QA also evaluates whether intent survived execution.
