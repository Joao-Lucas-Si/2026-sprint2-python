import flet as ft

from src.dados import Usuario
from src.routes.base.read_table import TabelaAdmin
from src.routes.dados import obter_usuario, obter_usuarios
from src.routes.base.base_forma import BaseForm

@ft.component
def UsuarioForm():
    print("form")
    return BaseForm([
        [
            {
                "label": "nome",
                "icon": ft.Icons.PEOPLE,
                "get": lambda x: x.nome,
                "set": lambda x, y: x.set_nome(y)
            },
            {
                "label": "email",
                "icon": ft.Icons.EMAIL,
                "get": lambda x: x.email,
                "set": lambda x, y: x.set_email(y)
            },
            
        ],
        [
            {
                "label": "senha",
                "icon": ft.Icons.PASSWORD,
                "get": lambda x: "",
                "set": lambda x, y: x.set_senha(y)
            },
            {
                "label": "role",
                "icon": ft.Icons.SECURITY,
                "get": lambda x: x.role,
                "set": lambda x, y: x.set_role(y),
                "opcoes": [
                    ("usuario","usuario"),
                    ("admin","admin"),
                    ("dono","dono")
                ],
                "tipo": "selecao"
            }
        ]
    ], Usuario(), lambda x: obter_usuario(x), "usuarios")

@ft.component
def UsuarioTabela():
    return TabelaAdmin(obter_usuarios(), [
        {
            'cabecalho': "nome",
            "celula": lambda x: {
                "valor": x.nome
            }
        },
        {
            "cabecalho": "email",
            "celula": lambda x: {
                "valor": x.email
            }
        }
    ], "usuario", "usuarios/form", "usuarios")