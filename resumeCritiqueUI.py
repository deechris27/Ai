import pdfplumber
import gradio as gr
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.4)

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)
    

def critique_resume(pdf_file, job_description):
    text = extract_text_from_pdf(pdf_file)

    messages = [
        SystemMessage(content="You are an expert career coach and resume reviewer."),
        HumanMessage(content=f"Here is resume: \n{text}\n\n Analyse the resume against the {job_description} and suggest changes to make it ATS friendly")
    ]

    response = llm(messages)
    return response.content

gr.Interface(
    fn=critique_resume,
    inputs=[gr.File(label="Upload resume (PDF)", file_types=[".pdf"]),
            gr.TextArea(label="Job Description", placeholder="Paste the Job description here")],
    outputs="text",
    title="AI ATS friendly resume critique",
    description="Upload your resume and get AI suggestions to make it ATS friendly"
).launch()