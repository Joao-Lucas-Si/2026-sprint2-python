from flask import jsonify
from app import app
from src.database.models.carregador import Carregador
from src.controlers.base import base_endpoints
from src.database.services.carregadores import CarregadorQuery
from src.database.services.posto import PostoQuery

def setAttr(instancia: Carregador, dados: dict):
    instancia.ocupado = dados["ocupado"]
    instancia.disponivel = dados["disponivel"]
    instancia.preco = dados["preco"]
    instancia.posto_id = dados["postoId"]
    instancia.capacidade = dados["capacidade"]
    

app.register_blueprint(base_endpoints("carregadores", setAttr, lambda : Carregador(),  CarregadorQuery()))



# @app.route("/carregadores", methods = ["GET"])
# def listar_carregadores():
#     query = CarregadorQuery()

#     carregadores = query.listarTodos()


#     return jsonify(list(map(lambda x: x.json(), carregadores)))

# @app.route("/carregadores/deletar/<int:id>", methods=["GET"])
# def remover_carregador(id):
#     return delete_endpoint(id, CarregadorQuery())

# @app.route("/carregadores/<int:id>", methods=["GET"])
# def obter_carregador_por_id(id):
#     return obter_por_id_endpoint(id, CarregadorQuery())