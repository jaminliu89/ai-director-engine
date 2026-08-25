import copy

from prototype.director_to_motion import compile_director_ir


def test_compile_director_ir_maps_semantics_without_mutating_input():
    source = {
        "schema_version": "1.0",
        "source": {"type": "video", "duration": 7.0, "language": "zh-CN"},
        "segments": [{
            "id": "s1",
            "start": 0.0,
            "end": 3.0,
            "transcript": "三个月前，我差点把公司关掉。",
            "attention_target": "差点把公司关掉",
            "director_intent": "force audience refocus",
            "camera_intent": {"movement": "subtle-push-in"},
            "motion_intent": {"enter": "blur-fade-rise", "exit": "fade"},
            "caption_intent": {"emphasis": "关掉"},
            "audio_intent": {"cue": "low-hit", "at": 2.4, "gain_db": -2},
        }],
    }
    before = copy.deepcopy(source)

    result = compile_director_ir(source)

    assert source == before
    scene = result["scenes"][0]
    assert scene["duration"] == 3.0
    assert scene["camera"]["movement"] == "subtle-push-in"
    assert scene["layers"][0]["content"] == "差点把公司关掉"
    assert scene["layers"][0]["enter"]["type"] == "blur-fade-rise"
    assert scene["subtitle_cues"][0]["emphasis"] == "关掉"
    assert scene["audio_cues"][0]["type"] == "low-hit"
