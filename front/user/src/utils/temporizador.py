from threading import Thread
from time import sleep
from typing import Any, Callable, Iterable, Mapping


class Temporizador(Thread):
    continuar = True
    tempo: float = 1
    codigo: Callable[[], None]

    def __init__(self, tempo:float, codigo: Callable[[], None],  group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = [], kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.tempo = tempo
        self.codigo = codigo
    
    def terminar(self):
        self.continuar = False
    
    def run(self) -> None:
        while self.continuar:
            self.codigo()
            sleep(self.tempo)