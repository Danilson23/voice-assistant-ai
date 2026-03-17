import streamlit as st
from utils.chat import responder
from utils.history import salvar
from utils.tts import falar

st.set_page_config(page_title="Voice Assistant AI")

st.title("🎤 Assistente Inteligente com IA")

texto = st.text_input("Digite sua pergunta:")

if st.button("Enviar") and texto:
    resposta, idioma = responder(texto)

    st.subheader("🤖 Resposta:")
    st.write(resposta)

    salvar(texto, resposta)

    audio_path = falar(resposta, idioma)
    st.audio(audio_path)
