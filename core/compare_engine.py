# core/compare_engine.py

import pandas as pd


def comparar_portais(dfs):

    resultados = []

    for portal, df in dfs.items():

        if df.empty:
            continue

        resultados.append({
            "portal": portal,

            "produtos": len(df),

            "estoqueTotal":
                df["estoqueTotal"].sum(),

            "vendaTotal":
                df["vendaTotal"].sum(),

            "margemMedia":
                df["margem"].mean(),

            "markupMedio":
                df["markup"].mean(),

            "lucroTotal":
                df["lucroEmpresa"].sum(),
        })

    return pd.DataFrame(resultados)