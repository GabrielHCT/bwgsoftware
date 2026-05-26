# modules/auditoria.py

import streamlit as st

from core.audit_engine import carregar_logs


def render_auditoria():

    st.title("📜 Auditoria")

    logs = carregar_logs()

    if logs.empty:
        st.info("Nenhum log encontrado.")
        return

    st.metric(
        "Total Logs",
        len(logs)
    )

    st.divider()

    st.dataframe(
        logs,
        use_container_width=True,
        hide_index=True,
    )