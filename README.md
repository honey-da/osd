# {{BlendBot}}  

{{한줄 소개}}  

> **다중 AI 모델 자동 라우팅 및 합성 응답 시스템**  

- 상태: {{**beta**}}
- 라이선스: {{**MIT License**}}
- 주요 기능: {{**모델 라우팅**, **응답 합성(JudgeAI)**, **난이도 분석**, **비용 최적화**}}
  
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
가장 적합한 AI 모델(GPT, Claude, Gemini 등)을 **자동 선택**하거나,  
필요 시 **여러 모델의 응답을 합성**하여 최적의 답을 제공하는 오픈소스 시스템이다.
Streamlit 기반의 웹 인터페이스를 통해 누구나 쉽게 AI 모델을 통합 활용할 수 있다.

BlendBot은 모델 간 편향을 상쇄하고, 
집단지성형 응답 합성을 구현하는 목표를 가진 **AI 앙상블(Multi-LLM Ensemble) 플랫폼**이다.  
또한 하나의 플랫폼 안에서 **GPT, Claude, Gemini 등 다양한 AI 모델을 통합적으로 활용할 수 있도록 설계되어**,  
사용자는 모델별 특성과 장점을 손쉽게 비교·결합하며 **높은 접근성과 편의성**을 동시에 누릴 수 있다.  

---

## 특징

-  **질문 난이도 분석기**  
  → 문장 복잡도, 도메인, 모델 확신도 기반 점수 계산  

-  **모델 라우팅 엔진**  
  → 난이도·도메인별로 GPT / Gemini / Claude 중 최적 모델 선택  

-  **합성 응답(JudgeAI)**  
  → 여러 모델의 응답을 비교·평가하여 가장 일관된 최종 답 생성  

-  **비용·지연 최적화**  
  → 쉬운 질문은 저비용 모델, 어려운 질문은 병렬 앙상블  

-  **확장성 높은 구조**  
  → 새로운 AI 모델 API 추가가 매우 쉬움  

---

##  설치

### 1️ 필수 요구사항
- Python **3.10 이상**
- pip 최신 버전
- 개인 API 키 (OpenAI / Google Gemini / Anthropic Claude)
- (선택) Git 및 가상환경(Virtualenv)

---

### 2️ 저장소 클론
```bash
git clone https://github.com/yourusername/BlendBot.git
cd BlendBot
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
pip install streamlit
pip install openai
pip install anthropic
pip install google-generativeai
pip install scikit-learn
pip install spacy
pip install python-dotenv
pip install requests
```
   
### 5️ 환경변수 설정 (.env 파일 생성)
```ini
#환경변수 설정 (.env 파일 생성)
프로젝트 루트 폴더에 .env 파일을 만들고 다음과 같이 입력한다.
OPENAI_API_KEY=sk-xxxx
ANTHROPIC_API_KEY=sk-xxxx
GOOGLE_API_KEY=xxxx
```
### 6 실행 
```bash
streamlit run app.py
```

---

## 빠른 시작
```bash
git clone https://github.com/yourusername/BlendBot.git
cd BlendBot
pip install -r requirements.txt #필수 패키지 모음
```
```ini
#환경변수 설정 (.env 파일 생성)
프로젝트 루트 폴더에 .env 파일을 만들고 다음과 같이 입력한다.
OPENAI_API_KEY=sk-xxxx
ANTHROPIC_API_KEY=sk-xxxx
GOOGLE_API_KEY=xxxx
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
(절대 공개 저장소에 올리지 말 것)

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
├── app.py                # Streamlit 메인 실행 파일
├── main.py               # (선택) FastAPI 백엔드
├── .env                  # 개인 API 키 저장
├── requirements.txt      # 패키지 목록
├── config.ini            # 라우팅 설정
├── docs/
│   └── BlendBot_ui.png  # 시스템 구조도 / UI 이미지
└── modules/
    ├── analyzer.py       # 질문 난이도 분석 모듈
    ├── router.py         # 모델 선택 엔진
    └── judge.py          # 합성 응답 생성기
```

## 로드맵

| 단계 | 주요 목표 | 세부 내용 |
|------|------------|------------|
| **1️ Prototype 구축** | 기본 구조 완성 | Streamlit UI 구축, GPT·Claude·Gemini API 연동, .env 설정 완료 |
| **2️ Routing Engine 고도화** | 질문 난이도 분석 | `analyzer.py`를 통해 문장 복잡도·도메인 분류 알고리즘 추가 |
| **3️ JudgeAI 응답 합성 구현** | 다중 응답 비교/평가 | 모델별 응답 품질 점수화 및 합성 로직(`judge.py`) 완성 |
| **4️ Config 확장성 추가** | 라우팅 설정 파일화 | `config.ini` 기반 사용자 설정(모드, threshold 등) 적용 |
| **5️ 최적화 및 UI 개선** | Streamlit 대시보드 개선 | 선택된 모델, 처리 시간, 비용 등 시각화 기능 강화 |
| **6️ 멀티모델 평가 리포트 자동화** | 분석 보고 자동 생성 | 응답 품질, 비용 효율성 지표를 JSON/CSV 형태로 자동 저장 |
| **7️ 상용화 및 오픈소스 공개** | 완성 및 배포 | 문서화, MIT License 정리, GitHub Actions 통한 자동 배포 |

---

## 라이선스
본 프로젝트의 코드는 MIT License를 따릅니다.
