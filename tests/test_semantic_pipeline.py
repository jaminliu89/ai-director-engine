import json
from copy import deepcopy
from pathlib import Path
from jsonschema import validate
from prototype.perception import build_perception
from prototype.semantic_director import direct
from prototype.director_to_motion import compile_director_ir
from prototype.director_intent_qa import validate_director_intent
from prototype.legacy_adapter import to_legacy
from prototype.motion_contract_qa import validate_motion_ir

def fixture_transcript():
    return {"language":"zh","language_probability":0.99,"segments":[{"id":"s1","start":0.0,"end":2.0,"text":"三个月前，我差点把公司关掉。","words":[]},{"id":"s2","start":2.5,"end":4.0,"text":"但是后来事情变了。","words":[]}]}

def test_perception_does_not_make_director_decisions():
    p=build_perception(fixture_transcript(),"fixture.mp4")
    assert "camera_intent" not in p["segments"][0]
    assert "observations" in p["segments"][0]
    assert p["segments"][1]["pause_before"] == 0.5

def test_semantic_director_detects_revelation_and_turn_and_matches_schema():
    d=direct(build_perception(fixture_transcript(),"fixture.mp4"))
    assert d["segments"][0]["narrative_function"] == "revelation"
    assert d["segments"][0]["camera_intent"]["movement"] == "subtle_push_in"
    assert d["segments"][0]["edit_decision"]["cutaway"] == "suppress"
    assert d["segments"][1]["narrative_function"] == "turn"
    assert validate_director_intent(d)["status"] == "PASS"
    schema=json.loads(Path("schemas/director-ir.v1.schema.json").read_text(encoding="utf-8"))
    validate(instance=d,schema=schema)

def test_director_to_motion_is_pure_and_preserves_intent():
    d=direct(build_perception(fixture_transcript(),"fixture.mp4")); before=deepcopy(d); motion=compile_director_ir(d)
    assert d == before
    assert motion["version"] == "1.0"
    assert motion["scenes"][0]["camera"]["movement"] == "subtle_push_in"
    assert motion["scenes"][0]["audio_cues"][0]["type"] == "low_hit"
    assert len(motion["scenes"][0]["subtitle_cues"]) == 2
    assert validate_motion_ir(motion)["status"] == "PASS"

def test_legacy_adapter_is_explicit_and_non_authoritative():
    d=direct(build_perception(fixture_transcript(),"fixture.mp4")); legacy=to_legacy(d)
    assert legacy["schema_version"] == "0.1"
    assert legacy["segments"][0]["director"]["caption_motion"] == "blur-fade-rise"
