# endpoint que lista todos os postos
# endpoint que retorna um unico posto através do 

from flask import jsonify, request
from app import app
from src.database.models.pagamento import Pagamento
from src.database.services.recarga import RecargaQuery
from src.database.services.pagamento import PagamentoQuery


@app.route("/pagamentos", methods = ["GET"])
def lister_pagamentos():
    query = PagamentoQuery()

    postos = query.listarTodos()


    return jsonify(list(map(lambda x: x.json(), postos)))

@app.route("/pagamentos/<int:id>", methods = ["GET"])
def obter_pagamento(id):
    query = PagamentoQuery()

    posto = query.obterPorId(id)
    if posto is None:
        
        return jsonify({
            "mensagem": "posto inexistente"
        })


    return jsonify(posto.json())

@app.route("/pagar", methods=["POST"])
def pagar():
    pagamento = Pagamento()
    json = request.get_json()
    pagamento.usuario_id = json["usuario"]
    pagamento.forma_pagamento = json["forma"]
    recargaQuery = RecargaQuery()
    query = PagamentoQuery()
    query.adicionar(pagamento)
    print(pagamento.id)

    recargaQuery.pagar(pagamento)
    return ""