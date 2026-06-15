from abc import ABC, abstractmethod
from typing import TypeVar

from sqlalchemy.orm import sessionmaker

from src.database.models.base import BaseModel
from src.database.conexao import instanciarBanco

T = TypeVar("T", bound= BaseModel)

class BaseQuery[T](ABC):
    
    @abstractmethod
    def tabela(self) -> type[T]:
        pass
    
    def extras(self) -> list[type]:
        return []
    
    
    def _criar_sessao(self):
        Session = sessionmaker(bind=instanciarBanco())
        session = Session()
        
        return session
    def adicionar(self, linha: T):
        sessao = self._criar_sessao()
        
        sessao.add(linha)
        
        sessao.commit()
        sessao.close()
        
    def listarTodos(self) -> list[T]:
        
        sessao = self._criar_sessao()
        
        
        lista = sessao.query(self.tabela(), *self.extras()).all()
        
        sessao.close()
        
        return lista
    
    def obterPorId(self, id: int):
        sessao = self._criar_sessao()
        
        lista = sessao.query(self.tabela()).where(self.tabela().id==id).one_or_none() # type: ignore
        
        sessao.close()
        
        return lista
    

        
    def tamanho(self):
        sessao = self._criar_sessao()
        
        tamanho = sessao.query(self.tabela()).count()
        
        sessao.close()
        
        return tamanho