from src.database.models.carregador import Carregador
from src.database.models.posto import Posto
from src.database.services.base import BaseQuery


class PostoQuery(BaseQuery[Posto]):
    def tabela(self) -> type[Posto]:
        return Posto
    
    # def extras(self) -> list[type]:
    #     return [Carregador]