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
    elif nivel == 90:
        return "Theyllor passou por aqui 🏳️‍🌈!"
    elif nivel == 80:
        return "Viadinho...🦄✨"
    elif nivel == 99:
        return "Baitolinha ein...💅✨👠"
    elif nivel == 95:
        return "Ui ui... És ganda paneleiro miga 💅✨👑"
    elif nivel <= 100:
        return "Ícone LGBT...+ 🌟"
    else:
        return "<UNK>cone LGBT...+ <UNK>"

def medir_nivel_gay(nome):
    if nome == "baiano" or nome == "joão pedro" or nome == "joao pedro":
        return 100
    elif nome == "aurelio" or nome == "aurélio":
        return 0
    elif nome == "tavas" or nome == "tavares" or nome == "joao victor" or nome == "joão victor":
        return 0
    elif nome == "pilot" or nome == "guilherme":
        return 99
    elif nome == "squilassi" or nome == "jaum":
        return 0
    elif nome == "gustavo" or nome == "gus":
        return 80
    elif nome == "davi":
        return 90
    elif nome == "tiago":
        return 95
    elif nome == "pedro" or nome == "pedrao" or nome == "pedrão":
        return 19
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
    if nivel == 95:
        st.snow()
    elif nivel >= 80:
        st.write("💅💖✨")

    if st.button("🔁 Testar outro nome"):
        st.session_state.mostrar_resultado = False
        st.rerun()
