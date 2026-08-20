import asyncio
from ctypes import alignment
import math
from time import sleep
from typing import Any
import websocket
import flet as ft
import socketio
from src.components.cabecalho import criarCabecalho
from src.utils.temporizador import Temporizador
from src.routes.postos import Posto
from src.utils.request.instanciar_request import instanciar_request
from random import randint

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
    esta_carregando, set_esta_carregando = ft.use_state(False)
    horas_passadas, set_hora_passada = ft.use_state(0)
    largura = 200
    altura = 200
    # codigo = 2345
    codigo, setCodigo = ft.use_state(randint(1000, 9999))
    print(codigo)
    porcentagem = ft.use_memo(lambda: atual / energiaInt, [atual])

    async def atualizar():
        # def on_open(ws: websocket.WebSocketApp):
        #     print("conectado")
        # def on_message(ws: websocket.WebSocketApp, message: str):
        #     print("message")
        # def on_error(ws: websocket.WebSocketApp, err: Any):
        #     print(err)
        # def on_close(ws, close_status_code, close_msg):
        #     print("desconectado")
        # ws = websocket.WebSocketApp("wss://localhost:5000",
        #                       on_open=on_open,
        #                       on_message=on_message,
        #                       on_error=on_error,
        #                       on_close=on_close)
        # ws.run_forever()
        sio = socketio.AsyncClient()
        @sio.event
        async def connect():
            print("I'm connected!")
            await sio.emit("join",data= {
                "codigo": codigo,
                "quantidade": energiaInt
            })
        

        @sio.event
        def connect_error(data):
            print("The connection failed!")

        @sio.event
        def disconnect(reason):
            print("I'm disconnected! reason:", reason)

        @sio.event
        def MeterValue(data):
            print(data)
            setAtual(data["valor"])

        @sio.on("startTransaction")
        async def start():
            print("transação iniciada")
            set_esta_carregando(True)
        await sio.connect("http://localhost:5000")
        # a = 0
        # while a < energiaInt:

        #     def atualizar(atual: int):
        #         nonlocal a
        #         a = atual + carregador.capacidade
        #         if a > energiaInt:
        #             a = energiaInt
        #         return a

        #     setAtual(atualizar)
        #     set_hora_passada(lambda x: x + 1)
        #     await asyncio.sleep(1)
        #     # sleep(1)
        # setAtual(energiaInt)

        # barra.value = porcentagem
        # valor.value =  f"{atual}/energia"
        # porcentagem_texto.value = f"{int(porcentagem * 100)}%"

    # temporizador = Temporizador(1, atualizar)
    
    ft.use_effect(atualizar, [])
    horas = math.ceil(energiaInt / carregador.capacidade)
    return ft.SafeArea(
        ft.Column(
             ([
                ft.Stack(
                    [
                        ft.Container(
                            ft.Text(f"{100 if  porcentagem > 1 else int(porcentagem * 100)}%"),
                            alignment=ft.Alignment.CENTER,
                        ),
                        ft.ProgressRing(porcentagem, width=largura, height=altura),
                    ],
                    width=largura,
                    height=altura,
                ),
                ft.Text(f"energia: {atual}/{energiaInt}"),
                ft.Text(f"horas restantes: {horas_passadas}/{horas}"),
                ft.Button("voltar", on_click=lambda : ft.context.page.navigate("/postos")) if atual >= energiaInt else ft.Column()
            ] if esta_carregando else [
                ft.Text(f"codigo: {codigo}")
            ]),
            align=ft.Alignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        ),
        # alignment=ft.Alignment.CENTER,
        
        expand=True,
    )
