import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import google.generativeai

load_dotenv(override=True)
gemini_api_key = os.getenv('GOOGLE_API_KEY')

if not gemini_api_key:
    print('No API key found')
else:
    print('Valid Gemini API found!')

google.generativeai.configure()

system_prompt = "You are my pet robot dog named Odin"

user_prompt = "What do you think is the best dog breed for a hot humid climate place like chennai, India?"

# gemini = google.generativeai.GenerativeModel(
#     model_name='gemini-2.0-flash',
#     system_instruction=system_prompt,
# )

# response = gemini.generate_content(user_prompt)

#print(response.text)

gemini = google.generativeai.GenerativeModel(model_name='gemini-2.0-flash', system_instruction= "you're a smart assistant")
chatbot = gemini.start_chat()

def chat(message, history):

    print("History is: ")
    print(history)
    print("Message is:")
    print(message)
    
    stream = chatbot.send_message(message, stream=True)

    response = ""

    for chunk in stream:
        response += chunk.text or ''
        yield response

gr.ChatInterface(fn=chat, type="messages").launch()
