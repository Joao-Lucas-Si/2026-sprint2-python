from flask import request
from app import app
from src.ai.engine.ai_engine import AiEngine


@app.route("/chat", methods=["POST"])
def chat():
    try:

        engine = AiEngine()
        json = request.json
        return engine.responder(json["pergunta"])
    except Exception as e:
        return e.__str__()