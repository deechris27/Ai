#   A simple util function that lets you question AI and get stream of replies in markdown

import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display
import time

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print('No API key found')
elif not api_key.startswith('sk-proj'):
    print('Invalid OpenAI api key')
else:
    print('Valid OpenAi API found!')

openai = OpenAI()

# Replace the value of this question variable with a question of your choice

question = "what does display and update_display from IPython do?"

messages = [
  {"role": "system", "content": "You're my teaching assistant"},
  {"role": "user", "content": question}
]

stream = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    stream=True
)
response=""
for chunk in stream:
    response += chunk.choices[0].delta.content or ''
    #print(response)
    response = response.replace("```", "").replace("markdown", "")
    for i in range(len(response)):
        print(f"\r {response}", end="", flush=True)
        time.sleep(1)