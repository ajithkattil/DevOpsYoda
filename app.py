# app.py
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
import gradio as gr

# Load environment variables
load_dotenv()

# Initialize LLM (Free: e.g., google/flan-t5-xl via HuggingFaceHub)
huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not huggingfacehub_api_token:
    raise ValueError("Missing HUGGINGFACEHUB_API_TOKEN in environment variables.")

llm = HuggingFaceHub(
    repo_id="google/flan-t5-xl",
    model_kwargs={"temperature": 0.1, "max_new_tokens": 500},
    huggingfacehub_api_token=huggingfacehub_api_token
)

# Load and split documents (markdown, YAML, logs, etc.)
loader = TextLoader("data/devops_sample.txt")
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False
)

def ask_bot(query):
    if not query.strip():
        return "Please enter a question."
    return qa_chain.run(query)

# Gradio Interface
demo = gr.Interface(
    fn=ask_bot,
    inputs="text",
    outputs="text",
    title="DevOpsYoda – Ask Me Anything About Your Infrastructure",
    description="An AI-powered assistant trained on CI/CD, Kubernetes, Terraform, logs, and DevOps best practices."
)

demo.launch()
