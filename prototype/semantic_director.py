"""Semantic Director v1.

Turns perception observations into provider-neutral cinematic intent. The first
implementation is deterministic and intentionally conservative; later LLM or
multimodal directors must preserve the same Director IR contract.
"""
from __future__ import annotations
from typing import Any, Dict

REVELATION_TERMS = ("秘密", "真相", "其实", "差点", "原来", "secret", "truth", "almost")
CONTRAST_TERMS = ("但是", "可是", "不过", "然而", "but", "however")
QUESTION_TERMS = ("为什么", "怎么", "?", "？", "why", "how")


def _narrative_function(text: str, emphasis: float) -> str:
    lower = text.lower()
    if any(term in lower for term in REVELATION_TERMS): return "revelation"
    if any(term in lower for term in CONTRAST_TERMS): return "turn"
    if any(term in lower for term in QUESTION_TERMS): return "question"
    if emphasis >= 0.5: return "emphasis"
    return "exposition"


def direct(perception: Dict[str, Any]) -> Dict[str, Any]:
    directed = []
    for segment in perception.get("segments", []):
        obs = segment["observations"]
        text = segment["text"]
        energy = float(obs["energy"])
        emphasis = float(obs["emphasis"])
        function = _narrative_function(text, emphasis)
        attention = text if function in {"revelation", "turn", "question", "emphasis"} else None
        camera = "subtle_push_in" if function == "revelation" else "none"
        enter = "blur-fade-rise" if function in {"revelation", "emphasis"} else "fade"
        audio_cue = "low_hit" if function == "revelation" else None
        directed.append({
            "id": segment["id"], "start": segment["start"], "end": segment["end"],
            "transcript": text,
            "narrative_function": function,
            "emotional_transition": {"to": obs["heuristic_affect"]},
            "attention_target": attention,
            "pacing": {"energy": energy, "hold_after": 0.35 if function == "revelation" else 0.0},
            "shot_intent": {"framing": "medium_close_up", "hold_subject": function == "revelation"},
            "edit_intent": {"cutaway": "suppress" if function == "revelation" else "allowed"},
            "camera_intent": {"movement": camera},
            "motion_intent": {"enter": enter, "exit": "fade", "intensity": energy},
            "caption_intent": {"emphasis": attention, "priority": "high" if attention else "normal"},
            "audio_intent": {"cue": audio_cue, "at": segment["start"], "gain_db": -2 if audio_cue else 0},
            "broll_intent": {"policy": "suppress" if function == "revelation" else "optional"},
            "performance_intent": {"preserve_pause": segment.get("pause_before", 0) >= 0.35},
            "confidence": 0.72 if function != "exposition" else 0.6,
            "rationale": f"deterministic-v1:{function}; energy={energy:.3f}; emphasis={emphasis:.3f}",
        })
    return {
        "schema_version": "1.0",
        "source": perception.get("source"),
        "language": perception.get("language"),
        "segments": directed,
    }
