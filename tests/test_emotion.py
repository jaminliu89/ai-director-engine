import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "prototype"))

from analyzer.emotion import analyze_emotion


def test_high_emphasis_generates_motion():
    segment = {
        "text": "但是这才是真正重要的秘密！",
        "start": 0.0,
        "end": 1.5,
        "words": [{"text": word} for word in ["但是", "这", "才", "是", "真正", "重要", "的", "秘密"]],
    }
    result = analyze_emotion(segment)
    assert result["energy"] > 0.5
    assert result["director"]["caption_motion"] in {"rise", "impact"}
