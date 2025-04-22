import google.generativeai
import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)
gemini_api_key = os.getenv('GOOGLE_API_KEY')


if not gemini_api_key:
    print('No API key found')
else:
    print('Valid Gemini API found!')

google.generativeai.configure()

system_prompt = "You are my pet robot dog named Odin"

user_prompt = "What do you think is the best dog breed for a working man?"

gemini = google.generativeai.GenerativeModel(
    model_name='gemini-2.0-flash',
    system_instruction=system_prompt
)

response = gemini.generate_content(user_prompt)

print(response.text)