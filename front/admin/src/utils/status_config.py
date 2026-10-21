from src.utils.use_colors import usar_cores


def status_config(status: str):
    Cores = usar_cores()

    """Retorna (texto, cor) de acordo com o status do posto."""
    if status == "disponivel":
        return "Disponível", Cores.DISPONIVEL
    elif status == "ocupado":
        return "Ocupado", Cores.OCUPADO
    else:
        return "Manutenção", Cores.MANUTENCAO
