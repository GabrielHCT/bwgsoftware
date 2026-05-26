# modules/ranking_dia_anterior.py

import streamlit as st
import plotly.express as px

from core.config import PORTAIS
from core.ranking_day_engine import top10_vendidos_dia_anterior
from core.helpers import moeda


def render_ranking_dia_anterior():
    st.title("📅 Top 10 Vendidos no Dia Anterior")

    col1, col2 = st.columns(2)

    with col1:
        portal = st.selectbox(
            "Portal",
            list(PORTAIS.keys()),
            key="ranking_dia_portal",
        )

    with col2:
        criterio = st.radio(
            "Critério",
            ["quantidade", "valor"],
            horizontal=True,
            key="ranking_dia_criterio",
        )

    ranking = top10_vendidos_dia_anterior(
        portal=portal,
        criterio=criterio,
    )

    if ranking.empty:
        st.warning(
            "Nenhum produto vendido no dia anterior encontrado."
        )
        return

    total_qtd = ranking["quantidadeDiaAnterior"].sum()
    total_valor = ranking["valorDiaAnterior"].sum()

    colA, colB, colC = st.columns(3)

    colA.metric("Produtos", len(ranking))
    colB.metric("Quantidade", int(total_qtd))
    colC.metric("Valor", moeda(total_valor))

    st.divider()

    coluna_grafico = (
        "valorDiaAnterior"
        if criterio == "valor"
        else "quantidadeDiaAnterior"
    )

    fig = px.bar(
        ranking.sort_values(
            coluna_grafico,
            ascending=True,
        ),
        x=coluna_grafico,
        y="descricao",
        orientation="h",
        title=f"Top 10 vendidos ontem por {criterio}",
        text_auto=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.divider()

    st.dataframe(
        ranking,
        use_container_width=True,
        hide_index=True,
    )