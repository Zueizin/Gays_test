import streamlit as st
import app as pd
import os

st.title("Formulário de Cadastro")

# Use keys ÚNICAS
nome = st.text_input("Nome", key="form_nome")
email = st.text_input("Email", key="form_email")

# Botão
if st.button("Salvar", key="botao_salvar"):
    if nome and email:
        novo_dado = pd.DataFrame([[nome, email]], columns=["Nome", "Email"])

        if os.path.exists("dados.csv"):
            dados = pd.read_csv("dados.csv")
            dados = pd.concat([dados, novo_dado], ignore_index=True)
        else:
            dados = novo_dado

        dados.to_csv("dados.csv", index=False)
        st.success("Dados salvos com sucesso!")
    else:
        st.warning("Preencha todos os campos.")
