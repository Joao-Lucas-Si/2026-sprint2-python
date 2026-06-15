# endpoint que lista todos os postos
# endpoint que retorna um unico posto através do 

from flask import jsonify
from app import app
from src.database.services.posto import PostoQuery


@app.route("/postos", methods = ["GET"])
def lister_postos():
    query = PostoQuery()

    postos = query.listarTodos()


    return jsonify(list(map(lambda x: x.json(), postos)))


@app.route("/postos/<int:id>", methods = ["GET"])
def obter_posto(id):
    query = PostoQuery()

    posto = query.obterPorId(id)
    if posto is None:
        
        return jsonify({
            "mensagem": "posto inexistente"
        })


    return jsonify(posto.json())