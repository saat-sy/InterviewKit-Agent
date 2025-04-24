from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():
    # Groq Model
    # llm = ChatGroq(
    #     model="llama-3.3-70b-versatile",
    # )
    # Google Model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
    )
    return llm
