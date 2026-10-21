from typing import Callable, TypeVar

from flask import Blueprint, jsonify, request

from app import app
from src.database.models.base import BaseModel
from src.database.services.base import BaseQuery

T = TypeVar("T", bound=BaseModel)

def base_endpoints(route: str, setAttr: Callable[[T, dict], None], instanciar: Callable[[], T], query: BaseQuery[T]):
    bp = Blueprint(route, __name__, url_prefix=f"/{route}")
    @bp.route(f"/editar/<int:id>", methods=["POST"])
    def editar(id):
        # print(id)
        # instance = query.obterPorId(id)
        
        dados = request.get_json()
        query.update(id, lambda x: setAttr(x, dados))
            # return ""
        return ""
        
    @bp.route(f"/adicionar", methods=["POST"])
    def adicionar():
        # print(id)
        # instance = query.obterPorId(id)
        instancia = instanciar()

        dados = request.get_json()

        setAttr(instancia, dados)

        query.adicionar(instancia)
        # query.update(id, lambda x: setAttr(x, dados))
            # return ""
        return ""

    @bp.route(f"/deletar/<int:id>", methods=["GET"])
    def deletar(id: int):
        query.remover(id)
        return "removido"

    @bp.route(f"/<int:id>", methods=["GET"])
    def obter_por_id_endpoint(id):

        entidade = query.obterPorId(id)
        if entidade is None:
            
            return jsonify({
                "mensagem": "posto inexistente"
            })


        return jsonify(entidade.json())

    @bp.route(f"", methods = ["GET"])
    def listar():

        carregadores = query.listarTodos()


        return jsonify(list(map(lambda x: x.json(), carregadores)))

    return bp