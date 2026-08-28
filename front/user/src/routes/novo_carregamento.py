import flet as ft
from src.constants import Constantes
from src.routes.postos import Carregador, Posto
from src.utils.request.instanciar_request import instanciar_request
from src.utils.use_colors import usar_cores

def converter_energia_para_preco(valor: float, carregador: Carregador):
    return carregador.preco * valor


def converter_preco_para_energia(valor: float, carregador: Carregador):
    if valor == 0:
        return 0
    return valor / carregador.preco  

@ft.component
def carregamento():
    Cores = usar_cores()
    page = ft.context.page
    page.title = "Elevo"
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.padding = 0
    # page.bgcolor = Cores.FUNDO

    params = ft.use_route_params()
    postoId = params["postoId"]
    carregadorId = params["carregadorId"]
    requisicao = instanciar_request(Constantes.HOST.value)
    posto = requisicao.get_entidade(Constantes.OBTER_POSTO(postoId), Posto)
    modo, setModo = ft.use_state(True)
    carregador = posto.carregadores[int(carregadorId)]
    valor,setValor = ft.use_state(20.0)

    energia_max = 200

    max = energia_max * carregador.preco if modo else energia_max

    medio = max / 2

    inicial =1 / 4 *  max 

    DADOS_ENERGIA = {
        "rotulo": "Carregar até",
        "valor_principal": lambda x: f"{x:.2f}kW",
        "chips":  lambda x: f"{x:.2f}kW",
        "valores": [inicial, medio, max],
        "rotulo_info_1": "Tempo estimado",
        "valor_info_1": "50 min",
        "rotulo_info_2": "Custo estimado",
        "valor_info_2": f"R$ {converter_energia_para_preco(valor, carregador):.2f}",
        "texto_link": "Prefiro definir por valor em R$  \u2197",
    }

    DADOS_VALOR = {
        "rotulo": "Valor a carregar",
        "valor_principal": lambda x: f"R$ {x:.2f}",
        "chips": lambda x: f"R$ {x:.2f}",
        "valores": [inicial, medio,max],
        "rotulo_info_1": "Tempo estimado",
        "valor_info_1": "50 min",
        "rotulo_info_2": "Energia estimada",
        "valor_info_2": f"{converter_preco_para_energia(valor, carregador):.2f} kW",
       
        "texto_link": "Prefiro definir por energia  \u2197",
    }


    escolhido =DADOS_VALOR if modo else DADOS_ENERGIA

    estado = {"modo_valor": False, "largura_conteudo": 340}


    titulo = ft.Text(
        posto.nome,
        size=20,
        weight=ft.FontWeight.W_600,
        color=Cores.TEXTO,
    )

    rotulo_meta = ft.Text(
        escolhido["rotulo"],
        size=15,
        color=Cores.TEXTO_SECUNDARIO,
        text_align=ft.TextAlign.CENTER,
    )

    valor_principal = ft.Text(
        escolhido["valor_principal"](valor),
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
        max=max,
        value=valor,
        width=estado["largura_conteudo"],
        active_color=Cores.PRIMARIO,
        inactive_color=Cores.ICONE_INATIVO,
        thumb_color=Cores.PRIMARIO_CLARO,
        on_change=lambda x: setValor(x.control.value or 0)
    )

    def criar_chip(texto: str, i: int):
        selecionado = valor == escolhido["valores"][i]
        texto_chip = ft.Text(
            texto,
            size=15,
            color=Cores.TEXTO,
            weight=ft.FontWeight.W_500,
        )
        container_chip = ft.GestureDetector(on_tap=lambda : setValor(escolhido["valores"][i]), content=ft.Container(
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
        ))
        return container_chip, texto_chip



    chips: list[ft.Control] = []

    for i, val in enumerate(escolhido["valores"]):
        chip1_container, chip1_texto = criar_chip(escolhido["chips"](val), i)
        chips.append(chip1_container)
    # chip2_container, chip2_texto = criar_chip(escolhido["chips"][1], 1)
    # chip3_container, chip3_texto = criar_chip(escolhido["chips"][2], 2)

    chips_rapidos = ft.Row(
        controls=chips,
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
        escolhido["rotulo_info_1"], escolhido["valor_info_1"], ft.CrossAxisAlignment.START
    )
    coluna_info_2, rotulo_info_2, valor_info_2 = criar_coluna_info(
        escolhido["rotulo_info_2"], escolhido["valor_info_2"], ft.CrossAxisAlignment.END
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
        escolhido["texto_link"],
        size=14,
        weight=ft.FontWeight.W_500,
        color=Cores.PRIMARIO_CLARO,
        text_align=ft.TextAlign.CENTER,
    )

    def alternar_modo(e):
        estado["modo_valor"] = not estado["modo_valor"]
        if modo:
            setValor(converter_preco_para_energia(valor, carregador))
        else:
            setValor(converter_energia_para_preco(valor, carregador))
        setModo(not modo)
        
        # dados = DADOS_VALOR if estado["modo_valor"] else DADOS_PORCENTAGEM

        # rotulo_meta.value = dados["rotulo"]
        # valor_principal.value = dados["valor_principal"]

        # chip1_texto.value = dados["chips"][0]
        # chip2_texto.value = dados["chips"][1]
        # chip3_texto.value = dados["chips"][2]

        # rotulo_info_1.value = dados["rotulo_info_1"]
        # valor_info_1.value = dados["valor_info_1"]
        # rotulo_info_2.value = dados["rotulo_info_2"]
        # valor_info_2.value = dados["valor_info_2"]

        # texto_link.value = dados["texto_link"]

        # page.update()

    link_definir_valor = ft.Container(
        content=texto_link,
        alignment=ft.Alignment.CENTER,
        on_click=alternar_modo,
    )

    async def carregar():
        energia = converter_preco_para_energia(valor, carregador) if modo else valor
        preco = converter_energia_para_preco(valor, carregador) if not modo else valor
        id = await ft.SharedPreferences().get("id")
        requisicao.post_map_sem("/recargas/add", {
            "usuario": id,
            "preco": preco,
            "quantidade": energia,
            "preco_kwh": carregador.capacidade,
            "carregador": carregador.id
        })
        page.navigate(f"/postos/{postoId}/{carregadorId}/{int(energia)}")

    botao_confirmar = ft.GestureDetector(on_tap=carregar, content=ft.Container(
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
    ))

    botao_voltar = ft.GestureDetector(on_tap=lambda : page.navigate(f"/postos/{postoId}/"), content=ft.Container(
        width=estado["largura_conteudo"],
        height=58,
        border_radius=14,
        gradient=Cores.gradiente(),
        alignment=ft.Alignment.CENTER,
        content=ft.Text(
            "Cancelar",
            size=16,
            weight=ft.FontWeight.W_600,
            color=Cores.TEXTO_PRIMARIO,
        ),
    ))

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
                botao_voltar
                
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
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

    def ajustar_layout():
        largura_janela = page.width or 480

        # espaço realmente livre dentro do container, descontando os 2 lados da margem
        espaco_disponivel = largura_janela - (MARGEM * 2)

        largura_cartao = min(LARGURA_MAXIMA_CARTAO, espaco_disponivel)
        largura_conteudo = largura_cartao - 60  # desconta padding lateral interno do cartão (30+30)

        estado["largura_conteudo"] = largura_conteudo

        cartao.width = largura_cartao
        barra_fundo.width = largura_conteudo
        barra_progresso.width = largura_conteudo
        barra_preenchida.width = largura_conteudo * ( (slider_carga.value or 1) / max)
        slider_carga.width = largura_conteudo
        caixa_estimativas.width = largura_conteudo
        botao_confirmar.width = largura_conteudo

        page.update()

    page.on_resized = ajustar_layout
    ajustar_layout()
    page.bottom_appbar = None
    page.appbar = None
    # page.overlay.append()
    # ft.CupertinoNavigationBar()
 
    return ft.SafeArea(ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[area_central],
        ))
    
