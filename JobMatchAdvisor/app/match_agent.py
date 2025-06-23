from langchain_anthropic import ChatAnthropic
from langchain.schema import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0.3)

def compare_resume_to_job(resume_text: str, job_text: str) -> str:
    system_msg = """You are an expert career advisor. Compare a resume and job description. Return:
                    - Match Score (out of 100)
                    - Key matching skills
                    - Skill gaps
                    - Suggestion to improve resume
                    Respond in clean bullet points."""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=f"Resume: \n{resume_text}\n\nJob description: \n {job_text}")
    ]

    response = llm(messages)
    return response.content