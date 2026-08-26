"""Semantic Director v2: deterministic evidence aggregation with restraint.

Provider-neutral and Director IR v1 compatible. This is deliberately not an LLM:
it provides an auditable fallback and a benchmarkable baseline for later semantic models.
"""
from __future__ import annotations
from typing import Any, Dict

REVELATION_TERMS=("秘密","真相","其实","差点","原来","真正的问题","secret","truth","almost","actually","real problem")
CONTRAST_TERMS=("但是","可是","不过","然而","却","but","however","yet")
QUESTION_TERMS=("为什么","怎么","为何","?","？","why","how","what if")


def _evidence(text:str, obs:Dict[str,Any], pause:float)->Dict[str,float]:
    lower=text.lower(); emphasis=float(obs.get("emphasis",0)); energy=float(obs.get("energy",.5)); affect=str(obs.get("heuristic_affect","neutral"))
    scores={"revelation":0.0,"turn":0.0,"question":0.0,"emphasis":0.0,"exposition":.32}
    scores["revelation"] += .62 if any(t in lower for t in REVELATION_TERMS) else 0
    scores["turn"] += .62 if any(t in lower for t in CONTRAST_TERMS) else 0
    scores["question"] += .72 if any(t in lower for t in QUESTION_TERMS) else 0
    scores["emphasis"] += min(.65, emphasis*.75)
    if pause >= .35:
        scores["revelation"] += .08; scores["turn"] += .06; scores["question"] += .04
    if energy >= .72: scores["emphasis"] += .12
    if affect in {"intense","surprised","sad"}: scores["revelation"] += .05
    return scores


def _classify(text:str, obs:Dict[str,Any], pause:float):
    scores=_evidence(text,obs,pause); ranked=sorted(scores.items(),key=lambda x:x[1],reverse=True); function,score=ranked[0]; margin=score-ranked[1][1]
    # Restraint/abstention: weak or ambiguous evidence becomes exposition rather than decoration.
    if function != "exposition" and (score < .48 or margin < .10): function="exposition"; score=max(scores["exposition"],.45)
    confidence=max(.5,min(.95,.5+score*.4+max(0,margin)*.2))
    return function,confidence,scores


def _intent(function:str)->str:
    return {"revelation":"force_audience_refocus","turn":"signal_narrative_turn","question":"open_attention_loop","emphasis":"amplify_key_point","exposition":"preserve_clarity"}[function]


def direct(perception:Dict[str,Any])->Dict[str,Any]:
    directed=[]; segments=perception.get("segments",[]); duration=max((float(s.get("end",0)) for s in segments),default=0.0)
    previous_affect=None
    for segment in segments:
        obs=segment["observations"]; text=segment["text"]; energy=float(obs.get("energy",.5)); pause=float(segment.get("pause_before",0)); function,confidence,scores=_classify(text,obs,pause); affect=obs.get("heuristic_affect","neutral")
        affect_changed=previous_affect is not None and affect != previous_affect
        attention=text if function in {"revelation","turn","question","emphasis"} else None
        camera="subtle-push-in" if function=="revelation" else "none"
        enter="blur-fade-rise" if function in {"revelation","emphasis"} else "fade"
        audio_cue="low_hit" if function=="revelation" and confidence>=.7 else None
        pacing_mode="decelerate" if function=="revelation" else "hold" if function in {"turn","question"} else "neutral"
        directed.append({"id":str(segment["id"]),"start":segment["start"],"end":segment["end"],"transcript":text,"narrative_function":function,
          "emotional_transition":{"from":previous_affect,"to":affect,"changed":affect_changed},"attention_target":attention,"director_intent":_intent(function),
          "pacing":{"mode":pacing_mode,"hold_delta":.35 if function=="revelation" else 0.0,"energy":energy},
          "shot_decision":{"framing":"medium_close_up","hold_subject":function=="revelation"},"edit_decision":{"cutaway":"suppress" if function=="revelation" else "allowed"},
          "camera_intent":{"movement":camera},"motion_intent":{"enter":enter,"exit":"fade","intensity":energy if function!="exposition" else min(energy,.35)},
          "caption_intent":{"emphasis":attention,"priority":"high" if attention else "normal"},"audio_intent":{"cue":audio_cue,"at":segment["start"],"gain_db":-2 if audio_cue else 0},
          "broll_intent":{"policy":"suppress" if function=="revelation" else "optional"},"performance_intent":{"preserve_pause":pause>=.35},"confidence":round(confidence,3),
          "rationale":f"evidence-v2:{function}; scores={{{', '.join(f'{k}:{v:.2f}' for k,v in scores.items())}}}; pause={pause:.2f}; affect_changed={affect_changed}"})
        previous_affect=affect
    return {"schema_version":"1.0","source":{"type":"video","path":perception.get("source"),"duration":duration,"language":perception.get("language") or "unknown"},"segments":directed}
