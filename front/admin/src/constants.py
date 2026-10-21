from enum import Enum, EnumType
import flet as ft

class Constantes(Enum):
    HOST="http://localhost:5000"
    OBTER_POSTO = lambda x: f"postos/{x}"


import flet as ft


class Cores:
    """
    Paleta inspirada na identidade visual da GoodWe:
    preto/branco como base neutra + gradiente laranja-vermelho como
    cor de destaque (energia, ação, "power").
    """

    # Gradiente principal — usado em botões de destaque e na nav bar inferior
    GRADIENTE_PRIMARIO = ["#FF6B4A", "#E8351C", "#C41E12"]

    # Tons sólidos do laranja-vermelho (derivados do gradiente),
    # úteis quando não dá pra aplicar gradient (ex: ícones, bordas, texto de destaque)
    PRIMARIO = "#E8351C"         # tom médio do gradiente
    PRIMARIO_CLARO = "#FF6B4A"   # ponta mais clara
    PRIMARIO_ESCURO = "#C41E12"  # ponta mais escura

    SUCESSO= "#4CAF50"
    ATENCAO= "#FB7944"
    ERRO= "#FD241B"

    # Status (mantidos iguais nos dois temas para consistência semântica)
    DISPONIVEL = "#2ECC71"
    OCUPADO = "#FF6B4A"       # reaproveita o tom do gradiente pra "ocupado/alerta"
    MANUTENCAO = "#F5A623"

    FUNDO = "#FFFFFF"             # fundo geral (branco puro, estilo GoodWe)
    FUNDO_SECUNDARIO = "#F5F5F7"  # fundo de seções/inputs
    CARD = "#FFFFFF"
    CARD_BORDA = "#EAEAEC"        # cards no claro precisam de borda sutil pra se destacar

    TEXTO = "#1A1A1A"             # quase preto, não preto puro (mais suave)
    TEXTO_SECUNDARIO = "#6E6E76"
    TEXTO_PRIMARIO = "#FFFFFF"  # texto em cima do gradiente/laranja

    ICONE = "#1A1A1A"
    ICONE_INATIVO = "#B0B0B6"

    DIVISOR = "#EAEAEC"
    SOMBRA = "#00000014"

    @staticmethod
    def gradiente(begin=None, end=None) -> ft.LinearGradient:
        """Helper pra criar o LinearGradient padrão em qualquer container/botão."""
        return ft.LinearGradient(
            begin=begin or ft.Alignment.TOP_LEFT,
            end=end or ft.Alignment.BOTTOM_RIGHT,
            colors=Cores.GRADIENTE_PRIMARIO,
        )



class TemaClaro(Cores):
    """Paleta para o tema claro."""

    FUNDO = "#FFFFFF"             # fundo geral (branco puro, estilo GoodWe)
    FUNDO_SECUNDARIO = "#F5F5F7"  # fundo de seções/inputs
    CARD = "#FFFFFF"
    CARD_BORDA = "#EAEAEC"        # cards no claro precisam de borda sutil pra se destacar

    TEXTO = "#1A1A1A"             # quase preto, não preto puro (mais suave)
    TEXTO_SECUNDARIO = "#6E6E76"
    TEXTO_PRIMARIO = "#FFFFFF"  # texto em cima do gradiente/laranja

    ICONE = "#1A1A1A"
    ICONE_INATIVO = "#B0B0B6"

    DIVISOR = "#EAEAEC"
    SOMBRA = "#00000014"  # preto com ~8% de opacidade, pra shadow de cards


class TemaEscuro(Cores):
    """Paleta para o tema escuro."""

    FUNDO = "#0F0F12"             # preto suave, não 100% preto
    FUNDO_SECUNDARIO = "#1A1A1F"
    CARD = "#1C1C22"
    CARD_BORDA = "#2A2A31"

    TEXTO = "#F5F5F7"
    TEXTO_SECUNDARIO = "#9A9AA2"
    TEXTO_PRIMARIO = "#FFFFFF"

    ICONE = "#F5F5F7"
    ICONE_INATIVO = "#5A5A63"

    DIVISOR = "#2A2A31"
    SOMBRA = "#00000040"  # sombra mais forte, já que o fundo é escuro

    
    
# class Cores(EnumType):
#     RPIMARIO= "#FD241B"
#     PRIMARIO_ESCURO= "#D62627"
#     PRIMARIO_CLARO = "#FD502D"

#     FUNDO= "#17181B"
#     SUPERFICIE= "#292729"
#     SUPERFICIE_ESCURO= "#120909"

#     TEXTO_PRIMARIO= "#FDE6DE"
#     TEXTO_SECUNDARIO= "#B9ADBA"
#     TEXTO_DESATIVADO= "#944749"

#     BORDA= "#EBB3A4"
#     BORDA_FOCADA= "#FD502D"

#     SUCESSO= "#4CAF50"
#     ATENCAO= "#FB7944"
#     ERRO= "#FD241B"

    
#     FUNDO_ESCURO= "#17181B"
#     INPUT_FUNDO= "#120909"
#     INPUT_BORDA= "#EBB3A4"
#     INPUT_FOCADO= "#FD502D"
#     # TEXTO_PRINCIPAL ="#FDE6DE",
#     # TEXTO_SECUNDARIO= "#B9ADBA",
    
    
class EstiloConstantes(Enum):
    borda=ft.Border.all(1, Cores.PRIMARIO_CLARO, )
    arredondamento=ft.BorderRadius.all(6)
class Assets(EnumType):
    login_fundo="assets/login-fundo.jpeg"