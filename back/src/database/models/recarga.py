from sqlalchemy import ForeignKey

from src.database.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from back.src.database.models.posto import Posto

class Recarga(BaseModel):
    __tablename__="recargas"
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    # veiculo_id: Mapped[int] = mapped_column(ForeignKey("veiculo.id"))
    carregador_id: Mapped[int] = mapped_column(ForeignKey("carregador.id"))
    #status: Mapped[int] = mapped_column()
    # bateria: Mapped[int] = mapped_column()
    #potencia: Mapped[int] = mapped_column()
    #energia_consumida: Mapped[int] = mapped_column()
    #tempo_decorrido: Mapped[int] = mapped_column()
    #tempo_restante: Mapped[int] = mapped_column()
    #custo_atual: Mapped[int] = mapped_column()
    #previsao_termino: Mapped[int] = mapped_column()
    quantidade: Mapped[int] = mapped_column()