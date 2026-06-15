from typing import Callable

from src.messages.internacionalizacao import Internacionalizacao, TextosBase


class Mensagens(TextosBase):
    projeto: str
    """nome do projeto"""
    oi: str
    """mensagem de boas vindas"""
    contagem: Callable[[int], str]
    """mensagem de contador"""