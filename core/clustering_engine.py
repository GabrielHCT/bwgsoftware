# core/clustering_engine.py

import pandas as pd


def classificar_curva_abc(df):

    if df.empty:
        return df

    base = df.copy()

    base = base.sort_values(
        by="vendaTotal",
        ascending=False,
    )

    total = base["vendaTotal"].sum()

    acumulado = 0

    classes = []

    for _, row in base.iterrows():

        percentual = (
            row["vendaTotal"] / total
            if total > 0 else 0
        )

        acumulado += percentual

        if acumulado <= 0.80:
            classe = "A"

        elif acumulado <= 0.95:
            classe = "B"

        else:
            classe = "C"

        classes.append(classe)

    base["curvaABC"] = classes

    return base