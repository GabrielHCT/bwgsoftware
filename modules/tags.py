# modules/tags.py

import streamlit as st

from core.sheets import carregar_dados
from core.dashboard import preparar_dataframe_produtos
from core.tags_engine import gerar_tags


def render_tags(portal):

    st.title("🏷️ Tags Estratégicas")

    df = carregar_dados(portal)

    df_produtos = preparar_dataframe_produtos(df)

    tags = gerar_tags(df_produtos)

    st.metric(
        "Produtos classificados",
        len(tags)
    )

    st.divider()

    st.dataframe(
        tags,
        use_container_width=True,
        hide_index=True,
    )