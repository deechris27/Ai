from langchain.chains import ConversationChain
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
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

memory = ConversationBufferMemory()
chain = ConversationChain(llm=ChatOpenAI(), memory=memory)

print(chain.run("Hello, How are you?"))
print(chain.run("My name is Deepak, what is your name?"))
print(chain.run("Do you remember previous conversations?"))