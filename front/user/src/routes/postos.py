from ast import Constant
from typing import Any

import flet as ft

from src.components.cabecalho import criarCabecalho
from src.constants import Constantes, Cores, EstiloConstantes
from src.utils.request.http_request import CorpoJson
from src.utils.request.instanciar_request import instanciar_request


class Carregador(CorpoJson):
    capacidade: int
    disponivel: int
    ocupado: bool

    def __init__(self, capacidade: int, disponivel: int, ocupado: bool) -> None:
        super().__init__()
        self.capacidade = capacidade
        self.disponivel = disponivel
        self.ocupado = ocupado

    @staticmethod
    def instanciar(json: dict) -> Any:
        instancia = Carregador(json["capacidade"], json["disponivel"], json["ocupado"])

        return instancia


class Posto(CorpoJson):
    id: int
    carregadores: list[Carregador]
    nome: str

    @property
    def capacidade_media(self):
        return sum(carregador.capacidade for carregador in self.carregadores) / len(
            self.carregadores
        )

    @property
    def carregadores_disponiveis(self):
        return [
            carregador for carregador in self.carregadores if not carregador.ocupado
        ]

    def __init__(self, id: int, nome: str, carregadores: list[Carregador]) -> None:
        super().__init__()
        self.id = id
        self.nome = nome
        self.carregadores = carregadores

    @staticmethod
    def instanciar(json: dict) -> Any:
        return Posto(json["id"], json["nome"], list(map(lambda x: Carregador.instanciar(x), json["carregadores"])))


@ft.component
def posto_card(posto: Posto):
    page = ft.context.page
    async def abrir():
        await page.push_route(f"/postos/{posto.id}")
        
        # page.update()
   
    return ft.Container(ft.Column(
        [
            ft.Text(posto.nome,  size=20, color=Cores.TEXTO_SECUNDARIO),
            ft.Row(
                [
                    ft.Text(
                        f"carregadores: {len(posto.carregadores)}",
                       
                    ),
                    ft.Text(f"carregadores disponiveis: {len(posto.carregadores_disponiveis)}"),
                    ft.Text(f"capacidade média: {posto.capacidade_media:.2f} kH/h")
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        ],

    ),  padding=20, on_click=abrir,  border=EstiloConstantes.borda.value,border_radius=EstiloConstantes.arredondamento.value )





@ft.component
def postos():
    requisicao = instanciar_request(Constantes.HOST.value)
    page = ft.context.page
    async def deslogar():
        await ft.SharedPreferences().remove("id")
        page.navigate("/")
        
    def criar_card_postos(postos: list[Posto]) -> list[ft.Control]:
        return [posto_card(posto) for posto in postos]
    lista = ft.ListView(criar_card_postos(requisicao.get_lista("postos", Posto)),  spacing=15, auto_scroll=True)
    criarCabecalho(deslogar)
    # def atribuir(postos: list[Posto]):
    #     lista.controls = criar_card_postos(postos)
    
    # def onMount():
    #     requisicao.assincrono(lambda : requisicao.get_lista("postos", Posto), atribuir)
    # ft.use_effect(onMount, [ft.rende])
    return ft.SafeArea(ft.Container(lista, padding=10, expand=True))
