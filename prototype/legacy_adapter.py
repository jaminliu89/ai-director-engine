"""Explicit Director IR v1 -> legacy Director JSON 0.1 compatibility adapter.

New code must not depend on this shape. It exists only for old consumers during migration.
"""

def to_legacy(director_ir):
    segments = []
    for s in director_ir.get("segments", []):
        energy = float((s.get("pacing") or {}).get("energy", 0.5))
        motion = (s.get("motion_intent") or {}).get("enter", "fade")
        segments.append({
            "id": s.get("id"), "start": s.get("start"), "end": s.get("end"),
            "text": s.get("transcript", ""),
            "emotion": (s.get("emotional_transition") or {}).get("to", "neutral"),
            "energy": energy,
            "director": {"caption_motion": motion, "scale": 1.22 if energy >= .78 else 1.08 if energy >= .5 else 1.0},
        })
    return {"schema_version":"0.1","source":director_ir.get("source"),"language":director_ir.get("language"),"segments":segments}
