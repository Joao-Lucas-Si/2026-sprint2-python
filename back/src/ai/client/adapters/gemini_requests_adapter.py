# import json
# import os
# from typing import Callable, Optional, TypedDict

# import requests


# from src.dados import Mensagem, MensagemChat
# from src.ai.client.adapters.ai_adapter import AiAdapter, system_prompts


# class GeminiAdapter(AiAdapter):
#     def chamarDiretamente(
#         self,
#         prompt: str,
#         historico: list[Mensagem] = [],
#         system: system_prompts = "assets/prompts/system_prompt.md",
#         formato: Optional[dict] = None,
#     ):
#         system_prompt = ""
#         with open(system, "r", encoding="utf-8") as f:
#             system_prompt = f.read()
#         mensagens = []
#         mensagens.extend(
#             map(
#                 lambda x: {
#                     "role": "model" if isinstance(x, MensagemChat) else "user",
#                     "parts": [{"text": x.conteudo}],
#                 },
#                 historico,
#             )
#         )
#         mensagens.append({"role": "user", "parts": [{"text": prompt}]})
#         config: dict = {"thinkingConfig": {"thinkingBudget": 0}}

#         if not formato is None:
#             config["responseFormat"] = {
#                 "text": {"mimeType": "application/json", "schema": formato}
#             }
#         resposta = requests.post(
#             "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent",
#             headers={
#                 "x-goog-api-key": os.getenv("CHAVE_GEMINI", ""),
#                 "Content-Type": "application/json",
#             },
#             json={
#                 "generationConfig": config,
#                 "system_instruction": {"parts": [{"text": system_prompt}]},
#                 "contents": mensagens,
#                 "options": {"temperature": 0.5, "num_predict": 250},
#             },
#         )

#         data = resposta.json()
#         raise Exception(json.dumps(data))
#         return  data["candidates"][0]["content"]["parts"][0]["text"]
#         # return ""

#     def chamarStream(
#         self,
#         observador: Callable[[str], None],
#         prompt: str,
#         historico: list[Mensagem] = [],
#         system: system_prompts = "assets/prompts/system_prompt.md",
#     ):
#         return super().chamarStream(observador, prompt, historico, system)
