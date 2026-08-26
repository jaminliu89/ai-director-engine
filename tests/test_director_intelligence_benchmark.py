import json
from pathlib import Path
from prototype.semantic_director import direct


def _perception(case):
    return {
        "source": "benchmark.mp4",
        "language": "mixed",
        "segments": [{
            "id": case["id"], "start": 0.0, "end": 2.0, "text": case["text"],
            "pause_before": case.get("pause_before", 0.0),
            "observations": {
                "energy": case.get("energy", 0.5),
                "emphasis": case.get("emphasis", 0.1),
                "heuristic_affect": case.get("affect", "neutral")
            }
        }]
    }


def test_director_intelligence_v1_benchmark():
    benchmark = json.loads(Path("benchmarks/director-intelligence-v1.json").read_text(encoding="utf-8"))
    failures = []
    for case in benchmark["cases"]:
        segment = direct(_perception(case))["segments"][0]
        if segment["narrative_function"] != case["expected"]:
            failures.append((case["id"], case["expected"], segment["narrative_function"]))
    assert not failures, f"Director intelligence benchmark regressions: {failures}"
