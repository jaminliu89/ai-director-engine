# PROJECT HANDOFF

## Project
AI Director Engine

## Current reality
The repository is in Phase 1.1. The CLI pipeline exists for local MP4/MOV -> FFmpeg audio -> faster-whisper transcription -> deterministic rhythm/emphasis analysis -> Director JSON.

The current phase is NOT accepted because no real talking-head media run and acceptance evidence has been checked in yet.

## What a new agent should understand first
This project previously over-invested in strategy/architecture discussion without runnable delivery. The correction is now explicit: one phase, one deliverable, one acceptance gate.

Do not restart product discovery. Do not rewrite the roadmap. Continue from the current repository state.

## Current critical path
1. Obtain a legitimate short talking-head video fixture.
2. Run the existing CLI end-to-end.
3. Verify the resulting JSON.
4. Harden obvious failure modes discovered by the run.
5. Record evidence in `docs/ACCEPTANCE.md`.
6. Only then unlock the first renderer task.

## Existing implementation facts
- FFmpeg extraction exists in `prototype/analyzer/audio.py`.
- Speech-to-text adapter exists in `prototype/analyzer/subtitle.py`.
- Deterministic energy/emphasis logic exists in `prototype/analyzer/emotion.py`.
- CLI orchestration exists in `prototype/analyze.py`.
- Runtime dependency is declared in `requirements.txt`.
- A basic deterministic analysis test exists under `tests/`.

## Product truth
The current emotion/rhythm layer is heuristic. It is useful metadata for MVP testing, but it is not a trained multimodal director model yet.

## Handoff rule
Any agent that changes functional state must leave a structured handoff in its task issue/PR and must not mark the phase complete without execution evidence.
