# components/sidebar.py

import streamlit as st

from core.config import (
    APP_NAME,
    EMPRESA,
    PORTAIS,
    PORTAL_PADRAO,
)

from core.auth import logout
from core.cache_manager import limpar_todos_caches

from components.dark_mode import toggle_dark_mode


def render_sidebar():

    with st.sidebar:

        st.markdown(
            f"""
            # {APP_NAME}

            {EMPRESA}
            """
        )

        st.divider()

        dark_mode = toggle_dark_mode()

        st.divider()

        st.success(
            f"👤 {st.session_state.get('usuario','')}"
        )

        st.caption(
            f"Perfil: {st.session_state.get('perfil','')}"
        )

        st.divider()

        portal = st.selectbox(
            "Portal / DRE",
            options=list(PORTAIS.keys()),
            index=list(PORTAIS.keys()).index(PORTAL_PADRAO),
        )

        st.divider()

        modulo = st.radio(
            "Menu",
            [
                "🏠 Início",
                "🔎 Pesquisa",
                "📊 Executivo",
                "🚨 Alertas",
                "🏆 Ranking",
                "🔥 Top 10 Rankings",
                "🧮 Simulador",
                "📦 Ruptura",
                "💼 Comercial",
                "🏷️ Tags",
                "📈 Comparativo",
                "⭐ Favoritos",
                "📜 Auditoria"
                "🛠️ Edição Massa",
                "📈 Forecast",
                "📤 Uploads",
                "🤖 Automações",
                "⚡ Tempo Real",
                "🧠 IA Anomalias",
                "📡 Monitoramento",
                "⚖️ Comparar Preços",
                "📅 Ranking Dia Anterior"
            ]
        )

        st.divider()

        if st.button(
            "🔄 Atualizar Dados",
            use_container_width=True
        ):

            limpar_todos_caches()

            st.success("Caches atualizados.")

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):
            logout()

    return portal, modulo, dark_mode