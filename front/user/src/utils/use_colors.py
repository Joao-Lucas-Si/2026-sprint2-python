from src.constants import Cores, TemaClaro, TemaEscuro

def usar_cores() -> Cores:
    usar_escuro = True

    return TemaEscuro( ) if usar_escuro else TemaClaro