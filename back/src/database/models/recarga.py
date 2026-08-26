from sqlalchemy import ForeignKey

from src.database.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from back.src.database.models.posto import Posto

class Recarga(BaseModel):
    __tablename__="recargas"
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    # veiculo_id: Mapped[int] = mapped_column(ForeignKey("veiculo.id"))
    carregador_id: Mapped[int] = mapped_column(ForeignKey("carregador.id"))
    # status: Mapped[int] = mapped_column()
    # bateria_inicio: Mapped[int] = mapped_column()
    # bateria_fim: Mapped[int] = mapped_column()
    # potencia: Mapped[int] = mapped_column()
    # energia_consumida: Mapped[int] = mapped_column()
    # data_hora_inicio: Mapped[int] = mapped_column()
    # data_hora_fim: Mapped[int] = mapped_column()
    # tempo_decorrido: Mapped[int] = mapped_column()
    # tempo_restante: Mapped[int] = mapped_column()
    # tempo_total: Mapped[int] = mapped_column()
    # previsao_termino: Mapped[int] = mapped_column()
    # preco_kwh: Mapped[int] = mapped_column()
    # preco_total: Mapped[int] = mapped_column()
    # custo_economizado_combustivel: Mapped[int] = mapped_column()
    # energia_utilizada: Mapped[int] = mapped_column()
    # quantidade: Mapped[int] = mapped_column()
    pagamento_id: Mapped[int] = mapped_column(ForeignKey("pagamento.id"))