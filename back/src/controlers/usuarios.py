from flask import jsonify, request

from app import app
from src.database.models.usuario import Usuario
from src.database.services.usuario import UsuarioQuery


@app.route("/cadastro", methods = ["POST"])
def cadastro():

    dados = request.get_json()

    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]
    
    query = UsuarioQuery()
    
     
    existente = query.obterPorEmail(email)
    
    if existente:
        return jsonify({
            "erro": "usuario existente"
        })

    usuario = Usuario()
    usuario.nome = nome
    usuario.email = email
    usuario.senha = senha
    
    

    query.adicionar(usuario)
    
    
   
    
    return jsonify({"mensagem": "usuario cadastrado"})

@app.route("/login", methods = ["POST"])
def login():
    dados = request.get_json()
    email = dados["email"]
    senha = dados["senha"]

    query = UsuarioQuery()
   

    usuario = query.login(email, senha)

    if usuario:
        return jsonify({
            "id": usuario.id
        })
        
    return jsonify({
        "id": -1
    })