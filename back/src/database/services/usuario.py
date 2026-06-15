from src.database.models.usuario import Usuario
from src.database.services.base import BaseQuery


class UsuarioQuery(BaseQuery):
    def tabela(self) -> type:
        return Usuario
    
    def login(self, email: str, senha: str):
        sessao = self._criar_sessao()
        
        data = sessao.query(Usuario).where(Usuario.email == email, Usuario.senha == senha).one_or_none()
        
        sessao.close()
        
        return data
    
    def obterPorEmail(self, email: str):
        sessao = self._criar_sessao()
        
        data = sessao.query(Usuario).where(Usuario.email == email).one_or_none()
        
        sessao.close()
        
        return data