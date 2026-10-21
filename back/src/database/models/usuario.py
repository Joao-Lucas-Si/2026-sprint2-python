from enum import Enum
from typing import Literal
from src.database.models.base import BaseModel
from src.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

UsuarioRole = Literal["usuario", "admin", "dono"]
# class UsuarioRole(Enum):
#     USUARIO="usuario"
#     ADMIN="admin"
#     DONO="dono"

class Usuario(BaseModel):
    __tablename__ = "usuarios"
    nome: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    senha: Mapped[str] = mapped_column()
    role: Mapped[UsuarioRole] = mapped_column(default="usuario")
    def json(self, direto = True):
        return {
            "id": self.id,
            "nome": self.nome,
            "role": self.role,
            "email": self.email,
            **super().json(False)
        }
    