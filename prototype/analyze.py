"""MP4 -> WAV -> Whisper -> Perception -> Semantic Director -> Director IR v1."""
from __future__ import annotations
import argparse, json, tempfile
from pathlib import Path
from analyzer.audio import extract_audio
from analyzer.subtitle import transcribe
from perception import build_perception
from semantic_director import direct
from director_to_motion import compile_director_ir


def analyze(video_path: str, output_path: str = "director-ir.json", model: str = "base", language: str | None = None):
    source = Path(video_path).expanduser().resolve()
    if not source.exists(): raise FileNotFoundError(f"Input video not found: {source}")
    with tempfile.TemporaryDirectory(prefix="ai-director-") as tmp:
        wav = Path(tmp) / "audio.wav"
        extract_audio(str(source), str(wav))
        transcript = transcribe(str(wav), model_size=model, language=language)
    perception = build_perception(transcript, str(source))
    result = direct(perception)
    target = Path(output_path).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result, target


def main():
    parser = argparse.ArgumentParser(description="Analyze talking-head video into Director IR v1.")
    parser.add_argument("video", help="Path to MP4/MOV input")
    parser.add_argument("-o", "--output", default="director-ir.json")
    parser.add_argument("--model", default="base")
    parser.add_argument("--language", default=None)
    parser.add_argument("--motion-output", default=None, help="Optionally compile Director IR to Motion IR JSON")
    args = parser.parse_args()
    result, target = analyze(args.video, args.output, args.model, args.language)
    print(f"Director IR written: {target}")
    if args.motion_output:
        motion = compile_director_ir(result)
        motion_target = Path(args.motion_output).expanduser().resolve()
        motion_target.parent.mkdir(parents=True, exist_ok=True)
        motion_target.write_text(json.dumps(motion, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Motion IR written: {motion_target}")
    print(f"Segments: {len(result['segments'])}; language: {result.get('language')}")

if __name__ == "__main__": main()
