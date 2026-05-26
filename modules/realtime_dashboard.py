# modules/realtime_dashboard.py

import streamlit as st

from core.realtime import auto_refresh
from core.sheets import carregar_dados
from core.dashboard import (
    preparar_dataframe_produtos,
)

from core.helpers import (
    moeda,
    percentual_formatado,
)


def render_realtime_dashboard(portal):

    st.title("⚡ Dashboard Tempo Real")

    auto_refresh(60)

    df = carregar_dados(portal)

    produtos = preparar_dataframe_produtos(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Produtos",
        len(produtos)
    )

    col2.metric(
        "Venda Total",
        moeda(
            produtos["vendaTotal"].sum()
        )
    )

    col3.metric(
        "Margem Média",
        percentual_formatado(
            produtos["margem"].mean()
        )
    )

    col4.metric(
        "Estoque Total",
        int(
            produtos["estoqueTotal"].sum()
        )
    )

    st.success(
        "Sistema atualizado em tempo real."
    )