# Knowledge Motion Engine — 知识动效引擎

## 产品定义
输入逐字稿或解说视频，系统先理解每句话在解释什么，再自动决定该用什么视觉表达，并把任务路由给不同执行引擎，最终输出一条真正有解释力的成片。

目标不是“给字幕加动画”，而是解决知识讲解视频最难的一件事：**抽象内容如何被视觉化。**

## 核心闭环

`Transcript / Talking-head Video`
→ `Semantic Understanding`
→ `Knowledge Unit Extraction`
→ `Visual Intent Planning`
→ `Motion IR`
→ `Visual Router`
→ `{Remotion | HyperFrames | ChatCut | B-roll}`
→ `Timeline Assembly`
→ `Render / Editable Project`
→ `Visual QA`
→ `Final MP4`

## 一、知识单元 Knowledge Unit
逐字稿不是按句号机械切分，而是识别每一段在承担什么认知功能。

首版类型：
- claim：观点/结论
- definition：概念定义
- contrast：对比/转折
- sequence：步骤/流程
- timeline：时间演变
- cause_effect：因果
- quantity：数字/比例/规模
- hierarchy：层级/分类
- example：案例
- analogy：类比
- quote：引用/金句
- question：问题
- revelation：揭示/反转
- evidence：证据/数据
- emotion：情绪节点
- transition：章节转场

每个 Knowledge Unit 至少输出：
- text
- start/end（有视频时）
- semantic_type
- entities
- key_terms
- narrative_role
- importance
- complexity
- visualizability
- confidence

## 二、视觉意图 Visual Intent
Director 不直接写 Remotion/HTML/ChatCut 指令，而先产生供应商无关的视觉意图。

首版 visual_intent：
- caption_emphasis：关键词/句子强化
- kinetic_typography：动态排版
- title_card：章节卡
- lower_third：人物/概念标识
- diagram：关系图/流程图
- timeline：时间轴
- chart：数据图表
- counter：数字增长/倒计时
- comparison：左右/前后对比
- map：地图/位置
- icon_sequence：图标序列
- object_explainer：对象拆解
- broll_real：真实 B-roll
- broll_generated：生成式视觉素材
- screenshot/web：网页/截图说明
- quote_card：金句卡
- transition：转场
- hold：刻意留白/维持原画面

原则：视觉必须服务理解，不以“每句话都动”为目标。

## 三、Visual Router — 视觉路由器

### Remotion
职责：可控、稳定、参数化、可复用的程序化视觉。
优先处理：
- 字幕系统
- 标题/章节卡
- Lower Third
- 时间轴
- 图表
- 数字动画
- 对比布局
- 品牌化组件
- 多轨合成
- 已知模板的确定性动画

### HyperFrames by HeyGen
职责：Agent 原生、HTML/CSS/JS 驱动的高自由度解释型动效。
优先处理：
- 独特 MG
- 概念关系动画
- 空间化排版
- GSAP / Three.js / Lottie / CSS 动画
- 没有现成模板、但能用网页技术视觉化的解释场景
- 透明 Overlay / MOV / WebM / PNG sequence 输出后交给总时间线

### ChatCut
职责：编辑器与时间线层，以及更高层的视频编辑/素材编排能力。
优先处理：
- 原始 talking-head 剪辑
- 多轨时间线
- B-roll 插入与替换
- Motion Graphics 轨
- 生成图片/视频/音乐/旁白等外部素材
- 可编辑项目交付
- 最终人工调整入口

注意：ChatCut 作为 provider adapter；其 API / Agent Plugin 能力必须通过真实可调用接口验证，未验证的能力不得写成已完成 runtime。

### B-roll Router
职责：决定什么时候“不该做 MG”，而应该让观众看到真实对象。
来源：
- 用户素材库
- 已授权素材
- 网页截图/产品 UI
- 图片生成
- 视频生成
- 未来合法的 stock/provider adapter

## 四、Router 决策示例

“过去十年，算力增长了几百倍。”
- semantic_type: quantity + timeline
- 首选：Remotion chart/timeline
- 若需要独特视觉隐喻：HyperFrames

“这就是 Transformer 的核心原理。”
- semantic_type: definition + hierarchy
- 首选：HyperFrames diagram / object explainer
- 备选：Remotion 组件化流程图

“OpenAI 发布 ChatGPT 后，整个行业开始改变。”
- semantic_type: timeline + event
- 首选：真实产品截图 / B-roll + Remotion timeline

“但真正改变的不是模型，而是人与机器的关系。”
- semantic_type: contrast + revelation
- 首选：留白 → kinetic typography → HyperFrames concept motion

## 五、Motion IR vNext 最小需求
Motion IR 必须允许一个场景声明：
- scene_id
- time_range
- source_knowledge_unit
- visual_intent
- provider_preference
- fallback_provider
- density
- prominence
- assets[]
- layers[]
- transition_in/out
- audio_cues
- acceptance_tags

Provider 不得重新解释故事语义；只能执行视觉意图。

## 六、密度控制
知识视频失败的常见原因不是“不够炫”，而是视觉过载。

首版规则：
- 普通陈述：原画面 + 字幕即可
- 关键观点：1 个主要视觉动作
- 复杂概念：进入完整解释场景
- 连续高密度动效后必须安排视觉恢复区
- 同屏核心注意点原则上 <= 3
- B-roll/MG/字幕不能同时争夺第一视觉层级

## 七、最终用户体验

### 输入 A：只有逐字稿
1. 粘贴逐字稿
2. 系统拆 Knowledge Units
3. 自动生成 Visual Plan
4. 需要素材的节点生成/检索素材任务
5. Remotion / HyperFrames 生成视觉片段
6. ChatCut / Timeline assembler 编排
7. 输出预览与可编辑工程

### 输入 B：已有口播视频
1. 自动转录 + 对齐
2. 切分知识单元
3. 判断保留人物 / 覆盖 B-roll / 全屏 MG / 留白
4. 自动创建多轨视觉计划
5. 执行与合成
6. 用户只处理少数低置信度决策

## 八、MVP 验收 — 不再用 CI 代替画面
第一版必须使用一段 30–60 秒知识讲解逐字稿，输出一条用户可直接观看的 MP4，并至少出现：
1. 关键词/标题型 Remotion 动效；
2. 一个真正解释概念的 HyperFrames MG 场景；
3. 一个真实或生成 B-roll 节点；
4. 至少一段主动留白/原画面，证明系统具备克制；
5. 字幕与所有视觉节点时间同步；
6. 输出逐字稿 → Knowledge Unit → Visual Intent → Provider Route 的可审计 JSON；
7. 成片必须在仓库 Release/Artifact 或可直接打开的位置提供，不允许只报告 PASS。

## 九、当前不做
- Blender / Unreal
- 完整 NLE 重造
- 电影级 3D
- Avatar 作为核心
- 每一句都强行动效
- Provider-specific 语义逻辑

## 十、最终产品边界
本系统的核心资产不是 Remotion、HyperFrames 或 ChatCut，而是：

**Transcript → Knowledge Understanding → Visual Intent → Routing → Quality Loop**

Provider 可以被替换，知识视觉化决策层必须长期独立。