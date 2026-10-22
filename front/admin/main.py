from src.routes.config_tema import aplicar_tema
from src.routes.router import main_router

import flet as ft
@ft.component
def App(page: ft.Page):
    aplicar_tema()
    page.padding = 0
    page.title="Elevo"
    # print(page.route)
    # if page.route == "/" or page.route == "":
    #     page.navigate("/dashboard")

    # def a():
    #     page.update()
    # page.window.on_event = a
    return main_router()

def main():
  
    ft.run(lambda page: page.render(lambda:App(page)), port=6900)
    
if __name__ == "__main__":
    main()