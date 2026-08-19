from datetime import datetime
import json
from typing import TypedDict

from flask import jsonify, request
from flask_socketio import emit, join_room, leave_room, send 
from app import app, socketio

last_heart: datetime|None = None
# O sistema simula uma comunicação com protocolo OCPP. Especificamente na versão 1.6 devido a
# integrar melhor no sistema, separando em 5 mensagens principais, Boot, que serve para iniciar uma
# conexão e ocorre na definição de um novo posto, HeartBeat, que ocorre toda vez que o tempo passa
# para avisar aos servidores que os postos estão funcionais, StartTransaction, que inicia uma recarga,
# MeterValue, que ocorre toda vez que um carro está carregando, mais ainda não terminou sua sessãoserve para ceder dados de rastreamento dos carregadores, e StopTransaction, que sinaliza o fim de
# uma recarga.


class Carregamento(TypedDict):
    quantidade: int 
    codigo: int 
    energia: int 

    

carregamentos: list[Carregamento] = [{
    'codigo': 12345,
    'energia': 0,
    'quantidade': 100
}, {
    'codigo': 573875,
    'energia': 0,
    'quantidade': 200
}]

def obter_carregamento(codigo: int):
    return (carregamento for carregamento in carregamentos if carregamento["codigo"] == codigo)


@app.route("/ocpp/data")
def data():
    return jsonify(carregamentos)

@app.route("/ocpp/HeartBeat")
def heart_beat():
    global last_heart

    last_heart = datetime.now()
    
    return "recebido"

@app.route("/ocpp/MeterValue/<int:codigo>/<int:valor>")
def meterValue(codigo: int, valor: int):
    carregamento = next(obter_carregamento(codigo))
    carregamento["energia"] += valor 
    socketio.emit("MeterValue", {
        "valor": carregamento["energia"]
    })
    return "success"

@app.route("/ocpp/startTransaction/<int:codigo>")
def startTransaction(codigo: int):
    carregamento = next(obter_carregamento(codigo))
    socketio.emit("startTransaction")
    # send(json.dumps({
    #     "type": "startTransaction"
    # }))
    return str(carregamento["quantidade"])

@app.route("/ocpp/stopTransaction/<int:codigo>")
def stopTransaction(codigo: int):
    # carregamento = next(obter_carregamento(codigo))
    return "finalizado"

@app.route("/ocpp/verificar-codigo/<int:codigo>")
def verificar_codigo(codigo: int):

    carregamento = next(obter_carregamento(codigo), None)

    if carregamento:
        return "1"

    return "0"

@socketio.on('join')
def handle_join(data):
    print(data)
    room = data['codigo']
    energia = data["quantidade"]
    carregamento: Carregamento = {
        "codigo": room,
        "energia": 0,
        "quantidade": energia
    }
    carregamentos.append(carregamento)
    join_room(room)
    send(f'requisição salva no servidor, insira o código no carregador escolhido para começar o abastecimento', to=room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    send(f'abastecimento finalizado', to=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    send(data['message'], to=room)