"""
Phase 1 entry point.

Future usage:
python analyze.py input.mp4

Output:
director.json
"""

import json
import sys


def analyze(video_path):
    return {
        "source": video_path,
        "segments": []
    }


if __name__ == "__main__":
    result = analyze(sys.argv[1] if len(sys.argv) > 1 else "demo.mp4")
    print(json.dumps(result, ensure_ascii=False, indent=2))
