# modules/comercial.py

import streamlit as st

from core.sheets import carregar_dados
from core.dashboard import preparar_dataframe_produtos
from core.comercial_engine import preparar_visao_comercial


def render_comercial(portal):

    st.title("💼 Modo Comercial")

    st.info(
        "Visualização sem dados financeiros sensíveis."
    )

    df = carregar_dados(portal)

    df_produtos = preparar_dataframe_produtos(df)

    comercial = preparar_visao_comercial(df_produtos)

    st.dataframe(
        comercial,
        use_container_width=True,
        hide_index=True,
    )