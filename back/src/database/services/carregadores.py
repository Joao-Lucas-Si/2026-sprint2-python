from src.database.models.posto import Posto
from src.database.models.carregador import Carregador
from src.database.models.pagamento import Pagamento
from src.database.services.base import BaseQuery


class CarregadorQuery(BaseQuery[Carregador]):
    def tabela(self) -> type[Carregador]:
        return Carregador
    
    def listarPorDono(self, id: int):
        sessao = self._criar_sessao()
        
        carregadores = sessao.query(Carregador, Posto).where(Posto.dono_id == id).where(Carregador.posto_id == Posto.id).all()
        
        return [c.tuple()[0] for c in carregadores]