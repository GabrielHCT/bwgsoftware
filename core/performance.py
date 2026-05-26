# core/performance.py

import pandas as pd


def paginar_dataframe(
    df,
    pagina=1,
    por_pagina=50,
):

    inicio = (pagina - 1) * por_pagina
    fim = inicio + por_pagina

    return df.iloc[inicio:fim]


def busca_ultra_rapida(
    df,
    termo,
):

    if not termo:
        return df

    termo = termo.lower()

    filtro = (
        df["descricao"]
        .str.lower()
        .str.contains(termo, na=False)
    )

    return df[filtro]