from gtts import gTTS
import os

def falar(texto, idioma="pt"):
    tts = gTTS(text=texto, lang=idioma)
    caminho = "resposta.mp3"
    tts.save(caminho)
    return caminho
