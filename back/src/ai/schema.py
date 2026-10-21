from enum import Enum

from pydantic import BaseModel, ConfigDict


class RespostaTipo(Enum):
    DUVIDA = 1
    SUPORTE = 2
    CRITICA = 3
    COMENTARIO = 4


class RespostaTema(Enum):
    PAGAMENTO = 1
    CARREGAMENTO = 2
    POSTO = 3


class AnaliseResposta(BaseModel):
    model_config = ConfigDict(use_attribute_docstrings=True)
    tipo: RespostaTipo
    tema: RespostaTema
    intencao_principal: str
    palavras_chaves: list[str]
    resumo: str

class Recomendacao(BaseModel):
    model_config = ConfigDict(use_attribute_docstrings=True)
    nome: str
    """nome do posto ou número do carregador"""
    motivo: str
    "motivo da escolha"

class AnalisePostos(BaseModel):
    model_config = ConfigDict(use_attribute_docstrings=True)
    recomendados: list[Recomendacao]
    """lista dos postos ou carregadores recomendados"""
    nao_recomendados: list[Recomendacao]
    """lista de postos ou carregadores não recomendados"""
    relatorio_geral: str
    """resumo geral sobre a situação dos postos"""

class Telemetria():
    localizacao: str
    