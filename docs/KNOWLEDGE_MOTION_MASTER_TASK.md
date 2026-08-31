# MASTER TASK — Knowledge Motion Engine

## KM-001 — Transcript → Visual Motion MVP
Status: **IN PROGRESS**

## Product Gate
一段 30–60 秒知识讲解逐字稿必须自动变成一条可直接观看的成片，而不是 JSON demo。

## Required chain
`transcript/video → knowledge units → visual intents → provider routing → {Remotion|HyperFrames|ChatCut|B-roll} → assembly → visual QA → MP4`

## Workstream A — Knowledge Parser
- [ ] transcript segmentation
- [ ] semantic type classification
- [ ] entities/key terms
- [ ] importance/complexity/visualizability scores
- [ ] confidence + abstain

## Workstream B — Visual Planner
- [ ] semantic type → visual intent mapping
- [ ] density/restraint rules
- [ ] fullscreen vs overlay vs b-roll decision
- [ ] visual hierarchy
- [ ] auditable Visual Plan JSON

## Workstream C — Provider Router
- [ ] Remotion adapter contract
- [ ] HyperFrames adapter contract
- [ ] ChatCut adapter capability probe/contract
- [ ] B-roll adapter contract
- [ ] fallback and failure behavior
- [ ] provider may execute, not reinterpret semantics

## Workstream D — Motion Runtime
- [ ] Remotion: kinetic title/caption + chart/timeline primitive
- [ ] HyperFrames: one real semantic explainer scene
- [ ] transparent-overlay path where appropriate
- [ ] assemble provider outputs onto one master timeline

## Workstream E — B-roll
- [ ] real/generated asset request schema
- [ ] material choice rules: B-roll vs MG
- [ ] placement/crop/duration/transition contract
- [ ] provenance field

## Workstream F — Visible Acceptance
- [ ] 30–60 sec knowledge script fixture
- [ ] Remotion visible motion scene
- [ ] HyperFrames visible explainer scene
- [ ] B-roll scene
- [ ] intentional hold/rest scene
- [ ] subtitles aligned
- [ ] final MP4 uploaded as visible evidence
- [ ] contact sheet / keyframes uploaded
- [ ] no “PASS” unless user-visible result exists

## Definition of Done
KM-001 is DONE only when the user can open one final MP4 and visually verify all four visual modes: Remotion motion, HyperFrames explainer motion, B-roll, and intentional restraint.

Code/schema/tests without this visible artifact are infrastructure progress only.