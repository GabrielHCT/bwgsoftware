# modules/automacoes.py

import streamlit as st

from core.notifications import (
    enviar_discord,
    enviar_telegram,
)


def render_automacoes():

    st.title("🤖 Automações")

    st.subheader("Discord")

    webhook = st.text_input(
        "Webhook Discord"
    )

    mensagem = st.text_area(
        "Mensagem Discord",
        value="Teste do sistema.",
    )

    if st.button("Enviar Discord"):

        enviar_discord(
            webhook,
            mensagem,
        )

        st.success("Mensagem enviada.")

    st.divider()

    st.subheader("Telegram")

    token = st.text_input(
        "Token Telegram"
    )

    chat_id = st.text_input(
        "Chat ID"
    )

    mensagem_tg = st.text_area(
        "Mensagem Telegram",
        value="Teste Telegram",
    )

    if st.button("Enviar Telegram"):

        enviar_telegram(
            token,
            chat_id,
            mensagem_tg,
        )

        st.success("Mensagem enviada.")