# CONSTRAINTS — Frozen MVP Guardrails

## Product constraint
The current product question is narrow:

Can a local tool understand a short talking-head video well enough to generate structured timing/emphasis decisions that later produce noticeably better dynamic captions?

Do not broaden this question during MT-001.

## Runtime constraints
Current runtime path:
- local file input;
- local FFmpeg;
- local faster-whisper;
- deterministic analysis;
- JSON artifact output.

Cloud services are optional future enhancements, not current dependencies.

## Architecture constraints
- `Director JSON` is the boundary between analysis and rendering.
- Analyzer code must not import or depend on a specific renderer.
- Renderer adapters must consume Director JSON.
- Future interfaces may be reserved but not implemented prematurely.

## Scope exclusions
Explicitly excluded from the current phase:
- Blender;
- Unreal Engine;
- Unity;
- generic 3D scenes;
- avatar generation;
- AI B-roll generation;
- publishing automation;
- cloud auth/billing/team systems;
- full timeline editor;
- marketplace/template ecosystem.

## Quality constraints
- No fake demos.
- No fake performance claims.
- No schema-breaking changes without migration/versioning.
- No hidden network dependency in the local-first path.
- No replacing deterministic heuristic labels with claims of emotion AI unless a real model is introduced and evaluated.

## UX constraint
Do not build a large UI before the CLI pipeline and visible rendering value are accepted.

## Future-compatibility reservation
Blender/game-engine/other renderers may later become adapters behind the Director JSON boundary. This is a reserved interface only and must not add current runtime complexity.
