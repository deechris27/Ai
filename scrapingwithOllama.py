import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display

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

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

# !ollama pull llama3.2

# Downloaded Ollama for my OS and "ollama run llama3.2"

# llama3.2 is running in my local

system_prompt = "You are an analyst that analyze the content of a website and provide a short summary.\
                 Ignore all links and texts that are navigation related. Respond in markdown"


def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "Please provide a short summary of the website in markdown ignoring navigation related links and texts"
    user_prompt += website.text
    return user_prompt
#print(user_prompt_for(scrapeddata))

def messages_for(webContent):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(webContent)}
    ]

messages_for(scrapeddata)

forTest = [
        {"role": "system", "content": "you are my smart pet robot dog named Odin"},
        {"role": "user", "content": "With the emergence of AI technologies, What do you think will future proof the career of a software professional with 10 plus years of experience?"}
    ]

test = requests.post(OLLAMA_API, json={"model":"llama3.2", "messages": forTest, "stream": False})
print(test.json()['message']['content'])

def summarize(url):
    scrapedData = Website(url)
    payload = {
        "model": MODEL,
        "messages": messages_for(scrapedData),
        "stream": False
    }
    response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    return response.json()['message']['content']

#summarize("https://cnn.com")