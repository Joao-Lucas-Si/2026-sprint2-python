import flet as ft
from src.utils.status_config import status_config
from src.components.navbar import navbar
from src.constants import Constantes
from src.routes.postos import Carregador, Posto
from src.utils.request.instanciar_request import instanciar_request
from src.utils.use_colors import usar_cores
 
 
# Dados de exemplo dos postos de recarga
# status pode ser: "disponivel", "ocupado" ou "manutencao"
# postos = [
#     {
#         "nome": "EletroPosto Central",
#         "local": "Av. Paulista, São Paulo",
#         "imagem": "https://picsum.photos/seed/posto1/200/200",
#         "preco": "R$ 1,20/kWh",
#         "tipo": "RÁPIDO",
#         "status": "disponivel",
#     },
#     {
#         "nome": "Shopping Recarga Sul",
#         "local": "Zona Sul, São Paulo",
#         "imagem": "https://picsum.photos/seed/posto2/200/200",
#         "preco": "R$ 0,95/kWh",
#         "tipo": "PADRÃO",
#         "status": "ocupado",
#     },
#     {
#         "nome": "VoltPark Norte",
#         "local": "Zona Norte, São Paulo",
#         "imagem": "https://picsum.photos/seed/posto3/200/200",
#         "preco": "R$ 1,35/kWh",
#         "tipo": "RÁPIDO",
#         "status": "disponivel",
#     },
#     {
#         "nome": "Posto Verde Energia",
#         "local": "Alphaville, Barueri",
#         "imagem": "https://picsum.photos/seed/posto4/200/200",
#         "preco": "R$ 1,10/kWh",
#         "tipo": "PADRÃO",
#         "status": "manutencao",
#     },
# ]
 
 


 
@ft.component
def lista_postos():
    Cores = usar_cores()
    page= ft.context.page
    page.title = "Postos de Recarga"
    page.bgcolor = Cores.FUNDO # fundo da pagina 
    page.padding = 0
    page.scroll = ft.ScrollMode.HIDDEN

 
    def selecionar_posto(posto: Posto):
        def handler(e):
            page.navigate(f"/postos/{posto.id}")
            #     ft.SnackBar(
            #         ft.Text(f"Navegando até {nome}..."),
            #         bgcolor=Cores.PRIMARIO,
            #     )
            # )
        return handler

    @ft.component
    def criar_card_posto(posto: Posto) -> ft.Container:
        disponivel = any([not carregador.ocupado for carregador in posto.carregadores])
        status = "disponivel" if disponivel else "ocupado"
        texto_status, cor_status = status_config(status)
        pode_reservar = status == "disponivel"
        # pode_reservar = True
 
        return ft.Container(
            bgcolor=Cores.CARD,
            border_radius=16,
            padding=12,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # Imagem do posto
                    ft.Container(
                        content=ft.Image(
                            src=posto.imagem,
                            width=70,
                            height=70,
                            fit=ft.BoxFit.COVER,
                            border_radius=12,
                        ),
                        border_radius=12,
                    ),
                    ft.Container(width=12),
                    # Infos do posto
                    ft.Column(
                        expand=True,
                        spacing=2,
                        controls=[
                            # ft.Text(
                            #     posto.tipo,
                            #     size=10,
                            #     weight=ft.FontWeight.BOLD,
                            #     color=Cores.TEXTO_SECUNDARIO,
                            #     style=ft.TextStyle(letter_spacing=1),
                            # ),
                            ft.Text(
                                posto.nome,
                                size=15,
                                weight=ft.FontWeight.W_600,
                                color=Cores.TEXTO,
                            ),
                            ft.Row(
                                spacing=4,
                                controls=[
                                    ft.Icon(
                                        ft.Icons.LOCATION_ON,
                                        size=13,
                                        color=Cores.TEXTO_SECUNDARIO,
                                    ),
                                    ft.Text(
                                        posto.local,
                                        size=12,
                                        color=Cores.TEXTO_SECUNDARIO,
                                    ),
                                ],
                            ),
                            ft.Container(height=4),
                            ft.Row(
                                spacing=6,
                                controls=[
                                    ft.Container(
                                        bgcolor=cor_status,
                                        border_radius=20,
                                        padding=ft.Padding.symmetric(
                                            horizontal=8, vertical=3
                                        ),
                                        content=ft.Text(
                                            texto_status,
                                            size=10,
                                            weight=ft.FontWeight.BOLD,
                                            color=Cores.FUNDO,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    
                    
                    
                    
                    # Preço e botão
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        spacing=8,
                        controls=[
                            ft.Text(
                                f"R$ {posto.preco_medio:0.2f}/kWh",
                                size=13,
                                weight=ft.FontWeight.BOLD,
                                color=Cores.TEXTO,
                            ),
                            ft.FilledButton(
                                content=ft.Text(
                                    "Reservar" if pode_reservar else "Indisponível",
                                    size=12,
                                ),
                                bgcolor=Cores.SUCESSO
                                if pode_reservar
                                else Cores.PRIMARIO_ESCURO,
                                color=Cores.TEXTO
                                if pode_reservar
                                else Cores.TEXTO_SECUNDARIO,
                                # disabled=not pode_reservar,
                                on_click=selecionar_posto(posto),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10)
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
 
    # Cabeçalho ---------------------------------------------------------------------------------------------------------------------
    
    
    cabecalho = ft.Container(
        expand=1,
        padding=ft.Padding(left=20, right=20, top=20, bottom=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
               
                ft.Icon(ft.Icons.SEARCH, color=Cores.TEXTO),
            ],
        ),
    )
 

    page.appbar = ft.CupertinoAppBar( bgcolor=Cores.FUNDO, padding=ft.Padding.symmetric(horizontal=20), leading=ft.Text(
                            "Postos de Recarga",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=Cores.TEXTO,
                        ),trailing=ft.Icon(ft.Icons.SEARCH, color=Cores.TEXTO))

    # Lista de cards
    navbar()
    requisicao = instanciar_request(Constantes.HOST.value)
    
    postos = requisicao.get_lista("postos", Posto)

    # postos.extend(postos)
    lista_postos = ft.ListView(
        expand=1,
        # height=page.window.height * 0.8,
        # height=float("inf") * 0.8,
        spacing=14,
        scroll=ft.ScrollMode.ALWAYS,
        padding=ft.Padding.symmetric(horizontal=20),
        controls=[criar_card_posto(p) for p in postos],
    )
 

   
    return ft.SafeArea(
        lista_postos
        # ft.Column(
        #     expand=True,
        #     # height=float("inf"),
        #     # height=page.window.height,
        #     spacing=0,
        #     # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        #     controls=[
        #         cabecalho,
        #         lista_postos,
        #         # nav_inferior,
        #     ],
        # )
    )
    
 
 
 