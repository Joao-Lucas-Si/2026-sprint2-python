"""Tela 2 do admin: tabela de postos (modelo para as demais entidades)."""

import flet as ft

# from paleta_app import Cores, TemaEscuro
from src.dados import Posto
from src.routes.base.base_forma import BaseForm
from src.routes.base.read_table import TabelaAdmin
from src.utils.use_colors import usar_cores
from src.components.admin import badge_status, card
from src.routes.dados import obter_posto, obter_postos

# T = TemaEscuro

# Colunas da tabela. Para criar a tabela de outra entidade
# (carregadores, recargas...) você troca esta lista e a função de linha.
# COLUNAS_POSTOS = ["Nome", "Local", "Carregadores", "Preço (kWh)", "Status", "Ações"]


# def filtrar_postos(postos: list[dict], termo: str) -> list[dict]:
#     termo = termo.strip().lower()
#     if not termo:
#         return postos
#     return [p for p in postos if termo in p["nome"].lower() or termo in p["local"].lower()]


# def _texto_celula(valor: str, secundario: bool = False, negrito: bool = False) -> ft.DataCell:
#     T = usar_cores()
#     return ft.DataCell(
#         ft.Text(
#             valor,
#             size=13,
#             color=T.TEXTO_SECUNDARIO if secundario else T.TEXTO,
#             weight=ft.FontWeight.W_600 if negrito else ft.FontWeight.W_400,
#         )
#     )


# def linha_posto(p: dict, ao_editar, ao_excluir) -> ft.DataRow:
#     T = usar_cores()
#     Cores = usar_cores()
#     return ft.DataRow(
#         cells=[
#             _texto_celula(p["nome"], negrito=True),
#             _texto_celula(p["local"], secundario=True),
#             _texto_celula(str(p["carregadores"])),
#             _texto_celula(f'R$ {p["preco"]:.2f}'.replace(".", ",")),
#             ft.DataCell(badge_status(p["status"])),
#             ft.DataCell(
#                 ft.Row(
#                     spacing=0,
#                     controls=[
#                         ft.IconButton(
#                             icon=ft.Icons.EDIT_OUTLINED,
#                             icon_size=18,
#                             icon_color=T.TEXTO_SECUNDARIO,
#                             tooltip="Editar",
#                             on_click=lambda e, pid=p["id"]: ao_editar(pid),
#                         ),
#                         ft.IconButton(
#                             icon=ft.Icons.DELETE_OUTLINE,
#                             icon_size=18,
#                             icon_color=Cores.PRIMARIO_CLARO,
#                             tooltip="Excluir",
#                             on_click=lambda e, pid=p["id"]: ao_excluir(pid),
#                         ),
#                     ],
#                 )
#             ),
#         ]
#     )


# def tabela_postos(postos: list[dict], ao_editar, ao_excluir) -> ft.DataTable:
#     T = usar_cores()
#     Cores = usar_cores()
#     return ft.DataTable(
#         columns=[
#             ft.DataColumn(
#                 ft.Text(c, size=12, weight=ft.FontWeight.W_600, color=T.TEXTO_SECUNDARIO),
#                 numeric=(c == "Carregadores"),
#             )
#             for c in COLUNAS_POSTOS
#         ],
#         rows=[linha_posto(p, ao_editar, ao_excluir) for p in postos],
#         expand=True,  # ocupa a largura toda do card
#         heading_row_color=T.FUNDO_SECUNDARIO,
#         divider_thickness=0.5,
#         column_spacing=32,
#         data_row_min_height=56,
#         data_row_max_height=56,
#     )


# def botao_novo(ao_clicar) -> ft.Container:
#     T = usar_cores()
#     Cores = usar_cores()
#     return ft.Container(
#         on_click=ao_clicar,#passe a funçao de cadastrar novo posto, se vira paizão
#         ink=True,
#         gradient=Cores.gradiente(),
#         border_radius=12,
#         padding=ft.Padding.symmetric(horizontal=18, vertical=12),
#         content=ft.Row(
#             tight=True,
#             spacing=8,
#             controls=[
#                 ft.Icon(ft.Icons.ADD, size=18, color=T.TEXTO_PRIMARIO),
#                 ft.Text("Novo posto", size=14, weight=ft.FontWeight.W_600, color=T.TEXTO_PRIMARIO),
#             ],
#         ),
#     )


# def campo_busca(ao_mudar) -> ft.TextField:
#     T = usar_cores()
#     Cores = usar_cores()
#     return ft.TextField(
#         hint_text="Buscar por nome ou local...",
#         hint_style=ft.TextStyle(color=T.TEXTO_SECUNDARIO),
#         color=T.TEXTO,
#         bgcolor=T.CARD,
#         border_color=T.CARD_BORDA,
#         focused_border_color=Cores.PRIMARIO,
#         border_radius=12,
#         height=46,
#         width=320,
#         content_padding=ft.Padding.symmetric(horizontal=14, vertical=0),
#         prefix_icon=ft.Icons.SEARCH,
#         on_change=lambda e: ao_mudar(e.control.value),
#     )


# @ft.component
# def PostosAdmin():
#     T = usar_cores()
#     Cores = usar_cores()
#     # Estado da tela: o texto digitado na busca
#     busca, set_busca = ft.use_state("")

#     # TODO backend: postos = requisicao.get_lista("postos", Posto)
#     todos = obter_postos()
#     visiveis = filtrar_postos(todos, busca)

#     # TODO: abrir formulário/diálogo de edição, confirmar exclusão, etc.
#     def editar(pid):
#         print("editar posto", pid)

#     def excluir(pid):
#         print("excluir posto", pid)

#     def novo(e):
#         print("novo posto")

#     return ft.Column(
#         expand=True,
#         spacing=16,
#         controls=[
#             ft.Row(
#                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
#                 controls=[
#                     ft.Text("Postos", size=24, weight=ft.FontWeight.W_600, color=T.TEXTO),
#                     botao_novo(novo),
#                 ],
#             ),
#             campo_busca(set_busca),
#             card(
#                 ft.Column(
#                     expand=True,
#                     scroll=ft.ScrollMode.AUTO,
#                     controls=[
#                         ft.Row(
#                             controls=[tabela_postos(visiveis, editar, excluir)],
#                         ),
#                         ft.Text(
#                             "Nenhum posto encontrado" if not visiveis else f"{len(visiveis)} posto(s)",
#                             size=12,
#                             color=T.TEXTO_SECUNDARIO,
#                         ),
#                     ],
#                 ),
#                 expand=True,
#                 padding=8,
#             ),
#         ],
#     )


@ft.component
def PostoForm():
    return BaseForm(
        [
            [
                {
                    "label": "nome",
                    "icon": ft.Icons.TITLE,
                    "get": lambda x: x.nome,
                    "set": lambda x, y: x.set_nome(y),
                },
                {
                    "label": "local",
                    "icon": ft.Icons.LOCATION_CITY,
                    "get": lambda x: x.local,
                    "set": lambda x, y: x.set_local(y),
                },
            ],
            [
                {
                    "label": "imagem",
                    "icon": ft.Icons.IMAGE,
                    "tipo": "imagem",
                    "get": lambda x: x.imagem,
                    "set": lambda x, y: x.set_imagem(y),
                }
            ],
            [
                {
                    "label": "descrição",
                    "icon": ft.Icons.DOCUMENT_SCANNER,
                    "get": lambda x: x.descricao,
                    "set": lambda x, y: x.set_descricao(y),
                }
            ],
        ],
        Posto(1, "", [], "", "", "", 0),
        obter_posto,
        "postos"
    )


# _texto_celula(p["nome"], negrito=True),
# _texto_celula(p["local"], secundario=True),
# _texto_celula(str(p["carregadores"])),
# _texto_celula(f'R$ {p["preco"]:.2f}'.replace(".", ",")),
# ft.DataCell(badge_status(p["status"])),


@ft.component
def PostosAdmin():
    return TabelaAdmin(
        obter_postos(),
        [
            {
                "cabecalho": "imagem",
                "celula": lambda x: {"valor": "", "content": ft.Image(x.imagem, width=100, height=60)}
            },
            {
                "cabecalho": "nome",
                "celula": lambda x: {"valor": x.nome, "negrito": True},
            },
            {
                "cabecalho": "local",
                "celula": lambda x: {"valor": x.local, "secundario": True},
            },
            {
                "cabecalho": "carregadores",
                "celula": lambda x: {"valor": str(len(x.carregadores))},
            },
            {
                "cabecalho": "preço",
                "celula": lambda x: {
                    "valor": f"R$ {x.preco_medio:.2f}".replace(".", ",")
                },
            },
            # {
            #     "cabecalho": "status",
            #     "celula": lambda x: {
            #         "valor": "",
            #         "content": badge_status(x.)
            #     }
            # }
        ],
        "posto",
        "/postos/form",
        "postos",
    )

    # _texto_celula(p["nome"], negrito=True),
    # _texto_celula(p["local"], secundario=True),
    # _texto_celula(str(p["carregadores"])),
    # _texto_celula(f'R$ {p["preco"]:.2f}'.replace(".", ",")),
    # ft.DataCell(badge_status(p["status"])),
