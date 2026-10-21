import flet as ft

from src.dados import Recarga
from src.routes.base.base_forma import BaseForm
from src.routes.base.read_table import TabelaAdmin
from src.routes.dados import obter_recarga, obter_recargas, obter_ultimas_recargas

@ft.component
def RecargasForm():
    return BaseForm([

    ], Recarga(), lambda x: obter_recarga(x), "recargas")

@ft.component
def RecargasTabela():
    return TabelaAdmin(obter_recargas(), [
            {
                "cabecalho": "posto",
                "celula": lambda x: {
                    "valor": x.posto.nome,
                    
                }
            },
            # {
            #     "cabecalho": "usuario",
            #     "celula": lambda x: {
            #         "valor": x["usuario"]
            #     }
            # },
            {
                "cabecalho": "carga",
                "celula": lambda x: {
                    "valor": str(x.quantidade)
                }

            },
            {
                "cabecalho": "valor",
                "celula": lambda x: {
                    "valor": f"R$ {x.preco}"
                }
            },
            # {
            #     "cabecalho": "hora",
            #     "celula": lambda x: {
            #         "valor": x["hora"]
            #     }
            # }
    ], "recarga", "/recargas/form", "recargas")


    # {"posto": "posto shopping tamboré", "usuario": "Mariana S.", "kwh": 32.5, "valor": "R$ 39,00", "hora": "17:02"},
    #     {"posto": "posto do aeroporto", "usuario": "Carlos E.", "kwh": 18.0, "valor": "R$ 24,30", "hora": "16:48"},
    #     {"posto": "posto ipiranga", "usuario": "Beatriz L.", "kwh": 41.2, "valor": "R$ 39,14", "hora": "16:31"},
    #     {"posto": "Recarga Pinheiros", "usuario": "Rafael M.", "kwh": 12.7, "valor": "R$ 15,24", "hora": "16:10"},