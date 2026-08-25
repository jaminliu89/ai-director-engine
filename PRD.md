# AI Director Engine PRD v1.0 — Revival

## 产品定位
AI Director Engine 是 AI 视频生产系统的“导演大脑”。它不负责绑定某个渲染器，而负责把视频/音频/脚本中的内容、节奏和叙事意义转成机器可执行的导演决策。

## 核心问题
旧式流水线通常只能做到：转录 → 关键词/情绪 → 动效。真正缺的是中间导演层：为什么这里需要停顿、推镜、删 B-roll、强调一句话、压低音乐或加入动效？

## 核心流水线
`Input → Perception → Semantic Director → Director IR → Edit/Performance/Voice/Visual/Motion Routers → Execution → QA`

## 当前 Revival 范围
1. 保留现有 local-first video/audio/transcript perception prototype。
2. 新增 Director IR v1，取代 v0.1 作为未来稳定契约。
3. 将 narrative function / attention / pacing / edit / camera / motion / caption / audio / performance intent 分离建模。
4. 建立 `Director IR → Motion IR` provider-neutral compiler seam，对接独立的 `motion-runtime-os`。
5. 保留真实 MP4/MOV acceptance gate；没有真实执行证据不得声称端到端完成。

## 用户输入
- 本地视频文件
- 音频
- 文本脚本
- 后续：结构化创作素材/故事图/品牌约束

## 输出
主输出：`Director IR v1`。
可派生输出：Edit Decisions、Motion IR、Voice/Performance/Visual intents。

## MVP 验收
- 真实 talking-head 视频能产出带时间戳的 perception 数据；
- Director IR 非空且通过 schema；
- 至少一个 segment 具有 director_intent + attention/pacing/camera/motion/caption/audio 中的有效决策；
- Director→Motion Compiler 产生 provider-neutral Motion IR；
- 编译器不修改输入 IR；
- Motion Runtime 可独立消费输出，不要求 Director Engine 引入 Remotion/HyperFrames API。

## 非目标
当前不做 Blender/Unreal、完整 NLE、Avatar 引擎、SaaS billing/social publishing。它们只作为未来 Provider/Adapter seam。
