# app.py

import streamlit as st

from core.styles import aplicar_estilos
from components.sidebar import render_sidebar

from modules.home import render_home
from modules.pesquisa import render_pesquisa
from modules.executivo import render_executivo
from modules.ranking import render_ranking
from modules.top10 import render_top10
from modules.alertas import render_alertas
from modules.ruptura import render_ruptura
from modules.tags import render_tags
from modules.comercial import render_comercial
from core.auth import login
from core.theme import aplicar_tema
from modules.simulador import render_simulador
from modules.comparativo import render_comparativo
from modules.auditoria import render_auditoria
from modules.favoritos import render_favoritos
from modules.edicao_massa import (
    render_edicao_massa
)

from modules.forecast import (
    render_forecast
)

from modules.uploads import (
    render_uploads
)

from modules.automacoes import (
    render_automacoes
)

from modules.realtime_dashboard import (
    render_realtime_dashboard
)

from modules.anomalies import (
    render_anomalies
)

from modules.monitoramento import (
    render_monitoramento
)

from modules.comparar_precos import render_comparar_precos

from modules.ranking_dia_anterior import render_ranking_dia_anterior

st.set_page_config(
    page_title="Sistema Produtos - BWG SHOP",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    aplicar_estilos()

    if not login():
        st.stop()

    portal, modulo, dark_mode = render_sidebar()

    aplicar_tema(dark_mode)

    st.markdown(
        f"""
        <div class="main-subtitle">
            Portal/DRE selecionado: <b>{portal}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if modulo == "🏠 Início":
        render_home()

    elif modulo == "🔎 Pesquisa":
        render_pesquisa(portal)

    elif modulo == "📊 Executivo":
        render_executivo(portal)

    elif modulo == "🚨 Alertas":
        render_alertas(portal)

    elif modulo == "🏆 Ranking":
        render_ranking()

    elif modulo == "🔥 Top 10 Rankings":
        render_top10(portal)

    elif modulo == "🧮 Simulador":
        render_simulador()

    elif modulo == "📦 Ruptura":
        render_ruptura(portal)

    elif modulo == "💼 Comercial":
        render_comercial(portal)

    elif modulo == "🏷️ Tags":
        render_tags(portal)

    elif modulo == "📈 Comparativo":
        render_comparativo()

    elif modulo == "⭐ Favoritos":
        render_favoritos()

    elif modulo == "📜 Auditoria":
        render_auditoria()
        
    elif modulo == "🛠️ Edição Massa":
        render_edicao_massa(portal)
        
    elif modulo == "📈 Forecast":
        render_forecast(portal)

    elif modulo == "📤 Uploads":
        render_uploads()

    elif modulo == "🤖 Automações":
        render_automacoes()    

    elif modulo == "⚡ Tempo Real":
        render_realtime_dashboard(portal)

    elif modulo == "🧠 IA Anomalias":
        render_anomalies(portal)

    elif modulo == "📡 Monitoramento":
        render_monitoramento()

    elif modulo == "⚖️ Comparar Preços":
        render_comparar_precos()

    elif modulo == "📅 Ranking Dia Anterior":
        render_ranking_dia_anterior()


if __name__ == "__main__":
    main()