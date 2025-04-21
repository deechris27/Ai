import requests
import time
import ollama

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}

question = "what does display and update_display from IPython do?"

messages = [
  {"role": "system", "content": "You're my teaching assistant"},
  {"role": "user", "content": question}
]

# stream = requests.post(OLLAMA_API, json={"model":"llama3.2", "messages": messages, "stream": True})
# print(f"so far good")
# print(stream.json()['message']['content'])
# response=""
# for chunk in stream:
#     response += chunk['message']['content'] or ''
#     response = response.replace("```", "").replace("markdown", "")
#     for i in range(len(response)):
#         print(f"\r {response}", end="", flush=True)
#         time.sleep(1)

response = ollama.chat(model="llama3.2", messages=messages)
reply = response['message']['content']
print(reply)