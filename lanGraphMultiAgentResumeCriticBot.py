from langgraph.graph import StateGraph, END
from typing import TypedDict
import google.generativeai as genai
import pdfplumber
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

llm = genai.GenerativeModel("gemini-1.5-flash")

# Define state schema
class ResumeState(TypedDict):
    resume: str
    grammar_feedback: str
    skills_feedback: str
    format_feedback: str
    final_summary: str

# Agents
def grammar_agent(state):
    resume = state["resume"]
    response = llm.generate_content([
        "You are a grammar reviewer.",
        f"Check grammar in the following resume:\n{resume}"
    ])
    state["grammar_feedback"] = response.text
    return state

def skills_agent(state):
    resume = state["resume"]
    response = llm.generate_content([
        "You are a tech recruiter.",
        f"List missing or outdated skills in this resume:\n{resume}"
    ])
    state["skills_feedback"] = response.text
    return state

def format_agent(state):
    resume = state["resume"]
    response = llm.generate_content([
        "You are a resume formatting expert.",
        f"Give formatting feedback:\n{resume}"
    ])
    state["format_feedback"] = response.text
    return state

def summary_agent(state):
    summary = f"""
🔍 **Grammar Issues**:\n{state['grammar_feedback']}
💼 **Skills Advice**:\n{state['skills_feedback']}
📐 **Formatting Tips**:\n{state['format_feedback']}
"""
    state["final_summary"] = summary
    return state

# Build Graph
graph = StateGraph(ResumeState)

graph.add_node("GrammarAgent", grammar_agent)
graph.add_node("SkillsAgent", skills_agent)
graph.add_node("FormatAgent", format_agent)
graph.add_node("SummaryAgent", summary_agent)

graph.set_entry_point("GrammarAgent")
graph.add_edge("GrammarAgent", "SkillsAgent")
graph.add_edge("SkillsAgent", "FormatAgent")
graph.add_edge("FormatAgent", "SummaryAgent")
graph.add_edge("SummaryAgent", END)

graph_instance = graph.compile()

# PDF Extract
def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

# Run
resume_text = extract_text_from_pdf("sample_resume.pdf")
result = graph_instance.invoke({"resume": resume_text})
print(result["final_summary"])
