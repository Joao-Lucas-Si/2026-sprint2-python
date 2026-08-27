import flet as ft
from src.utils.use_colors import usar_cores
@ft.component
def detalhes_postos():
    Cores = usar_cores()
    page=ft.context.page
    page.title = "Carregadores"
    page.bgcolor = Cores.FUNDO
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    
   
    # JANELA MAXIMIZADA
    page.window.maximized = True  
    page.window.min_width = 600
    page.window.min_height = 600
   
    
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
                        src=r"imagem posto.png",
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
                                        content=ft.Icon(ft.Icons.ARROW_BACK, size=20 ,color="#EEEDED")
                                    ),
                                    ft.Container(expand=True),
                                    ft.Container(
                                        width=42, height=42,
                                        bgcolor="#EEEEEE",
                                        border_radius=25,
                                        content=ft.Icon(ft.Icons.FAVORITE_BORDER, size=19,color="#EEEDED")
                                    )
                                ]
                            ),
                            ft.Container(expand=True),
                            txt("Localização", 20, "#EEEEEE", True),
                            txt("Av. Paulista, São Paulo", 40, "white", True),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.LOCATION_ON, color="white", size=17),
                                    txt("Brasil", 12, "white"),
                                    ft.Container(width=15),
                                    ft.Icon(ft.Icons.STAR, color=Cores.MANUTENCAO, size=16),
                                    txt("5.0", 12, "white", True),
                                    txt("067reviews", 12, "white")
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
            controls=[
                ft.Column(
                    controls=[
                        txt("EletroPosto Central", 23,Cores.TEXTO,True),
                        txt("status: disponivel", 16, Cores.TEXTO, True)
                    ],
                    spacing=4
                ),
                ft.Container(expand=True),
                ft.Column(
                    controls=[
                        txt("horario de funcionamento", 14,Cores.TEXTO, True),
                        txt("10h às 22h", 16, Cores.TEXTO,True)
                    ],
                    spacing=3
                ),
                ft.Container(width=30),
                ft.Column(
                    controls=[
                        txt("Preço", 14, Cores.TEXTO, True),
                        txt("R$ 10,50", 16, Cores.TEXTO,True)
                    ],
                    spacing=3
                ),
                ft.Container(width=20),
                ft.Container(
                    width=150, height=48,
                    # bgcolor=Cores.DESLOCAMENTO,
                    bgcolor=Cores.PRIMARIO,
                    border_radius=25,
                    content=ft.Row(
                        controls=[
                            ft.Container(expand=True),
                            txt("IR", 12, "white", True),
                            ft.Icon(ft.Icons.ARROW_FORWARD, color="white", size=17),
                            ft.Container(expand=True)
                        ]
                    )
                )
            ]
        )
    )

    # DESCRIÇÃO
    descricao = ft.Container(
        content=ft.Column(
            controls=[
                txt("Sobre o local", 21, Cores.TEXTO,True),
                txt(
                    "Localizado no coração de São Paulo, na Avenida Paulista, "
                    "o EletroPosto Central oferece uma solução prática "
                    "e eficiente para motoristas de carros elétricos. "
                    "Atenção: O posto dispõe de poucas vagas cobertas, sujeitas à "
                    "disponibilidade no momento da chegada. "
                    "Aproveite a localização privilegiada para resolver seus "
                    "compromissos enquanto o seu veículo recarrega!.",
                    15,
                    Cores.TEXTO
                ),
            ],
            spacing=8
        )
    )

    
    # Sugestao

    titulo_roteiro = ft.Row(
        controls=[
            txt("Outros Postos de abastecimento", 21, Cores.TEXTO , True),
            ft.Container(expand=True),
            txt("Parceiros de Goodwe", 11, Cores.GRADIENTE_PRIMARIO, True)
        ]
    )

    
    # sugestao 1 
   

    sg1 = ft.Container(
        bgcolor=Cores.FUNDO_SECUNDARIO,
        border_radius=20,
        padding=15,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            width=90,
                            height=70,
                            border_radius=10,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            content=ft.Image(
                                src=r"posto2.jpeg",
                                fit=ft.BoxFit.COVER,
                            ),
                        ),
                        ft.Container(width=15),
                        ft.Column(
                            controls=[
                                txt("Zona Norte, São Paulo", 9,Cores.TEXTO, True),
                                txt("VoltPark Norte", 15, Cores.TEXTO,negrito=True),
                                txt("disponivel", 10, Cores.TEXTO)
                            ],
                            spacing=4
                        ),
                        ft.Container(expand=True),
                        ft.Icon(ft.Icons.KEYBOARD_ARROW_UP, size=22)
                    ]
                ),
                ft.Divider(height=10, color=Cores.TEXTO),
                txt("Preço", 10, Cores.TEXTO, True),
                txt("R$ 1,35/kWh",   11 , Cores.TEXTO),
                txt("Numero de vagas", 10, Cores.TEXTO, True),
                txt("3", 11 ,Cores.TEXTO),
            ],
            spacing=7
        )
    )

    
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
                                txt("5", 12, Cores.TEXTO , True)
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
                ft.Container(
                    height=55,
                    # bgcolor=Cores.DESLOCAMENTO,
                    bgcolor=Cores.PRIMARIO,
                    border_radius=28,
                    content=ft.Row(
                        controls=[
                            ft.Container(expand=True),
                            txt("Se deslocar", 20, "white", True),
                            ft.Icon(ft.Icons.ARROW_FORWARD, color="white", size=18),
                            ft.Container(expand=True)
                        ]
                    )
                )
            ],
            spacing=15
        )
    )

    
    # CONTEÚDO PRINCIPAL
   

    conteudo = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                cabecalho,
                imagem_principal,
                informacoes,
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                descricao,
                                ft.Container(height=20),
                                titulo_roteiro,
                                sg1,
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
    

