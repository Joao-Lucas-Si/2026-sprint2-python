from typing import Any, TypeVar

import requests

from src.utils.request.http_request import CorpoJson, HttpRequest

T = TypeVar("T", bound=CorpoJson)


class RequestsAdapter(HttpRequest):

    def get_json(self, caminho: str) -> Any:
        resposta = requests.get(self.caminhoFinal(caminho))

        return resposta.json()

    def get_entidade(self, caminho: str, data: type[T]) -> T:
        json = self.get_json(caminho)

        return data.instanciar(json)

    def get_lista(self, caminho: str, data: type[T]) -> list[T]:
        json = self.get_json(caminho)

        return list(map(lambda x: data.instanciar(x), json))

    def post_sem(self, caminho: str, data: T) -> None:
        requests.post(self.caminhoFinal(caminho), json=data.converter())

    def post_map_sem(self, caminho: str, data: dict) -> None:
        requests.post(self.caminhoFinal(caminho), json=data)

    def post_map(self, caminho: str, data: dict, resposta: type[T]) -> T:

        retorno = requests.post(self.caminhoFinal(caminho), json=data)
        json = retorno.json()

        return resposta.instanciar(json)

    def post_map_dict(self, caminho: str, data: dict) -> dict:

        retorno = requests.post(self.caminhoFinal(caminho), json=data)
        json = retorno.json()

        return json
