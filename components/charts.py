# components/charts.py

import plotly.express as px
import streamlit as st


def grafico_top_marcas(df_produtos):
    if df_produtos.empty:
        st.info("Sem dados para gráfico.")
        return

    base = (
        df_produtos
        .groupby("marca", as_index=False)["vendaTotal"]
        .sum()
        .sort_values("vendaTotal", ascending=False)
        .head(10)
    )

    fig = px.bar(
        base,
        x="marca",
        y="vendaTotal",
        title="Top marcas por venda total",
        text_auto=True,
    )

    st.plotly_chart(fig, use_container_width=True)


def grafico_margem_estoque(df_produtos):
    if df_produtos.empty:
        st.info("Sem dados para gráfico.")
        return

    fig = px.scatter(
        df_produtos,
        x="estoqueTotal",
        y="margem",
        size="vendaTotal",
        hover_name="descricao",
        title="Margem x Estoque",
    )

    st.plotly_chart(fig, use_container_width=True)


def grafico_top10_ranking(ranking, criterio):
    if ranking.empty:
        st.info("Ranking vazio.")
        return

    fig = px.bar(
        ranking.sort_values(criterio, ascending=True),
        x=criterio,
        y="descricao",
        orientation="h",
        title=f"Top 10 por {criterio}",
        text_auto=True,
    )

    st.plotly_chart(fig, use_container_width=True)