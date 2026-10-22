"""
Layout do admin: sidebar fixa à esquerda + área de conteúdo à direita.

Dashboard e Postos NÃO repetem a sidebar. O Router renderiza este
componente em volta delas (rota de layout) e ele encaixa a tela atual
na área de conteúdo com `use_route_outlet()`.
"""
import asyncio

import flet as ft
from src.hooks.use_is_admin import use_is_admin
from src.utils.use_colors import usar_cores
from src.routes.dados import MENU_ADMIN

LARGURA_SIDEBAR = 260


def _rota_ativa(rota_item: str) -> bool:
    # "/admin" só é ativo quando é exatamente "/admin" (senão ficaria
    # aceso em todas as telas, já que todas começam com /admin).
    # if rota_item == "/admin":
    #     return rota_atual.rstrip("/") == "/admin"
    return ft.is_route_active(rota_item)
    # return rota_atual.startswith(rota_item)


def item_menu(item: dict, ativo: bool, ao_clicar) -> ft.Container:
    T = usar_cores()
    Cores=  usar_cores()
    cor = T.TEXTO_PRIMARIO if ativo else T.TEXTO_SECUNDARIO
    return ft.Container(
        on_click=lambda e: ao_clicar(item["rota"]),
        ink=True,
        height=46,
        border_radius=12,
        padding=ft.Padding.symmetric(horizontal=14),
        gradient=Cores.gradiente() if ativo else None,
        content=ft.Row(
            spacing=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(getattr(ft.Icons, item["icone"]), size=20, color=cor),
                ft.Text(
                    item["rotulo"],
                    size=14,
                    weight=ft.FontWeight.W_600 if ativo else ft.FontWeight.W_500,
                    color=cor,
                ),
            ],
        ),
    )


def construir_sidebar(rota_atual: str, ao_navegar, notificacoes_nao_lidas: int = 0) -> ft.Container:
    itens = []
    Cores = usar_cores()
    T = usar_cores()
    is_admin = use_is_admin()
    for item in MENU_ADMIN:
        if not "isAdmin" in item or (item["isAdmin"] == True and is_admin):
            linha = item_menu(item, _rota_ativa( item["rota"]), ao_navegar)
            if item["rota"] == "/admin/notificacoes" and notificacoes_nao_lidas:
                linha = ft.Stack(
                    controls=[
                        linha,
                        ft.Container(
                            right=12,
                            top=13,
                            bgcolor=Cores.PRIMARIO_ESCURO,
                            border_radius=10,
                            padding=ft.Padding.symmetric(horizontal=7, vertical=1),
                            content=ft.Text(
                                str(notificacoes_nao_lidas),
                                size=11,
                                weight=ft.FontWeight.BOLD,
                                color=T.TEXTO_PRIMARIO,
                            ),
                        ),
                    ]
                )
            itens.append(linha)

    topo = ft.Row(
        spacing=12,
        controls=[
            ft.Container(
                width=40,
                height=40,
                border_radius=20,
                gradient=Cores.gradiente(),
                alignment=ft.Alignment.CENTER,
                content=ft.Text("EV", size=13, weight=ft.FontWeight.BOLD, color=T.TEXTO_PRIMARIO),
            ),
            ft.Column(
                spacing=0,
                controls=[
                    ft.Text("Elevo", size=16, weight=ft.FontWeight.W_600, color=T.TEXTO),
                    ft.Text("Painel admin", size=12, color=T.TEXTO_SECUNDARIO),
                ],
            ),
        ],
    )

    def logout(e):
        ft.context.page.run_task(ft.SharedPreferences().remove, "admin.id")
        ao_navegar("/")
        print("vack")


    rodape = item_menu(
        {"rota": "/", "rotulo": "Sair", "icone": "LOGOUT"},
        ativo=False,
        ao_clicar=logout,
    )

    return ft.Container(
        width=LARGURA_SIDEBAR,
        bgcolor=T.FUNDO_SECUNDARIO,
        padding=20,
        content=ft.Column(
            expand=True,
            spacing=8,
            controls=[
                topo,
                ft.Container(height=20),
                *itens,
                ft.Container(expand=True),  # empurra o "Sair" pro fim
                rodape,
            ],
        ),
    )


@ft.component
def AdminLayout():
    page = ft.context.page
    T  = usar_cores()
    page.bgcolor = T.FUNDO
    page.padding = 0

    rota_atual = ft.use_route_location()
    conteudo = ft.use_route_outlet()

    return ft.Row(
        expand=True,
        spacing=0,
        # vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            construir_sidebar(
                rota_atual,
                ao_navegar=lambda x: page.navigate(x),
                notificacoes_nao_lidas=2, 
            ),
            ft.Container(expand=True, padding=24, content=conteudo),
        ],
    )
