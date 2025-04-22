import google.generativeai
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

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

system_prompt = "You are my pet robot dog named Odin"

user_prompt = "What do you think is the best dog breed for a working man?"

gemini = google.generativeai.GenerativeModel(
    model_name='gemini-2.0-flash',
    system_instruction=system_prompt
)

response = gemini.generate_content(user_prompt)

#print(response.text)

gemini_via_openapi_client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = gemini_via_openapi_client.chat.completions.create(
    model="gemini-2.0-flash",
    messages= [
        {"role": "system", "content": "You are an astro scientist"},
        {"role": "user", "content": "Do you think Humans will colonize another planet someday?"}
    ]
)

#print(response.choices[0].message.content)

# system_prompt = "You are a standup comedian"
# user_prompt = "Tell me nice adult Joke"

# prompts = [
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content": user_prompt}
# ]

# response = openai.chat.completions.create(
#     model='gpt-4o-mini',
#     messages=prompts,
#     temperature=0.5
# )

# print(response.choices[0].message.content)