# core/anomalies_engine.py

import pandas as pd


def detectar_anomalias(df):

    anomalias = []

    if df.empty:
        return pd.DataFrame()

    margem_media = df["margem"].mean()
    venda_media = df["vendaTotal"].mean()

    for _, row in df.iterrows():

        # margem extremamente baixa
        if row["margem"] < margem_media * 0.3:

            anomalias.append({
                "tipo": "Margem",
                "sku": row["sku"],
                "descricao": row["descricao"],
                "valor": row["margem"],
                "risco": "ALTO",
            })

        # venda extremamente alta
        if row["vendaTotal"] > venda_media * 4:

            anomalias.append({
                "tipo": "Venda",
                "sku": row["sku"],
                "descricao": row["descricao"],
                "valor": row["vendaTotal"],
                "risco": "MÉDIO",
            })

        # estoque exagerado
        if (
            row["estoqueTotal"] > 100
            and row["giro"] < 0.3
        ):

            anomalias.append({
                "tipo": "Estoque",
                "sku": row["sku"],
                "descricao": row["descricao"],
                "valor": row["estoqueTotal"],
                "risco": "ALTO",
            })

    return pd.DataFrame(anomalias)