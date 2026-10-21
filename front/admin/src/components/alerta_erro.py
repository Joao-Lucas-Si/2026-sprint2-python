import flet as ft

from src.constants import Cores

def alerta_erro(mensagem: str):
    page = ft.context.page
    snackbar_error = ft.SnackBar(
        content=ft.Text(mensagem),
        bgcolor=Cores.ERRO,
        show_close_icon=True,
    )
    page.overlay.append(snackbar_error)
    snackbar_error.open = True
    page.update()


def alerta_sucesso(mensagem: str):
    page = ft.context.page
    snackbar = ft.SnackBar(
        content=ft.Text(mensagem),
        bgcolor=Cores.SUCESSO
    )
    snackbar.open = True
    page.overlay.append(snackbar)
    page.update()