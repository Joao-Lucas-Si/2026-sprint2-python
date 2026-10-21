import flet as ft

from src.utils.use_colors import usar_cores

# Troque TemaEscuro pelo seu `usar_cores()` quando integrar com o tema do projeto.
# T = TemaEscuro

def status_posto():
    Cores = usar_cores()
    STATUS_POSTO = {
        "disponivel": ("Disponível", Cores.DISPONIVEL),
        "ocupado": ("Ocupado", Cores.OCUPADO),
        "manutencao": ("Manutenção", Cores.MANUTENCAO),
    }
    return STATUS_POSTO


@ft.component
def card(conteudo: ft.Control, expand=None, padding: int = 20, altura: int | None = None) -> ft.Container:
    """Caixa escura com borda sutil — base de todos os blocos do admin."""
    T = usar_cores()
    return ft.Container(
        content=conteudo,
        expand=expand,
        height=altura,
        padding=padding,
        bgcolor=T.CARD,
        border_radius=16,
        border=ft.Border.all(1, T.CARD_BORDA),
    )


@ft.component
def titulo_secao(texto: str, acao: ft.Control | None = None) -> ft.Row:
    T = usar_cores()
    controles = [ft.Text(texto, size=14, color=T.TEXTO_SECUNDARIO)]
    if acao is not None:
        controles.append(acao)
    return ft.Row(
        controls=controles,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

@ft.component
def badge_status(status: str) -> ft.Container:
    STATUS_POSTO = status_posto()
    T= usar_cores()
    texto, cor = STATUS_POSTO.get(status, STATUS_POSTO["manutencao"])
    return ft.Container(
        content=ft.Text(texto, size=11, weight=ft.FontWeight.BOLD, color=T.FUNDO),
        bgcolor=cor,
        border_radius=20,
        padding=ft.Padding.symmetric(horizontal=10, vertical=3),
    )

@ft.component
def badge_delta(delta: float) -> ft.Row:
    Cores = usar_cores()
    subiu = delta >= 0
    cor = Cores.DISPONIVEL if subiu else Cores.PRIMARIO_CLARO
    icone = ft.Icons.ARROW_UPWARD if subiu else ft.Icons.ARROW_DOWNWARD
    return ft.Row(
        spacing=4,
        controls=[
            ft.Icon(icone, size=14, color=cor),
            ft.Text(f"{delta:+.1f}%".replace(".", ","), size=12, color=cor),
        ],
    )


@ft.component
def kpi_card(rotulo: str, valor: str, delta: float) -> ft.Container:
    T = usar_cores()
    return card(
        ft.Column(
            spacing=6,
            controls=[
                ft.Text(rotulo, size=13, color=T.TEXTO_SECUNDARIO),
                ft.Text(valor, size=28, weight=ft.FontWeight.W_600, color=T.TEXTO),
                badge_delta(delta),
            ],
        ),
        expand=True,
    )