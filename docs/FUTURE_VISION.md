# FUTURE VISION — Reserved, Not Current Scope

This file exists to preserve long-term architectural intent without allowing it to contaminate the MVP.

## Long-term direction
AI Director Engine may eventually evolve from dynamic-caption direction into a general visual-direction layer that can express camera, typography, timing, sound, motion, scene, and style decisions through a renderer-independent Director JSON contract.

Potential future renderer adapters may include:
- browser/video-code renderers;
- Remotion/Hyperframes-style systems;
- 3D renderers such as Blender;
- real-time/game engines such as Unreal or Unity.

## Current rule
None of those future engines are implementation priorities during MT-001 unless the Master Task explicitly unlocks them after the current acceptance gate.

## Architectural reservation only
The only current commitment to the future is:

`analysis -> Director JSON -> renderer adapter`

No current code should import future engine SDKs, create engine-specific scene models, or force Director JSON to mirror a particular renderer.

## Why this file is intentionally short
The project previously spent too much time expanding strategic vision instead of shipping runnable proof. Long-term ideas are preserved here so agents do not repeatedly reopen the discussion, while current development stays narrow.
