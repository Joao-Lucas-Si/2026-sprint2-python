import flet as ft

from src.utils.use_colors import usar_cores


def navbar():
    Cores = usar_cores()
    page = ft.context.page
        # Barra de navegação inferior

    async def deslogar():
        await ft.SharedPreferences().remove("id")
        page.navigate("/")

    nav_inferior = ft.Container(
        # height=60,
        expand=1,
        padding=ft.Padding.symmetric(horizontal=30),
        # bgcolor=Cores.PRIMARIO,
        gradient=Cores.gradiente(),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                #CORES CABEÇALHO
                 ft.Icon(ft.Icons.HOME_FILLED, color=Cores.TEXTO, ),
                # ft.Icon(ft.Icons.MAP_OUTLINED, color=Cores.TEXTO),
                ft.GestureDetector( on_tap=lambda : page.navigate("/postos"), content=ft.Icon(ft.Icons.EV_STATION, color=Cores.TEXTO)),
                ft.GestureDetector( on_tap=lambda : page.navigate("/pagamento"),content= ft.Icon(ft.Icons.ATTACH_MONEY, color=Cores.TEXTO)),
                # ft.Icon(ft.Icons.HISTORY, color=Cores.TEXTO),
                ft.GestureDetector( on_tap=deslogar, content=ft.Icon(ft.Icons.PERSON_OUTLINE, color=Cores.TEXTO)),
            ],
        ),
    )
    
    page.bottom_appbar = ft.BottomAppBar(content=nav_inferior, padding=0)