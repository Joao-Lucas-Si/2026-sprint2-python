# endpoint que lista todos os postos
# endpoint que retorna um unico posto através do 

from flask import jsonify, request
from app import app
from src.database.services.posto import PostoQuery
from src.database.models import recarga
from src.database.models.recarga import Recarga
from src.database.services.recarga import RecargaQuery


@app.route("/recargas", methods = ["GET"])
def lister_recargas():
    query = RecargaQuery()

    postos = query.listarTodos()


    return jsonify(list(map(lambda x: x.json(), postos)))

@app.route("/recargas/dividas", methods = ["GET"])
def listar_dividas():
    query = RecargaQuery()
    postoQuery = PostoQuery()
    recargas = query.nao_pagos()

    for recarga in recargas:
        recarga.posto = postoQuery.obterPorId(recarga.carregador.posto_id)
    return jsonify(list(map(lambda x: x.json(), recargas)))


@app.route("/recargas/add", methods=["POST"])
def adicionar_recarga():
    query = RecargaQuery()
    dados = request.get_json()

    recarga = Recarga()

    recarga.carregador_id = dados["carregador"]
    recarga.preco = dados["preco"]
    recarga.preco_kwh = dados["preco_kwh"]
    recarga.quantidade = dados["quantidade"]
    recarga.usuario_id = dados["usuario"]
    

    query.adicionar(recarga)

    return jsonify({})

@app.route("/recargas/<int:id>", methods = ["GET"])
def obter_recarga(id):
    query = RecargaQuery()

    posto = query.obterPorId(id)
    if posto is None:
        
        return jsonify({
            "mensagem": "recarga inexistente"
        })


    return jsonify(posto.json())