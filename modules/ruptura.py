# modules/ruptura.py

import streamlit as st

from core.sheets import carregar_dados
from core.dashboard import preparar_dataframe_produtos
from core.rupture_engine import calcular_risco_ruptura


def render_ruptura(portal):

    st.title("📦 Previsão de Ruptura")

    df = carregar_dados(portal)

    df_produtos = preparar_dataframe_produtos(df)

    ruptura = calcular_risco_ruptura(df_produtos)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Críticos",
        len(ruptura[ruptura["risco"] == "CRÍTICO"])
    )

    col2.metric(
        "Altos",
        len(ruptura[ruptura["risco"] == "ALTO"])
    )

    col3.metric(
        "Médios",
        len(ruptura[ruptura["risco"] == "MÉDIO"])
    )

    col4.metric(
        "Baixos",
        len(ruptura[ruptura["risco"] == "BAIXO"])
    )

    st.divider()

    st.dataframe(
        ruptura[
            [
                "sku",
                "descricao",
                "marca",
                "estoqueTotal",
                "vendaTotal",
                "diasRestantes",
                "risco",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )