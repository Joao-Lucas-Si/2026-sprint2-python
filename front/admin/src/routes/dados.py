from src.hooks.use_is_admin import use_is_admin
from src.dados import Carregador, Posto, Recarga, Usuario
from src.constants import Constantes
from src.utils.request.instanciar_request import instanciar_request
import flet as ft

MENU_ADMIN = [
    {"rota": "/dashboard", "rotulo": "Dashboard", "icone": "DASHBOARD_OUTLINED"},
    {"rota": "/recargas", "rotulo": "Recargas", "icone": "BOLT"},
    {"rota": "/postos", "rotulo": "Postos", "icone": "LOCATION_ON_OUTLINED"},
    {"rota": "/carregadores", "rotulo": "Carregadores", "icone": "EV_STATION"},
    {"rota": "/usuarios", "rotulo": "Usuarios", "icone": "PEOPLE", "isAdmin": True},
    # {
    #     "rota": "/notificacoes",
    #     "rotulo": "Notificações",
    #     "icone": "NOTIFICATIONS_OUTLINED",
    # },
]


def obter_kpis():
    carregadores = obter_carregadores()
    recargas = obter_ultimas_recargas()
    hoje = obter_recargas_hoje()
    # delta > 0 = subiu (verde), delta < 0 = caiu (vermelho)
    return [
        {"rotulo": "Recargas hoje", "valor": len(hoje), "delta": 12.4},
        {
            "rotulo": "Energia (kWh)",
            "valor": f"{sum([c.quantidade for c in recargas] ):.2f}",
            "delta": 8.1,
        },
        {
            "rotulo": "Receita (R$)",
            "valor": f"{sum([c.preco for c in recargas] ):.2f}",
            "delta": -3.2,
        },
        {
            "rotulo": "Carregadores ativos",
            "valor": f"{len([c for c in carregadores if not c.ocupado ])}/{len(carregadores)}",
            "delta": 4.5,
        },
    ]


def obter_recargas_semana():
    requisicao = instanciar_request(Constantes.HOST.value)

    return requisicao.get_json(
        "/recargas/semanas",
    )
    # return [
    #     {"dia": "Seg", "total": 82},
    #     {"dia": "Ter", "total": 97},
    #     {"dia": "Qua", "total": 90},
    #     {"dia": "Qui", "total": 110},
    #     {"dia": "Sex", "total": 128},
    #     {"dia": "Sáb", "total": 141},
    #     {"dia": "Dom", "total": 104},
    # ]


def obter_ocupacao():
    carregadores = obter_carregadores()
    if len(carregadores) == 0:
        return 1
    return (sum([int(c.ocupado) for c in carregadores])) / len(carregadores)


def obter_carregador(id):
    requisicao = instanciar_request(Constantes.HOST.value)

    carregadores = requisicao.get_entidade(f"carregadores/{id}", Carregador)

    return carregadores


def obter_posto(id):
    requisicao = instanciar_request(Constantes.HOST.value)

    carregadores = requisicao.get_entidade(f"postos/{id}", Posto)

    return carregadores


def obter_recarga(id):
    requisicao = instanciar_request(Constantes.HOST.value)

    carregadores = requisicao.get_entidade(f"recargas/{id}", Recarga)

    return carregadores




def obter_carregadores():
    carregadores, setCarregadores = ft.use_state([])
  
    async def obter():
        preferences = ft.SharedPreferences()
        isAdmin = await preferences.get("admin.role") == "admin"
        id = await preferences.get("admin.id")
        requisicao = instanciar_request(Constantes.HOST.value)

        setCarregadores(requisicao.get_lista(f"carregadores/admin/{id}" if not isAdmin else "carregadores", Carregador))
    ft.on_mounted(obter)
    return carregadores


def obter_usuario(id):
    requisicao = instanciar_request(Constantes.HOST.value)

    carregadores = requisicao.get_entidade(f"usuarios/{id}", Usuario)

    return carregadores



def obter_usuarios():
    requisicao = instanciar_request(Constantes.HOST.value)

    carregadores = requisicao.get_lista("usuarios", Usuario)

    return carregadores


def obter_recargas():
    # /recargas/ultimas
    requisicao = instanciar_request(Constantes.HOST.value)

    recargas = requisicao.get_lista("/recargas", Recarga)

    return recargas


def obter_recargas_hoje():
    # /recargas/ultimas
    requisicao = instanciar_request(Constantes.HOST.value)

    recargas = requisicao.get_lista("/recargas/hoje", Recarga)

    return recargas


def obter_ultimas_recargas():
    # /recargas/ultimas
    requisicao = instanciar_request(Constantes.HOST.value)

    recargas = requisicao.get_lista("/recargas/ultimas", Recarga)

    return recargas
    # return [
    #     {"posto": "posto shopping tamboré", "usuario": "Mariana S.", "kwh": 32.5, "valor": "R$ 39,00", "hora": "17:02"},
    #     {"posto": "posto do aeroporto", "usuario": "Carlos E.", "kwh": 18.0, "valor": "R$ 24,30", "hora": "16:48"},
    #     {"posto": "posto ipiranga", "usuario": "Beatriz L.", "kwh": 41.2, "valor": "R$ 39,14", "hora": "16:31"},
    #     {"posto": "Recarga Pinheiros", "usuario": "Rafael M.", "kwh": 12.7, "valor": "R$ 15,24", "hora": "16:10"},
    # ]


def obter_postos():
    postos, setPostos = ft.use_state([])
  
    async def obter():
        preferences = ft.SharedPreferences()
        isAdmin = await preferences.get("admin.role") == "admin"
        id = await preferences.get("admin.id")
        requisicao = instanciar_request(Constantes.HOST.value)

        setPostos(requisicao.get_lista(f"postos/admin/{id}" if not isAdmin else "postos", Posto))
    ft.on_mounted(obter)
    return postos
    # status: "disponivel" | "ocupado" | "manutencao"
    # return [
    #     {"id": 1, "nome": "posto shopping tamboré", "local": "Av. Paulista, São Paulo", "carregadores": 8, "preco": 1.20, "status": "disponivel"},
    #     {"id": 2, "nome": "posto do aeroporto", "local": "Guarulhos, São Pauslo", "carregadores": 6, "preco": 1.25, "status": "ocupado"},
    #     {"id": 3, "nome": "posto ipiranga", "local": "Zona Sul, São Paulo", "carregadores": 10, "preco": 0.77, "status": "disponivel"},
    #     {"id": 4, "nome": "Posto do villa lobos", "local": "IRINEU vc não sabe nem eu", "carregadores": 4, "preco": 1.35, "status": "manutencao"},
    #     {"id": 5, "nome": "Recarga Pinheiros", "local": "Pinheiros, São Paulo", "carregadores": 5, "preco": 1.25, "status": "disponivel"},
    # ]
