import flet as ft

from src.components.alerta_erro import alerta_erro
from src.components.cabecalho import criarCabecalho
from src.components.campo_entrada import campo_entrada


@ft.component
def abastecer():
    page = ft.context.page
    params = ft.use_route_params()
    postoId = params["postoId"]
    carregadorId = params["carregadorId"]

    criarCabecalho(lambda: page.navigate(f"/postos/{postoId}"))
    valor: str = ""
    campo = campo_entrada("quantidade", ft.Icons.STORAGE)

    def on_update(evento: ft.Event["ft.TextField"]):
        nonlocal valor
        valor = str(evento.data)

    def iniciar_carregamento():
        try:
            int(campo.value)
            page.navigate(f"/postos/{postoId}/{carregadorId}/{campo.value}")
        except:
            alerta_erro("o valor deve ser um número")

    return ft.SafeArea(
        ft.Container(
        ft.Column(
            [campo, ft.Button("carregar", on_click=iniciar_carregamento)],
            alignment=ft.MainAxisAlignment.CENTER,
            align=ft.Alignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        align=ft.Alignment.CENTER,
        expand=True,
        alignment=ft.Alignment(0, 0),
        ),
        expand=True
    )
