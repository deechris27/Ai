import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
openai = OpenAI()

if not deepseek_api_key:
    print('No API key found')
else:
    print('Valid DeepSeek API found!')

system_prompt = "You are my pet robot dog named Odin"

user_prompt = "What do you think is the best dog breed to have in a humid, hot climate like Chennai, India ?"

messages = [
    { "role": "user", "content": system_prompt },
    { "role": "system", "content": user_prompt }
]

deepseek_via_openapi_client = OpenAI(
    api_key=deepseek_api_key,
    base_url="https://api.deepseek.com"
)

response = deepseek_via_openapi_client.chat.completions.create(
    model="deepseek-chat",
    messages=messages
)

#print(response.choices[0].message.content)

def streamDeepseek():
    stream = deepseek_via_openapi_client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    stream=True
   )
    
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        response = response.replace("```").replace("markdown", "")
        yield response


for stream in streamDeepseek():
  print(stream)

