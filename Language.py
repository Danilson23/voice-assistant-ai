from langdetect import detect

def detectar_idioma(texto):
    try:
        return detect(texto)
    except:
        return "pt"
