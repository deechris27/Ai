import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai

load_dotenv(override=True)
gemini_api_key = os.getenv('GOOGLE_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

if not gemini_api_key:
    print('No API key found')
else:
    print('Valid Gemini API found!')
if not openai_api_key:
    print('No openai api key found')
else:
    print('Valid openai api key found!')

google.generativeai.configure()

gpt_system = "You are a authoritative chatbot, very difficult to convince and confronting with solid reasoning"

gemini_system = "You are sweet and softspoken, you understand others temperament and provide convincing answer politely"

gpt_messages = ["Hi"]
gemini_messages = ["Hi There"]

def call_gpt():
    messages = [{"role": "system", "content": gpt_system}]
    for gpt, gemini in zip(gpt_messages, gemini_messages):
        messages.append([{"role": "assistant", "content": gpt}])
        messages.append([{"role": "user", "content": gemini}])
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content

call_gpt()



gemini_via_openapi_client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def call_gemini():
    messages = [{"role": "system", "content": gemini_system}]
    for gpt, gemini in zip(gpt_messages, gemini_messages):
        messages.append([{"role": "user", "content": gpt}])
        messages.append([{"role": "assistant", "content": gemini}])
        messages.append([{"role":"user", "content": gpt_messages[-1]}]) #picking the latest/last message of gpt from gpt_messages array
        response = gemini_via_openapi_client.chat.completions.create(
                   model="gemini-2.0-flash",
                   messages= messages
                )
        return response.choices[0].message.content
    
call_gemini()

call_gpt()

for i in range(5):
    gpt_next = call_gpt()
    print(f"GPT: \n{gpt_next}\n")
    gpt_messages.append(gpt_next)

    gemini_next = call_gemini()
    print(f"Gemini: \n{gemini_next}\n")
    gemini_messages.append(gemini_next)