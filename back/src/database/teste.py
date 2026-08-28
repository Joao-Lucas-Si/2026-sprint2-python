from src.database.models.carregador import Carregador
from src.database.models.posto import Posto
from src.database.services.posto import PostoQuery


def exemplos():
    posto1 = Posto()
    posto1.id = 1
    posto1.nome = "posto shopping tamboré"
    posto1.descricao = ""
    posto1.local = ""
    posto1.imagem = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fallos.com.br%2Fwp-content%2Fuploads%2F2022%2F12%2FShop_Tambore.jpg&f=1&nofb=1&ipt=9f7287e407af1ee09aa57dc927c3888abc353d52db354429ad96839622fa7d48"
    posto1.carregadores = [Carregador.instanciar(capacidade=14, disponivel=1000, preco=1, ocupado=False), Carregador.instanciar(capacidade=21, preco=1.4, disponivel=1100, ocupado=False)]

    posto2 = Posto()
    posto2.id = 2
    posto2.nome = "posto do aeroporto"
    posto2.descricao = ""
    posto2.local = ""
    posto2.imagem = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ft.ctcdn.com.br%2F2MSB9UU34OZsh8Gxf5dJJM9tPdw%3D%2F4000x2250%2Fsmart%2Fi731618.jpeg&f=1&nofb=1&ipt=f3f69b653ac1561044795c57e2aec9ec643be610f2d66c7c1ec42fac101886f6"
    posto2.carregadores = [Carregador.instanciar(capacidade=10, disponivel=1100, preco=0.5, ocupado=True), Carregador.instanciar(capacidade=20, preco=2, disponivel=1500, ocupado=False)]

    posto3 = Posto()
    posto3.id = 3
    posto3.nome = "posto ipiranga"
    posto3.descricao = ""
    posto3.local = ""
    posto3.imagem = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpetrolgroup.pro%2Fwp-content%2Fuploads%2F2025%2F06%2FSite-_-Capa-do-Blog-1920X1080.png&f=1&nofb=1&ipt=ebe0a6c7f9bf2c952baf51a2ebd9688685f14f44be27cba0610b74dd6ed64b78"
    posto3.carregadores = [Carregador.instanciar(capacidade=34, disponivel=1500, preco=0.9, ocupado=False), Carregador.instanciar(capacidade=30, preco=0.4, disponivel=1000, ocupado=True), Carregador.instanciar(capacidade=24, preco=1, disponivel=2000, ocupado=False)]

    posto4 = Posto()
    posto4.id = 4
    posto4.nome = "posto do villa lobos"
    posto4.descricao = ""
    posto4.local = ""
    posto4.imagem = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fallos.com.br%2Fwp-content%2Fuploads%2F2022%2F12%2FFoto_att_8.jpg&f=1&nofb=1&ipt=d1e18c162b749c919e527795d9530ba832aecee50cc7eea7a283cd4f115c8154"
    posto4.carregadores = [Carregador.instanciar(capacidade=4, disponivel=500, preco=1.2, ocupado=True), Carregador.instanciar(capacidade=13, preco=1.5, disponivel=1000, ocupado=True)]
    
    return [posto1, posto2, posto3, posto4]

def criarExemplos():
    query = PostoQuery()
    if query.tamanho() == 0:
        postos = exemplos()
        for posto in postos:
            query.adicionar(posto)