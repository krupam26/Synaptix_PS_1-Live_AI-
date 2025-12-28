import os
import git
from typing import List
from pydantic import BaseModel, Field

print("1. Starting imports...")

import pathway as pw
from pathway.xpacks.llm import embedders, parsers, splitters
from pathway.xpacks.llm.document_store import DocumentStore
from pathway.xpacks.llm.question_answering import BaseRAGQuestionAnswerer
from pathway.stdlib.indexing import HybridIndexFactory, BruteForceKnnFactory
from pathway.stdlib.indexing.bm25 import TantivyBM25Factory

print("2. Pathway imports successful")

from langchain_community.vectorstores import PathwayVectorClient
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END, START

print("3. LangChain imports successful")

# -----------------------------
# Configuration
# -----------------------------
CODEBASE_PATH = "./codebase"
HOST = "127.0.0.1"
PORT = 8000

print(f"4. Monitoring folder: {os.path.abspath(CODEBASE_PATH)}")

# -----------------------------
# Git Pull Tool
# -----------------------------
def git_pull():
    print("Git pull triggered")
    try:
        repo = git.Repo(CODEBASE_PATH)
        repo.remotes.origin.pull()
        return "Latest commits pulled successfully!"
    except Exception as e:
        return f"Git pull failed: {str(e)}"

# -----------------------------
# Pathway Live Indexing
# -----------------------------
print("5. Starting Pathway FS read...")

folder = pw.io.fs.read(
    path=CODEBASE_PATH,
    format="binary",
    mode="streaming",
    with_metadata=True,
)

print("6. FS read successful – creating parser/splitter...")

parser = parsers.UnstructuredParser()
splitter = splitters.TokenCountSplitter(min_tokens=100, max_tokens=400)

print("7. Loading local embeddings model (this may take 20-40 seconds first time)...")

from sentence_transformers import SentenceTransformer
st_model = SentenceTransformer("all-MiniLM-L6-v2")

print("8. Model loaded – creating embedder...")

embedder = embedders.SentenceTransformerEmbedder(model=st_model)

print("9. Embedder ready – building index...")

index = HybridIndexFactory([
    TantivyBM25Factory(),
    BruteForceKnnFactory(embedder=embedder)
])

print("10. Creating document store...")

document_store = DocumentStore(
    docs=[folder],
    parser=parser,
    splitter=splitter,
    retriever_factory=index
)

print("11. Document store ready")

client = PathwayVectorClient(host=HOST, port=PORT)
retriever = client.as_retriever(k=10)

print("12. Initializing Ollama LLM (mistral)...")

llm = ChatOllama(model="mistral", temperature=0)

print("13. LLM ready")

# ... (rest of agent code stays the same)

# At the very end, before run_server:
print("\n*** EVERYTHING LOADED SUCCESSFULLY ***")
print("*** STARTING SERVER NOW – WAITING FOR REQUESTS ON PORT 8000 ***\n")

rag_app.build_server(host=HOST, port=PORT)
rag_app.run_server()