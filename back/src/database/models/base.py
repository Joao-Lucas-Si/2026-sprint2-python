from abc import ABC
from datetime import datetime
from enum import Enum
from typing import Any

from src.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
import sqlalchemy

class Status(Enum):
    ATIVO="ativo"
    INATIVO="inativo"

class BaseModel(Base):
    __abstract__=True
    id: Mapped[int] = mapped_column( primary_key=True)
    status: Mapped[Status] = mapped_column(sqlalchemy.Enum(Status))
    data_criacao: Mapped[datetime] = mapped_column(server_default=func.now(),)
    data_atualizacao: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now()) 
    
    
    def json(self) -> dict:
        return {
            "id": self.id,
            "status": self.status.value
        }
    
    def __init__(self, **kw: Any):
        super().__init__(**kw)
        self.status = Status.ATIVO
        