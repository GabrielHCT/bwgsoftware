# core/styles.py

import streamlit as st
from pathlib import Path


def carregar_css(arquivo):
    path = Path(arquivo)

    if not path.exists():
        return

    with open(path, "r", encoding="utf-8") as f:
        css = f.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )


def aplicar_estilos():
    carregar_css("assets/styles.css")

    dark_mode = st.session_state.get(
        "dark_mode",
        False,
    )

    if dark_mode:
        carregar_css("assets/dark.css")