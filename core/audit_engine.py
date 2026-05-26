# core/audit_engine.py

import pandas as pd
import os
from datetime import datetime


ARQUIVO_AUDITORIA = "auditoria.csv"


def registrar_log(
    usuario,
    acao,
    sku="",
    detalhes="",
):

    linha = {
        "data": datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        ),

        "usuario": usuario,
        "acao": acao,
        "sku": sku,
        "detalhes": detalhes,
    }

    df_novo = pd.DataFrame([linha])

    if os.path.exists(ARQUIVO_AUDITORIA):

        df = pd.read_csv(ARQUIVO_AUDITORIA)

        df = pd.concat(
            [df, df_novo],
            ignore_index=True,
        )

    else:
        df = df_novo

    df.to_csv(
        ARQUIVO_AUDITORIA,
        index=False,
    )


def carregar_logs():

    if not os.path.exists(ARQUIVO_AUDITORIA):
        return pd.DataFrame()

    return pd.read_csv(ARQUIVO_AUDITORIA)