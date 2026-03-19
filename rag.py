import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


def load_rag_chain(pdf_path: str):
    """PDF를 로드하고 RAG 체인을 반환합니다."""

    # 1. PDF 로드
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # 2. 텍스트 청크 분할
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_documents(documents)

    # 3. 임베딩 & 벡터DB 저장
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    # 4. LLM 설정
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )

    # 5. 프롬프트 설정
    prompt = PromptTemplate.from_template("""
당신은 주택임대차보호법 전문 법률 AI 어시스턴트입니다.
아래 법률 문서를 참고하여 질문에 친절하고 이해하기 쉽게 답변해주세요.
법률 용어는 쉽게 풀어서 설명하고, 관련 법 조항이 있으면 함께 언급해주세요.
문서에 없는 내용은 "해당 내용은 문서에서 찾을 수 없습니다"라고 말해주세요.

[참고 문서]
{context}

[질문]
{question}

[답변]
""")

    # 6. RAG 체인 구성 (LangChain 1.0 방식)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


def get_answer(chain, question: str) -> str:
    """질문에 대한 답변을 반환합니다."""
    try:
        return chain.invoke(question)
    except Exception as e:
        return f"답변 생성 중 오류가 발생했습니다: {str(e)}"