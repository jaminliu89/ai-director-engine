# ACCEPTANCE — AI Director Engine Revival

## A-001 Real Human Media → Director IR → Motion IR

Status: **PASS (upstream director/contract layer)**

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

### Important limitation
The deterministic Semantic Director classified all four segments in this interview as exposition and made conservative decisions. This acceptance proves real-media plumbing, schema integrity, timing and cross-repository contract compatibility; it does **not** prove high-level creative-director quality.

### Downstream gate
A-002 remains open until `motion-runtime-os` renders this exact accepted Motion IR with the pinned source footage and the final MP4 passes media-stream verification. Remotion and HyperFrames provider evidence are recorded downstream rather than fabricated here.
