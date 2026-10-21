# import json
# import os
# from typing import Callable, Optional, TypedDict

# from google import genai
# import requests


# from src.dados import Mensagem, MensagemChat
# from src.ai.client.adapters.ai_adapter import AiAdapter, system_prompts


# class GeminiGenaiAdapter(AiAdapter):
#     def chamarDiretamente(
#         self,
#         prompt: str,
#         historico: list[Mensagem] = [],
#         system: system_prompts = "assets/prompts/system_prompt.md",
#         formato: Optional[dict] = None,
#     ):
#         client = genai.Client(api_key= os.getenv("CHAVE_GEMINI", ""))
#         mensagens: list[dict] = []
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
#         system_prompt = ""
#         with open(system, "r", encoding="utf-8") as f:
#             system_prompt = f.read()
#         resposta = client.models.generate_content(model="gemini-3.1-flash-lite", contents=mensagens,  config={
#             "response_json_schema": formato,
#             "response_mime_type":  "application/json" if formato else None,
            
#             "thinking_config": {
#                 "thinking_budget": 0
#             },
#             "system_instruction": {"parts": [{"text": system_prompt}]},
#         })

#         return resposta.text if resposta.text else "algo deu errado"
#         # return ""

#     # def chamarStream(
#     #     self,
#     #     observador: Callable[[str], None],
#     #     prompt: str,
#     #     historico: list[Mensagem] = [],
#     #     system: system_prompts = "assets/prompts/system_prompt.md",
#     # ):
#     #     return super().chamarStream(observador, prompt, historico, system)
