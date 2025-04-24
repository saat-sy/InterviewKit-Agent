from langchain_groq import ChatGroq

def get_llm():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
    )
    return llm