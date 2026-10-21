import flet as ft

from src.routes.carregadores import CarregadorForm, CarregadoresTabela
from src.routes.recargas import RecargasTabela
from src.routes.postos import PostoForm, PostosAdmin
from src.routes.layout import AdminLayout
from src.routes.dashboard import Dashboard
from src.routes.login import login
from src.routes.usuario import UsuarioTabela, UsuarioForm


def main_router():
    return ft.Router(
        [
            ft.Route(
                component=AdminLayout,
                outlet=True,
                children=[
                    ft.Route(
                        path="dashboard",
                        component=Dashboard,
                    ),
                    ft.Route(
                        path="postos",
                        children=[
                            ft.Route(
                                index=True,
                                component=PostosAdmin,
                            ),
                            ft.Route(
                                path="form",
                                children=[
                                    ft.Route(
                                        index=True,
                                        component=PostoForm,
                                    ),
                                    ft.Route(
                                        path=":id",
                                        component=PostoForm,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.Route(path="recargas", component=RecargasTabela),
                    ft.Route(
                        path="usuarios",
                        children=[
                            ft.Route(index=True, component=UsuarioTabela),
                            ft.Route(
                                path="form",
                                children=[
                                    ft.Route(
                                        index=True,
                                        component=UsuarioForm,
                                    ),
                                    ft.Route(
                                        path=":id",
                                        component=UsuarioForm,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.Route(
                        path="carregadores",
                        children=[
                            ft.Route(
                                index=True,
                                component=CarregadoresTabela,
                            ),
                            ft.Route(
                                path="form",
                                children=[
                                    ft.Route(index=True, component=CarregadorForm),
                                    ft.Route(path=":id", component=CarregadorForm),
                                ],
                            ),
                        ],
                    ),
                    # ft.Route(path="notificacoes", component=tela_em_breve("Notificações")),
                ],
            ),
        ],
        manage_views=True,
    )
