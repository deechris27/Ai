# Retrieve Augment Generate. We make the LLM to query a specific knowledge base/DB 
# to get a more context specific output
# Example: chatbot for a company like "Lufthansa airlines". The end users would want 
# data related to their booking with ticket, Id, availability etc and not some regular prompt output



import os
import glob
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI

load_dotenv(override=True)

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

openai = OpenAI()

context = {}

employees = glob.glob("knowledge/employees/*")

for employee in employees:
    filename = os.path.basename(employee) # Iterate through all the employees and get their last and first name
    name = os.path.splitext(filename)[0]
    doc = ""
    with open(employee, "r", encoding="utf-8") as f: 
      doc = f.read()
    context[name] = doc  # read the file named after the employee and store it with their name as key in context object

system_prompt = "You're an assistant for Odin LLC company. You answer questions about this company info, employees with relevant data and not any general data from web."


def get_employee_info(message):
   relevant_context = []
   for context_title, context_details in context.items():
      if context_title.lower().split(' ')[0] in message.lower():
         relevant_context.append(context_details)
   return relevant_context

#print(get_employee_info("Who is Deepak"))

def chat(message, history):
   messages = [{"role": "system", "content": system_prompt}] + history
   context_block = "\n\n".join(get_employee_info(message))
   
   messages.append({"role": "user", "content": message})
   if context_block:
      messages.append({"role": "user", "content": context_block})

   stream = openai.chat.completions.create(model="gpt-4o-mini", messages=messages, stream=True)

   response = ""
   for chunk in stream:
      response += chunk.choices[0].delta.content or ''
      yield response



gr.ChatInterface(fn=chat, type="messages").launch()