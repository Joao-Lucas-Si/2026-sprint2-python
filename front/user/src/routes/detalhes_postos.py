import flet as ft
from src.components.alerta_erro import alerta_erro
from src.utils.status_config import status_config
from src.components.navbar import navbar
from src.routes.postos import Carregador, Posto
from src.constants import Constantes
from src.utils.request.instanciar_request import instanciar_request
from src.utils.use_colors import usar_cores
@ft.component
def detalhes_postos():
    Cores = usar_cores()
    page=ft.context.page
    page.title = "Carregadores"
    page.bgcolor = Cores.FUNDO
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    
   
    # # JANELA MAXIMIZADA
    # page.window.maximized = True  
    # page.window.min_width = 600
    # page.window.min_height = 600
   
    params = ft.use_route_params()
    
    postoId = params["postoId"]
    requisicao = instanciar_request(Constantes.HOST.value)

    posto = requisicao.get_entidade(Constantes.OBTER_POSTO(postoId), Posto)
    #FUNÇÃO DE TEXTO
    
    def txt(
        texto,
        tamanho=14,
        cor="#222222",
        negrito=False
    ):
        return ft.Text(
            texto,
            size=tamanho,
            color=cor,
            weight=(
                ft.FontWeight.BOLD
                if negrito
                else ft.FontWeight.NORMAL
            )
        )


    # CABEÇALHO
    
    cabecalho = ft.Container(
        padding=25,
        content=ft.Row(
            controls=[
                # Logo / nome
                ft.Column(
                    controls=[
                        txt("Carregadores", 20, Cores.PRIMARIO, True),
                        txt("BRASIL", 9,Cores.FUNDO, True)
                    ],
                    spacing=0
                ),
                # Busca responsiva
                ft.Container(
                    expand=2,
                    height=45,
                    bgcolor=Cores.FUNDO_SECUNDARIO,
                    border_radius=25,
                    padding=10,
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.SEARCH, size=20, color="#EEEDED"),
                            txt("Procure carregadores", 15, Cores.TEXTO, True),
                            ft.Container(expand=True),
                        ]
                    )
                ),
                ft.Container(width=20),
                # Favoritos
                ft.Container(
                    width=45,
                    height=45,
                    bgcolor= Cores.PRIMARIO_CLARO,
                    border_radius=25,
                    content=ft.Icon(ft.Icons.FAVORITE_BORDER, size=21)
                ),
                ft.Container(width=10),
                ft.CircleAvatar(
                    radius=22,
                    bgcolor= Cores.PRIMARIO_CLARO,
                    content=txt("V", 15, "white", True)
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    largura, set_largura = ft.use_state(page.window.width or 0)
    page.appbar = ft.CupertinoAppBar(bgcolor=Cores.FUNDO, 
    trailing=ft.Row( width=100, spacing=10, controls= [ft.Container(
                    width=45,
                    height=45,
                    bgcolor= Cores.PRIMARIO_CLARO,
                    border_radius=25,
                    content=ft.Icon(ft.Icons.FAVORITE_BORDER, size=21)
                ),
                # ft.Container(width=10),
                ft.CircleAvatar(
                    radius=22,
                    bgcolor= Cores.PRIMARIO_CLARO,
                    content=txt("V", 15, "white", True)
                )]), 
                
                leading=ft.Column(
                    controls=[
                        txt("Carregadores", 20, Cores.PRIMARIO, True),
                        # txt("BRASIL", 9,Cores.FUNDO, True)
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.CENTER
                ), 
                title= ft.Container(
                    # expand=True,
                    width=largura - 100 - 40 - 50,
                    height=50,
                    bgcolor=Cores.FUNDO_SECUNDARIO,
                    border_radius=25,
                    padding=10,
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.SEARCH, size=20, color="#EEEDED"),
                            txt("Procure carregadores", 15, Cores.TEXTO, True),
                            ft.Container(expand=True),
                        ]
                    )
                ),)

    
    # IMAGEM PRINCIPAL
   
    imagem_principal = ft.Container(
        height=390,
        width=float("inf"),  
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        content=ft.Stack(
            controls=[
                
                ft.Container(
                    width=float("inf"),
                    height=390,
                    content=ft.Image(
                        src=posto.imagem,
                        fit=ft.BoxFit.COVER,
                    )
                ),
                # Escurece levemente a imagem

                ft.Container(
                    bgcolor="#000000dd",
                    border_radius=30,
                    width=float("inf")
                ),
                # Conteúdo sobre a imagem
                ft.Container(
                    padding=35,
                #       gradient=ft.LinearGradient(
                #                     begin=ft.Alignment.TOP_LEFT,
                #                     end=ft.Alignment(0.8, 1),
                #                     tile_mode=ft.GradientTileMode.MIRROR,
                #                     # rotation=math.pi / 3,
                #                     colors=[
                #                         Cores.PRIMARIO_CLARO_TRANSPARENT,
                #                         Cores.PRIMARIO_ESCURO_TRANSPARENT
                #                     ],
                #       ),
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment.TOP_CENTER,
                        end=ft.Alignment.BOTTOM_CENTER,
                        colors=[
                            "0x00000000",
                            "0xef000000"
                        ]
                    ),
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        width=42, height=42,
                                        bgcolor = Cores.FUNDO,
                                        border_radius=25,
                                        on_click=lambda : page.navigate("/postos"),
                                        content=ft.Icon(ft.Icons.ARROW_BACK, size=20 ,color="#EEEDED")
                                    ),
                                    # ft.Container(expand=True),
                                    # ft.Container(
                                    #     width=42, height=42,
                                    #     bgcolor="#EEEEEE",
                                    #     border_radius=25,
                                    #     content=ft.Icon(ft.Icons.FAVORITE_BORDER, size=19,color="#EEEDED")
                                    # )
                                ]
                            ),
                            ft.Container(expand=True),
                            # txt("Localização", 20, "#EEEEEE", True),
                            txt(posto.nome, 40, "white", True),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.LOCATION_ON, color="white", size=17),
                                    txt("Brasil", 12, "white"),
                                    ft.Container(width=15),
                                    ft.Icon(ft.Icons.STAR, color=Cores.MANUTENCAO, size=16),
                                    txt("5.0", 12, "white", True),
                                    txt("069 reviews", 12, "white")
                                ],
                                spacing=5
                            )
                        ]
                    )
                )
            ]
        )
    )

    
    
    informacoes = ft.Container(
        bgcolor=Cores.FUNDO_SECUNDARIO,
        border_radius=25,
        padding=25,
        content=ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                # ft.Column(
                #     controls=[
                #         txt("EletroPosto Central", 23,Cores.TEXTO,True),
                #         txt("status: disponivel", 16, Cores.TEXTO, True)
                #     ],
                #     spacing=4
                # ),
                # ft.Container(expand=True),
                ft.Column(
                    controls=[
                        txt("horario de funcionamento", 14,Cores.TEXTO, True),
                        txt("10h às 22h", 16, Cores.TEXTO,True)
                    ],
                    spacing=3
                ),
                # ft.Container(width=30),
                ft.Column(
                    controls=[
                        txt("Localização", 14, Cores.TEXTO, True),
                        txt(f"{posto.local}", 16, Cores.TEXTO,True)
                    ],
                    spacing=3
                ),
                # ft.Container(width=20),
                 ft.Column(
                    controls=[
                        txt("Preço médio", 14, Cores.TEXTO, True),
                        txt(f"R$ {posto.preco_medio:.2}", 16, Cores.TEXTO,True)
                    ],
                    spacing=3
                ),
                # ft.Container(
                #     width=150, height=48,
                #     # bgcolor=Cores.DESLOCAMENTO,
                #     bgcolor=Cores.PRIMARIO,
                #     border_radius=25,
                #     content=ft.Row(
                #         controls=[
                #             ft.Container(expand=True),
                #             txt("IR", 12, "white", True),
                #             ft.Icon(ft.Icons.ARROW_FORWARD, color="white", size=17),
                #             ft.Container(expand=True)
                #         ]
                #     )
                # )
            ]
        )
    )

    # DESCRIÇÃO
    descricao = ft.Container(
        content=ft.Column(
            controls=[
                txt("Sobre o local", 21, Cores.TEXTO,True),
                txt(
                    posto.descricao,
                    15,
                    Cores.TEXTO
                ),
            ],
            spacing=8
        )
    )

    
    # Sugestao

    # titulo_roteiro = ft.Row(
    #     controls=[
    #         txt("Outros Postos de abastecimento", 21, Cores.TEXTO , True),
    #         ft.Container(expand=True),
    #         txt("Parceiros de Goodwe", 11, Cores.GRADIENTE_PRIMARIO, True)
    #     ]
    # )

    
    # sugestao 1 
   
    def card_carregador(carregador: Carregador, i: int):
        disponivel = not carregador.ocupado
        status = "disponivel" if disponivel else "ocupado"
        texto_status, cor_status = status_config(status)
        pode_reservar = status == "disponivel"
        def click():
            if disponivel:
                page.navigate(f"/postos/{params["postoId"]}/{i}")
            else:
                alerta_erro("carregador indisponivel")
        return ft.Container(
        
        bgcolor=Cores.FUNDO_SECUNDARIO,
        
        border_radius=20,
        padding=15,
        content=ft.GestureDetector(on_tap=click, content= ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        # ft.Container(
                        #     width=90,
                        #     height=70,
                        #     border_radius=10,
                        #     clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        #     content=ft.Image(
                        #         src=r"posto2.jpeg",
                        #         fit=ft.BoxFit.COVER,
                        #     ),
                        # ),
                        ft.Icon(ft.Icons.EV_STATION, color=cor_status, size=50),
                        # ft.Container(width=15),
                        ft.Column(
                            controls=[
                                # txt("Zona Norte, São Paulo", 9,Cores.TEXTO, True),
                                txt(f"carregador {i + 1}", 15, Cores.TEXTO,negrito=True),
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
                                # txt("indisponivel" if  carregador.ocupado else "disponivel", 10, Cores.TEXTO)
                            ],
                            spacing=4
                        ),
                        ft.Container(expand=True),
                        ft.Icon(ft.Icons.KEYBOARD_ARROW_UP, size=22)
                    ]
                ),
                ft.Divider(height=10, color=Cores.TEXTO),
                txt("Preço", 10, Cores.TEXTO, True),
                txt(f"R$ {carregador.preco}/kWh",   11 , Cores.TEXTO),
                # txt("Capacidade", 10, Cores.TEXTO, True),
                # txt(f"{carregador.capacidade}", 11 ,Cores.TEXTO),
            ],
            spacing=7
        )
    ))

    sg1: list[ft.Control] = [card_carregador(carregador, i) for i, carregador in enumerate(posto.carregadores)]

    
    #  LATERAL
    

    painel_lateral = ft.Container(
        width=320,
        bgcolor=Cores.FUNDO_SECUNDARIO,
        border_radius=25,
        padding=22,
        content=ft.Column(
            controls=[
                txt("Detalhes", 19, Cores.TEXTO,True),
                ft.Divider(color="#FFFFFF"),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.CALENDAR_MONTH, size=20),
                        ft.Column(
                            controls=[
                                txt("fluxo de pessoas", 9,Cores.TEXTO),
                                txt("Alta", 12, Cores.TEXTO,True)
                            ],
                            spacing=2
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.GROUP, size=20),
                        ft.Column(
                            controls=[
                                txt("O local oferece uma ampla variedade de opções e serviços", 9,Cores.TEXTO),
                                txt("30 estabelecimentos parceiros", 12, Cores.TEXTO,True)
                            ],
                            spacing=2
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.LANGUAGE, size=20),
                        ft.Column(
                            controls=[
                                txt("Numero de carregadores", 9,Cores.TEXTO),
                                txt(f"{len(posto.carregadores)}", 12, Cores.TEXTO , True)
                            ],
                            spacing=2
                        )
                    ]
                ),
                ft.Container(height=10),
                ft.Container(
                    bgcolor=Cores.PRIMARIO,
                    border_radius=18,
                    padding=15,
                    content=ft.Column(
                        controls=[
                            txt("Vantagens exclusivas aplicáveis aos clientes assinantes", 14,  Cores.TEXTO,True),
                            txt("✓ Reservar a vaga com antecedência", 10,  Cores.TEXTO , True),
                            txt("✓ Cashback", 10,  Cores.TEXTO , True),
                        ],
                        spacing=7
                    )
                ),
                ft.Container(expand=True),
                # ft.Container(
                #     height=55,
                #     # bgcolor=Cores.DESLOCAMENTO,
                #     bgcolor=Cores.PRIMARIO,
                #     border_radius=28,
                #     content=ft.Row(
                #         controls=[
                #             ft.Container(expand=True),
                #             txt("Se deslocar", 20, "white", True),
                #             ft.Icon(ft.Icons.ARROW_FORWARD, color="white", size=18),
                #             ft.Container(expand=True)
                #         ]
                #     )
                # )
            ],
            spacing=15
        )
    )

    
    # CONTEÚDO PRINCIPAL
    navbar()

    conteudo = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                # cabecalho,
                imagem_principal,
                informacoes,
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                descricao,
                                ft.Container(height=20),
                                # titulo_roteiro,
                                ft.Column(sg1),
                            ],
                            spacing=15,
                            expand=True
                        ),
                        painel_lateral
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=25
                )
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH  
        )
    )

    
    # Pagina 
  

    return ft.Container(
            expand=True,
            padding=20,
            content=conteudo
        )
    

