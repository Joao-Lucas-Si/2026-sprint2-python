from src.database.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.carregador import Carregador

class Posto(BaseModel):
    __tablename__="postos"
    nome: Mapped[str] = mapped_column()
    
    carregadores: Mapped[list[Carregador]] = relationship(lazy="subquery")
    
    
    def json(self):
        proprio = {
            "nome": self.nome,
            "carregadores": list(map(lambda x: x.json(), self.carregadores))
        }
        base = super().json()
        proprio.update(base)
        return proprio