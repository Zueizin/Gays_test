import streamlit as st
import os
st.title("📝 Cadastro Simples de Nomes")
st.write("Digite um nome para cadastrar. O sistema verificará se já existe.")
ARQUIVO_TXT = 'nomes_cadastrados.txt'
nomes_cadastrados = []
if os.path.exists(ARQUIVO_TXT):
    with open(ARQUIVO_TXT, 'r') as f:
        nomes_cadastrados = [linha.strip() for linha in f.readlines() if linha.strip()]
nome = st.text_input("Digite um nome:")
if st.button("Cadastrar"):
    if not nome:
        st.warning("Por favor, digite um nome!")
    elif nome.lower() in [n.lower() for n in nomes_cadastrados]:
        st.error(f"O nome '{nome}' já está cadastrado!")
    else:
        with open(ARQUIVO_TXT, 'a') as f:
            f.write(nome + '\n')
        st.success(f"Nome '{nome}' cadastrado com sucesso!")
        nomes_cadastrados.append(nome)
if nomes_cadastrados:
    st.subheader("Nomes Cadastrados:")
    for nome in nomes_cadastrados:
        st.write(f"- {nome}")
    st.write(f"Total: {len(nomes_cadastrados)} nomes")
else:
    st.info("Nenhum nome cadastrado ainda.")
if st.checkbox("Mostrar opção de reset"):
    if st.button("Apagar todos os nomes"):
        if os.path.exists(ARQUIVO_TXT):
            os.remove(ARQUIVO_TXT)
            nomes_cadastrados = []
            st.success("Todos os nomes foram removidos!")