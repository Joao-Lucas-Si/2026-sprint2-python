from abc import ABC, abstractmethod
from typing import Callable, TypeVar

from sqlalchemy.orm import Session, sessionmaker

from src.database.models.base import BaseModel
from src.database.conexao import instanciarBanco

T = TypeVar("T",  bound=BaseModel)

class BaseQuery[T](ABC):
    
    @abstractmethod
    def tabela(self) -> type[T]:
        pass
    
    def extras(self) -> list[type]:
        return []
    global_session: Session = None
    
    def _criar_sessao(self) -> Session:
        if BaseQuery.global_session:
            return BaseQuery.global_session    
        Session = sessionmaker(bind=instanciarBanco())
        session = Session()
        BaseQuery.global_session = session
        return session

    def remover(self, id: int):
        sessao = self._criar_sessao()

        sessao.query(self.tabela()).where(self.tabela().id == id).delete()  # pyright: ignore[reportAttributeAccessIssue]
        sessao.commit()

        # sessao.close()

    def adicionar(self, linha: T):
        sessao = self._criar_sessao()
        sessao.add(linha)
        sessao.commit()
        sessao.refresh(linha)
   
        sessao.expunge(linha)
        # sessao.close()

    
        
    def listarTodos(self) -> list[T]:
        
        sessao = self._criar_sessao()
        
        
        lista = sessao.query(self.tabela(), *self.extras()).all()
        
        # sessao.close()
        
        return lista

    def _idQuery(self, sessao: Session, id):
        return sessao.query(self.tabela()).where(self.tabela().id==id).one_or_none()# type: ignore
    
    def obterPorId(self, id: int):
        sessao = self._criar_sessao()
        
        lista = self._idQuery(sessao, id)
        
        # sessao.close()
        
        return lista
    
    def update(self, id: int, set: Callable[[T], None]):
        sessao = self._criar_sessao()

        row = self._idQuery(sessao, id)


        if row:
            set(row)

        sessao.commit()
        # sessao.close()
        
    def tamanho(self):
        sessao = self._criar_sessao()
        
        tamanho = sessao.query(self.tabela()).count()
        
        # sessao.close()
        
        return tamanho