from abc import ABC, abstractmethod
from typing import Callable, Literal, Optional

from src.ai.dados import Mensagem

system_prompts = Literal["assets/prompts/system_prompt.md", "assets/prompts/analise_pergunta.md", "assets/prompts/relatorio.md"]

class AiAdapter(ABC):
    @abstractmethod
    def chamarDiretamente(self, prompt: str,historico: list[Mensagem] = [],  system: system_prompts="assets/prompts/system_prompt.md",  formato: Optional[dict] = None, dados: dict = {}) -> str:
        pass
    
    

    # @abstractmethod
    # def chamarStream(self, observador: Callable[[str], None], prompt: str, historico: list[Mensagem] = [], system: system_prompts="assets/prompts/system_prompt.md") -> str:
    #     pass
    
    