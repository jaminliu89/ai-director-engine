"""Perception layer: normalize transcript + deterministic acoustic/text cues.

This layer observes. It does not make cinematic decisions.
"""
from __future__ import annotations
from typing import Any, Dict, List
from analyzer.emotion import analyze_emotion


def build_perception(transcript: Dict[str, Any], source: str) -> Dict[str, Any]:
    segments: List[Dict[str, Any]] = []
    previous_end = 0.0
    for index, raw in enumerate(transcript.get("segments", []), start=1):
        observed = analyze_emotion(raw)
        start = float(raw.get("start", 0.0))
        end = float(raw.get("end", start))
        segments.append({
            "id": raw.get("id") or f"seg-{index}",
            "start": start,
            "end": end,
            "text": raw.get("text", "").strip(),
            "words": raw.get("words") or [],
            "pause_before": round(max(0.0, start - previous_end), 3),
            "observations": {
                "energy": observed["energy"],
                "emphasis": observed["emphasis"],
                "speech_rate": observed["speech_rate"],
                "heuristic_affect": observed["emotion"],
            },
        })
        previous_end = end
    return {
        "schema_version": "1.0",
        "source": source,
        "language": transcript.get("language"),
        "language_probability": transcript.get("language_probability"),
        "segments": segments,
    }
