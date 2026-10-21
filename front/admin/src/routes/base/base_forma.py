from typing import Any, Callable, List, Literal, NotRequired, TypeVar, TypedDict

import flet as ft

from src.constants import Constantes
from src.utils.request.http_request import CorpoJson
from src.utils.request.instanciar_request import instanciar_request
from src.utils.use_colors import usar_cores
from src.components.campo_entrada import campo_entrada


def campo_imagem_admin(
    label: str, icon: ft.IconData, value: str, set: Callable[[str], None]
):
    Cores = usar_cores()
    image, set_image = ft.use_state(value)

    def update(x: ft.Event[ft.TextField]):
        set(x.control.value)
        set_image(x.control.value)

    return ft.Column(
        [
            ft.Image(image, width=300, height=200),
            ft.TextField(
                label=label,
                prefix_icon=icon,
                value=value,
                on_change=update,
                bgcolor=Cores.FUNDO_SECUNDARIO,
                color=Cores.TEXTO_PRIMARIO,
                label_style=ft.TextStyle(color=Cores.TEXTO_SECUNDARIO),
                border_color=Cores.CARD_BORDA,
                focused_border_color=Cores.CARD_BORDA,
                border_radius=8,
            ),
        ]
    )


def campo_numero_admin(
    label: str, icon: ft.IconData, value: str, set: Callable[[str], None]
):
    Cores = usar_cores()
    image, set_image = ft.use_state(value)

    def update(x: ft.Event[ft.TextField]):
        set(x.control.value)
        set_image(x.control.value)

    return ft.Column(
        [
            ft.Image(image, width=300, height=200),
            ft.TextField(
                label=label,
                prefix_icon=icon,
                value=value,
                on_change=update,
                bgcolor=Cores.FUNDO_SECUNDARIO,
                color=Cores.TEXTO_PRIMARIO,
                label_style=ft.TextStyle(color=Cores.TEXTO_SECUNDARIO),
                border_color=Cores.CARD_BORDA,
                focused_border_color=Cores.CARD_BORDA,
                border_radius=8,
            ),
        ]
    )


def campo_selecao_admin(
    label: str,
    icon: ft.IconData,
    value: str,
    set: Callable[[str], None],
    opcoes: list[tuple[str, str]],
):
    Cores = usar_cores()
    image, set_image = ft.use_state(value)

    def update(x: ft.Event[ft.Dropdown]):
        if x.control.value:
            set(x.control.value)
            set_image(x.control.value)

    return ft.Column(
        [
            ft.Dropdown(
                value,
                [ft.DropdownOption(opcao[1], opcao[0]) for opcao in opcoes],
                label,
                on_select=update,
                bgcolor=Cores.FUNDO_SECUNDARIO,
                color=Cores.TEXTO_PRIMARIO,
                label_style=ft.TextStyle(color=Cores.TEXTO_SECUNDARIO),
                border_color=Cores.CARD_BORDA,
                
                focused_border_color=Cores.CARD_BORDA,
                border_radius=8,
            )
            # ft.TextField(
            #     label=label,
            #     prefix_icon=icon,
            #     value=value,
            #     on_change=update,
            #     bgcolor=Cores.FUNDO_SECUNDARIO,
            #     color=Cores.TEXTO_PRIMARIO,
            #     label_style=ft.TextStyle(color=Cores.TEXTO_SECUNDARIO),
            #     border_color=Cores.CARD_BORDA,
            #     focused_border_color=Cores.CARD_BORDA,
            #     border_radius=8,
            # )
        ]
    )


def campo_entrada_admin(
    label: str, icon: ft.IconData, value: str, set: Callable[[str], None]
):
    Cores = usar_cores()

    return ft.TextField(
        label=label,
        prefix_icon=icon,
        value=value,
        on_change=lambda x: set(x.control.value),
        bgcolor=Cores.FUNDO_SECUNDARIO,
        color=Cores.TEXTO_PRIMARIO,
        label_style=ft.TextStyle(color=Cores.TEXTO_SECUNDARIO),
        border_color=Cores.CARD_BORDA,
        focused_border_color=Cores.CARD_BORDA,
        border_radius=8,
    )


class FormField[T](TypedDict):
    get: Callable[[T], str]
    set: Callable[[T, str], None]
    icon: ft.IconData
    label: str
    tipo: NotRequired[Literal["numero", "texto", "multilinha", "imagem", "selecao"]]
    opcoes: NotRequired[List[tuple[str, str]]]


@ft.component
def adminField[T](field: FormField[T], value: T):
    def set(x: str):
        try:
            field["set"](value, x)
        except:
            ...

    if "tipo" in field:
        if field["tipo"] == "selecao":
            opcoes = field["opcoes"] if "opcoes" in field else []
            return campo_selecao_admin(
                field["label"], field["icon"], field["get"](value), set, opcoes
            )
    return ft.Column(
        [
            # ft.Text(field["label"]),
            (
                campo_imagem_admin(
                    field["label"], field["icon"], field["get"](value), set
                )
                if "tipo" in field and field["tipo"] == "imagem"
                else campo_entrada_admin(
                    field["label"], field["icon"], field["get"](value), set
                )
            )
        ]
    )


T = TypeVar("T", bound=CorpoJson)


@ft.component
def BaseForm(
    fields: List[List[FormField[T]]],
    default: T,
    getById: Callable[[int], T],
    route: str,
):
    params = ft.use_route_params()
    print(params)
    def back():
        ft.context.page.views.pop()

    value = default
    if "id" in params:
        value = getById(int(params["id"]))

    def save():
        requisicao = instanciar_request(Constantes.HOST.value)
        if "id" in params:

            requisicao.post_sem(f"{route}/editar/{params["id"]}", value)
        else:
            requisicao.post_sem(f"{route}/adicionar", value)

    # id = params["id"]
    return ft.Column(
        [
            ft.Row(
                [ft.Button("voltar", on_click=back), ft.Button("salvar", on_click=save)]
            ),
            ft.Column(
                [
                    ft.Row(
                        [adminField(field, value) for field in line],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                    for line in fields
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=10,
            ),
        ]
    )
