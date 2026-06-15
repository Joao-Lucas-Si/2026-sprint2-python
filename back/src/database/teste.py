from src.database.models.carregador import Carregador
from src.database.models.posto import Posto
from src.database.services.posto import PostoQuery


def exemplos():
    posto1 = Posto()
    posto1.id = 1
    posto1.nome = "posto shopping tamboré"
    carregador1 = Carregador()
    carregador1.capacidade = 10
    carregador1.disponivel = 1000
    posto1.carregadores = [Carregador.instanciar(capacidade=14, disponivel=1000, ocupado=False), Carregador.instanciar(capacidade=21, disponivel=1100, ocupado=False)]

    posto2 = Posto()
    posto2.id = 2
    posto2.nome = "posto do aeroporto"
    carregador2 = Carregador()
    carregador2.capacidade = 10
    carregador2.disponivel = 900
    posto2.carregadores = [Carregador.instanciar(capacidade=10, disponivel=1100, ocupado=True), Carregador.instanciar(capacidade=20, disponivel=1500, ocupado=False)]

    posto3 = Posto()
    posto3.id = 3
    posto3.nome = "posto ipiranga"
    carregador3 = Carregador()
    carregador3.capacidade = 50
    carregador3.disponivel = 2000
    posto3.carregadores = [Carregador.instanciar(capacidade=34, disponivel=1500, ocupado=False), Carregador.instanciar(capacidade=30, disponivel=1000, ocupado=True), Carregador.instanciar(capacidade=24, disponivel=2000, ocupado=False)]

    posto4 = Posto()
    posto4.id = 4
    posto4.nome = "posto do villa lobos"
    carregador4 = Carregador()
    carregador4.capacidade = 25
    carregador4.disponivel = 1500
    posto4.carregadores = [Carregador.instanciar(capacidade=4, disponivel=500, ocupado=True), Carregador.instanciar(capacidade=13, disponivel=1000, ocupado=True)]
    
    return [posto1, posto2, posto3, posto4]

def criarExemplos():
    query = PostoQuery()
    if query.tamanho() == 0:
        postos = exemplos()
        for posto in postos:
            query.adicionar(posto)