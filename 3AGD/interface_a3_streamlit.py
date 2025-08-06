
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(page_title="MVP A3 – Assistente Cognitivo", layout="wide")
st.title("🤖  A3 – Assistente Cognitivo  (MVP)")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    with st.spinner("Consultando o modelo..."):
        try:
            resposta = requests.post(API_URL, json={"pergunta": pergunta})
            if resposta.status_code == 200:
                resultado = resposta.json()
                st.subheader("🔹 Origem da resposta:")
                st.write(resultado["origem"])
                st.subheader("🔹 Resposta:")
                st.write(resultado["resposta"])
            else:
                st.error(f"Erro {resposta.status_code}: {resposta.text}")
        except Exception as e:
            st.error(f"Erro de conexão: {e}")
