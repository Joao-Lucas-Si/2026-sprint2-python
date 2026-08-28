from src.database.models.pagamento import Pagamento
from src.database.services.base import BaseQuery


class PagamentoQuery(BaseQuery[Pagamento]):
    def tabela(self) -> type[Pagamento]:
        return Pagamento