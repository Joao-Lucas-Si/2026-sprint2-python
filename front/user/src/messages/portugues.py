from src.messages.base import Mensagens
from src.messages.internacionalizacao import Lingua


class Portugues(Lingua[Mensagens]):
    nome = "portugues"
    textos: Mensagens = {
        "contagem": lambda x: f"total de {x}",
        "oi": "oi",
        "projeto": 'Projeto Goodwee'
    }