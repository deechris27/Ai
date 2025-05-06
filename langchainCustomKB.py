from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import retrieval_qa
from langchain_community.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document


docs = [
    Document(page_content="The capital of Italy is Rome"),
    Document(page_content="Captain of black pearl is Jack Sparrow"),
    Document(page_content="India is the largest democratic country in the world"),
    Document(page_content="Vector DB maps semantically matching statements")
]

splitter = CharacterTextSplitter(chunk_size=100)
texts = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)

qa = retrieval_qa.from_chain_type(llm=ChatOpenAI(), retriever=db.as_retriever())

while True:
    query = input("Your question : ")
    if query.lower() == "exit":
        break
    print(qa.run(query))