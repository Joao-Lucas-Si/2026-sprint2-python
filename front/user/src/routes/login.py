from typing import Any

import flet as ft

from src.components.alerta_erro import alerta_erro
from src.utils.request.http_request import CorpoJson
from src.utils.request.instanciar_request import instanciar_request
from src.components.campo_entrada import campo_entrada
from src.constants import Assets, Constantes, Cores


class LoginResposta(CorpoJson):
    id: int
    
    def converter(self) -> dict:
        return {
            "id": self.id
        }
        
    @staticmethod
    def instanciar(json: dict) -> Any:
        resposta = LoginResposta()
        
        resposta.id = json["id"]
        
        return resposta

@ft.component
def login():
    
    page = ft.context.page
    page.appbar = None
    page.update()
    async def redirecionar():
        id = await ft.SharedPreferences().get("id")
        if not id is None:
            page.navigate("/postos")
            page.update()
    ft.on_mounted(redirecionar)
    username =campo_entrada("email", ft.Icons.PERSON)
    password = campo_entrada("senha", ft.Icons.KEY, True)
    requisicao = instanciar_request(Constantes.HOST.value)
    async def on_sucess_login(e):
        if username.value == "" or password.value == "":
            alerta_erro("insirá as credenciais")
            
        elif not "@" in username.value:
            alerta_erro("email invalido")
        else:
            credenciais = {
                "email": username.value,
                "senha": password.value
            }
            
            resposta = requisicao.post_map("login", credenciais, LoginResposta)
            
            if resposta.id == -1:
                snackbar = ft.SnackBar(
                    content=ft.Text("credenciais invalidas"),
                    bgcolor=Cores.ERRO
                )
                snackbar.open = True
                page.overlay.append(snackbar)
                page.update()
            else:
                await ft.SharedPreferences().set("id", resposta.id)
                
                page.navigate("/postos")
                # page.update()
        # if username.value == "" and password.value == "":
        #     # page.controls.clear()

        #     snackbar_sucess = ft.SnackBar(
        #         content=ft.Text("O login foi um sucesso"),
        #         bgcolor=COLORS["success"],
        #         show_close_icon=True,
        #     )
        #     page.overlay.append(snackbar_sucess)
        #     snackbar_sucess.open = True
        #     page.update()
        # else:
        #     snackbar_error = ft.SnackBar(
        #         content=ft.Text("Credencias invalidas"),
        #         bgcolor=COLORS["error"],
        #         show_close_icon=True,
        #     )
        #     page.overlay.append(snackbar_error)
        #     snackbar_error.open = True
        #     page.update()

    button_login = ft.Button(
        "login",
        width=300,
        bgcolor=Cores.PRIMARIO_CLARO,
        color=Cores.TEXTO_PRIMARIO,
        on_click=on_sucess_login,
    )

    Button_cadastro = ft.TextButton(
        content=ft.Text(
            spans=[
                ft.TextSpan(
                    "Não tem uma Conta? ",
                    style=ft.TextStyle(
                        
                        size=14,
                    ),
                ),
                ft.TextSpan(
                    "Cadastre-se",
                    style=ft.TextStyle(
                        color=Cores.PRIMARIO_CLARO,
                        size=14,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
            ],
        ),
        on_click=lambda e: ft.context.page.navigate("/cadastro"),
    )

    return ft.Container(
            image=ft.DecorationImage(
                src=Assets.login_fundo, fit=ft.BoxFit.COVER
            ),
            expand=True,
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                controls=[username, password, button_login, Button_cadastro],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
