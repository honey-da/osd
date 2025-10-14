# {{BlendBot}}  

> **{{다중 AI 모델 자동 라우팅 및 합성 응답 시스템}}**  

- 상태: {{**alpha**}}
- 라이선스: {{**MIT License**}}
- 주요 기능: {{**모델 라우팅**, **응답 합성(JudgeAI)**, **난이도 분석**, **지연 최적화**}}
  
---
 
## 목차
- [소개](#소개)
- [특징](#특징)
- [설치](#설치)
- [빠른 시작](#빠른-시작)
- [사용법](#사용법)
- [설정](#설정)
- [프로젝트 구조](#프로젝트-구조)
- [로드맵](#로드맵)
- [라이선스](#라이선스)
  
---

## 소개
**BlendBot**는 사용자의 질문을 분석하여  
가장 적합한 AI 모델(GPT-4o, Claude 3.5, Gemini 1.5 Pro, Stable Diffusion XL, Runway Gen-2, Whisper)을 **자동 선택**하거나,  
필요 시 **여러 모델의 응답을 합성**하여 최적의 답을 제공하는 AI 앙상블 시스템이다.
Streamlit 기반의 웹 인터페이스를 통해 누구나 쉽게 AI 모델을 통합 활용할 수 있다.

BlendBot은 모델 간 편향을 상쇄하고, 
집단지성형 응답 합성을 구현하는 목표를 가진 **AI 앙상블 플랫폼**이다.  
또한 하나의 플랫폼 안에서 **GPT, Claude, Gemini 등 다양한 AI 모델을 통합적으로 활용할 수 있도록 설계되어**,  
사용자는 모델별 특성과 장점을 손쉽게 비교·결합하며 **높은 접근성과 편의성**을 동시에 누릴 수 있다.  

---

## 특징

-  **질문 난이도 분석기**  
  → 문장 복잡도, 도메인, 모델 확신도 기반 점수 계산  

-  **모델 라우팅 엔진**  
  → 난이도·도메인별로 GPT / Gemini / Claude / Stable Diffusion / Runway 등 중 최적 모델 선택  

-  **합성 응답(JudgeAI)**  
  → 여러 모델의 응답을 비교·평가하여 가장 일관된 최종 답 생성  

-  **지연 최적화**  
  → 쉬운 질문은 단일 모델, 어려운 질문은 병렬 앙상블  

-  **확장성 높은 구조**  
  → 새로운 AI 모델 API 추가가 매우 쉬움  

---

##  설치

### 1️ 필수 요구사항
- Python **3.10 이상**
- pip 최신 버전
- 개인 API 키 (OOpenAI / Google Gemini / Anthropic Claude / StableDiffusion / Runway / Whisper)
  #이 중(API키) 몇개만 가지고 있어도 관계없다.
- Git 및 가상환경(Virtualenv)

---

### 2️ 저장소 클론
```bash
git clone https://github.com/honey-da/osd.git
cd osd
```   
### 3️ 가상환경 생성 및 활성화
```bash
#windows
python -m venv venv
venv\Scripts\activate

#Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4️ 필수 패키지 설치
```bash
# --- 기본 프레임워크 ---
pip install streamlit
pip install python-dotenv
pip install requests

# --- LLM 통합 ---
pip install openai                # GPT-4o, Whisper(STT/TTS)
pip install anthropic             # Claude 3.5
pip install google-generativeai   # Gemini 1.5 Pro

# --- 이미지 / 비디오 모델 통합 ---
pip install diffusers             # Stable Diffusion XL
pip install transformers          # 텍스트→이미지 프롬프트 처리
pip install torch                 # Diffusers 실행용
pip install accelerate            # GPU 최적화
pip install pillow                # 이미지 입출력
pip install opencv-python         # 비디오 처리 (Runway Gen-2 보조용)
pip install imageio               # 이미지·비디오 입출력 유틸
pip install moviepy               # 비디오 편집/렌더링

# --- 음성 입출력 ---
pip install whisper               # 음성 인식(STT)
pip install gTTS                  # 텍스트→음성(TTS)
pip install pydub                 # 오디오 파일 변환

# --- 분석 및 라우팅 ---
pip install scikit-learn          # 난이도 분석, 텍스트 분류
pip install spacy                 # 자연어 전처리
pip install numpy
pip install pandas

# --- 선택: 캐싱 / 속도 개선 ---
pip install redis
```
   
### 5️ 환경변수 설정 (.env 파일 생성)
```ini
#환경변수 설정 (.env 파일 생성)
프로젝트 루트 폴더에 .env 파일을 만들고 다음과 같이 입력한다.
OPENAI_API_KEY=sk-xxxx
ANTHROPIC_API_KEY=sk-xxxx
GOOGLE_API_KEY=xxxx
STABLE_DIFFUSION_KEY=xxxx
RUNWAY_API_KEY=xxxx
WHISPER_API_KEY=xxxx
#API키 6개를 다쓸필요x(지닌 것만 작성하면, 작성된 AI모델로만 실행됨)
```
### 6 실행 
```bash
streamlit run app.py
```

---

## 빠른 시작
```bash
git clone https://github.com/honey-da/osd.git
cd osd
pip install -r requirements.txt #필수 패키지 모음
```
```ini
#환경변수 설정 (.env 파일 생성)
프로젝트 루트 폴더에 .env 파일을 만들고 다음과 같이 입력한다.
OPENAI_API_KEY=sk-xxxx
ANTHROPIC_API_KEY=sk-xxxx
GOOGLE_API_KEY=xxxx
STABLE_DIFFUSION_KEY=xxxx
RUNWAY_API_KEY=xxxx
WHISPER_API_KEY=xxxx
```
```bash
streamlit run app.py
```
➡ 실행 후 브라우저에서 자동으로 열리는
http://localhost:8501 에 접속하면 바로 사용 가능 

 ---

## 사용법

1️ 질문 입력

예: “라플라스 방정식의 물리적 의미를 설명해줘”

2️ 시스템 동작

난이도 분석 → 라우팅 → 모델 선택/병렬 호출

JudgeAI가 여러 응답을 비교 후 합성 결과 출력

3️ 결과 확인

 “선택된 모델: GPT-4o + Claude 3.5”
 “최종 합성 응답: 논리적·사실적 균형 유지된 답변 표시”

4️ 종료 방법
터미널에서 Ctrl + C 입력 후 종료
가상환경 비활성화 → deactivate

---

## 설정
.env

개인 API 키를 저장하는 환경변수 파일

config.ini (선택)
```ini
[router]
mode = hybrid
threshold = 0.6
```

---

## 프로젝트 구조
```bash
BlendBot/
│
├── app.py                # Streamlit UI
├── main.py               # FastAPI 백엔드 (선택)
├── .env                  # API 키
├── requirements.txt
├── config.ini
│
├── modules/
│   ├── analyzer.py       # 질문 난이도 분석
│   ├── router.py         # 모델 선택 엔진
│   ├── judge.py          # 응답 합성 로직
│   ├── image_router.py   # 이미지 모델 연동 (Stable Diffusion 등)
│   ├── video_router.py   # 비디오 생성 모델 (Runway 등)
│   ├── audio_router.py   # 음성 인식/합성 (Whisper 등)
│
├── services/
│   ├── openai_api.py
│   ├── anthropic_api.py
│   ├── google_api.py
│   ├── stable_diffusion_api.py
│   ├── runway_api.py
│   └── whisper_api.py
│
└── judge/
    └── judge_ai.py       # 멀티모델 응답 평가기

```

## 로드맵

| 단계 | 주요 목표 | 세부 내용 |
|------|------------|------------|
| **1️ Prototype 구축** | 기본 구조 완성 | Streamlit UI 구축, GPT·Claude·Gemini 등 API 연동, .env 설정 완료 |
| **2️ Routing Engine 고도화** | 질문 난이도 분석 | `analyzer.py`를 통해 문장 복잡도·도메인 분류 알고리즘 추가 |
| **3️ JudgeAI 응답 합성 구현** | 다중 응답 비교/평가 | 모델별 응답 품질 점수화 및 합성 로직(`judge.py`) 완성 |
| **4 이미지 생성 기능 통합** | 텍스트→이미지 생성 | Stable Diffusion XL 연동, LLM 프롬프트 정제 및 CLIP 기반 결과 평가 추가 |
| **5 비디오 생성 기능 추가** | 텍스트→비디오 생성 | Runway Gen-2 연동, 시나리오 요약→비디오 스크립트 변환→API 호출 자동화 |
| **6 음성 입출력 기능 확장** | STT / TTS 통합 | Whisper 기반 음성→텍스트 및 텍스트→음성 지원, 대화형 입출력 완성 |
| **7 Config 확장성 추가** | 라우팅 설정 파일화 | `config.ini` 기반 사용자 설정(모드, threshold 등) 적용 |
| **8 최적화 및 UI 개선** | Streamlit 대시보드 개선 | 선택된 모델, 처리 시간, 비용 등 시각화 기능 강화 |

---

## 라이선스
본 프로젝트의 코드는 MIT License를 따릅니다.
