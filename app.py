# app.py

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import gradio as gr

# Load environment variables
load_dotenv()

# Get API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Missing OPENAI_API_KEY in .env file")

# Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    openai_api_key=openai_api_key
)

# Load and split documents
loader = TextLoader("data/devops_sample.txt")
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = splitter.split_documents(documents)

# Create embeddings and FAISS index
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False
)

# Bot function
def ask_bot(query):
    if not query.strip():
        return "Please enter a question."
    return qa_chain.run(query)

# Gradio UI
demo = gr.Interface(
    fn=ask_bot,
    inputs="text",
    outputs="text",
    title="DevOpsYoda – Ask Me Anything About Your Infrastructure",
    description="An AI assistant trained on CI/CD, Kubernetes, Terraform, and DevOps best practices."
)

if __name__ == "__main__":
    demo.launch()
