# core/realtime.py

import time
import streamlit as st


def auto_refresh(segundos=60):
    """
    Faz atualização automática simples da tela no Streamlit.
    """

    if "ultimo_refresh" not in st.session_state:
        st.session_state["ultimo_refresh"] = time.time()

    agora = time.time()
    diferenca = agora - st.session_state["ultimo_refresh"]

    restante = max(0, int(segundos - diferenca))

    st.caption(f"🔄 Atualização automática em {restante}s")

    if diferenca >= segundos:
        st.session_state["ultimo_refresh"] = agora
        st.rerun()