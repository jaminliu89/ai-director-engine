"""Phase 1.1: MP4 -> WAV -> Whisper -> director.json."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import tempfile

from analyzer.audio import extract_audio
from analyzer.subtitle import transcribe
from analyzer.emotion import analyze_emotion


def analyze(video_path: str, output_path: str = "director.json", model: str = "base", language: str | None = None):
    source = Path(video_path).expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(f"Input video not found: {source}")

    with tempfile.TemporaryDirectory(prefix="ai-director-") as tmp:
        wav = Path(tmp) / "audio.wav"
        extract_audio(str(source), str(wav))
        transcript = transcribe(str(wav), model_size=model, language=language)

    directed_segments = []
    for segment in transcript["segments"]:
        directed_segments.append({**segment, **analyze_emotion(segment)})

    result = {
        "schema_version": "0.1",
        "source": str(source),
        "language": transcript["language"],
        "language_probability": transcript["language_probability"],
        "segments": directed_segments,
    }

    target = Path(output_path).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result, target


def main():
    parser = argparse.ArgumentParser(description="Analyze a talking-head video into Director JSON.")
    parser.add_argument("video", help="Path to MP4/MOV input")
    parser.add_argument("-o", "--output", default="director.json")
    parser.add_argument("--model", default="base", help="faster-whisper model size")
    parser.add_argument("--language", default=None, help="Optional language code, e.g. zh/en")
    args = parser.parse_args()

    result, target = analyze(args.video, args.output, args.model, args.language)
    print(f"Director JSON written: {target}")
    print(f"Segments: {len(result['segments'])}; language: {result['language']}")


if __name__ == "__main__":
    main()
