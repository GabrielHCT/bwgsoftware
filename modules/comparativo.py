# modules/comparativo.py

import streamlit as st

from core.sheets import carregar_dados
from core.dashboard import preparar_dataframe_produtos
from core.compare_engine import comparar_portais

from core.config import PORTAIS

import plotly.express as px


def render_comparativo():

    st.title("📈 Comparativo Entre Portais")

    dfs = {}

    with st.spinner("Carregando portais..."):

        for portal in PORTAIS.keys():

            df = carregar_dados(portal)

            dfs[portal] = preparar_dataframe_produtos(df)

    comparativo = comparar_portais(dfs)

    if comparativo.empty:
        st.warning("Sem dados.")
        return

    st.dataframe(
        comparativo,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    fig = px.bar(
        comparativo,
        x="portal",
        y="vendaTotal",
        title="Venda Total por Portal",
        text_auto=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    fig2 = px.bar(
        comparativo,
        x="portal",
        y="lucroTotal",
        title="Lucro Total por Portal",
        text_auto=True,
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
    )