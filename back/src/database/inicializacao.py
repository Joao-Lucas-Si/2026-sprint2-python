from src.database.conexao import instanciarBanco
from src.database.base import Base
import src.database.models.usuario
import src.database.models.posto
import src.database.models.carregador
import src.database.models.pagamento
import src.database.models.recarga


def iniciarBanco():
    db = instanciarBanco()
    Base.metadata.create_all(db)