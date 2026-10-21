from typing import Any, Callable

import flet as ft

def criarCabecalho(back: Any|None = None):
    page = ft.context.page
    
    page.appbar = ft.AppBar(title="Elevo", actions=[ft.IconButton(ft.Icons.ARROW_BACK, on_click=back)] if back else [], leading=ft.Icon(ft.Icons.PERSON))

    page.update()