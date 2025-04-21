

#   A simple webscraper using GPT LLM to scrape 
#   the contents of a website
#   through util functions that builds the system and user prompts
#   from the given url

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print('No API key found')
elif not api_key.startswith('sk-proj'):
    print('Invalid OpenAI api key')
else:
    print('Valid OpenAi API found!')

openai = OpenAI()

response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":"Hello AI, What do you think will future proof my career as software professional with 13 years of experience?"}])
print(response.choices[0].message.content)

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:

    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        webcontent = BeautifulSoup(response.content, 'html.parser')
        self.title = webcontent.title.string if webcontent.title else "No title found"
        for unncecessary in webcontent.body(['img', 'url', 'script', 'style', 'input']):
            unncecessary.decompose()
        self.text = webcontent.get_text(separator='\n', strip=True)


scrapeddata = Website('https://cnn.com')
print(scrapeddata.title)
#print(scrapeddata.text)

# Querying with system and user prompt

system_prompt = "You are an analyst that analyze the content of a website and provide a short summary.\
                 Ignore all links and texts that are navigation related. Respond in markdown"


def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "Please provide a short summary of the website in markdown ignoring navigation related links and texts"
    user_prompt += website.text
    return user_prompt
#print(user_prompt_for(scrapeddata))

# Example structure to query OpenAI API

messages = [
    {"role": "system", "content": "You are my smart pet dog robot named Odin" },
    {"role": "user", "content": "Tell me all the causes and preventive steps for seizure"}
]
    
response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
print(response.choices[0].message.content)

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

messages_for(scrapeddata)

def summarize(url):
    scrapedData = Website(url)
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for(scrapedData)
    )

    return response.choices[0].message.content

summarize("https://cnn.com")
