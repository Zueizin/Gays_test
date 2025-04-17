import streamlit as st
import random

def mensagem(nivel):
    if nivel == 0:
        return "### Chad Detectado 🗿🗿🗿 "
    elif nivel < 20:
        return "Quase hétero... quase!"
    elif nivel < 50:
        return "Um pé no arco-íris 🦶🌈"
    elif nivel < 80:
        return "Bastante glitter por aqui!"
    elif nivel <= 100:
        return "Ícone LGBT...+ 🌟"
    else:
        return "<UNK>cone LGBT...+ <UNK>"

def medir_nivel_gay(nome):
    if nome == "baiano":
        return 100
    elif nome == "aurelio":
        return 0
    elif nome == "tavas":
        return 0
    elif nome == "theyllor":
        return 1000000000
    else:
        random.seed(nome.lower())
        return random.randint(0, 100)

st.title("🌈 Medidor de Nível Gay")

if "mostrar_resultado" not in st.session_state:
    st.session_state.mostrar_resultado = False

if not st.session_state.mostrar_resultado:
    nome = st.text_input("Digite seu nome:").lower()
    if nome:
        st.session_state.nome = nome
        st.session_state.nivel = medir_nivel_gay(nome)
        st.session_state.mostrar_resultado = True
        st.rerun()

if st.session_state.mostrar_resultado:
    nome = st.session_state.nome
    nivel = st.session_state.nivel

    st.subheader(f"{nome.title()}, seu nível gay é: {nivel}%")
    st.progress(nivel)
    st.success(mensagem(nivel))

    if nivel == 100:
        st.balloons()
    elif nivel >= 80:
        st.write("💅💖✨")

    if st.button("🔁 Testar outro nome"):
        st.session_state.mostrar_resultado = False
        st.rerun()
