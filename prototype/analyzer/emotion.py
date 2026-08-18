"""Deterministic MVP rhythm/emphasis analysis.

This deliberately avoids pretending we have a trained emotion model. Phase 1.1
uses timing, punctuation and keyword cues to produce useful director metadata.
"""
import re

EMPHASIS_TERMS = {
    "但是", "可是", "突然", "终于", "失败", "成功", "最", "真正", "为什么",
    "秘密", "重要", "never", "but", "finally", "failed", "failure", "success",
    "why", "secret", "important", "really",
}


def _keyword_score(text: str) -> float:
    lower = text.lower()
    hits = sum(1 for term in EMPHASIS_TERMS if term in lower)
    punctuation = len(re.findall(r"[!?！？]", text))
    return min(1.0, hits * 0.25 + punctuation * 0.2)


def analyze_emotion(segment):
    text = segment.get("text", "")
    start = float(segment.get("start", 0.0))
    end = float(segment.get("end", start))
    duration = max(0.15, end - start)
    words = segment.get("words") or []
    token_count = max(1, len(words) if words else len(text.replace(" ", "")))
    rate = token_count / duration
    emphasis = _keyword_score(text)
    energy = min(1.0, max(0.1, 0.22 + min(rate / 8.0, 0.55) + emphasis * 0.35))

    if emphasis >= 0.45 or energy >= 0.8:
        emotion = "intense"
    elif duration >= 3.5 and energy < 0.55:
        emotion = "reflective"
    else:
        emotion = "neutral"

    motion = "impact" if energy >= 0.78 else "rise" if energy >= 0.5 else "fade"
    return {
        "emotion": emotion,
        "energy": round(energy, 3),
        "emphasis": round(emphasis, 3),
        "speech_rate": round(rate, 3),
        "director": {
            "caption_motion": motion,
            "scale": 1.22 if motion == "impact" else 1.08 if motion == "rise" else 1.0,
        },
    }
