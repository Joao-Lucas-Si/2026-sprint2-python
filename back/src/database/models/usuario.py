from src.database.models.base import BaseModel
from src.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Usuario(BaseModel):
    __tablename__ = "usuarios"
    nome: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    senha: Mapped[str] = mapped_column()
    
Usuario().nome