from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)


def chat_over_summary(query: str, summary: dict) -> str:
    system_prompt = f"""You are a helpful agent who answers questions using the following resume {summary}
                         answer clearly concisely based only on the resume summary."""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]

    response = llm(messages)
    return response.content
