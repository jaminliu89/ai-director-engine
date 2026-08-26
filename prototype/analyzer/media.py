"""Deterministic source-media metadata probe using ffprobe."""
from __future__ import annotations
import json, shutil, subprocess
from pathlib import Path


def probe_video(video_path: str):
    if shutil.which("ffprobe") is None:
        raise RuntimeError("ffprobe is required but was not found in PATH")
    source=Path(video_path)
    if not source.exists(): raise FileNotFoundError(f"Input video not found: {source}")
    command=["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height,r_frame_rate:format=duration","-of","json",str(source)]
    raw=subprocess.run(command,check=True,capture_output=True,text=True).stdout
    data=json.loads(raw); stream=(data.get("streams") or [{}])[0]; duration=float((data.get("format") or {}).get("duration") or 0)
    rate=str(stream.get("r_frame_rate") or "0/1"); num,den=(rate.split("/",1)+["1"])[:2]
    fps=float(num)/float(den) if float(den) else 0
    return {"duration":round(duration,3),"width":int(stream.get("width") or 0),"height":int(stream.get("height") or 0),"fps":round(fps,3)}
