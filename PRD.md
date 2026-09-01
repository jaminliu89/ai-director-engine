# AI Director Engine PRD v1.1 — Director Brain Boundary

## 产品定位
AI Director Engine 是 AI 视频生产系统的“导演大脑”。它不负责绑定某个渲染器，也不负责直接把逐字稿拼成素材视频；它负责把视频/音频/脚本中的内容、节奏和叙事意义转成机器可执行的导演决策。

## 核心问题
旧式流水线通常只能做到：转录 → 关键词/情绪 → 素材/动效。真正缺的是中间导演层：为什么这里需要停顿、推镜、删 B-roll、强调一句话、压低音乐、加入图表、保持 A-roll、切黑场，或者什么都不做？

MoneyPrinterTurbo 一类自动视频系统进一步证明了这个边界：媒体搜索、TTS、字幕和 FFmpeg 合成可以高度自动化，但这些能力属于媒体基础设施，不能替代导演语义。

## 核心流水线
`Input → Perception → Semantic Director → Beat Graph / Director IR → Visual Intent → downstream Director Timeline → Execution Providers → QA`

其中：
- `ai-director-engine` 负责 why / what；
- `creator-os-video-agent` 负责将 Director IR/Beat Graph 编译成持久化 `Director Timeline` 并进行 Provider Routing；
- `motion-runtime-os` / Remotion / HyperFrames / FFmpeg / ChatCut / stock / image-video / avatar providers 负责 bounded execution。

## 当前范围
1. 保留现有 local-first video/audio/transcript perception prototype。
2. Director IR v1 作为稳定语义契约。
3. narrative function / attention / pacing / edit / camera / motion / caption / audio / performance / visual intent 分离建模。
4. 输出足够明确的 beat-level 决策，使下游可以无猜测地生成 Director Timeline。
5. 建立 `Director IR → Motion IR` provider-neutral compiler seam，对接独立 `motion-runtime-os`。
6. 保留真实 MP4/MOV acceptance gate；没有真实执行证据不得声称端到端完成。

## Visual Intent 最低要求
对关键 beat，Director IR 应尽可能明确：
- narrative function；
- attention target；
- pacing / hold / pause；
- 是否保留 A-roll；
- 是否需要 B-roll / still / generated visual / MG / kinetic text / chart / screen/UI / digital human / black frame / none；
- visual purpose，而不仅是关键词；
- motion/caption emphasis；
- audio/music/SFX/silence intent；
- 允许的 fallback 和语义不可丢失项。

Director Engine 不需要知道最终由 Pexels、Remotion、HyperFrames、HeyGen、D-ID 或其他 provider 执行。

## 输出
主输出：`Director IR v1` / Beat semantics。

可派生输出：Edit Decisions、Motion IR、Voice/Performance/Visual intents。

下游 durable contract：由 `creator-os-video-agent/schemas/director-timeline.v1.schema.json` 承接，不在本仓库复制第二份真相源。

## 与 MoneyPrinterTurbo 的关系
MoneyPrinterTurbo 不是本引擎的竞争性替代架构，而是下游 Media Infrastructure Benchmark。

允许下游借鉴它的：
- stock adapter；
- TTS/timestamp；
- subtitle/transcription；
- FFmpeg assembly；
- batch/retry；
- encoding controls。

AI Director Engine 不吸收“keyword → stock footage”作为核心导演逻辑。

## MVP 验收
- 真实 talking-head 视频能产出带时间戳的 perception 数据；
- Director IR 非空且通过 schema；
- 关键 segment 具有 narrative function + attention/pacing + visual purpose；
- 至少存在一个明确的“不要换素材/保持 A-roll/none/hold”决策能力，而不是强制每句加视觉；
- Director→Motion Compiler 产生 provider-neutral Motion IR；
- 编译器不修改输入 IR；
- 下游可将同一 Director IR 确定性编译为 Director Timeline；
- Motion Runtime 可独立消费输出，不要求 Director Engine 引入 Remotion/HyperFrames API。

## 非目标
当前不做 Blender/Unreal、完整 NLE、Avatar 引擎、SaaS billing/social publishing、stock crawler、FFmpeg 编码器或 MoneyPrinterTurbo fork。它们属于 Provider/Adapter/Infrastructure seam。
