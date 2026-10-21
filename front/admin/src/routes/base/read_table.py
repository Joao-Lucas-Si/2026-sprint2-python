from typing import _TypedDict, Callable, List, NotRequired, TypeVar, TypedDict

import flet as ft

from src.constants import Constantes
from src.dados import Recarga
from src.utils.request.instanciar_request import instanciar_request
from src.components.admin import badge_status, card
from src.utils.use_colors import usar_cores


class DataCelula(TypedDict):
    valor: str
    content: NotRequired[ft.Control]
    secundario: NotRequired[bool]
    negrito: NotRequired[bool]


class ColunaTabela[T](TypedDict):
    cabecalho: str
    celula: Callable[[T], DataCelula]
    numerico: NotRequired[bool]


def filtrar_postos(postos: list[dict], termo: str) -> list[dict]:
    termo = termo.strip().lower()
    if not termo:
        return postos
    return [
        p for p in postos if termo in p["nome"].lower() or termo in p["local"].lower()
    ]


def _texto_celula(
    valor: str, secundario: bool = False, negrito: bool = False
) -> ft.DataCell:
    T = usar_cores()
    return ft.DataCell(
        ft.Text(
            valor,
            size=13,
            color=T.TEXTO_SECUNDARIO if secundario else T.TEXTO,
            weight=ft.FontWeight.W_600 if negrito else ft.FontWeight.W_400,
        )
    )

# T = TypeVar("T", bound=)

def linha_posto[T](
    p: T, colunas: List[ColunaTabela[T]], ao_editar, ao_excluir
) -> ft.DataRow:
    Cores = usar_cores()
    celulas = [c["celula"](p) for c in colunas]
    return ft.DataRow(
        cells=[
            *[
                (
                    ft.DataCell(c["content"])
                    if "content" in c and c["content"]
                    else _texto_celula(
                        c["valor"],
                        secundario=c["secundario"] if "secundario" in c else False,
                        negrito=c["negrito"] if "negrito" in  c else False,
                    )
                )
                for i, c in enumerate(celulas)
            ],
            # _texto_celula(p["nome"], negrito=True),
            # _texto_celula(p["local"], secundario=True),
            # _texto_celula(str(p["carregadores"])),
            # _texto_celula(f'R$ {p["preco"]:.2f}'.replace(".", ",")),
            # ft.DataCell(badge_status(p["status"])),
            ft.DataCell(
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.EDIT_OUTLINED,
                            icon_size=18,
                            icon_color=Cores.TEXTO_SECUNDARIO,
                            tooltip="Editar",
                            on_click=lambda e, pid=p.id: ao_editar(pid),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            icon_size=18,
                            icon_color=Cores.PRIMARIO_CLARO,
                            tooltip="Excluir",
                            on_click=lambda e, pid=p.id: ao_excluir(pid),
                        ),
                    ],
                )
            ),
        ]
    )




def tabela_postos[T](
    items: list[T], colunas: List[ColunaTabela[T]], ao_editar, ao_excluir
) -> ft.DataTable:
    C = usar_cores()
    Cores = usar_cores()
    return ft.DataTable(
        columns=[
            *(ft.DataColumn(
                label=ft.Text(
                    c["cabecalho"],
                    size=12,
                    weight=ft.FontWeight.W_600,
                    color=C.TEXTO_SECUNDARIO,
                ),
                numeric=(c["numerico"] if "numerico" in c else False),
            )
            for c in colunas),
            ft.DataColumn(label="Ações")       
        ],
        rows=[linha_posto(p, colunas, ao_editar, ao_excluir) for p in items],
        expand=True,  # ocupa a largura toda do card
        heading_row_color=C.FUNDO_SECUNDARIO,
        divider_thickness=0.5,
        column_spacing=32,
        data_row_min_height=56,
        data_row_max_height=56,
    )


def botao_novo(ao_clicar, alvo: str) -> ft.Container:
    T = usar_cores()
    Cores = usar_cores()
    return ft.Container(
        on_click=ao_clicar,  # passe a funçao de cadastrar novo posto, se vira paizão
        ink=True,
        gradient=Cores.gradiente(),
        border_radius=12,
        padding=ft.Padding.symmetric(horizontal=18, vertical=12),
        content=ft.Row(
            tight=True,
            spacing=8,
            controls=[
                ft.Icon(ft.Icons.ADD, size=18, color=T.TEXTO_PRIMARIO),
                ft.Text(
                    f"Novo {alvo}",
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color=T.TEXTO_PRIMARIO,
                ),
            ],
        ),
    )


def campo_busca(ao_mudar) -> ft.TextField:
    T = usar_cores()
    Cores = usar_cores()
    return ft.TextField(
        hint_text="Buscar por nome ou local...",
        hint_style=ft.TextStyle(color=T.TEXTO_SECUNDARIO),
        color=T.TEXTO,
        bgcolor=T.CARD,
        border_color=T.CARD_BORDA,
        focused_border_color=Cores.PRIMARIO,
        border_radius=12,
        height=46,
        width=320,
        content_padding=ft.Padding.symmetric(horizontal=14, vertical=0),
        prefix_icon=ft.Icons.SEARCH,
        on_change=lambda e: ao_mudar(e.control.value),
    )


@ft.component
def TabelaAdmin[T](obter: List[T], celulas: List[ColunaTabela[T]], alvo: str, form: str, endpoint: str):
    T = usar_cores()
    Cores = usar_cores()
    # Estado da tela: o texto digitado na busca
    busca, set_busca = ft.use_state("")

    # TODO backend: postos = requisicao.get_lista("postos", Posto)
    todos = obter
    visiveis = todos
    # visiveis = filtrar_postos(todos, busca)

    # TODO: abrir formulário/diálogo de edição, confirmar exclusão, etc.
    def editar(pid):
        ft.context.page.navigate(f"{form}/{pid}")

    def excluir(pid):
        print(pid)
        requisicao = instanciar_request(Constantes.HOST.value)
        # /carregadores/deletar/<int:id>
        requisicao.get_sem(f"/{endpoint}/deletar/{pid}")
        
        ft.context.page.update()
        # recargas = requisicao.get_lista("/recargas", Recarga)

    def novo(e):
        ft.context.page.navigate(form)

    return ft.Column(
        expand=True,
        spacing=16,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        f"{alvo.capitalize()}s", size=24, weight=ft.FontWeight.W_600, color=T.TEXTO
                    ),
                    botao_novo(novo, alvo),
                ],
            ),
            campo_busca(set_busca),
            card(
                ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Row(
                            controls=[tabela_postos(visiveis, celulas, editar, excluir)],
                        ),
                        ft.Text(
                            (
                                f"Nenhum {alvo} encontrado"
                                if not visiveis
                                else f"{len(visiveis)} {alvo}(s)"
                            ),
                            size=12,
                            color=T.TEXTO_SECUNDARIO,
                        ),
                    ],
                ),
                expand=True,
                padding=8,
            ),
        ],
    )
