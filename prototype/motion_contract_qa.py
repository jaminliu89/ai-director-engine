"""Compatibility gate against motion-runtime-os Motion IR v1 semantics.

Pinned upstream evidence:
- schema blob: 23bb8ef01053e23931d995c7fc5c627e34c54ca6
- validator blob: 40891f6fab40ba38394d9f91960bf5a399be09bd
This is not a fork of the runtime; it is a narrow consumer contract test.
"""

def validate_motion_ir(ir):
    failures=[]
    if ir.get("version") != "1.0": failures.append("version must be 1.0")
    canvas=ir.get("canvas") or {}
    if not isinstance(canvas.get("width"),int) or not isinstance(canvas.get("height"),int): failures.append("canvas dimensions must be integers")
    if not isinstance(canvas.get("fps"),(int,float)) or canvas.get("fps",0) <= 0: failures.append("canvas.fps must be > 0")
    scenes=ir.get("scenes")
    if not isinstance(scenes,list) or not scenes: failures.append("at least one scene is required"); scenes=[]
    seen=set()
    for scene in scenes:
        sid=scene.get("id")
        if not sid: failures.append("scene.id is required")
        if sid in seen: failures.append(f"duplicate scene id {sid}")
        seen.add(sid); duration=scene.get("duration",0)
        if not isinstance(duration,(int,float)) or duration <= 0: failures.append(f"{sid}: duration must be > 0"); continue
        ids=set()
        for layer in scene.get("layers",[]):
            lid=layer.get("id")
            if not lid: failures.append(f"{sid}: layer.id is required")
            if lid in ids: failures.append(f"{sid}: duplicate layer id {lid}")
            ids.add(lid)
            if not (layer.get("start",-1) >= 0 and layer.get("end",0) > layer.get("start",0) and layer.get("end",0) <= duration): failures.append(f"{sid}/{lid}: invalid start/end window")
        for cue in scene.get("subtitle_cues",[]):
            if not cue.get("id") or not str(cue.get("text","")).strip(): failures.append(f"{sid}: subtitle cue requires id/text")
            if not (cue.get("start",-1) >= 0 and cue.get("end",0) > cue.get("start",0) and cue.get("end",0) <= duration): failures.append(f"{sid}/{cue.get('id')}: invalid subtitle window")
        for cue in scene.get("audio_cues",[]):
            if not (cue.get("time",-1) >= 0 and cue.get("time",0) <= duration): failures.append(f"{sid}/{cue.get('id')}: audio cue outside scene")
    return {"status":"FAIL" if failures else "PASS","failures":failures,"upstream_schema_blob":"23bb8ef01053e23931d995c7fc5c627e34c54ca6","upstream_validator_blob":"40891f6fab40ba38394d9f91960bf5a399be09bd"}
