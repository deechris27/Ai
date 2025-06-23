import pdfplumber
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv
import tempfile
import re
import ast

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)


# agents.py

def extract_summary_from_text(text):
    system_prompt = """You are a resume summarizer. Extract these fields:
- Name
- Years of Experience
- Technologies (as list)
- Recent Projects
- Education

Respond in valid JSON, no markdown, no text outside the JSON."""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=text)
    ]

    result = llm(messages)
    cleaned = re.sub(r"```json|```", "", result.content.strip())

    try:
        return ast.literal_eval(cleaned)
    except Exception as e:
        print("[ERROR] Failed to parse Gemini output:", e)
        return {"error": "Gemini output invalid"}
