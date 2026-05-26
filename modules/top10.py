# modules/top10.py

import streamlit as st

from core.config import RANKING_PORTAIS
from core.rankings import buscar_ranking_top10_portal
from core.helpers import moeda
from components.charts import grafico_top10_ranking


def render_top10(portal_dre):
    st.title("🔥 Top 10 Rankings")

    col1, col2 = st.columns(2)

    with col1:
        portal_ranking = st.selectbox(
            "Portal do Ranking",
            ["Geral"] + RANKING_PORTAIS,
            index=0,
        )

    with col2:
        criterio = st.radio(
            "Critério",
            ["quantidade", "venda"],
            horizontal=True,
        )

    ranking = buscar_ranking_top10_portal(
        portal_dre=portal_dre,
        portal_ranking=portal_ranking,
        criterio=criterio,
    )

    if ranking.empty:
        st.warning("Nenhum item encontrado para esse ranking.")
        return

    total_venda = ranking["venda"].sum()
    total_quantidade = ranking["quantidade"].sum()
    principal = ranking.iloc[0]["descricao"]

    colA, colB, colC = st.columns(3)

    colA.metric("Produtos", len(ranking))
    colB.metric("Venda Total Top 10", moeda(total_venda))
    colC.metric("Quantidade Top 10", int(total_quantidade))

    st.info(f"🏆 Principal item: {principal}")

    st.divider()

    coluna_grafico = "venda" if criterio == "venda" else "quantidade"

    grafico_top10_ranking(ranking, coluna_grafico)

    st.divider()

    st.dataframe(
        ranking[
            [
                "posicao",
                "sku",
                "ean",
                "marca",
                "descricao",
                "portal",
                "venda",
                "quantidade",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )