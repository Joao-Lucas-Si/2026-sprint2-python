from src.database.models.carregador import Carregador
from src.database.models.posto import Posto
from src.database.services.base import BaseQuery


class PostoQuery(BaseQuery[Posto]):
    def tabela(self) -> type[Posto]:
        return Posto
    
    
    def listarPorDono(self, id: int):
        sessao = self._criar_sessao()
        
        postos = sessao.query(Posto).where(Posto.dono_id == id).all()
        
        return postos
    
    # def extras(self) -> list[type]:
    #     return [Carregador]