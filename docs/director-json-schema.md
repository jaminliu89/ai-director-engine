# Director JSON Schema v0.1 — LEGACY

> Legacy reference only. New development must target `schemas/director-ir.v1.schema.json`.

旧字段：

```json
{
  "scene": "",
  "start": 0,
  "end": 0,
  "emotion": "",
  "energy": 0,
  "visual_action": "",
  "caption_style": ""
}
```

## 为什么升级
v0.1 能描述浅层标签，但无法表达完整导演推理链，例如 narrative function、emotional transition、attention target、pacing、shot/edit/camera/motion/caption/audio/performance intents。

## Migration
当前采取 additive migration：保留旧 schema 和 prototype 历史，不删除；新 Semantic Director 输出 Director IR v1。只有真实媒体 acceptance 和兼容策略验证后，才决定是否正式淘汰 v0.1。
