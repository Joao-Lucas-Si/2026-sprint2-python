from src.messages.base import Mensagens
from src.messages.internacionalizacao import Lingua


class Ingles(Lingua[Mensagens]):
    nome="ingles"
    textos: Mensagens={
        "oi": "hello",
        "contagem": lambda x: f"{x} count",
        "projeto": "goodwee"
    }