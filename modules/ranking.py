# modules/ranking.py

import streamlit as st


def render_ranking():
    st.title("🏆 Ranking")

    st.markdown(
        """
        <div class="module-hero">
            <h2>Ranking de Produtos</h2>
            <p>Acesse rankings rápidos por portal, venda e quantidade. Todos os rankings mostram Top 10.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info("Abra o módulo 🔥 Top 10 Rankings no menu lateral para visualizar os rankings completos.")