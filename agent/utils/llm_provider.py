from dotenv import load_dotenv
from langchain_groq import ChatGroq

def get_llm():
    load_dotenv()
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
    )
    return llm