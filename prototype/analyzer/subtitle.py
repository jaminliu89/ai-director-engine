"""Local speech-to-text adapter using faster-whisper."""


def transcribe(audio_path: str, model_size: str = "base", language: str | None = None):
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError(
            "faster-whisper is not installed. Run: pip install -r requirements.txt"
        ) from exc

    model = WhisperModel(model_size, device="auto", compute_type="int8")
    segments, info = model.transcribe(
        audio_path,
        language=language,
        vad_filter=True,
        word_timestamps=True,
    )

    result = []
    for index, segment in enumerate(segments):
        text = segment.text.strip()
        if not text:
            continue
        words = []
        for word in segment.words or []:
            words.append({
                "text": word.word.strip(),
                "start": round(float(word.start), 3),
                "end": round(float(word.end), 3),
                "probability": round(float(word.probability), 4),
            })
        result.append({
            "id": index,
            "text": text,
            "start": round(float(segment.start), 3),
            "end": round(float(segment.end), 3),
            "words": words,
        })

    return {
        "language": getattr(info, "language", language or "unknown"),
        "language_probability": round(float(getattr(info, "language_probability", 0.0)), 4),
        "segments": result,
    }


def build_subtitle_segments(transcript):
    """Compatibility adapter for earlier prototype callers."""
    return transcript.get("segments", transcript)
