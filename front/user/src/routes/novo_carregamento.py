import flet as ft
from src.utils.use_colors import usar_cores

@ft.component
def carregamento():
    Cores = usar_cores()
    page = ft.context.page
    page.title = "Elevo"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0
    page.bgcolor = Cores.FUNDO

    DADOS_PORCENTAGEM = {
        "rotulo": "Carregar até",
        "valor_principal": "50%",
        "chips": ["50%", "80%", "100%"],
        "rotulo_info_1": "Tempo estimado",
        "valor_info_1": "50 min",
        "rotulo_info_2": "Custo estimado",
        "valor_info_2": "R$ 30,00",
        "texto_link": "Prefiro definir por valor em R$  \u2197",
    }

    DADOS_VALOR = {
        "rotulo": "Valor a carregar",
        "valor_principal": "R$ 60",
        "chips": ["R$ 20", "R$ 50", "R$ 100"],
        "rotulo_info_1": "Energia estimada",
        "valor_info_1": "50 kWh",
        "rotulo_info_2": "Bateria estimada",
        "valor_info_2": "~100%",
        "texto_link": "Prefiro definir por porcentagem  \u2197",
    }

    estado = {"modo_valor": False, "largura_conteudo": 340}

    titulo = ft.Text(
        "Posto Av. Paulista",
        size=20,
        weight=ft.FontWeight.W_600,
        color=Cores.TEXTO,
    )

    rotulo_meta = ft.Text(
        DADOS_PORCENTAGEM["rotulo"],
        size=15,
        color=Cores.TEXTO_SECUNDARIO,
        text_align=ft.TextAlign.CENTER,
    )

    valor_principal = ft.Text(
        DADOS_PORCENTAGEM["valor_principal"],
        size=60,
        weight=ft.FontWeight.BOLD,
        color=Cores.PRIMARIO,
    )

    barra_fundo = ft.Container(
        width=estado["largura_conteudo"],
        height=10,
        border_radius=10,
        bgcolor=Cores.ICONE_INATIVO,
    )
    barra_preenchida = ft.Container(
        width=estado["largura_conteudo"] * 0.5,
        height=10,
        border_radius=10,
        bgcolor=Cores.PRIMARIO,
    )
    barra_progresso = ft.Stack(
        width=estado["largura_conteudo"],
        height=10,
        controls=[barra_fundo, barra_preenchida],
    )

    slider_carga = ft.Slider(
        min=0,
        max=100,
        value=50,
        width=estado["largura_conteudo"],
        active_color=Cores.PRIMARIO,
        inactive_color=Cores.ICONE_INATIVO,
        thumb_color=Cores.PRIMARIO_CLARO,
    )

    def criar_chip(texto: str, selecionado: bool = False):
        texto_chip = ft.Text(
            texto,
            size=15,
            color=Cores.TEXTO,
            weight=ft.FontWeight.W_500,
        )
        container_chip = ft.Container(
            content=texto_chip,
            width=104,
            height=54,
            alignment=ft.Alignment.CENTER,
            border_radius=12,
            bgcolor=Cores.CARD,
            border=ft.Border.all(
                2 if selecionado else 1,
                Cores.PRIMARIO if selecionado else Cores.DIVISOR,
            ),
        )
        return container_chip, texto_chip

    chip1_container, chip1_texto = criar_chip(DADOS_PORCENTAGEM["chips"][0], selecionado=True)
    chip2_container, chip2_texto = criar_chip(DADOS_PORCENTAGEM["chips"][1])
    chip3_container, chip3_texto = criar_chip(DADOS_PORCENTAGEM["chips"][2])

    chips_rapidos = ft.Row(
        controls=[chip1_container, chip2_container, chip3_container],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    def criar_coluna_info(rotulo_txt: str, valor_txt: str, alinhamento):
        texto_rotulo = ft.Text(rotulo_txt, size=13, color=Cores.TEXTO_SECUNDARIO)
        texto_valor = ft.Text(valor_txt, size=17, weight=ft.FontWeight.W_600, color=Cores.TEXTO)
        coluna = ft.Column(
            controls=[texto_rotulo, texto_valor],
            spacing=4,
            horizontal_alignment=alinhamento,
        )
        return coluna, texto_rotulo, texto_valor

    coluna_info_1, rotulo_info_1, valor_info_1 = criar_coluna_info(
        DADOS_PORCENTAGEM["rotulo_info_1"], DADOS_PORCENTAGEM["valor_info_1"], ft.CrossAxisAlignment.START
    )
    coluna_info_2, rotulo_info_2, valor_info_2 = criar_coluna_info(
        DADOS_PORCENTAGEM["rotulo_info_2"], DADOS_PORCENTAGEM["valor_info_2"], ft.CrossAxisAlignment.END
    )

    caixa_estimativas = ft.Container(
        width=estado["largura_conteudo"],
        padding=ft.Padding.symmetric(horizontal=20, vertical=16),
        border_radius=14,
        bgcolor=Cores.FUNDO_SECUNDARIO,
        content=ft.Row(
            controls=[coluna_info_1, coluna_info_2],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    texto_link = ft.Text(
        DADOS_PORCENTAGEM["texto_link"],
        size=14,
        weight=ft.FontWeight.W_500,
        color=Cores.PRIMARIO_CLARO,
        text_align=ft.TextAlign.CENTER,
    )

    def alternar_modo(e):
        estado["modo_valor"] = not estado["modo_valor"]
        dados = DADOS_VALOR if estado["modo_valor"] else DADOS_PORCENTAGEM

        rotulo_meta.value = dados["rotulo"]
        valor_principal.value = dados["valor_principal"]

        chip1_texto.value = dados["chips"][0]
        chip2_texto.value = dados["chips"][1]
        chip3_texto.value = dados["chips"][2]

        rotulo_info_1.value = dados["rotulo_info_1"]
        valor_info_1.value = dados["valor_info_1"]
        rotulo_info_2.value = dados["rotulo_info_2"]
        valor_info_2.value = dados["valor_info_2"]

        texto_link.value = dados["texto_link"]

        page.update()

    link_definir_valor = ft.Container(
        content=texto_link,
        alignment=ft.Alignment.CENTER,
        on_click=alternar_modo,
    )

    botao_confirmar = ft.Container(
        width=estado["largura_conteudo"],
        height=58,
        border_radius=14,
        gradient=Cores.gradiente(),
        alignment=ft.Alignment.CENTER,
        content=ft.Text(
            "Confirmar carga",
            size=16,
            weight=ft.FontWeight.W_600,
            color=Cores.TEXTO_PRIMARIO,
        ),
    )

    cartao = ft.Container(
        width=420,
        padding=ft.Padding.symmetric(horizontal=30, vertical=36),
        border_radius=24,
        bgcolor=Cores.CARD,
        border=ft.Border.all(1, Cores.CARD_BORDA),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=24,
            color=Cores.SOMBRA,
            offset=ft.Offset(0, 8),
        ),
        content=ft.Column(
            controls=[
                titulo,
                ft.Container(height=24),
                rotulo_meta,
                valor_principal,
                ft.Container(height=8),
                barra_progresso,
                slider_carga,
                ft.Container(height=6),
                chips_rapidos,
                ft.Container(height=20),
                caixa_estimativas,
                ft.Container(height=20),
                link_definir_valor,
                ft.Container(height=20),
                botao_confirmar,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
        ),
    )

    nav_inferior = ft.Container(
        padding=ft.Padding.symmetric(horizontal=30, vertical=16),
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=[
                "#FF6B4A",
                "#E8351C",
                "#C41E12",
            ],
            stops=[0.0, 0.5, 1.0],
        ),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Icon(ft.Icons.HOME_FILLED, color=Cores.TEXTO_PRIMARIO),
                ft.Icon(ft.Icons.MAP_OUTLINED, color=Cores.TEXTO_PRIMARIO),
                ft.Icon(ft.Icons.EV_STATION, color=Cores.TEXTO_PRIMARIO),
                ft.Icon(ft.Icons.HISTORY, color=Cores.TEXTO_PRIMARIO),
                ft.Icon(ft.Icons.PERSON_OUTLINE, color=Cores.TEXTO_PRIMARIO),
            ],
        ),
    )

    # área central: expande junto com a janela (expand=True), mas o padding
    # abaixo é o que GARANTE que sempre sobra fundo preto visível nas bordas
    area_central = ft.Container(
        content=cartao,
        alignment=ft.Alignment.CENTER,
        expand=True,
        padding=20,
    )

   

    # Responsividade: recalcula larguras com base no tamanho da janela
    MARGEM = 20                    # PRECISA ser igual ao padding do area_central acima
    LARGURA_MAXIMA_CARTAO = 420    # trava o cartão em telas grandes (senão ele "esparrama")

    def ajustar_layout(e=None):
        largura_janela = page.width or 480

        # espaço realmente livre dentro do container, descontando os 2 lados da margem
        espaco_disponivel = largura_janela - (MARGEM * 2)

        largura_cartao = min(LARGURA_MAXIMA_CARTAO, espaco_disponivel)
        largura_conteudo = largura_cartao - 60  # desconta padding lateral interno do cartão (30+30)

        estado["largura_conteudo"] = largura_conteudo

        cartao.width = largura_cartao
        barra_fundo.width = largura_conteudo
        barra_progresso.width = largura_conteudo
        barra_preenchida.width = largura_conteudo * (slider_carga.value / 100)
        slider_carga.width = largura_conteudo
        caixa_estimativas.width = largura_conteudo
        botao_confirmar.width = largura_conteudo

        page.update()

    page.on_resized = ajustar_layout
    ajustar_layout()

    return ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[area_central, nav_inferior],
        )
    
