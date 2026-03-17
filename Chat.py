import os
from openai import OpenAI
from dotenv import load_dotenv
from utils.language import detectar_idioma

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def responder(texto):
    idioma = detectar_idioma(texto)

    prompt = f"""
    Você é um assistente inteligente.

    Responda no mesmo idioma ({idioma}).
    Seja claro, direto e útil.

    Usuário: {texto}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content, idioma
