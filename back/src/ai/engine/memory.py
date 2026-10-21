from abc import ABC
from typing import Any, Literal
import tiktoken

from langchain_core.messages import BaseMessage, MessageLikeRepresentation

from src.ai.dados import Mensagem


def contar_tokens(texto):
    encoding = tiktoken.get_encoding("o200k_base")
 
    return len(encoding.encode(texto))

class MensagemMemoria():
    tokens: int
    mensagem: Mensagem

    def __init__(self, tokens: int, mensagem: Mensagem) -> None:
        self.tokens = tokens
        self.mensagem = mensagem

class Memory(ABC):
    messages: list[MensagemMemoria] = []

    def chat_message(self) -> list[Mensagem]:
        return [message.mensagem for message in self.messages]

    def save_context(self, mensagem: Mensagem):
        ...

class TokenMemory(Memory):
    max_tokens = 1000
    def save_context(self, mensagem: Mensagem):
        tokens = contar_tokens(mensagem.conteudo)
        
        self.messages.append(MensagemMemoria(tokens, mensagem))
        
        def calc_tokens():
            return sum(message.tokens for message in self.messages)

        total_tokens = calc_tokens()
        while (total_tokens > self.max_tokens):
            removed = self.messages.pop(0)
            total_tokens -= removed.tokens