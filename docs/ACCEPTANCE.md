# ACCEPTANCE — AI Director Engine Revival

## A-001 Real Human Media → Director IR → Motion IR

Status: **PASS**

### Source
- Fixture: Public-domain U.S. Army participant interview registered in `docs/REAL_MEDIA_FIXTURE.md`
- Input SHA-256: `a93869b5712154b990909a3bfb14e2636a5cce59174ecd64854abdbda302fad0`
- Media observed by ffprobe: 1080×1920 H.264 video + AAC audio, duration ~28.733333s, size 34,404,050 bytes

### Execution evidence
- GitHub Actions workflow: `Real Media Acceptance`
- Successful run: `32926244006` / run #7
- Pipeline: download+hash → FFmpeg extraction → faster-whisper tiny.en → Perception → Semantic Director → Director Intent QA → Director IR v1 JSON Schema → Director→Motion compiler → Motion Runtime consumer-contract QA

### Result
- Transcript/director segments: 4
- Director Intent QA: PASS, errors `[]`, warnings `[]`
- Director IR JSON Schema: PASS
- Motion Runtime consumer contract: PASS
- Motion IR canvas: 1080×1920 @ 30fps
- Motion IR duration: 28.733s
- Source footage preserved as `source-video` layer pointing to `assets/real-media-interview.mp4`
- Subtitle cues: 4

## A-002 Exact Accepted Motion IR → Two Real Runtime Providers

Status: **PASS**

### Remotion
- Downstream repository: `jaminliu89/motion-runtime-os`
- Workflow: `Director Bridge Acceptance`
- Run: `32926421757` / run #1 — SUCCESS
- Same pinned source SHA + exact accepted Motion IR
- Motion IR validation PASS
- TypeScript PASS
- Final Remotion render PASS
- Final MP4 video+audio media probe PASS
- Artifact: `real-media-director-render`, ID `9591739910`

### HyperFrames
- Downstream workflow: `Real Media HyperFrames Acceptance`
- Run: `32926669798` / run #2 — SUCCESS
- Same pinned source SHA + exact accepted Motion IR
- Strict HyperFrames render PASS
- First attempt exposed a real strict-lint contract issue for audible timed video; compiler was fixed with explicit embedded-audio declaration rather than weakening strict mode
- Final MP4 video+audio media probe PASS
- Artifact: `real-media-hyperframes-render`, ID `9591815442`

### Semantic provider evidence
- `motion-runtime-os` Provider Independence run `32926669799` / run #9 — SUCCESS
- Includes Remotion + HyperFrames render, both media probes, provider comparison, Cross-provider Semantic QA and semantic evidence gate.

## Accepted end-to-end chain

`real human MP4 → FFmpeg → faster-whisper → Perception → Semantic Director → Director IR v1 → Director Intent QA → Motion IR v1 → {Remotion | HyperFrames} → MP4`

This is now real-media execution evidence, not a synthetic/JSON-only demonstration.

## Important limitation
The deterministic Semantic Director classified all four segments in this interview as exposition and made conservative decisions. Therefore this acceptance proves real-media plumbing, schema integrity, timing, provider-neutral execution and media preservation; it does **not** prove high-level creative-director quality. Director intelligence quality is the next benchmark phase.
