import datetime
from typing import Any, Self

from src.utils.request.http_request import CorpoJson


class Usuario(CorpoJson):
    id: int
    nome: str
    email: str
    senha: None | str
    role: str

    def set_nome(self, v: str):
        self.nome = v

    def set_email(self, v: str):
        self.email = v

    def set_senha(self, v: str):
        self.senha = v

    def set_role(self, v: str):
        self.role = v

    def __init__(self):
        self.id = 0
        self.nome = ""
        self.email = ""
        self.senha = None
        self.role = "usuario"

    @staticmethod
    def instanciar(json: dict):
        instancia = Usuario()
        print(json)
        instancia.id = json["id"]
        instancia.nome = json["nome"]
        instancia.email = json["email"]
        instancia.role = json["role"]
        return instancia

    def converter(self):
        dados = {"email": self.email, "nome": self.nome, "role": self.role}
        if self.senha:
            dados["senha"] = self.senha
        return dados


class Carregador(CorpoJson):
    capacidade: int
    disponivel: int
    ocupado: bool
    id: int
    preco: float = 1.4
    posto: str
    posto_id: int

    def set_preco(self, v: float):
        self.preco = v

    def set_disponivel(self, v: int):
        self.disponivel = v

    def set_capacidade(self, v: int):
        self.capacidade = v

    def set_ocupado(self, v: bool):
        self.ocupado = v

    def set_posto_id(self, v: int):
        self.posto_id = v

    def converter(self) -> dict:
        return {
            "capacidade": self.capacidade,
            "disponivel": self.disponivel,
            "preco": self.preco,
            "ocupado": self.ocupado,
            "postoId": self.posto_id,
        }

    def __init__(
        self,
        id: int,
        capacidade: int,
        preco: int,
        disponivel: int,
        ocupado: bool,
        posto_id: int,
        posto: str = "",
    ) -> None:
        super().__init__()
        self.id = id
        self.capacidade = capacidade
        self.disponivel = disponivel
        self.ocupado = ocupado
        self.preco = preco
        self.posto = posto
        self.posto_id = posto_id

    @staticmethod
    def instanciar(json: dict) -> Any:
        instancia = Carregador(
            json["id"],
            json["capacidade"],
            json["preco"],
            json["disponivel"],
            json["ocupado"],
            json["postoId"],
            json["posto"] if "posto" in json else "",
        )

        return instancia


class Posto(CorpoJson):
    id: int
    carregadores: list[Carregador]
    imagem: str
    descricao: str = ""
    nome: str
    local: str = ""
    preco_medio: float = 0
    dono_id: int

    def set_descricao(self, v: str):
        self.descricao = v

    # def set_imagem(self, v: str):
    #     self.imagem = v

    def set_nome(self, v: str):
        self.nome = v

    def set_local(self, v: str):
        self.local = v

    def set_imagem(self, v: str):
        self.imagem = v

    @property
    def capacidade_media(self):
        return sum(carregador.capacidade for carregador in self.carregadores) / len(
            self.carregadores
        )

    def converter(self) -> dict:
        return {
            "imagem": self.imagem,
            "descricao": self.descricao,
            "local": self.local,
            "nome": self.nome,
            "dono_id": self.dono_id
        }

    @property
    def carregadores_disponiveis(self):
        return [
            carregador for carregador in self.carregadores if not carregador.ocupado
        ]

    def __init__(
        self,
        id: int,
        nome: str,
        carregadores: list[Carregador],
        imagem: str,
        descricao: str,
        local: str,
        preco_medio: float,
        dono_id=0,
    ) -> None:
        super().__init__()
        self.id = id
        self.nome = nome
        self.carregadores = carregadores
        self.imagem = imagem
        self.preco_medio = preco_medio
        self.descricao = descricao
        self.local = local
        self.dono_id = dono_id

    @staticmethod
    def instanciar(json: dict) -> Any:
        return Posto(
            json["id"],
            json["nome"],
            list(
                map(
                    lambda x: Carregador.instanciar(x),
                    json["carregadores"] if "carregadores" in json else [],
                )
            ),
            json["imagem"],
            json["descricao"],
            json["local"],
            json["preco_medio"],
            json["dono_id"]
        )


class Recarga(CorpoJson):
    id: int
    preco_kwh: float
    preco: float
    quantidade: float
    carregador: Carregador
    posto: Posto | None = None
    data: datetime.datetime
    usuario: Usuario | None = None

    @staticmethod
    def instanciar(json: dict) -> Any:
        # print(json)
        recarga = Recarga()

        recarga.data = datetime.datetime.fromisoformat(json["data"])
        recarga.preco = json["preco"]
        recarga.quantidade = json["quantidade"]
        recarga.preco_kwh = json["preco_kwh"]
        # recarga.preco = 0
        recarga.usuario = (
            Usuario.instanciar(json["usuario"]) if "usuario" in json else None
        )
        recarga.posto = Posto.instanciar(json["posto"]) if "posto" in json else None
        recarga.id = json["id"]
        return recarga
