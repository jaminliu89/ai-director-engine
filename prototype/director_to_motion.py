"""Director IR v1 -> Motion IR bridge, aligned to motion-runtime-os schema."""
from __future__ import annotations
from typing import Any, Dict


def compile_director_ir(director_ir: Dict[str, Any]) -> Dict[str, Any]:
    segments=director_ir.get("segments",[])
    source=director_ir.get("source") or {}
    duration=max(float(source.get("duration") or 0),max((float(s.get("end",0)) for s in segments),default=.001))
    width=int(source.get("width") or 1920); height=int(source.get("height") or 1080); fps=float(source.get("fps") or 30)
    layers=[]; subtitles=[]; audio=[]; cameras=[]
    if source.get("asset_ref"):
        layers.append({"id":"source-video","type":"video","asset_ref":source["asset_ref"],"start":0.0,"end":duration,"z":-100})
    for s in segments:
        start=float(s.get("start",0)); end=float(s.get("end",start)); motion=s.get("motion_intent") or {}; camera=s.get("camera_intent") or {}; a=s.get("audio_intent") or {}; text=s.get("transcript") or ""
        movement=camera.get("movement","none")
        if movement != "none": cameras.append(movement)
        if text: subtitles.append({"id":f"subtitle-{s['id']}","start":start,"end":end,"text":text})
        attention=s.get("attention_target")
        if attention: layers.append({"id":f"attention-{s['id']}","type":"text","content":attention,"start":start,"end":end,"z":20,"enter":{"type":motion.get("enter","fade"),"duration":motion.get("enter_duration",.35)},"exit":{"type":motion.get("exit","fade"),"duration":motion.get("exit_duration",.25)}})
        if a.get("cue"): audio.append({"id":f"audio-{s['id']}","time":float(a.get("at",start)),"type":a["cue"]})
    return {"version":"1.0","canvas":{"width":width,"height":height,"fps":fps,"background":"#000000"},"scenes":[{"id":"director-scene-1","duration":max(duration,.001),"camera":{"movement":cameras[0] if cameras else "none"},"layers":layers,"subtitle_cues":subtitles,"audio_cues":audio}]}
