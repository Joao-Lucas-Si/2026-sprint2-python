import flet as ft

from src.routes.cadastro import cadastro
from src.routes.login import login
from src.routes.abastecer import abastecer
from src.routes.carregadores import carregadores
from src.routes.carregamento import carregar
from src.routes.postos import postos
from src.messages.utils import obterTextos


def main_router():
    return ft.Router(
        [
            ft.Route(index=True, component=login),
            ft.Route("cadastro", component=cadastro),
            ft.Route(
                "postos",
                children=[
                    ft.Route(
                        index=True,
                        component=lambda: postos(),
                    ),
                    ft.Route(
                        ":postoId",
                        children=[
                            ft.Route(
                                index=True,
                                component=carregadores,
                            ),
                            ft.Route(
                                ":carregadorId",
                                children=[
                                    ft.Route(
                                        index=True,
                                        component=abastecer,
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
