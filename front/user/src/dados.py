from typing import Any

from src.utils.request.http_request import CorpoJson


class Carregador(CorpoJson):
    capacidade: int
    disponivel: int
    ocupado: bool
    id: int
    preco: float = 1.4
    # posto: "Posto"

    def __init__(self,id: int,  capacidade: int, preco: int, disponivel: int, ocupado: bool) -> None:
        super().__init__()
        self.id = id
        self.capacidade = capacidade
        self.disponivel = disponivel
        self.ocupado = ocupado
        self.preco = preco

    @staticmethod
    def instanciar(json: dict) -> Any:
        instancia = Carregador(json["id"], json["capacidade"], json["preco"], json["disponivel"], json["ocupado"])

        return instancia


class Posto(CorpoJson):
    id: int
    carregadores: list[Carregador]
    imagem: str
    descricao: str = ""
    nome: str
    local: str = ""
    preco_medio: float = 0

    @property
    def capacidade_media(self):
        return sum(carregador.capacidade for carregador in self.carregadores) / len(
            self.carregadores
        )

    @property
    def carregadores_disponiveis(self):
        return [
            carregador for carregador in self.carregadores if not carregador.ocupado
        ]

    def __init__(self, id: int, nome: str, carregadores: list[Carregador], imagem: str, descricao: str, local: str, preco_medio: float) -> None:
        super().__init__()
        self.id = id
        self.nome = nome
        self.carregadores = carregadores
        self.imagem = imagem
        self.preco_medio = preco_medio
        self.descricao = descricao
        self.local = local

    @staticmethod
    def instanciar(json: dict) -> Any:
        return Posto(json["id"], json["nome"], list(map(lambda x: Carregador.instanciar(x), json["carregadores"])),  json["imagem"], json["descricao"], json["local"], json["preco_medio"])

class Recarga(CorpoJson):
    preco_kwh: float
    preco: float
    quantidade: float
    carregador: Carregador
    posto: Posto

    @staticmethod
    def instanciar(json: dict) -> Any:
        recarga = Recarga()

        recarga.preco = json["preco"]
        recarga.quantidade = json["quantidade"]
        recarga.preco_kwh = json["preco_kwh"]
        recarga.posto = Posto.instanciar(json["posto"])
        return recarga
