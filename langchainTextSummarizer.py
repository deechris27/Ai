from langchain.chains.summarize import load_summarize_chain
from langchain_community.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print('No API key found')
elif not api_key.startswith('sk-proj'):
    print('Invalid OpenAI api key')
else:
    print('Valid OpenAi API found!')


with open("SampleArticle.txt", "r", encoding="utf-8") as f:
    content = f.read()
docs = [Document(page_content=content)]
chain = load_summarize_chain(ChatOpenAI(), chain_type="stuff")

print(chain.run(docs))
