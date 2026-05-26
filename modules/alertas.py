# modules/alertas.py

import streamlit as st

from core.sheets import carregar_dados
from core.dashboard import preparar_dataframe_produtos
from core.alerts_engine import gerar_alertas_globais


def render_alertas(portal):

    st.title("🚨 Alertas Inteligentes")

    df = carregar_dados(portal)

    df_produtos = preparar_dataframe_produtos(df)

    alertas = gerar_alertas_globais(df_produtos)

    if alertas.empty:
        st.success("Nenhum alerta encontrado.")
        return

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Alertas",
        len(alertas)
    )

    col2.metric(
        "Críticos",
        len(alertas[alertas["prioridade"] >= 9])
    )

    col3.metric(
        "Médios",
        len(
            alertas[
                (alertas["prioridade"] >= 6)
                & (alertas["prioridade"] < 9)
            ]
        )
    )

    st.divider()

    for _, alerta in alertas.iterrows():

        texto = (
            f"**{alerta['categoria']}** — "
            f"{alerta['descricao']} "
            f"({alerta['sku']})\n\n"
            f"{alerta['mensagem']}"
        )

        if alerta["tipo"] == "erro":
            st.error(texto)

        else:
            st.warning(texto)