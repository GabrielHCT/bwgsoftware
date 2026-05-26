# components/kpis.py

import streamlit as st

from core.helpers import percentual_formatado


def render_kpis(produto):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Estoque Total",
            int(produto["estoqueTotal"])
        )

    with col2:
        st.metric(
            "Venda Total",
            int(produto["vendaTotal"])
        )

    with col3:
        st.metric(
            "Giro Estoque",
            f"{produto['giroEstoque']:.2f}"
        )

    with col4:
        st.metric(
            "Eficiência Portal",
            percentual_formatado(
                produto["eficienciaPortal"]
            )
        )

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric(
            "Cobertura Estoque",
            f"{produto['coberturaEstoque']:.2f}"
        )

    with col6:
        st.metric(
            "Comissão",
            percentual_formatado(produto["comissao"])
        )

    with col7:
        st.metric(
            "B Seller",
            percentual_formatado(produto["bSeller"])
        )

    with col8:
        st.metric(
            "B Portal",
            percentual_formatado(produto["bPortal"])
        )