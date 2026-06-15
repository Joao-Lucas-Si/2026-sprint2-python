import flet as ft

from src.constants import Cores


def campo_entrada(label: str, icon: ft.IconData, senha: bool = False):
    
    return ft.TextField(
        label=label,
        prefix_icon=icon,
        password=senha, 
        can_reveal_password=senha, 
        bgcolor=Cores.SUPERFICIE_ESCURO,
        color=Cores.TEXTO_PRIMARIO,
        label_style=ft.TextStyle(color=Cores.TEXTO_SECUNDARIO),
        border_color=Cores.BORDA_FOCADA,
        focused_border_color=Cores.BORDA_FOCADA,
        border_radius=8,
    )