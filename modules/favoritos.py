# modules/favoritos.py

import streamlit as st

from core.favorites_engine import (
    inicializar_favoritos,
    remover_favorito,
)


def render_favoritos():

    st.title("⭐ Favoritos")

    inicializar_favoritos()

    favoritos = st.session_state["favoritos"]

    if not favoritos:
        st.info("Nenhum favorito.")
        return

    for produto in favoritos:

        with st.container():

            st.markdown(
                f"""
                <div class="produto-card">

                <div class="produto-title">
                    {produto['descricao']}
                </div>

                <div class="produto-meta">
                    SKU: {produto['skuSeller']}
                </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                "Remover",
                key=produto["skuSeller"]
            ):
                remover_favorito(
                    produto["skuSeller"]
                )

                st.rerun()