# modules/forecast.py

import streamlit as st
import plotly.express as px

from core.sheets import carregar_dados
from core.dashboard import preparar_dataframe_produtos
from core.forecast_engine import gerar_forecast


def render_forecast(portal):

    st.title("📈 Forecast Operacional")

    df = carregar_dados(portal)

    produtos = preparar_dataframe_produtos(df)

    forecast = gerar_forecast(produtos)

    if forecast.empty:
        st.warning("Sem dados.")
        return

    st.dataframe(
        forecast,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    fig = px.bar(
        forecast.head(20),
        x="descricao",
        y="forecast30d",
        title="Forecast 30 dias",
        text_auto=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )