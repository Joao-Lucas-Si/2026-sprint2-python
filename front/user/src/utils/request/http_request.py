from abc import ABC, abstractmethod
import os
from threading import Thread
from typing import Any, Callable, TypeVar


class CorpoJson():

    @staticmethod
    @abstractmethod
    def instanciar(json: dict) -> Any:
        pass

    @abstractmethod
    def converter(self) -> dict:
        pass


T = TypeVar("T", bound=CorpoJson)

I = TypeVar("I", bound=CorpoJson)

D= TypeVar("D")


class HttpRequest(ABC):
    host: str
    
    def __init__(self, host: str) -> None:
        super().__init__()
        self.host = host

    def caminhoFinal(self, caminho: str):
        return os.path.join(self.host, caminho)

    def assincrono[J](
        self, func: Callable[[], J], receptor: Callable[[J], None]
    ) -> None:
        class Tarefa(Thread):
            def run(self) -> None:
                data = func()

                receptor(data)

        tarefa = Tarefa()

        tarefa.start()

    @abstractmethod
    def get_entidade(self, caminho: str, data: type[T]) -> T:
        pass

    @abstractmethod
    def get_lista(self, caminho: str, data: type[T]) -> list[T]:
        pass
    
    @abstractmethod
    def post_sem(self, caminho: str, data: T) -> None:
        pass
    
    @abstractmethod
    def post_map_sem(self, caminho: str, data: dict) -> None:
        pass
    
    @abstractmethod
    def post_map(self, caminho: str, data: dict, resposta: type[T]) -> T:
        pass
    
    @abstractmethod
    def post_map_dict(self, caminho: str, data: dict) -> dict:
        pass
    
    
    
