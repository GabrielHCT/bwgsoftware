# modules/monitoramento.py

import streamlit as st

from core.observability import (
    carregar_logs
)


def render_monitoramento():

    st.title("📡 Monitoramento")

    logs = carregar_logs()

    if not logs:

        st.info(
            "Nenhum log encontrado."
        )

        return

    st.metric(
        "Eventos",
        len(logs)
    )

    st.divider()

    st.code(
        "".join(logs[-200:]),
        language="log",
    )