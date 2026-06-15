from sqlalchemy import Engine, create_engine


caminho = "sqlite:///data.db"

# db = create_engine(caminho)
db: Engine|None = None
def instanciarBanco() -> Engine:
    global db
    if db is None:
        db = create_engine(caminho)
    if db:
        return db
    raise Exception("por algum motivo não foi possivel instanciar o banco")