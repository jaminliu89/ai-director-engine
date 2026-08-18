"""Audio extraction utilities for Phase 1.1."""
from pathlib import Path
import shutil
import subprocess


def extract_audio(video_path: str, output_path: str) -> str:
    """Extract 16 kHz mono WAV audio with ffmpeg."""
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg is required but was not found in PATH")

    source = Path(video_path)
    if not source.exists():
        raise FileNotFoundError(f"Input video not found: {source}")

    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "ffmpeg", "-y", "-i", str(source),
        "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
        str(target),
    ]
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    return str(target)
