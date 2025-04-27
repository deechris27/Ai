from langchain_community.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print('No API key found')
elif not api_key.startswith('sk-proj'):
    print('Invalid OpenAI api key')
else:
    print('Valid OpenAi API found!')

openai = OpenAI(api_key=api_key)

loader = PyPDFLoader("HarryPotter.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(api_key=api_key)
db = FAISS.from_documents(texts, embeddings)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


qa_chain = ConversationalRetrievalChain.from_llm(
    llm = ChatOpenAI(model_name="gpt-40-mini", temperature=0.2, api_key=api_key),
    retriever = db.as_retriever(),
    memory=memory,
)

while True:
    query = input("You : ")
    if query.lower() == "exit":
        break
    result = qa_chain.invoke({"question": query})
    print("Bot :", result['answer'])