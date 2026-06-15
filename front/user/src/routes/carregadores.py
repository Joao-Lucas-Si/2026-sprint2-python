import flet as ft

from src.components.alerta_erro import alerta_erro
from src.components.cabecalho import criarCabecalho
from src.constants import Constantes, Cores, EstiloConstantes
from src.routes.postos import Posto, Carregador
from src.utils.request.instanciar_request import instanciar_request


@ft.component
def carregador_card(carregador: Carregador, i : int):
    params = ft.use_route_params()
    page = ft.context.page
    async def selecionar():
        if carregador.ocupado:
            alerta_erro("carregador ocupado")
        else:
            await page.push_route(f"/postos/{params["postoId"]}/{i}")
   
    return ft.Container(
        ft.Column(
            [
                ft.Text(f"carregador {i + 1}"),
                ft.Row(
                    [
                        ft.Text("em uso", color=Cores.ERRO) if carregador.ocupado else ft.Text("disponivel", color=Cores.SUCESSO),
                        ft.Text(f"capacidade: {carregador.capacidade} kH/h"),
                        ft.Text(f"energia disponivel: {carregador.disponivel}"),
                    ]
                )
            ]
        ),
        border=EstiloConstantes.borda.value,
        border_radius=EstiloConstantes.arredondamento.value,
        padding=6,
        on_click=selecionar
    )


@ft.component
def carregadores():
    page = ft.context.page
    criarCabecalho(lambda : page.navigate("/postos"))
    params = ft.use_route_params()
    
    postoId = params["postoId"]
    requisicao = instanciar_request(Constantes.HOST.value)

    posto = requisicao.get_entidade(Constantes.OBTER_POSTO(postoId), Posto)

    carregadores = posto.carregadores
    
    
    return ft.SafeArea(
        
        #ft.Text(f"ss{postoId}")
        ft.Container(ft.ListView([carregador_card(carregador, i) for i, carregador in enumerate(carregadores)], spacing=15), padding=10)
    )
