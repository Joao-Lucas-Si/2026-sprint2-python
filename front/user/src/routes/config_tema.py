import flet as ft

from src.constants import Cores


def aplicar_tema():
    pagina = ft.context.page

    pagina.theme = ft.Theme(
        color_scheme_seed=Cores.PRIMARIO_CLARO,
        text_theme=ft.TextTheme(),
        button_theme=ft.ButtonTheme(ft.ButtonStyle(bgcolor=Cores.PRIMARIO_CLARO, color=Cores.TEXTO_PRIMARIO, padding=10))
        # color_scheme=ft.ColorScheme( primary=CoresConstantes.PRIMARIO_CLARO, surface=CoresConstantes.SUPERFICIE),
    )
    pagina.theme.scaffold_bgcolor = Cores.FUNDO
    if pagina.theme.color_scheme:
        pagina.theme.color_scheme.surface = Cores.SUPERFICIE
