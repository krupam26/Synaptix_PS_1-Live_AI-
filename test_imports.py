print("=== STARTING BASIC TEST ===")

try:
    import pathway as pw
    print("Pathway imported OK")
except Exception as e:
    print(f"Pathway import FAILED: {e}")

try:
    from pathway.xpacks.llm import embedders
    print("Pathway LLM xpack imported OK")
except Exception as e:
    print(f"Pathway LLM import FAILED: {e}")

try:
    from langchain_ollama import ChatOllama
    print("LangChain Ollama imported OK")
except Exception as e:
    print(f"LangChain Ollama import FAILED: {e}")

try:
    from sentence_transformers import SentenceTransformer
    print("Sentence Transformers imported OK")
except Exception as e:
    print(f"Sentence Transformers import FAILED: {e}")

print("=== TEST COMPLETE ===")