from src.routes.config_tema import aplicar_tema
from src.routes.router.main_router import main_router
from src.messages.utils import obterTextos
import flet as ft
@ft.component
def App(page: ft.Page):
    aplicar_tema()
    page.padding = 0
    page.title="Elevo"
    def a():
        page.update()
    page.window.on_event = a
    return main_router()

def main():
  
    ft.run(lambda page: page.render(lambda:App(page)))
    
if __name__ == "__main__":
    main()