# endpoint que lista todos os postos
# endpoint que retorna um unico posto através do 

import calendar
from datetime import date, datetime, timedelta
from typing import List

from flask import jsonify, request
from app import app
from src.database.services.posto import PostoQuery
from src.database.models import recarga
from src.database.models.recarga import Recarga
from src.database.services.recarga import RecargaQuery
from src.controlers.base import base_endpoints

def setRecargaAttr(recarga: Recarga, dados: dict):
    recarga.carregador_id = dados["carregador"]
    recarga.preco = dados["preco"]
    recarga.preco_kwh = dados["preco_kwh"]
    recarga.quantidade = dados["quantidade"]
    recarga.usuario_id = dados["usuario"]

app.register_blueprint(base_endpoints("recargas", setRecargaAttr, lambda : Recarga(), RecargaQuery()))

# @app.route("/recargas", methods = ["GET"])
# def lister_recargas():
#     query = RecargaQuery()

#     postos = query.listarTodos()


#     return jsonify(list(map(lambda x: x.json(), postos)))

@app.route("/recargas/ultimas", methods = ["GET"])
def lister_ultimas_recargas():
    query = RecargaQuery()

    postos = query.listarUltimas()
    # print(postos)

    return jsonify(list(map(lambda x: x.json(), postos)))

@app.route("/recargas/dividas", methods = ["GET"])
def listar_dividas():
    query = RecargaQuery()
    postoQuery = PostoQuery()
    recargas = query.nao_pagos()

    for recarga in recargas:
        recarga.posto = postoQuery.obterPorId(recarga.carregador.posto_id)
    return jsonify(list(map(lambda x: x.json(), recargas)))


# @app.route("/recargas/add", methods=["POST"])
# def adicionar_recarga():
#     query = RecargaQuery()
#     dados = request.get_json()

#     recarga = Recarga()

#     recarga.carregador_id = dados["carregador"]
#     recarga.preco = dados["preco"]
#     recarga.preco_kwh = dados["preco_kwh"]
#     recarga.quantidade = dados["quantidade"]
#     recarga.usuario_id = dados["usuario"]
    

#     query.adicionar(recarga)

#     return jsonify({})

# @app.route("/recargas/<int:id>", methods = ["GET"])
# def obter_recarga(id):
#     query = RecargaQuery()

#     posto = query.obterPorId(id)
#     if posto is None:
        
#         return jsonify({
#             "mensagem": "recarga inexistente"
#         })


#     return jsonify(posto.json())

@app.route("/recargas/hoje", methods=["GET"])
def recargas_hoje():
    query = RecargaQuery()

    entidades = query.obterPorData(datetime.now())
    return jsonify([e.json() for e in entidades])

@app.route("/recargas/semanas", methods=["GET"])
def recargas_por_semena():
    #.strftime('%a')
#     Sun
# Sat
# Fri
# Thu
# Wed
# Tue
# Mon
    current =  datetime.now()
    semanas = {
        "Sun": "Dom",
        "Sat": "Sab",
        "Fri": "Sex",
        "Thu": "Qui",
        "Wed": "Qua",
        "Tue": "Ter",
        "Mon": "Seg" 
    }
    resposta: list[tuple[str, List[Recarga]]] = []


    query = RecargaQuery()
    for i in range(7):
        target = current - timedelta(days=i)

        recargas = query.obterPorData(target)

        resposta.append((semanas[target.strftime("%a")], recargas))
    dados = [ { "dia": r[0], "total": len(r[1]) } for r in resposta]
    dados.reverse()
    
    return jsonify(dados)
