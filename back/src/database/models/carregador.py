from sqlalchemy import ForeignKey

from src.database.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from back.src.database.models.posto import Posto

class Carregador(BaseModel):
    __tablename__="carregadores"
    capacidade: Mapped[int] = mapped_column()
    disponivel: Mapped[int] = mapped_column()
    ocupado: Mapped[bool] = mapped_column()
    
    posto_id: Mapped[int] = mapped_column(ForeignKey("postos.id"))
    
    @staticmethod
    def instanciar(capacidade: int, disponivel: int, ocupado: bool):
        instancia = Carregador()
        
        instancia.capacidade = capacidade
        instancia.disponivel = disponivel
        instancia.ocupado = ocupado

    
        return instancia 
        
    def json(self):
        return {
            "capacidade": self.capacidade,
            "disponivel": self.disponivel,
            "ocupado": self.ocupado
        }



    # posto: Mapped["Posto"] = relationship(back_populates="carregadores")