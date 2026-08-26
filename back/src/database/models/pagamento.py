from sqlalchemy import ForeignKey

from src.database.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from back.src.database.models.posto import Posto

class Pagamento(BaseModel):
    __tablename__="pagamento"
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    # veiculo_id: Mapped[int] = mapped_column(ForeignKey("veiculo.id"))
    # recarga_id: Mapped[int] = mapped_column(ForeignKey("recarga.id"))
    # data_hora: Mapped[int] = mapped_column()
    # local_eletroposto: Mapped[int] = mapped_column()
    # energia_consumida_kwh: Mapped[int] = mapped_column()
    # tempo_carregamento: Mapped[int] = mapped_column()
    # preco_kwh: Mapped[int] = mapped_column()
    # desconto: Mapped[int] = mapped_column()
    # taxa_utilizacao: Mapped[int] = mapped_column()
    # seguranca: Mapped[int] = mapped_column()
    # comprovante: Mapped[int] = mapped_column()
    # custo_economizado_combustivel: Mapped[int] = mapped_column()
    quantidade: Mapped[int] = mapped_column()
    forma_pagamento: Mapped[str] = mapped_column()
        # Cartao de credito
        # Cartao de debito
        # PIX
        # Carteira digital/saldo
        # Cartao cadastrado
        # Ultimos 4 digitos do cartao, por exemplo: ____ 1234
        # Opcao para adicionar novo metodo de pagamento

        # Seguranca

        # Status do pagamento: Pendente / Processando / Aprovado / Recusado
        # Identificacao da transacao
        # Data/hora da transacao
        # Mensagem de confirmacao
        # Informacao de que o pagamento foi processado com seguranca

        # Comprovante

        #Numero da transacao
        # Valor pago
        # Forma de pagamento
        # Data e horario
        # Resumo da recarga
        # Baixar/visualizar comprovante
        # Enviar comprovante por e-mail

        # EXTRA

        #Economia em relacao a combustivel
        # CO2 evitado
        # Historico de pagamentos
        # Historico de recargas
        # Programa de pontos/beneficios/fidelidade
        # Cupom ou codigo promocional
