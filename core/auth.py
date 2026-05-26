# core/auth.py

import streamlit as st


USUARIOS = {
    "admin": {
        "senha": "admin123",
        "perfil": "admin",
    },

    "comercial": {
        "senha": "comercial123",
        "perfil": "comercial",
    }
}


def login():

    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if st.session_state["autenticado"]:
        return True

    st.markdown(
        """
        <div style="
            max-width:420px;
            margin:auto;
            margin-top:120px;
            background:white;
            padding:35px;
            border-radius:28px;
            box-shadow:0 12px 34px rgba(15,23,42,.12);
        ">
        <h1 style="text-align:center;">🔐 Login</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", use_container_width=True):

        if usuario in USUARIOS:

            user = USUARIOS[usuario]

            if user["senha"] == senha:

                st.session_state["autenticado"] = True
                st.session_state["usuario"] = usuario
                st.session_state["perfil"] = user["perfil"]

                st.rerun()

        st.error("Usuário ou senha inválidos.")

    return False


def logout():
    st.session_state.clear()
    st.rerun()