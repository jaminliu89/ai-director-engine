# Revival Decision — 2026-08-26

## Decision
Revive, do not rewrite.

Preserve:
- prototype perception/analyzer work;
- Director JSON seam concept;
- repository execution discipline and phase gates.

Upgrade:
- Director JSON v0.1 → Director IR v1;
- keyword/emotion heuristics → Perception + Semantic Director separation;
- direct renderer coupling → Director→Motion Compiler → `motion-runtime-os`;
- tool-specific thinking → provider-neutral decision contracts.

## Why
The old repository stopped at the correct seam but its schema was too shallow to bridge perception to real directing. The missing layer is semantic director reasoning, not another renderer.

## Compatibility
`docs/director-json-schema.md` remains a legacy v0.1 reference. New work targets `schemas/director-ir.v1.schema.json`. Migration should be additive until a real acceptance fixture proves the v1 pipeline.

## Non-claims
This decision does not mark the old real-video acceptance as complete. A real talking-head MP4/MOV still needs to pass the perception pipeline with recorded evidence.
