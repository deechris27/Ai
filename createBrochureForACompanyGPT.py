#   Create brochure for a company with the scraped data from their website using GPT LLM 
#   through util functions that builds the system and user prompts from the given url

import os
import requests
import json
from dotenv import load_dotenv
from typing import List
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
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
        links = [link.get('href') for link in webcontent.find_all('a')]
        self.links = [link for link in links if link]

    def get_contents(self):
        return f"Webpage title {self.title}, webpage content {self.text}"
    

scrapeddata = Website('https://huggingface.co')
#print(scrapeddata.title)
#print(scrapeddata.links)
#print(scrapeddata.text)

# Querying with system and user prompt

system_prompt = "You are an analyst who is provided with a long list of links from a company website.\
                 you should decide which are the links would be relevant to include in the company's brochure.\n"

system_prompt += "You respond in JSON format like the example below:"

system_prompt += """{
    "links": [
      {"type": "contactUS page", "url": "https://somewebsite.com/contactus"},
      {"type: "careers page", "url": "https://somewebsite.com/careers"},
      {"type": "about page", "url": "https://somewebsite.com/aboutus"}
    ]
}"""

#print(system_prompt)

def get_user_prompt(website):
     user_prompt = f"Here is the list of links from the website {website.url}"
     user_prompt += "You are able to decide which of the links would be most relevant to include in a brochure about the company, such as links to an About page, or a Company page, or Careers/Jobs pages.\
     Respond with full https url in JSON format. \n"
     user_prompt += "\n".join(website.links)
     return user_prompt

 # print(get_user_prompt(scrapeddata))

def get_links(url):
    scrapedData = Website(url)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_prompt },
                  {"role": "user", "content": get_user_prompt(scrapedData)}],
       response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)

    
site = Website("https://huggingface.co")
site.links

def get_details(url):
    result = "Landing page \n"
    result += Website(url).get_contents()

    links = get_links(url)
    for link in links["links"]:
        result += f"\n\n {link['type']}\n"
        result += Website(link["url"]).get_contents()
    return result


#print(get_details("https://huggingface.co"))
        

system_prompt = "You are an analyst that analyses the contents from webpages of a company url and create \n"
"a brochure for the company with details about their investors, customers, culture, careers. Respond in markdown"

def get_user_prompt_for_brochure(company_name, url):
     user_prompt = f"You are looking at a company called {company_name} \n"
     user_prompt += f"here are the contents of its landing page. Build a brochure for the company in markdown \n"
     user_prompt += get_details(url)
     user_prompt = user_prompt[:6_000] # truncate more than 6k characters
     return user_prompt

get_user_prompt_for_brochure("huggingface", "https://huggingface.co")

def create_brochure(company_name, url):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_user_prompt_for_brochure(company_name, url)},
        ],
    )
    result = response.choices[0].message.content
    display(Markdown(result))

    #create_brochure("huggingface", "https://huggingface.co")


def stream_brochure(company_name, url):
    stream = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_user_prompt_for_brochure(company_name, url)}
        ],
        stream=True
    )
    response=""
    display_handle = display(Markdown(""), display_id=True)
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        response = response.replace("```", "").replace("markdown", "")
        update_display(Markdown(response), display_id=display_handle.display_id)

stream_brochure("huggingface", "https://huggingface.co")