from typing import Any

import flet as ft
from src.components.alerta_erro import alerta_sucesso
from src.routes.postos import Carregador, Posto
from src.constants import Constantes
from src.utils.request.http_request import CorpoJson
from src.utils.request.instanciar_request import instanciar_request
from src.utils.use_colors import usar_cores


def borda_all(width, color):
    return ft.Border.all(width=width, color=color)

# APLICAÇÃO

class Recarga(CorpoJson):
    preco_kwh: float
    preco: float
    quantidade: float
    carregador: Carregador
    posto: Posto

    @staticmethod
    def instanciar(json: dict) -> Any:
        recarga = Recarga()

        recarga.preco = json["preco"]
        recarga.quantidade = json["quantidade"]
        recarga.preco_kwh = json["preco_kwh"]
        recarga.posto = Posto.instanciar(json["posto"])
        return recarga

@ft.component
def tela_pagamento():
    Cores = usar_cores()
    page= ft.context.page
    page.title = "Link de pagamento"

    page.padding = 0
    page.spacing = 0

    page.bgcolor = Cores.FUNDO
    page.theme_mode = ft.ThemeMode.DARK

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

   
    # TEMA ATUAL (Fixo no Escuro)
    

    def tema():
        return Cores

    
    # LARGURA RESPONSIVA
   

    def largura_conteudo():
        largura = page.width

        if largura is None or largura <= 0:
            largura = 800

        # Celular
        if largura <= 500:
            return max(280, largura - 32)

        # Tablet
        if largura <= 900:
            return largura - 64

        # Desktop
        return min(560, largura - 80)

    
    # ÍCONE SIMPLES
    

    def icone(simbolo, tamanho=44) -> ft.Control:
        t = tema()

        return ft.Container(
            width=tamanho,
            height=tamanho,
            bgcolor=t.FUNDO_SECUNDARIO,
            border_radius=tamanho / 2,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        simbolo,
                        size=18,
                        color=Cores.PRIMARIO,
                    )
                ],
            ),
        )

    
    # HEADER
    

    def header():
        t = tema()

        return ft.Container(
            # width=largura_conteudo(),
            padding=16,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        expand=True,
                        spacing=4,
                        controls=[
                            ft.Text(
                                "Escolha como quer pagar",
                                size=25,
                                weight=ft.FontWeight.W_600,
                                color=t.TEXTO,
                            ),
                            ft.Text(
                                "Selecione o método de pagamento",
                                size=12,
                                color=t.TEXTO_SECUNDARIO,
                            ),
                        ],
                    ),
                ],
            ),
        )

    
    # BARRA SUPERIOR

    page.appbar = ft.CupertinoAppBar(bgcolor=Cores.CARD, trailing= ft.Container(
                        padding=8,
                        border_radius=20,
                        width=25,
                        bgcolor="#2ECC7118",
                        content=ft.Row(
                            spacing=6,
                            controls=[
                                ft.Container(
                                    width=7,
                                    height=7,
                                    bgcolor=Cores.DISPONIVEL,
                                    border_radius=4,
                                ),
                                
                                
                            ],
                        ),
                    ), leading= ft.Container(
                        width=42,
                        height=42,
                        border_radius=21,
                        gradient=Cores.gradiente(),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "G",
                                    size=20,
                                    color="#FFFFFF",
                                    weight=ft.FontWeight.BOLD,
                                )
                            ],
                        ),
                    ),)

    def top_bar():
        t = tema()

        return ft.Container(
            width=page.width,
            height=68,
            bgcolor=t.CARD,
            padding=12,
            border=ft.Border(
                bottom=ft.BorderSide(
                    1,
                    t.DIVISOR,
                )
            ),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # Logo
                    ft.Container(
                        width=42,
                        height=42,
                        border_radius=21,
                        gradient=Cores.gradiente(),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "G",
                                    size=20,
                                    color="#FFFFFF",
                                    weight=ft.FontWeight.BOLD,
                                )
                            ],
                        ),
                    ),
                    ft.Container(width=12),
                    ft.Column(
                        spacing=1,
                    ),
                    ft.Container(expand=True),
                    # Status
                    ft.Container(
                        padding=8,
                        border_radius=20,
                        bgcolor="#2ECC7118",
                        content=ft.Row(
                            spacing=6,
                            controls=[
                                ft.Container(
                                    width=7,
                                    height=7,
                                    bgcolor=Cores.DISPONIVEL,
                                    border_radius=4,
                                ),
                                
                                
                            ],
                        ),
                    ),
                ],
            ),
        )

    
    # BOTÃO PRINCIPAL
    

    def botao_principal():
        t = tema()

        return ft.Container(
            width=largura_conteudo(),
            height=52,
            border_radius=9,
            gradient=Cores.gradiente(),
            ink=True,
            on_click=informar_valor,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Continuar Pagamento",
                        size=15,
                        weight=ft.FontWeight.W_600,
                        color=Cores.TEXTO_PRIMARIO,
                    )
                ],
            ),
        )

    
    # CARD DE PAGAMENTO
    

    def card_pagamento():
        valor = sum([recarga.preco for recarga in recargas])
        t = tema()

        return ft.Container(
            width=largura_conteudo(),
            bgcolor=t.CARD,
            border_radius=14,
            border=borda_all(1, t.CARD_BORDA),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=18,
                color=t.SOMBRA,
                offset=ft.Offset(0, 5),
            ),
            padding=24,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    ft.Text(
                        "Resumo do Pedido",
                        size=14,
                        weight=ft.FontWeight.W_600,
                        color=t.TEXTO,
                    ),
                    ft.Container(height=18),
                    # Valor
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "R$",
                                size=22,
                                color=t.TEXTO_SECUNDARIO,
                            ),
                            ft.Container(width=8),
                            ft.Text(
                                f"{valor:.2f}",
                                size=48,
                                weight=ft.FontWeight.W_300,
                                color=t.TEXTO,
                            ),
                        ],
                    ),
                    ft.Container(height=6),
                    ft.Text(
                        "Total a pagar com impostos inclusos",
                        size=11,
                        color=t.TEXTO_SECUNDARIO,
                    ),
                    # ft.Container(height=22),
                    # botao_principal(),
                ],
            ),
        )

    
    # CARD DE OPÇÃO (MÉTODO DE PAGAMENTO)
    
    def card_recarga(recarga: Recarga):
        t = tema()
        titulo_controles: list[ft.Control] = [
            ft.Text(
                f"recarga em {recarga.posto.nome}",
                size=14,
                weight=ft.FontWeight.W_600,
                color=t.TEXTO,
            )
        ]

        # if badge:
        #     titulo_controles.append(
        #         ft.Container(
        #             bgcolor=Cores.PRIMARIO,
        #             border_radius=5,
        #             padding=4,
        #             content=ft.Text(
        #                 badge,
        #                 size=8,
        #                 color=Cores.TEXTO_PRIMARIO,
        #                 weight=ft.FontWeight.BOLD,
        #             ),
        #         )
        #     )

        return ft.Container(
            width=largura_conteudo(),
            height=85,
            bgcolor=t.CARD,
            border_radius=12,
            border=borda_all(1, t.CARD_BORDA),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=14,
                color=t.SOMBRA,
                offset=ft.Offset(0, 4),
            ),
            ink=True,
            # on_click=on_click,
            padding=12,
            content=ft.Row(
                spacing=14,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # icone(simbolo, 44),
                    ft.Image(src=recarga.posto.imagem, border_radius=10, width=80),
                    ft.Column(
                        expand=True,
                        spacing=4,
                        
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                spacing=7,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=titulo_controles,
                            ),
                            ft.Text(
                                f"valor: {recarga.preco:.2f}$",
                                size=13,
                                color=Cores.SUCESSO,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                f"energia abastecida: {recarga.quantidade:.2f}kW",
                                size=11,
                                color=Cores.TEXTO_SECUNDARIO,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            # ft.Text(
                            #     f"data: {recarga.:.2f}kW",
                            #     size=11,
                            #     color=Cores.TEXTO_SECUNDARIO,
                            #     max_lines=1,
                            #     overflow=ft.TextOverflow.ELLIPSIS,
                            # ),
                        ],
                    ),
                    ft.Text(
                        "*",
                        size=26,
                        color=t.ICONE_INATIVO,
                    ),
                ],
            ),
        )

    def card_opcao(
        simbolo,
        titulo,
        descricao,
        badge=None,
        on_click=None,
    ):
        t = tema()
        titulo_controles: list[ft.Control] = [
            ft.Text(
                titulo,
                size=14,
                weight=ft.FontWeight.W_600,
                color=t.TEXTO,
            )
        ]

        if badge:
            titulo_controles.append(
                ft.Container(
                    bgcolor=Cores.PRIMARIO,
                    border_radius=5,
                    padding=4,
                    content=ft.Text(
                        badge,
                        size=8,
                        color=Cores.TEXTO_PRIMARIO,
                        weight=ft.FontWeight.BOLD,
                    ),
                )
            )

        return ft.Container(
            width=largura_conteudo(),
            height=76,
            bgcolor=t.CARD,
            border_radius=12,
            border=borda_all(1, t.CARD_BORDA),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=14,
                color=t.SOMBRA,
                offset=ft.Offset(0, 4),
            ),
            ink=True,
            on_click=on_click,
            padding=12,
            content=ft.Row(
                spacing=14,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    icone(simbolo, 44),
                    ft.Column(
                        expand=True,
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                spacing=7,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=titulo_controles,
                            ),
                            ft.Text(
                                descricao,
                                size=11,
                                color=Cores.TEXTO_SECUNDARIO,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ],
                    ),
                    ft.Text(
                        "›",
                        size=26,
                        color=t.ICONE_INATIVO,
                    ),
                ],
            ),
        )

    
    # FOOTER


    def footer():
        t = tema()

        return ft.Container(
            width=largura_conteudo(),
            padding=20,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Pagamento seguro",
                        size=10,
                        color=t.TEXTO_SECUNDARIO,
                    ),
                    ft.Text(
                        " • ",
                        size=10,
                        color=t.ICONE_INATIVO,
                    ),
                    ft.Text(
                        "Criptografia de ponta a ponta",
                        size=10,
                        color=t.TEXTO_SECUNDARIO,
                    ),
                ],
            ),
        )

   
    # AÇÕES DOS MÉTODOS DE PAGAMENTO
    async def pagar(forma: str):
        id = await ft.SharedPreferences().get("id")
        requisicao.post_map_sem("pagar", {
            "forma": forma,
            "usuario": id
        })
        initRecargas()

    async def pagar_pix(e):
        await pagar("pix")
        alerta_sucesso("Pagamento com Pix efetuado")
        # print("Método selecionado: PIX")

    async def pagar_cartao(e):
        await pagar("credito")
        alerta_sucesso("Pagamento com cartão efetuado")
        # print("Método selecionado: Cartão de Crédito")

    def ver_fatura(e):
        print("Método selecionado: Fatura")
  

    def informar_valor(e):
        print("Avançar para preenchimento de dados")

    
    # RECONSTRUIR
    requisicao = instanciar_request(Constantes.HOST.value)
    defl: list[Recarga] = []
    recargas, setRecargas = ft.use_state(defl)

    def initRecargas():
        setRecargas(requisicao.get_lista("/recargas/dividas" ,Recarga ))

    ft.use_effect(initRecargas, [ ])

    def rebuild():
        Cores = tema()
        page.bgcolor = Cores.FUNDO
 

        # Corpo central com os métodos de pagamento
        corpo = ft.Column(
            width=largura_conteudo(),
            # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
            controls=[
                header(),
                card_pagamento(),
                card_opcao(
                    "⚡",
                    "Pix",
                    "Aprovação instantânea • Sem taxas",
                    badge="POPULAR",
                    on_click=pagar_pix,
                ),
                
                card_opcao(
                    "💳",
                    "Cartão de Crédito",
                    "Pagar na fatura",
                    on_click=pagar_cartao,
                ),
                # card_opcao(
                #     "🧾",
                #     "ver fatura",
                #     "faturas",
                #     on_click=ver_fatura,
                # ),
                
                ft.Container(padding=ft.Padding.only(left=20), content=ft.Column( spacing=2, controls=[

                    ft.Text("Dividas", size=25),
                    ft.Text("todas as recargas aindas não pagas", color=Cores.TEXTO_SECUNDARIO, size=12),
                ])),

                ft.Column([card_recarga(recarga) for recarga in recargas]),
                footer(),
            ],
        )

        # Área principal
        principal = ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
               
                ft.Column(
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[corpo],
                ),
            ],
        )

        return principal
        

    
    # RESPONSIVIDADE
    

    def on_resize(e):
        rebuild()

    page.on_resize = on_resize

    
    # INICIALIZAÇÃO
    

    return rebuild()

