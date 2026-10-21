from enum import Enum
import random
from typing import Self

from pydantic import BaseModel, ConfigDict

from src.database.services.posto import PostoQuery
from src.database.models.posto import Posto

def exemplos():
    global salvos
    if len(salvos) == 0:
        query = PostoQuery()
        salvos = query.listarTodos()
        
    return salvos

# class Carregador(BaseModel):
#     model_config = ConfigDict(use_attribute_docstrings=True)
#     capacidade: int = 0
#     """capacidade de carregamento por hora"""
#     disponivel: int = 0
#     """quantidade de energia disponivel"""
#     ocupado: bool = False
#     """estado de ocupação do carregador"""
#     numero: int
#     """número de identificação do carregador"""
    

# class Posto(BaseModel):
#     model_config = ConfigDict(use_attribute_docstrings=True)
#     nome: str = ""
    
#     carregadores: list[Carregador] = []


class Papel(Enum):
    USUARIO = "user"
    CHAT = "chat"


class Mensagem():
    conteudo: str
    role: Papel
    def __init__(self, conteudo: str, role: Papel = Papel.USUARIO) -> None:
        self.conteudo = conteudo
        self.role = role


class MensagemChat(Mensagem):
    pensamento: str

    def __init__(self, conteudo: str, pensamento: str = "") -> None:
        super().__init__(conteudo, Papel.CHAT)
        self.pensamento = pensamento


salvos: list[Posto] = []