import os
import git
from typing import List
from pydantic import BaseModel, Field

print("1. Starting imports...")

import pathway as pw
from pathway.xpacks.llm import parsers, splitters
from pathway.xpacks.llm.document_store import DocumentStore
from pathway.xpacks.llm.question_answering import BaseRAGQuestionAnswerer
from pathway.stdlib.indexing.bm25 import TantivyBM25Factory

print("2. Pathway imports successful")

from langchain_community.vectorstores import PathwayVectorClient
from langchain_core.prompts import PromptTemplate
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
# Pathway Live Indexing (BM25 Only)
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

print("7. Using BM25 keyword indexing (fast & reliable for code/docs)...")

# Single BM25 factory — no embedder, no hybrid issues
index = TantivyBM25Factory()

print("8. Creating document store...")

document_store = DocumentStore(
    docs=[folder],
    parser=parser,
    splitter=splitter,
    retriever_factory=index
)

print("9. Document store ready")

# -----------------------------
# LangChain Retriever + LLM
# -----------------------------
print("10. Connecting to Pathway vector client...")

client = PathwayVectorClient(host=HOST, port=PORT)
retriever = client.as_retriever(k=10)

print("11. Initializing Ollama LLM (mistral)...")

llm = ChatOllama(model="mistral", temperature=0)

print("12. LLM ready")

# -----------------------------
# Simple RAG Chain
# -----------------------------
rag_prompt = PromptTemplate.from_template(
    "You are a senior developer. Answer using only the provided context. Keep concise.\n"
    "Question: {question}\nContext: {context}\nAnswer:"
)
rag_chain = rag_prompt | llm.invoke | StrOutputParser()

# -----------------------------
# Minimal Agent
# -----------------------------
class AgentState(dict):
    question: str
    docs: List
    answer: str

def retrieve(state):
    state["docs"] = retriever.invoke(state["question"])
    return state

def generate(state):
    context = "\n\n".join([doc.page_content for doc in state["docs"]])
    state["answer"] = rag_chain.invoke({"question": state["question"], "context": context})
    return state

workflow = StateGraph(AgentState)
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

graph_app = workflow.compile()

# -----------------------------
# Pathway Server + Agent Endpoint
# -----------------------------
rag_app = BaseRAGQuestionAnswerer(llm=llm, indexer=document_store)

@rag_app.serve_callable(route="/v1/agent")
def call_agent(query: str) -> str:
    if any(word in query.lower() for word in ["update", "latest", "pull"]):
        git_pull()
    
    result = graph_app.invoke({"question": query})
    return result["answer"]

print("\n*** EVERYTHING LOADED SUCCESSFULLY ***")
print("*** STARTING SERVER NOW – WAITING FOR REQUESTS ON PORT 8000 ***\n")

rag_app.build_server(host=HOST, port=PORT)
rag_app.run_server()