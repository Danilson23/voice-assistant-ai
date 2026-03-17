import json
import os

ARQUIVO = "data/history.json"

def salvar(pergunta, resposta):
    if not os.path.exists("data"):
        os.makedirs("data")

    try:
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
    except:
        dados = []

    dados.append({
        "pergunta": pergunta,
        "resposta": resposta
    })

    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=2)
