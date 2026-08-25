# AI Director Engine

AI 视频导演大脑：理解内容、推理导演意图、输出 provider-neutral `Director IR`，再把编辑/声音/表演/视觉/动效任务路由给下游执行系统。

## 核心边界

`AI Director Engine = Understand → Reason → Decide`

`Motion Runtime OS = Compile Motion → Render → QA`

本仓库不绑定 Remotion/HyperFrames。两者属于独立 `motion-runtime-os` 的执行 Provider。

## Revival Architecture

```text
Video / Audio / Script
        ↓
Perception
        ↓
Semantic Director
        ↓
Director IR v1
        ↓
 ┌──────┼─────────┬──────────┬──────────┐
 Edit  Voice   Performance  Visual    Motion
        ↓
Director→Motion Compiler
        ↓
motion-runtime-os
        ↓
Remotion / HyperFrames
```

## 当前资产
- `prototype/analyzer/`：旧的 audio/subtitle/emotion perception 原型，保留并逐步升级。
- `schemas/director-ir.v1.schema.json`：新的稳定导演语义契约。
- `prototype/director_to_motion.py`：第一版 Director IR → Motion IR provider-neutral bridge。
- `examples/director-ir.sample.json`：Director IR 示例。
- `docs/AI_VIDEO_PIPELINE_2026.md`：AI 视频流水线调研沉淀。
- `docs/VIDEO_PRODUCTION_OS_ARCHITECTURE.md`：系统分层与仓库边界。
- `docs/REVIVAL_DECISION.md`：为什么选择 Revival 而不是 Rewrite。

## 当前执行状态
Revival 的契约/桥接层已经落库；真实 talking-head MP4/MOV → perception → Director IR 的 acceptance 仍未通过，因此不得宣称端到端完成。

## 原则
1. Director IR 表达“为什么/应该发生什么”，不表达具体 Provider API。
2. Motion IR 表达 timed motion execution，由 `motion-runtime-os` 管理。
3. 真实执行证据优先于文档声称。
4. 不因未来 Avatar/Blender/Unreal/完整 NLE 扩张当前 MVP。
5. 旧代码不因重构冲动而删除；先迁移、验证，再决定淘汰。
