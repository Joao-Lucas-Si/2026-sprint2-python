from enum import Enum, EnumType
import flet as ft

class Constantes(Enum):
    HOST="http://localhost:5000"
    OBTER_POSTO = lambda x: f"postos/{x}"
    
    
    
    
class Cores(EnumType):
    RPIMARIO= "#FD241B"
    PRIMARIO_ESCURO= "#D62627"
    PRIMARIO_CLARO = "#FD502D"

    FUNDO= "#17181B"
    SUPERFICIE= "#292729"
    SUPERFICIE_ESCURO= "#120909"

    TEXTO_PRIMARIO= "#FDE6DE"
    TEXTO_SECUNDARIO= "#B9ADBA"
    TEXTO_DESATIVADO= "#944749"

    BORDA= "#EBB3A4"
    BORDA_FOCADA= "#FD502D"

    SUCESSO= "#4CAF50"
    ATENCAO= "#FB7944"
    ERRO= "#FD241B"

    
    FUNDO_ESCURO= "#17181B"
    INPUT_FUNDO= "#120909"
    INPUT_BORDA= "#EBB3A4"
    INPUT_FOCADO= "#FD502D"
    # TEXTO_PRINCIPAL ="#FDE6DE",
    # TEXTO_SECUNDARIO= "#B9ADBA",
    
    
class EstiloConstantes(Enum):
    borda=ft.Border.all(1, Cores.PRIMARIO_CLARO, )
    arredondamento=ft.BorderRadius.all(6)
class Assets(EnumType):
    login_fundo="assets/login-fundo.jpeg"