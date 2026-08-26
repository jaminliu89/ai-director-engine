"""Director Intent QA: fail closed on structurally contradictory or unsafe timing decisions."""

def validate_director_intent(ir):
    errors=[]; warnings=[]; last_end=0.0
    for s in ir.get("segments",[]):
        sid=str(s.get("id","?")); start=float(s.get("start",0)); end=float(s.get("end",start))
        if end <= start: errors.append(f"{sid}: end must be > start")
        if start < last_end: warnings.append(f"{sid}: overlaps previous segment")
        if not s.get("narrative_function"): errors.append(f"{sid}: missing narrative_function")
        if not s.get("director_intent"): errors.append(f"{sid}: missing director_intent")
        if not s.get("rationale"): errors.append(f"{sid}: missing rationale")
        if s.get("narrative_function") == "revelation":
            if (s.get("edit_decision") or {}).get("cutaway") != "suppress": warnings.append(f"{sid}: revelation should normally suppress cutaway")
            if not s.get("attention_target"): warnings.append(f"{sid}: revelation has no attention target")
        confidence=float(s.get("confidence",0))
        if confidence < .5: warnings.append(f"{sid}: low confidence {confidence}")
        last_end=max(last_end,end)
    return {"status":"FAIL" if errors else "PASS","errors":errors,"warnings":warnings}
