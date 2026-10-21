import flet as ft

from src.constants import Cores
from src.utils.use_colors import usar_cores


def campo_entrada(label: str, icon: ft.IconData, senha: bool = False):
    Cores = usar_cores()
    return ft.TextField(
        label=label,
        prefix_icon=icon,
        password=senha, 
        can_reveal_password=senha, 
        bgcolor=Cores.FUNDO_SECUNDARIO,
        color=Cores.TEXTO_PRIMARIO,
        label_style=ft.TextStyle(color=Cores.TEXTO_SECUNDARIO),
        border_color=Cores.CARD_BORDA,
        focused_border_color=Cores.CARD_BORDA,
        border_radius=8,
    )