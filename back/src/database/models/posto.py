from src.database.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.carregador import Carregador

class Posto(BaseModel):
    __tablename__="postos"
    nome: Mapped[str] = mapped_column()
    imagem: Mapped[str] = mapped_column()
    descricao: Mapped[str] = mapped_column()
    local: Mapped[str] = mapped_column()
    carregadores: Mapped[list[Carregador]] = relationship(lazy="subquery")
    
    @property
    def preco_medio(self) -> float:
        return sum(carregador.preco for carregador in self.carregadores) / len(self.carregadores)
    
    def json(self):
        proprio = {
            "nome": self.nome,
            "imagem": self.imagem,
            "preco_medio": self.preco_medio,
            "local": self.local,
            "descricao": self.descricao,
            "carregadores": list(map(lambda x: x.json(), self.carregadores))
        }
        base = super().json()
        proprio.update(base)
        return proprio