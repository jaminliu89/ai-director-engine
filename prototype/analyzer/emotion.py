"""
Emotion and energy analysis interface.

Future implementation will connect audio/text models.
"""


def analyze_emotion(segment):
    return {
        "emotion": "neutral",
        "energy": 0.5,
        "source": segment
    }
