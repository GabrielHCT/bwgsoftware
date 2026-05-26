# modules/simulador.py

import streamlit as st

from core.simulator_engine import calcular_simulacao
from core.helpers import moeda, percentual_formatado


def render_simulador():

    st.title("🧮 Simulador Avançado")

    col1, col2 = st.columns(2)

    with col1:

        preco = st.number_input(
            "Preço Venda",
            min_value=0.0,
            value=100.0,
        )

        custo = st.number_input(
            "Custo",
            min_value=0.0,
            value=50.0,
        )

        comissao = st.number_input(
            "Comissão %",
            min_value=0.0,
            value=15.0,
        )

    with col2:

        bseller = st.number_input(
            "B Seller %",
            min_value=0.0,
            value=5.0,
        )

        bportal = st.number_input(
            "B Portal %",
            min_value=0.0,
            value=2.0,
        )

    resultado = calcular_simulacao(
        preco=preco,
        custo=custo,
        comissao=comissao / 100,
        bseller=bseller / 100,
        bportal=bportal / 100,
    )

    st.divider()

    colA, colB, colC, colD = st.columns(4)

    colA.metric(
        "Lucro",
        moeda(resultado["lucro"])
    )

    colB.metric(
        "Margem",
        percentual_formatado(
            resultado["margem"]
        )
    )

    colC.metric(
        "Markup",
        f"{resultado['markup']:.2f}"
    )

    colD.metric(
        "Taxas",
        moeda(resultado["taxas"])
    )