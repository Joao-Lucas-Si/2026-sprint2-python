
from src.database.teste import criarExemplos
from src.database.services.usuario import UsuarioQuery
from src.database.inicializacao import iniciarBanco
from app import app, socketio
import src.controlers.usuarios
import src.controlers.posto
import src.controlers.ocpp


# @app.route("/")
# def index():
#     servico = UsuarioQuery()
#     return f"{servico.tamanho()}"

    
    

if __name__ == "__main__":
    iniciarBanco()
    criarExemplos()
    socketio.run(app)