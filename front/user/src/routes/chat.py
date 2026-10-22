from datetime import datetime
import flet as ft

from src.constants import Constantes
from src.utils.request.instanciar_request import instanciar_request
from src.components.navbar import navbar
from src.utils.use_colors import usar_cores

# colors.FUNDO = "#121316"  # Fundo geral escuro
SIDEBAR = "#1B1C22"  # Fundo da barra
CARD_BG = "#23252E"  # Fundo dos cards
# colors.PRIMARIO = "#FF452B"  # Laranja/vermelho
WHITE = "#FFFFFF"  # Tex principais
# TEXT = "#E0E0E5"  # Tex normais
MUTED = "#8E8F99"  # Tex secundários
# colors.CARD_BORDA = "#2C2D38"  # Bordas discretas
GREEN = "#27AE78"  #  online
BLUE = "#3B82F6"  #  suporte


def pad(left=0, top=0, right=0, bottom=0):
    return ft.Padding(
        left=left,
        top=top,
        right=right,
        bottom=bottom,
    )


@ft.component
def chatbot():
    page = ft.context.page
    # page.title = "Central de Suporte"
    # page.theme_mode = ft.ThemeMode.DARK
    # page.bgcolor = colors.FUNDO
    # page.padding = 0
    # page.spacing = 0
    # page.window.width = 1440
    # page.window.height = 900
    # page.window.min_width = 950
    # page.window.min_height = 650
    navbar()
    colors = usar_cores()
    current = datetime.now()
    a, set_a = ft.use_state("")
    messages, set_messages = ft.use_state(
        [
            {
                "agent": True,
                "name": "Suporte",
                "text": (
                    "Olá, sou o energyAi!\n\n"
                    "Bem-vindo à nossa central de suporte. "
                    "Estou aqui para ajudar você."
                ),
                "time": f"{current.hour}:{current.minute}",
            },
            # {
            #     "agent": True,
            #     "name": "Suporte",
            #     "text": (
            #         "Para começarmos o seu atendimento, "
            #         "escolha com qual equipe deseja falar:"
            #     ),
            #     "time": f"{current.hour}:{current.minute}",
            # },
        ]
    )

    selected_team = {"value": "Atendimento geral"}
    ticket_number = "SUP-2026-1042"
    closed = {"value": False}

    #  AUXILIARES

    @ft.component
    def txt(value, size=12, color=colors.TEXTO, bold=False):
        return ft.Text(
            str(value),
            size=size,
            color=color,
            weight=ft.FontWeight.BOLD if bold else ft.FontWeight.NORMAL,
        )

    def notify(message):
        ft.context.page.show_dialog(ft.SnackBar(content=ft.Text(message)))

    def close_dialog():
        ft.context.page.pop_dialog()

    @ft.component
    def divider():
        return ft.Container(
            height=1,
            bgcolor=colors.CARD_BORDA,
        )

    @ft.component
    def badge(value, fg=colors.PRIMARIO, bg="#2E1C20"):
        return ft.Container(
            bgcolor=bg,
            border_radius=20,
            padding=pad(10, 5, 10, 5),
            content=txt(value, 10, fg, True),
        )

    # MENU LATERAL

    @ft.component
    def menu_item(icon, title, selected=False, count=None):
        items = [
            ft.Icon(
                icon,
                size=19,
                color=WHITE if selected else MUTED,
            ),
            txt(
                title,
                12,
                WHITE if selected else MUTED,
                selected,
            ),
            ft.Container(expand=True),
        ]

        if count is not None:
            items.append(
                ft.Container(
                    bgcolor=colors.PRIMARIO if selected else "#2D2E38",
                    border_radius=12,
                    padding=pad(7, 3, 7, 3),
                    content=txt(count, 10, WHITE, True),
                )
            )

        return ft.Container(
            bgcolor=colors.PRIMARIO if selected else None,
            border_radius=8,
            padding=pad(12, 12, 12, 12),
            content=ft.Row(controls=items, spacing=10),
            on_click=lambda e: notify(f"Seção selecionada: {title}"),
        )


    conversation_header = ft.Container(
        bgcolor=colors.FUNDO,
        padding=pad(20, 14, 20, 14),
        border=ft.Border(bottom=ft.BorderSide(1, colors.CARD_BORDA)),
        content=ft.Row(
            controls=[
                ft.CircleAvatar(
                    content=ft.Icon(
                        ft.Icons.SMART_TOY_OUTLINED,
                        color=WHITE,
                        size=23,
                    ),
                    bgcolor=colors.PRIMARIO,
                    radius=24,
                ),
                ft.Column(
                    controls=[
                        txt("Suporte", 14, WHITE, True),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    width=8,
                                    height=8,
                                    bgcolor=GREEN,
                                    border_radius=10,
                                ),
                                txt("Online agora", 10, GREEN),
                            ],
                            spacing=5,
                        ),
                    ],
                    spacing=4,
                ),
                ft.Container(expand=True),
                badge("Atendimento em andamento", colors.PRIMARIO, "#2E1C20"),
                ft.IconButton(
                    icon=ft.Icons.MORE_VERT,
                    icon_color=MUTED,
                    tooltip="Opções",
                    on_click=lambda e: notify("Opções do atendimento"),
                ),
            ],
            spacing=10,
        ),
    )

    # MENSAGENS

    @ft.component
    def message_bubble(message):
        agent = message["agent"]

        avatar = ft.CircleAvatar(
            content=ft.Icon(
                (ft.Icons.SMART_TOY_OUTLINED if agent else ft.Icons.PERSON),
                size=18,
                color=WHITE,
            ),
            bgcolor=colors.PRIMARIO if agent else "#383B47",
            radius=17,
        )

        bubble = ft.Container(
            width=440,
            bgcolor=CARD_BG if agent else "#2B2D38",
            border=ft.Border.all(
                1,
                colors.CARD_BORDA,
            ),
            border_radius=12,
            padding=pad(14, 14, 14, 12),
            content=ft.Column(
                controls=[
                    txt(
                        message["name"],
                        10,
                        colors.PRIMARIO if agent else WHITE,
                        True,
                    ),
                    ft.Text(
                        message["text"],
                        size=12,
                        color=colors.TEXTO,
                        selectable=True,
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(expand=True),
                            txt(message["time"], 9, MUTED),
                            (
                                ft.Icon(
                                    ft.Icons.DONE_ALL,
                                    size=13,
                                    color=colors.PRIMARIO,
                                )
                                if not agent
                                else ft.Container()
                            ),
                        ],
                        spacing=4,
                    ),
                ],
                spacing=8,
                tight=True,
            ),
        )

        if agent:
            return ft.Row(
                controls=[
                    avatar,
                    bubble,
                    ft.Container(expand=True),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )

        return ft.Row(
            controls=[
                ft.Container(expand=True),
                bubble,
                avatar,
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    message_input = ft.TextField(
        hint_text="Digite sua mensagem.......",
        multiline=True,
        min_lines=1,
        max_lines=4,
        expand=True,
        text_size=12,
        border_color=colors.CARD_BORDA,
        focused_border_color=colors.PRIMARIO,
        bgcolor=CARD_BG,
        border_radius=10,
        content_padding=pad(12, 10, 12, 10),
    )

    def send_message(e=None):
        content = (message_input.value or "").strip()

        if not content:
            return

        # if closed["value"]:
        #     notify("O atendimento está encerrado.")
        #     return

        now = datetime.now().strftime("%H:%M")

        messages.append(
            {
                "agent": False,
                "name": "usuario",
                "text": content,
                "time": now,
            }
        )

        set_messages(lambda x: [*messages])
        set_a(a + "a")

        requisicao = instanciar_request(Constantes.HOST.value)


        resposta = requisicao.post_dict_str("chat", {
            "pergunta": content
        })

        messages.append(
            {
                "agent": True,
                "name": "assistente",
                "text": resposta,
                "time": now,
            }
        )
        # print(messages)
        # message_input.value = ""
        set_messages(lambda x: [*messages])
        set_a(a + "a")
        print("send")
        # render_messages()

    composer = ft.Container(
        bgcolor=colors.FUNDO,
        padding=pad(15, 12, 15, 15),
        border=ft.Border(top=ft.BorderSide(1, colors.CARD_BORDA)),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        # ft.IconButton(
                        #     icon=ft.Icons.ATTACH_FILE,
                        #     icon_color=MUTED,
                        #     tooltip="Anexar arquivo",
                        #     on_click=lambda e: notify(
                        #         "O envio de arquivos precisa de integração."
                        #     ),
                        # ),
                        # ft.IconButton(
                        #     icon=ft.Icons.IMAGE_OUTLINED,
                        #     icon_color=MUTED,
                        #     tooltip="Enviar imagem",
                        #     on_click=lambda e: notify(
                        #         "O envio de imagens precisa de integração."
                        #     ),
                        # ),
                        ft.Container(expand=True),
                        txt(
                            "Atendimento seguro",
                            10,
                            MUTED,
                        ),
                        ft.Icon(
                            ft.Icons.LOCK_OUTLINE,
                            size=14,
                            color=GREEN,
                        ),
                    ],
                    spacing=3,
                ),
                ft.Row(
                    controls=[
                        message_input,
                        ft.Button(
                            content=ft.Row(
                                controls=[
                                    txt("Enviar", 12, WHITE, True),
                                    ft.Icon(
                                        ft.Icons.SEND_ROUNDED,
                                        size=16,
                                        color=WHITE,
                                    ),
                                ],
                                spacing=7,
                            ),
                            bgcolor=colors.PRIMARIO,
                            on_click=send_message,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    spacing=10,
                ),
            ],
            spacing=6,
        ),
    )

    # PAINEL DE DETALHES

    @ft.component
    def detail_row(icon, title, value):
        return ft.Row(
            controls=[
                ft.Container(
                    width=34,
                    height=34,
                    bgcolor="#2B2D38",
                    border_radius=8,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(
                        icon,
                        size=17,
                        color=colors.PRIMARIO,
                    ),
                ),
                ft.Column(
                    controls=[
                        txt(title, 10, MUTED),
                        txt(value, 11, WHITE, True),
                    ],
                    spacing=3,
                    expand=True,
                ),
            ],
            spacing=10,
        )

    def end_ticket(e=None):
        def confirm_end(ev):
            closed["value"] = True
            close_dialog()
            notify("Atendimento encerrado.")

        page.show_dialog(
            ft.AlertDialog(
                modal=True,
                title=ft.Text("Encerrar atendimento?"),
                content=ft.Text("Deseja realmente encerrar esta conversa?"),
                actions=[
                    ft.TextButton(
                        "Cancelar",
                        on_click=lambda ev: close_dialog(),
                    ),
                    ft.Button(
                        content="Encerrar",
                        on_click=confirm_end,
                    ),
                ],
            )
        )

    details_panel = ft.Container(
        width=270,
        bgcolor=CARD_BG,
        padding=pad(18, 18, 18, 18),
        border=ft.Border(left=ft.BorderSide(1, colors.CARD_BORDA)),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        txt(
                            "Detalhes do atendimento",
                            13,
                            WHITE,
                            True,
                        ),
                        ft.Container(expand=True),
                        ft.Icon(
                            ft.Icons.MORE_HORIZ,
                            color=MUTED,
                        ),
                    ],
                ),
                ft.Container(height=8),
                ft.Container(
                    alignment=ft.Alignment(0, 0),
                    content=ft.CircleAvatar(
                        content=ft.Text(
                            "TA",
                            size=20,
                            color=WHITE,
                        ),
                        bgcolor=colors.PRIMARIO,
                        radius=35,
                    ),
                ),
                ft.Column(
                    controls=[
                        ft.Container(
                            alignment=ft.Alignment(0, 0),
                            content=txt(
                                "Tiago Assis",
                                14,
                                WHITE,
                                True,
                            ),
                        ),
                        ft.Container(
                            alignment=ft.Alignment(0, 0),
                            content=txt(
                                "tiago.assis@email.com",
                                10,
                                MUTED,
                            ),
                        ),
                        ft.Container(
                            alignment=ft.Alignment(0, 0),
                            content=badge(
                                "Cliente ativo",
                                GREEN,
                                "#1A2E25",
                            ),
                        ),
                    ],
                    spacing=8,
                ),
                ft.Container(height=5),
                divider(),
                ft.Container(height=4),
                txt("INFORMAÇÕES", 9, MUTED, True),
                detail_row(
                    ft.Icons.CONFIRMATION_NUMBER_OUTLINED,
                    "Protocolo",
                    ticket_number,
                ),
                detail_row(
                    ft.Icons.CATEGORY_OUTLINED,
                    "Categoria",
                    selected_team["value"],
                ),
                detail_row(
                    ft.Icons.PRIORITY_HIGH,
                    "Prioridade",
                    "Normal",
                ),
                detail_row(
                    ft.Icons.CALENDAR_TODAY_OUTLINED,
                    "Data de abertura",
                    "14 out. 2026",
                ),
                detail_row(
                    ft.Icons.TIMER_OUTLINED,
                    "Tempo de resposta",
                    "Aguardando equipe",
                ),
                ft.Container(height=5),
                divider(),
                ft.Container(height=5),
                txt("AÇÕES", 9, MUTED, True),
                ft.Button(
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.HELP_OUTLINE,
                                size=17,
                                color=colors.PRIMARIO,
                            ),
                            txt(
                                "Central de ajuda",
                                11,
                                WHITE,
                            ),
                        ],
                        spacing=8,
                    ),
                    on_click=lambda e: notify(
                        "Configure aqui o endereço da central de ajuda."
                    ),
                ),
                ft.Button(
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.CANCEL_OUTLINED,
                                size=17,
                                color="#E54D42",
                            ),
                            txt(
                                "Encerrar conversa",
                                11,
                                "#E54D42",
                            ),
                        ],
                        spacing=8,
                    ),
                    on_click=end_ticket,
                ),
                ft.Container(expand=True),
                ft.Container(
                    bgcolor=colors.FUNDO,
                    border_radius=10,
                    padding=pad(12, 12, 12, 12),
                    border=ft.Border.all(1, colors.CARD_BORDA),
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(
                                        ft.Icons.LIGHTBULB_OUTLINE,
                                        size=18,
                                        color=colors.PRIMARIO,
                                    ),
                                    txt(
                                        "Dica rápida",
                                        11,
                                        WHITE,
                                        True,
                                    ),
                                ],
                                spacing=7,
                            ),
                            txt(
                                "Guarde o número do protocolo para consultar seu atendimento.",
                                10,
                                MUTED,
                            ),
                        ],
                        spacing=8,
                    ),
                ),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
    )

    # PAINEL CENTRAL

    # MONTAGEM FINAL DA TELA

    # render_messages()
    return ft.SafeArea(
        
        ft.Row(
        controls=[
            # sidebar,
            ft.Column(
                # bgcolor=colors.PRIMARIO,
                controls=[
                    # header,
                    ft.Row(
                        controls=[
                            ft.Container(
                                expand=True,
                                expand_loose=True,
                                # bgcolor=colors.PRIMARIO,
                                # alignment=ft.Alignment.,
                                
                                content=ft.Column(
                                    expand_loose=True,
                                    run_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    # horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                    
                                    controls=[
                                        conversation_header,
                                        ft.Container(
                                            expand=True,
                                            expand_loose=True,
                                            # bgcolor=colors.PRIMARIO,
                                            padding=pad(20, 20, 20, 20),
                                            content=ft.ListView(
                                                        controls=[
                                                            message_bubble(message)
                                                            for message in messages
                                                        ],
                                                        spacing=18,
                                                        scroll=ft.ScrollMode.AUTO,
                                                        expand=True,
                                                    ),
                                                    # quick_options,
                                            
                                        ),
                                        composer,
                                    ],
                                    spacing=0,
                                    expand=True,
                                ),
                            ),
                            # details_panel,
                        ],
                        spacing=0,
                        expand=True,
                        expand_loose=True,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                spacing=0,
                expand_loose=True,
                expand=True,
            ),
        ],
        spacing=0,
        expand=True,
        expand_loose=True,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
    ),
    expand=True,
    expand_loose=True,
    
    )
