import requests
import time
import ollama
from openai import OpenAI

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}

question = "what does display and update_display from IPython do?"

messages = [
  {"role": "system", "content": "You're my teaching assistant"},
  {"role": "user", "content": question}
]

# regular non streaming output
response = ollama.chat(model="llama3.2", messages=messages)
reply = response['message']['content']
#print(reply)

stream = requests.post(OLLAMA_API, json={"model":"llama3.2", "messages": messages, "stream": True})
# print(f"so far good")
# print(stream.json()['message']['content'])
# response=""

# for chunk in ollama.chat(model="llama3.2", messages=messages, stream=True):
#       if chunk.get('message', {}).get('content', {}):
#         response += chunk['message']['content']
#         yield response
# for chunk in stream:
#     # response += getattr(chunk, "content", "")
#      response += chunk['message']['content']
#      response = response.replace("```", "").replace("markdown", "")
#     for i in range(len(response)):
#         print(f"\r {response}", end="", flush=True)
#         time.sleep(1)

ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
stream = ollama_via_openai.chat.completions.create(model="llama3.2", messages=messages, stream=True)
 
response = ""
#display_handle = display(Markdown(""), display_id=True)
for chunk in stream:
    response += reply.replace("```","").replace("markdown","")
    #update_display(Markdown(reply), display_id=display_handle.display_id)
    for i in range(len(response)):
         time.sleep(0.5)
         print(f"\r {response}", end="", flush=True)

