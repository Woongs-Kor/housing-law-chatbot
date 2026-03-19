import streamlit as st
from rag import load_rag_chain, get_answer

st.set_page_config(
    page_title="전세사기 예방 법률 AI 챗봇", page_icon="⚖️", layout="centered"
)

st.title("⚖️ 주택임대차 법률 AI 챗봇")
st.caption("주택임대차보호법 기반 전세사기 예방 AI 챗봇")


# RAG 체인 로드 (최초 1회)
@st.cache_resource
def init_chain():
    return load_rag_chain("주택임대차보호법.pdf")


with st.spinner("법률 문서를 불러오는 중..."):
    chain = init_chain()

# 대화 히스토리 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 주택임대차보호법 기반 법률 AI 챗봇입니다.\n\n전세 계약, 보증금, 대항력, 확정일자 등 궁금한 점을 물어보세요! 😊",
        }
    ]

# 대화 히스토리 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
if prompt := st.chat_input("질문을 입력하세요. 예) 확정일자가 뭐야?"):
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 답변 생성
    with st.chat_message("assistant"):
        with st.spinner("답변을 생성하는 중..."):
            answer = get_answer(chain, prompt)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
