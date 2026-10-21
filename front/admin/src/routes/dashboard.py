"""Tela 1 do admin: dashboard com estatísticas."""
import flet as ft
# from paleta_app import Cores, TemaEscuro
from src.dados import Recarga
from src.components.admin import card, kpi_card, titulo_secao
from src.routes.dados import (
    obter_kpis,
    obter_ocupacao,
    obter_recargas_semana,
    obter_ultimas_recargas,
)
from src.utils.use_colors import usar_cores

# T = TemaEscuro

ALTURA_MAX_BARRA = 160
ALTURA_CARDS_MEIO = 340  # os dois cards da linha do meio têm a mesma altura


def faixa_kpis(kpis: list[dict]) -> ft.Row:
    return ft.Row(
        spacing=16,
        controls=[kpi_card(k["rotulo"], k["valor"], k["delta"]) for k in kpis],
    )


def grafico_barras(dados: list[dict]) -> ft.Row:
    """
    Gráfico de barras desenhado com Containers (sem dependência extra).
    A altura de cada barra é proporcional ao maior valor da lista.
    Para um gráfico "de verdade" depois, instale o pacote flet-charts.
    """
    T = usar_cores()
    Cores = usar_cores()
    maximo = max(d["total"] for d in dados) or 1
    colunas = []
    for d in dados:
        altura = max(6, int(ALTURA_MAX_BARRA * d["total"] / maximo))
        colunas.append(
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.END,
                spacing=6,
                controls=[
                    ft.Text(str(d["total"]), size=11, color=T.TEXTO_SECUNDARIO),
                    ft.Container(
                        width=28,
                        height=altura,
                        border_radius=6,
                        gradient=Cores.gradiente(ft.Alignment.TOP_CENTER, ft.Alignment.BOTTOM_CENTER),
                    ),
                    ft.Text(d["dia"], size=11, color=T.TEXTO_SECUNDARIO),
                ],
            )
        )
    return ft.Row(
        controls=colunas,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.END,
        height=ALTURA_MAX_BARRA + 50,
    )


def card_recargas_semana(dados: list[dict]) -> ft.Container:
    T = usar_cores()
    total = sum(d["total"] for d in dados)
    return card(
        ft.Column(
            spacing=16,
            controls=[
                titulo_secao("Recargas na semana"),
                ft.Text(f"{total}", size=28, weight=ft.FontWeight.W_600, color=T.TEXTO),
                grafico_barras(dados),
            ],
        ),
        expand=2,
        altura=ALTURA_CARDS_MEIO,
    )


def card_ocupacao(fracao: float) -> ft.Container:
    T = usar_cores()
    Cores = usar_cores()
    return card(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
            controls=[
                titulo_secao("Ocupação agora"),
                ft.Stack(
                    width=140,
                    height=140,
                    controls=[
                        ft.ProgressRing(
                            value=fracao,
                            width=140,
                            height=140,
                            stroke_width=12,
                            color=Cores.PRIMARIO,
                            bgcolor=T.ICONE_INATIVO,
                        ),
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text(
                                f"{fracao * 100:.0f}%",
                                size=28,
                                weight=ft.FontWeight.W_600,
                                color=T.TEXTO,
                            ),
                        ),
                    ],
                ),
                ft.Text("dos carregadores em uso", size=12, color=T.TEXTO_SECUNDARIO),
            ],
        ),
        expand=1,
        altura=ALTURA_CARDS_MEIO,
    )


def linha_recarga(r: Recarga) -> ft.Container:
    T = usar_cores()
    return ft.Container(
        padding=ft.Padding.symmetric(vertical=10),
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    expand=True,
                    spacing=2,
                    controls=[
                        ft.Text(r.posto.nome, size=14, weight=ft.FontWeight.W_500, color=T.TEXTO),
                        ft.Text(
                            f'{r.usuario.nome} · {str(round(r.quantidade, 1)).replace(".", ",")} kWh',
                            size=12,
                            color=T.TEXTO_SECUNDARIO,
                        ),
                    ],
                ),
                ft.Text(f"R$ {r.preco:.2f}".replace(".", ","), size=14, weight=ft.FontWeight.W_600, color=T.TEXTO),
                ft.Text(f"{r.data.hour}:{r.data.minute}", size=12, color=T.TEXTO_SECUNDARIO, width=48, text_align=ft.TextAlign.END),
            ],
        ),
    )


def card_ultimas_recargas(recargas: list[Recarga], ao_ver_todas) -> ft.Container:
    Cores = usar_cores()
    return card(
        ft.Column(
            spacing=0,
            controls=[
                titulo_secao(
                    "Últimas recargas",
                    acao=ft.TextButton(
                        content=ft.Text("Ver todas", size=13, color=Cores.PRIMARIO_CLARO),
                        on_click=ao_ver_todas,
                    ),
                ),
                *[linha_recarga(r) for r in recargas],
            ],
        ),
        expand=True,
    )


@ft.component
def Dashboard():
    page = ft.context.page
    T = usar_cores()
    # Cada função obter_* é o ponto de integração com o backend
    kpis = obter_kpis()
    semana = obter_recargas_semana()
    ocupacao = obter_ocupacao()
    ultimas = obter_ultimas_recargas()

    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=16,
        controls=[
            ft.Text("Dashboard", size=24, weight=ft.FontWeight.W_600, color=T.TEXTO),
            faixa_kpis(kpis),
            ft.Row(
                spacing=16,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[card_recargas_semana(semana), card_ocupacao(ocupacao)],
            ),
            card_ultimas_recargas(ultimas, ao_ver_todas=lambda e: page.navigate("/recargas")),
        ],
    )
