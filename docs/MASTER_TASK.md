# MASTER TASK — AI Director Engine

## MT-002 — MVP Plumbing
Status: **DONE / ACCEPTED**

Verified chain:
`real MP4 → FFmpeg → faster-whisper → Perception → Semantic Director → Director IR v1 → Motion IR v1 → {Remotion | HyperFrames} → MP4`

Evidence:
- Upstream Real Media Acceptance `32926244006`: PASS.
- Remotion Director Bridge `32926421757`: PASS, artifact `9591739910`.
- HyperFrames Real Media Acceptance `32926669798`: PASS, artifact `9591815442`.
- Cross-provider semantic QA `32926669799`: PASS.

## MT-003 — Director Intelligence Quality Loop
Status: **IN PROGRESS**

### Objective
Move from executable plumbing to measurable directing quality while keeping Director IR v1 stable.

### Master Gate
`benchmark media/text → Perception → Semantic Director → Director IR → neutral vs directed render → machine QA + blinded preference evidence → quality decision`

### Workstream A — Benchmark corpus
- [x] Establish `benchmarks/director-intelligence-v1.json` covering revelation, turn/contrast, question, emphasis and exposition in Chinese/English.
- [x] Add fail-closed semantic benchmark test.
- [ ] Add licensed/owned real-media clips exhibiting revelation, turn, question, emphasis, emotional transition and pacing change.
- [ ] Pin source provenance and hashes.

### Workstream B — Quality evaluation
- [x] Define `docs/DIRECTOR_QUALITY_SPEC.md`.
- [x] Separate Q0 contract, Q1 semantic benchmark, Q2 render survival and Q3 human preference.
- [ ] Produce neutral baseline and directed variant for each real benchmark clip.
- [ ] Record blinded A/B preference and failure tags.
- [ ] Require preference lift before claiming Director Intelligence acceptance.

### Workstream C — Semantic Director v2
- [ ] Replace fragile keyword-only classification with evidence aggregation over transcript semantics + pause + emphasis + energy + affect transition.
- [ ] Preserve deterministic fallback and Director IR v1 compatibility.
- [ ] Add confidence calibration and abstention/neutral behavior for weak evidence.
- [ ] Prevent cinematic over-decoration through restraint rules.

### Workstream D — Decision routers
- [ ] Define provider-neutral Edit Router contract.
- [ ] Define B-roll/Visual Router contract.
- [ ] Define Audio Router contract.
- [ ] Keep Voice and Avatar/Performance as optional adapters after core quality gate.
- [ ] Routers consume Director IR; they may not redefine narrative intent.

### Workstream E — Acceptance
- [ ] Q1 semantic benchmark green in CI.
- [ ] Q2 directed intent survives Remotion and HyperFrames execution.
- [ ] Q3 blinded preference evidence recorded.
- [ ] Update Acceptance, Progress, Decision Log and Agent Handoff with actual evidence.

## Definition of Done for MT-003
MT-003 is not DONE because code compiles or videos render. It closes only when real benchmark media demonstrates measurable preference lift over a neutral baseline while contract and cross-provider gates remain green.

## Constraints
- Repository evidence is Source of Truth.
- No provider-specific API leakage into Director IR.
- No Blender/Unreal/full NLE on this critical path.
- No synthetic-only evidence may satisfy real-media quality acceptance.
- No claim of human-equivalent directing without preference evidence.
