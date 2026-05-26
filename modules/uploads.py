# modules/uploads.py

import streamlit as st

from core.upload_engine import (
    processar_excel_upload
)


def render_uploads():

    st.title("📤 Uploads")

    arquivo = st.file_uploader(
        "Upload Excel",
        type=["xlsx", "xls"],
    )

    if not arquivo:
        return

    resultado = processar_excel_upload(
        arquivo
    )

    if not resultado["sucesso"]:

        st.error(
            resultado["erro"]
        )

        return

    st.success(
        "Arquivo carregado."
    )

    st.dataframe(
        resultado["df"],
        use_container_width=True,
    )