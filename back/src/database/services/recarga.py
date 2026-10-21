from datetime import datetime
from typing import List

from sqlalchemy.sql import and_

from src.database.models.posto import Posto
from src.database.models.pagamento import Pagamento
from src.database.models.recarga import Recarga
from src.database.services.base import BaseQuery


class RecargaQuery(BaseQuery[Recarga]):
    def tabela(self) -> type[Recarga]:
        return Recarga
    
    # def listarPorDono(self, id: int):
    #     sessao = self._criar_sessao()
        
    #     recargas = sessao.query(Recarga, Posto).where(Recarga.po).where(Posto.dono_id == id)

    def nao_pagos(self):
        sessao = self._criar_sessao()

        recargas = sessao.query(Recarga).where(Recarga.pagamento_id == None).all()

        return recargas

    def listarUltimas(self) -> List[Recarga]:
        sessao = self._criar_sessao()

        recargas = sessao.query(Recarga).order_by(Recarga.data_criacao).limit(10).all()

        return recargas

    def pagar(self, pagamento: Pagamento):
        sessao = self._criar_sessao()

        sessao.query(Recarga).filter(Recarga.pagamento_id == None).update(
            {Recarga.pagamento_id: pagamento.id}
        )
        sessao.commit()
        sessao.close()

    def obterPorData(self, data: datetime):
        sessao = self._criar_sessao()

        resultados = sessao.query(Recarga).where(and_(
            Recarga.data_criacao
            >= datetime(data.year, data.month, data.day, 0, 0, 0, 0)
            , Recarga.data_criacao
            <= datetime(data.year, data.month, data.day, 23, 59, 59, 49))
        ).all()

        # sessao.close()

        return resultados
