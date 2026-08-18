# Architecture v0.1

```
Input Video
    |
    v
Audio Analyzer
    |
    v
Subtitle Intelligence
    |
    v
Director JSON
    |
    v
Motion Renderer
    |
    v
Output MP4
```

## Design Principle

导演决策层与渲染层分离。

未来可以接入不同执行引擎：

- HyperFrames
- Remotion
- Blender
- Unreal Engine

当前 MVP 只实现最小可运行链路。
