# core/observability.py

import os
from datetime import datetime


ARQUIVO_LOG = "system.log"


def registrar_evento(
    nivel,
    evento,
):

    linha = (
        f"[{datetime.now()}] "
        f"[{nivel}] "
        f"{evento}\n"
    )

    with open(
        ARQUIVO_LOG,
        "a",
        encoding="utf-8",
    ) as f:

        f.write(linha)


def carregar_logs():

    if not os.path.exists(ARQUIVO_LOG):
        return []

    with open(
        ARQUIVO_LOG,
        "r",
        encoding="utf-8",
    ) as f:

        return f.readlines()