"""Minimal Director IR v1 -> Motion IR bridge.

This is intentionally provider-neutral. It translates director semantics into
Motion Runtime intent primitives without importing Remotion/HyperFrames APIs.
"""
from __future__ import annotations

from typing import Any, Dict


def compile_director_ir(director_ir: Dict[str, Any]) -> Dict[str, Any]:
    segments = director_ir.get("segments", [])
    duration = max((float(s.get("end", 0)) for s in segments), default=0.0)
    layers = []
    subtitle_cues = []
    audio_cues = []
    camera_movements = []

    for segment in segments:
        start = float(segment.get("start", 0))
        end = float(segment.get("end", start))
        caption = segment.get("caption_intent") or {}
        motion = segment.get("motion_intent") or {}
        camera = segment.get("camera_intent") or {}
        audio = segment.get("audio_intent") or {}
        transcript = segment.get("transcript") or ""

        movement = camera.get("movement", "none")
        if movement != "none":
            camera_movements.append(movement)

        if transcript:
            subtitle_cues.append({
                "id": f"subtitle-{segment['id']}",
                "start": start,
                "end": end,
                "text": transcript,
                "emphasis": caption.get("emphasis"),
            })

        attention = segment.get("attention_target")
        if attention:
            layers.append({
                "id": f"attention-{segment['id']}",
                "type": "text",
                "content": attention,
                "start": start,
                "end": end,
                "z": 20,
                "enter": {
                    "type": motion.get("enter", "fade"),
                    "duration": motion.get("enter_duration", 0.35),
                },
                "exit": {
                    "type": motion.get("exit", "fade"),
                    "duration": motion.get("exit_duration", 0.25),
                },
            })

        if audio.get("cue"):
            audio_cues.append({
                "id": f"audio-{segment['id']}",
                "at": float(audio.get("at", start)),
                "type": audio["cue"],
                "gain_db": audio.get("gain_db", 0),
            })

    return {
        "schema_version": "1.0",
        "canvas": {"width": 1920, "height": 1080, "fps": 30, "background": "#000000"},
        "scenes": [{
            "id": "director-scene-1",
            "duration": duration,
            "camera": {"movement": camera_movements[0] if camera_movements else "none"},
            "layers": layers,
            "subtitle_cues": subtitle_cues,
            "audio_cues": audio_cues,
            "director_metadata": {
                "source": "ai-director-engine",
                "director_ir_version": director_ir.get("schema_version", "unknown"),
            },
        }],
    }
