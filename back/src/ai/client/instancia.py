import os

from src.ai.client.adapters.langchain_adapter import LangChainAdapter
# from src.ai.client.adapters.gemini_genai_adapter import GeminiGenaiAdapter
# from src.ai.client.adapters.ollama_request import Ollama_Request_adapter
# from src.ai.client.adapters.gemini_requests_adapter import GeminiAdapter
from src.ai.client.adapters.ai_adapter import AiAdapter


def instanciarAi() -> AiAdapter:
    return LangChainAdapter()
    # if os.getenv("CHAVE_GEMINI"):
    #     return GeminiGenaiAdapter()
    # elif os.getenv("HOST") and os.getenv("MODEL"):
    #     return Ollama_Request_adapter()
    
    # raise Exception("arquivo env em formato invalido, siga os exemplos de gemini ou ollama")