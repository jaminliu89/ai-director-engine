"""MP4 -> WAV -> Whisper -> Perception -> Semantic Director -> Director IR v1."""
from __future__ import annotations
import argparse, json, tempfile
from pathlib import Path
from prototype.analyzer.audio import extract_audio
from prototype.analyzer.subtitle import transcribe
from prototype.perception import build_perception
from prototype.semantic_director import direct
from prototype.director_to_motion import compile_director_ir
from prototype.director_intent_qa import validate_director_intent


def analyze(video_path: str, output_path: str = "director-ir.json", model: str = "base", language: str | None = None):
    source = Path(video_path).expanduser().resolve()
    if not source.exists(): raise FileNotFoundError(f"Input video not found: {source}")
    with tempfile.TemporaryDirectory(prefix="ai-director-") as tmp:
        wav = Path(tmp) / "audio.wav"
        extract_audio(str(source), str(wav))
        transcript = transcribe(str(wav), model_size=model, language=language)
    perception = build_perception(transcript, str(source))
    result = direct(perception)
    qa = validate_director_intent(result)
    if qa["status"] != "PASS": raise ValueError("Director Intent QA failed: " + "; ".join(qa["errors"]))
    target = Path(output_path).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result, target, qa


def main():
    parser = argparse.ArgumentParser(description="Analyze talking-head video into Director IR v1.")
    parser.add_argument("video", help="Path to MP4/MOV input")
    parser.add_argument("-o", "--output", default="director-ir.json")
    parser.add_argument("--model", default="base")
    parser.add_argument("--language", default=None)
    parser.add_argument("--motion-output", default=None, help="Optionally compile Director IR to Motion IR JSON")
    parser.add_argument("--qa-output", default=None, help="Optionally write Director Intent QA JSON")
    args = parser.parse_args()
    result, target, qa = analyze(args.video, args.output, args.model, args.language)
    print(f"Director IR written: {target}")
    if args.qa_output:
        qa_target=Path(args.qa_output).expanduser().resolve(); qa_target.parent.mkdir(parents=True,exist_ok=True); qa_target.write_text(json.dumps(qa,ensure_ascii=False,indent=2),encoding="utf-8")
    if args.motion_output:
        motion = compile_director_ir(result)
        motion_target = Path(args.motion_output).expanduser().resolve()
        motion_target.parent.mkdir(parents=True, exist_ok=True)
        motion_target.write_text(json.dumps(motion, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Motion IR written: {motion_target}")
    print(f"Segments: {len(result['segments'])}; language: {result.get('source',{}).get('language')}; qa={qa['status']}")

if __name__ == "__main__": main()
