import os
from typing import Literal

from langchain_classic.memory.chat_memory import BaseChatMemory
from src.ai.dados import Mensagem, Papel
from src.ai.client.adapters.ai_adapter import AiAdapter, system_prompts
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_classic.runnables import 

class LangChainAdapter(AiAdapter):
    def __init__(self) -> None:
        self.model = ChatGoogleGenerativeAI(
            model="gemini-3-flash-preview",
            api_key=os.getenv("CHAVE_GEMINI"),
        )
        # self.memory: BaseChatMemory = ConversationTokenBufferMemory(llm=self.model, max_token_limit=400)
   
    def chamarDiretamente(self, prompt: str,historico: list[Mensagem] = [],  system: system_prompts = "assets/prompts/system_prompt.md", formato: dict | None = None, dados: dict = {}) -> str:
        
        if formato:
            self.model.response_schema = formato
            self.model.response_mime_type = "application/json"
        else:
            self.model.response_mime_type = "text/plain"
            self.model.response_schema  = None
        # base = open("assets/prompt/templates/base.md").read()
        # return base

        template = ChatPromptTemplate( [
            ("system", open(system).read()),
            #  MessagesPlaceholder("history"),
            *[( "ai" if mensagem.role == Papel.CHAT else "human", mensagem.conteudo) for mensagem in historico],
            ("human", prompt)
            # MessagesPlaceholder("input")
        ], )
        
        # return sys.argv[1]
        # message = model.invoke(sys.argv[1])
        chain =  template  | self.model |  StrOutputParser()
        
        # if usar_memoria:
        #     chain = RunnableWithMessageHistory(chain, get_session_history=  lambda : self.memory.chat_memory, input_messages_key="prompt", history_messages_key="history" )
        input = {} | dados
        # print(chain)
        message = chain.invoke(input)
        # if usar_memoria:
        #     # print(template.messages[-1].content)
        #     self.memory.save_context(inputs={"human": template.messages[-1].}, outputs={"ai": message })  # pyright: ignore[reportAttributeAccessIssue]
        # print(message)
        return message