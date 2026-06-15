from typing import TypeVar, TypedDict

class TextosBase(TypedDict):
    pass
T = TypeVar("T", bound=TextosBase)

class Lingua[T]():
    nome: str
    textos: T

class Internacionalizacao[T]():
    __linguas: list[Lingua[T]] = []
    __atual: Lingua[T]
    
    @property
    def textos(self) -> T:
        return self.__atual.textos
    
    def mudar_idioma(self, alvo: str):
        dest = next(lingua for lingua in self.__linguas if lingua.nome == alvo)
        
        if dest:
            self.__atual = dest
        raise Exception("idioma não encontrado")
    
    def adicionar_lingua(self, lingua: Lingua[T]):
        self.__linguas.append(lingua)
        if len(self.__linguas) == 1:
            self.__atual = lingua