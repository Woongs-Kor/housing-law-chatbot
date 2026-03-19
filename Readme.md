# ⚖️ 주택임대차 법률 AI 챗봇

전세사기 예방을 위한 주택임대차보호법 기반 RAG AI 챗봇입니다.

<br>

## 📌 프로젝트 개요

전세사기 피해가 사회적 문제로 대두되면서, 일반인이 쉽게 법률 정보에 접근할 수 있도록 AI 챗봇을 개발했습니다.
주택임대차보호법 PDF를 기반으로 RAG(Retrieval-Augmented Generation) 파이프라인을 구축하여, 사용자의 질문에 관련 법 조항을 근거로 답변을 생성합니다.

<br>

## 🛠 기술 스택

| 분류 | 기술 |
|------|------|
| LLM | Gemini 2.5 Flash |
| Embedding | Gemini text-embedding-004 |
| RAG Framework | LangChain 1.0+ |
| Vector DB | ChromaDB |
| UI | Streamlit |
| 배포 | Docker, Oracle Cloud |

<br>

## 🏗 아키텍처

```
PDF 문서 (주택임대차보호법)
    ↓
텍스트 추출 및 청크 분할
    ↓
Gemini 임베딩 → ChromaDB 저장
    ↓
사용자 질문 입력
    ↓
유사 청크 검색 (Top-K)
    ↓
Gemini 2.5 Flash → 답변 생성
    ↓
Streamlit UI 출력
```

<br>

## ⚙️ 설치 및 실행

### 1. 레포지토리 클론
```bash
git clone https://github.com/your-username/housing-law-chatbot.git
cd housing-law-chatbot
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정
```bash
cp .env.example .env
# .env 파일을 열어서 Gemini API 키 입력
```

### 4. PDF 파일 추가
`주택임대차보호법.pdf` 파일을 프로젝트 루트에 위치시킵니다.
[국가법령정보센터](https://www.law.go.kr)에서 다운로드 가능합니다.

### 5. 실행
```bash
streamlit run app.py
```

<br>

## 💬 사용 예시

```
Q: 확정일자가 뭐야?
Q: 전입신고는 언제까지 해야 해?
Q: 전세보증금 반환보증보험이 뭐야?
Q: 집이 경매로 넘어가면 보증금 돌려받을 수 있어?
Q: 묵시적 갱신이 뭐야?
```

<br>

## 📁 프로젝트 구조

```
housing-law-chatbot/
├── app.py                  # Streamlit UI
├── rag.py                  # RAG 파이프라인
├── requirements.txt        # 패키지 목록
├── .env.example            # 환경변수 예시
└── .dockerignore
```

<br>

## 🔑 API 키 발급

Gemini API 키는 [Google AI Studio](https://aistudio.google.com)에서 무료로 발급받을 수 있습니다.

<br>

## ⚠️ 주의사항

- `.env` 파일은 절대 GitHub에 올리지 마세요.
- 본 챗봇은 법률 참고용으로만 사용하세요. 실제 법률 문제는 전문가와 상담하세요.