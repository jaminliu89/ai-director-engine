# AI Video Pipeline 2026

## 结论
AI 视频正在从“单模型生成视频”演化成 Agent 驱动的 Production Pipeline：不同工具负责身份、声音、表演、剪辑、动效、渲染与质量验证，上层由 Producer/Director Agent 做语义编排。

## 主要流水线范式

1. 真人 AI Edit：Footage → Transcript → Edit Decision List → captions/B-roll/motion → export。
2. Digital Performer：Script → Voice → Avatar Identity → Gesture/Expression/Body Performance → video。
3. Character Performance：Identity/Appearance 与 Performance 分离，支持 motion reference / lip sync / face or character transfer。
4. Voice Clone：Script → cloned voice → word timestamps → subtitle/audio cues → lip sync/motion。
5. Programmatic Video：Director/Motion spec → Remotion React compositions → deterministic render。
6. Web Motion：Director/Motion spec → HTML/CSS/GSAP/Three → HyperFrames → deterministic render。
7. Agent Editing：自然语言 → EDL/trim/reorder/zoom/B-roll/caption decisions（ChatCut 类）。
8. Hybrid Production：真人/数字人/生成素材/剪辑/程序化动效混合，由 Agent 路由。

## 工具在系统中的正确层级
- Codex / WorkBuddy / Claude Code：Creative Execution Agent，不是 Renderer。
- ChatCut：Edit Engine / Natural-language EDL provider。
- HeyGen 等：Digital Performer / Avatar provider。
- Voice Clone/TTS：Voice provider。
- Remotion：programmatic motion/render provider。
- HyperFrames：HTML-native motion/render provider。
- FFmpeg：media transform / mux / probe substrate。

## 核心架构判断
不要做“工具列表”。稳定资产应该是中间语义：

`Perception → Semantic Director → Director IR → Edit/Motion/Performance intents → Provider adapters`

Director IR 表达为什么以及应该发生什么；Motion IR 表达如何在时间线上执行视觉运动。Provider-specific API 不允许泄漏进 Director IR。

## 研究机会
- Reference Video → frame/timing analysis → Motion Spec / Director IR reverse engineering。
- Audio as Master Clock：word timestamps/pauses/energy 驱动字幕、镜头、motion cue 和节奏。
- Motion Recipe Retrieval：从语义意图检索可复用 motion recipe，而非每次从零 Prompt。
- Human Director Approval：高风险身份/品牌/发布前保留人工审批。
- Outcome Flywheel：发布表现反馈回 Director policy / recipe ranking，而不是直接污染 renderer contracts。
