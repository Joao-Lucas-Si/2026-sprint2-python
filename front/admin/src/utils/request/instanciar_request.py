from src.utils.request.adapters.requests_adapter import RequestsAdapter
from src.utils.request.http_request import HttpRequest


def instanciar_request(host: str) -> HttpRequest:
    return RequestsAdapter(host)