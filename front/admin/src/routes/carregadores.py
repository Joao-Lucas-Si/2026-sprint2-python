import flet as ft

from src.dados import Carregador
from src.routes.base.base_forma import BaseForm
from src.components.admin import badge_status
from src.routes.base.read_table import TabelaAdmin
from src.routes.dados import obter_carregador, obter_carregadores, obter_postos


@ft.component
def CarregadorForm():
    postos = obter_postos()
    return BaseForm(
        [
            [
                {
                    "label": "posto",
                    "icon": ft.Icons.CHARGING_STATION,
                    "get": lambda x: str(x.posto_id),
                    "set": lambda x, y: x.set_posto_id(int(y)),
                    "tipo": "selecao",
                    "opcoes": [(p.nome, str(p.id)) for p in postos]
                },
            ],
            [
                {
                    "label": "capacidade",
                    "icon": ft.Icons.BATTERY_FULL,
                    "get": lambda x: str(x.capacidade),
                    "set": lambda x, y: x.set_capacidade(int(y)),
                },
                {
                    "label": "disponivel",
                    "icon": ft.Icons.BATTERY_1_BAR,
                    "get": lambda x: str(x.disponivel),
                    "set": lambda x, y: x.set_disponivel(int(y)),
                },
            ],
            [
                {
                    "label": "ocupado",
                    "icon": ft.Icons.LOCK,
                    "get": lambda x: str(x.ocupado),
                    "set": lambda x, y: x.set_ocupado(bool(y)),
                },
                {
                    "label": "preço",
                    "icon": ft.Icons.MONEY,
                    "get": lambda x: str(x.preco),
                    "set": lambda x, y: x.set_preco(float(y)),
                },
            ],
        ],
        Carregador(0, 100, 1, 1000, False, 0, "Posto"),
        lambda x: obter_carregador(x),
        "carregadores"
    )


#  capacidade: int
#     disponivel: int
#     ocupado: bool
#     id: int
#     preco: float = 1.4
@ft.component
def CarregadoresTabela():
    carregadores = obter_carregadores()

    return TabelaAdmin(
        carregadores,
        [
            {
                "cabecalho": "posto",
                "celula": lambda x: {
                    "valor": x.posto,
                },
            },
            {
                "cabecalho": "disponivel",
                "celula": lambda x: {"valor": str(x.disponivel)},
            },
            {
                "cabecalho": "capacidade",
                "celula": lambda x: { "valor": str(x.capacidade) }
            },
            {
                "cabecalho": "ocupado",
                "celula": lambda x: {
                    "valor": "",
                    "content": badge_status("ocupado" if x.ocupado else "disponivel"),
                },
            },
            {
                "cabecalho": "preco",
                "celula": lambda x: {
                    "valor": str(f"R$ {x.preco:.2f}").replace(".", ",")
                },
            },
        ],
        "carregador",
        "/carregadores/form",
        "carregadores"
    )
