import asyncio
from ctypes import alignment
import math
from time import sleep

import flet as ft

from src.components.cabecalho import criarCabecalho
from src.utils.temporizador import Temporizador
from src.routes.postos import Posto
from src.utils.request.instanciar_request import instanciar_request


@ft.component
def carregar():
    criarCabecalho()
    params = ft.use_route_params()
    energia = params["energia"]
    postoId = params["postoId"]
    carregadorId = params["carregadorId"]
    energiaInt = int(energia)

    request = instanciar_request("http://localhost:5000")
    posto = request.get_entidade(f"postos/{postoId}", Posto)
    carregador = posto.carregadores[int(carregadorId)]
    atual, setAtual = ft.use_state(0)
    horas_passadas, set_hora_passada = ft.use_state(0)
    largura = 200
    altura = 200
    porcentagem = ft.use_memo(lambda: atual / energiaInt, [atual])

    async def atualizar():
        a = 0
        while a < energiaInt:

            def atualizar(atual: int):
                nonlocal a
                a = atual + carregador.capacidade
                if a > energiaInt:
                    a = energiaInt
                return a

            setAtual(atualizar)
            set_hora_passada(lambda x: x + 1)
            await asyncio.sleep(1)
            # sleep(1)
        setAtual(energiaInt)

        # barra.value = porcentagem
        # valor.value =  f"{atual}/energia"
        # porcentagem_texto.value = f"{int(porcentagem * 100)}%"

    # temporizador = Temporizador(1, atualizar)

    ft.use_effect(atualizar, [])
    horas = math.ceil(energiaInt / carregador.capacidade)
    return ft.SafeArea(
        ft.Column(
            [
                ft.Stack(
                    [
                        ft.Container(
                            ft.Text(f"{int(porcentagem * 100)}%"),
                            alignment=ft.Alignment.CENTER,
                        ),
                        ft.ProgressRing(porcentagem, width=largura, height=altura),
                    ],
                    width=largura,
                    height=altura,
                ),
                ft.Text(f"energia: {atual}/{energiaInt}"),
                ft.Text(f"horas restantes: {horas_passadas}/{horas}"),
                ft.Button("voltar", on_click=lambda : ft.context.page.navigate("/postos")) if atual == energiaInt else ft.Column()
            ],
            align=ft.Alignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        ),
        # alignment=ft.Alignment.CENTER,
        
        expand=True,
    )
