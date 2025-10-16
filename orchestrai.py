from typing import Dict, List
import re
import numpy as np
from utils import getenv_float, strip_markdown, Scores, clip01, softmax

def _factuality_heuristic(text: str) -> float:
    t = strip_markdown(text)
    # 숫자/인용/구조 점수
    digits = len(re.findall(r"\d", t))
    refs = len(re.findall(r"\[(?:\d+|MOCK|SIMULATED)", t))
    bullets = len(re.findall(r"(\n-|\n\*|\n\d+\.)", "\n"+t))
    score = 0.4*clip01(digits/10) + 0.3*clip01(refs/3) + 0.3*clip01(bullets/5)
    return clip01(score)

def _coherence_heuristic(text: str) -> float:
    t = strip_markdown(text)
    # 길이/문장수/연결어
    sents = re.split(r"[.!?]\s+", t)
    connectors = len(re.findall(r"\b(따라서|그러나|한편|또한|결론적으로|In conclusion|However|Therefore)\b", t, flags=re.I))
    score = 0.4*clip01(len(t)/800) + 0.3*clip01(len(sents)/8) + 0.3*clip01(connectors/4)
    return clip01(score)

def _style_heuristic(text: str) -> float:
    t = strip_markdown(text)
    # 과한 반복/오탈자 패널티
    repeat = 1.0 if re.search(r"(ㅋㅋ|ㅎㅎ|~~~~|!!!!!){2,}", t) else 0.0
    typos  = len(re.findall(r"[A-Za-z]{25,}", t))
    base = 0.8 - 0.3*repeat - 0.1*clip01(typos/3)
    return clip01(base)

def evaluate(resp: str) -> Scores:
    return Scores(
        factuality=_factuality_heuristic(resp),
        coherence=_coherence_heuristic(resp),
        style=_style_heuristic(resp),
    )

def weighted_merge(responses: Dict[str, str], scores: Dict[str, Scores]) -> str:
    wf = getenv_float("W_FACTUALITY", 0.5)
    wc = getenv_float("W_COHERENCE", 0.3)
    ws = getenv_float("W_STYLE", 0.2)

    names = list(responses.keys())
    raw = np.array([wf*scores[n].factuality + wc*scores[n].coherence + ws*scores[n].style for n in names], dtype=float)
    weights = softmax(raw)

    # 핵심 문장 추출(아주 단순한 버전)
    merged = []
    for i, n in enumerate(names):
        text = strip_markdown(responses[n])
        lines = [ln.strip() for ln in re.split(r"[\n\.]", text) if ln.strip()]
        keep = max(2, int(5*weights[i]))
        merged.extend(lines[:keep])

    # 중복 제거
    seen = set()
    uniq = []
    for ln in merged:
        key = re.sub(r"\s+", " ", ln.lower())
        if key not in seen:
            seen.add(key)
            uniq.append(ln)

    # 최종 합성
    return " ".join(uniq[:12])

def orchestrate(responses: Dict[str, str]) -> Dict:
    scores = {name: evaluate(txt) for name, txt in responses.items()}
    final = weighted_merge(responses, scores)
    return {
        "scores": {k: vars(v) for k, v in scores.items()},
        "final": final
    }
    그리워져 slrkekdkfjweiods

