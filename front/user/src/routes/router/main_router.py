import flet as ft

from src.routes.tela_pagamento import tela_pagamento
from src.routes.cadastro import cadastro
from src.routes.login import login
from src.routes.abastecer import abastecer
from src.routes.carregadores import carregadores
from src.routes.carregamento import carregar
from src.routes.postos import postos
from src.messages.utils import obterTextos
from src.routes.novo_carregamento import carregamento
from src.routes.detalhes_postos import detalhes_postos
from src.routes.lista_postos import lista_postos
def main_router():
    return ft.Router(
        [
            ft.Route(index=True, component=login),
            ft.Route("cadastro", component=cadastro),
            ft.Route("pagamento", component=tela_pagamento),
            ft.Route(
                "postos",
                children=[
                    ft.Route(
                        index=True,
                        component=lista_postos,
                    ),
                    ft.Route(
                        ":postoId",
                        children=[
                            ft.Route(
                                index=True,
                                component=detalhes_postos,
                            ),
                            ft.Route(
                                ":carregadorId",
                                children=[
                                    ft.Route(
                                        index=True,
                                        component=carregamento,
                                    ),
                                    ft.Route(":energia", component=carregar),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
        manage_views=True
    )
