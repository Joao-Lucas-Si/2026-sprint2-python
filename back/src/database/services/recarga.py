from src.database.models.pagamento import Pagamento
from src.database.models.recarga import Recarga
from src.database.services.base import BaseQuery


class RecargaQuery(BaseQuery[Recarga]):
    def tabela(self) -> type[Recarga]:
        return Recarga

    def nao_pagos(self):
        sessao = self._criar_sessao()

        recargas = sessao.query(Recarga).where(Recarga.pagamento_id == None).all()

        return recargas

    def pagar(self, pagamento: Pagamento):
        sessao = self._criar_sessao()

        sessao.query(Recarga).filter(Recarga.pagamento_id == None).update({ Recarga.pagamento_id: pagamento.id })
        sessao.commit()
        sessao.close()