# modules/anomalies.py

import streamlit as st

from core.sheets import carregar_dados
from core.dashboard import (
    preparar_dataframe_produtos,
)

from core.anomalies_engine import (
    detectar_anomalias
)


def render_anomalies(portal):

    st.title("🧠 IA de Anomalias")

    df = carregar_dados(portal)

    produtos = preparar_dataframe_produtos(df)

    anomalias = detectar_anomalias(
        produtos
    )

    if anomalias.empty:

        st.success(
            "Nenhuma anomalia encontrada."
        )

        return

    st.metric(
        "Anomalias Detectadas",
        len(anomalias)
    )

    st.divider()

    st.dataframe(
        anomalias,
        use_container_width=True,
        hide_index=True,
    )