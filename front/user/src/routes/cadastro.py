from typing import Any

import flet as ft

from src.components.alerta_erro import alerta_erro
from src.utils.request.http_request import CorpoJson
from src.utils.request.instanciar_request import instanciar_request
from src.constants import Assets, Constantes, Cores
from src.components.campo_entrada import campo_entrada


@ft.component
def cadastro():
    page = ft.context.page
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    requisicao = instanciar_request(Constantes.HOST.value)
    nome_completo = campo_entrada("nome", ft.Icons.PERSON)

    email_user = campo_entrada("email", ft.Icons.EMAIL)

    password = campo_entrada("senha", ft.Icons.LOCK, True)

    confirm_password = campo_entrada("confirmar senha", ft.Icons.LOCK, True)

    button_cadastrar = ft.Button(
        "Cadastrar",
        width=300,
        bgcolor=Cores.PRIMARIO_CLARO,
        color=Cores.TEXTO_PRIMARIO,
        on_click=lambda e: on_sucess_cadastro(e),
    )

    button_voltar_login = ft.TextButton(
        content=ft.Text(
            spans=[
                ft.TextSpan(
                    "Já tem uma Conta? ",
                    style=ft.TextStyle(
                        color=Cores.TEXTO_PRIMARIO,
                        size=14,
                    ),
                ),
                ft.TextSpan(
                    "Entrar",
                    style=ft.TextStyle(
                        color="#FD502D",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
            ],
        ),
        on_click=lambda e: page.navigate("/"),
    )

    def on_sucess_cadastro(e):
        if (
            nome_completo.value == ""
            or email_user.value == ""
            or password.value == ""
            or confirm_password.value == ""
        ):
            alerta_erro("confira se todos os campos estão preenchidos")
        elif not "@" in email_user.value:
            alerta_erro("email invalido")
        elif password.value != confirm_password.value:
            alerta_erro("Confira se as senhas estão iguais")
        else:
            snackbar_sucess = ft.SnackBar(
                content=ft.Text("O Cadastro foi um sucesso"),
                bgcolor=Cores.SUCESSO,
                show_close_icon=True,
            )
            page.overlay.append(snackbar_sucess)
            snackbar_sucess.open = True
            resposta = requisicao.post_map_dict(
                "cadastro",
                {
                    "nome": nome_completo.value,
                    "email": email_user.value,
                    "senha": password.value,
                },
            )
            if resposta.get("erro"):
                alerta_erro("usuário já existe")
                return
            page.navigate("/")

    return ft.Container(
        image=ft.DecorationImage(src=Assets.login_fundo, fit=ft.BoxFit.COVER),
        expand=True,
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            controls=[
                nome_completo,
                email_user,
                password,
                confirm_password,
                button_cadastrar,
                button_voltar_login,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )
