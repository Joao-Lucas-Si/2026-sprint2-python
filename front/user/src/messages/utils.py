from src.messages.ingles import Ingles
from src.messages.base import Mensagens
from src.messages.internacionalizacao import Internacionalizacao
from src.messages.portugues import Portugues


class I18N(Internacionalizacao[Mensagens]):
    pass



i18n = I18N()

i18n.adicionar_lingua(Ingles())

i18n.adicionar_lingua(Portugues())


def obterTextos() -> Mensagens:
    return i18n.textos