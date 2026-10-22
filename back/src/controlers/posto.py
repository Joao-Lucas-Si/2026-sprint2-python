# endpoint que lista todos os postos
# endpoint que retorna um unico posto através do 

from flask import jsonify
from app import app
# from src.controlers.base import delete_endpoint
from src.controlers.base import base_endpoints
from src.database.models.posto import Posto
from src.database.services.posto import PostoQuery

def setPostoAttr(instancia: Posto, dados: dict):
    instancia.descricao = dados["descricao"]
    instancia.imagem = dados["imagem"]
    instancia.local = dados["local"]
    instancia.nome = dados["nome"]
    instancia.dono_id = dados["dono_id"]
    # instancia.
    

app.register_blueprint(base_endpoints("postos", setPostoAttr, lambda : Posto(), PostoQuery()))

@app.route(f"/postos/admin/<int:id>")
def listagemDono(id):
    query = PostoQuery()

    postos = query.listarPorDono(id)

    return jsonify([p.json() for p in postos])

# @app.route("/postos", methods = ["GET"])
# def lister_postos():
#     query = PostoQuery()

#     postos = query.listarTodos()


#     return jsonify(list(map(lambda x: x.json(), postos)))


# @app.route("/postos/<int:id>", methods = ["GET"])
# def obter_posto(id):
#     query = PostoQuery()

#     posto = query.obterPorId(id)
#     if posto is None:
        
#         return jsonify({
#             "mensagem": "posto inexistente"
#         })


#     return jsonify(posto.json())

# @app.route("/postos/deletar/<int:id>", methods=["GET"])
# def remover_posto(id):
#     return delete_endpoint(id, PostoQuery())
