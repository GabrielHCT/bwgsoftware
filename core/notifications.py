# core/notifications.py

import requests


def enviar_discord(
    webhook,
    mensagem,
):

    payload = {
        "content": mensagem
    }

    requests.post(
        webhook,
        json=payload,
        timeout=10,
    )


def enviar_telegram(
    token,
    chat_id,
    mensagem,
):

    url = (
        f"https://api.telegram.org/"
        f"bot{token}/sendMessage"
    )

    payload = {
        "chat_id": chat_id,
        "text": mensagem,
    }

    requests.post(
        url,
        json=payload,
        timeout=10,
    )