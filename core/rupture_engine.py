# core/rupture_engine.py

import pandas as pd


def calcular_risco_ruptura(df_produtos):

    dados = []

    for _, row in df_produtos.iterrows():

        estoque = row["estoqueTotal"]
        venda = row["vendaTotal"]

        if venda <= 0:
            dias = 999
        else:
            dias = estoque / venda

        # SCORE
        if dias <= 3:
            risco = "CRÍTICO"

        elif dias <= 7:
            risco = "ALTO"

        elif dias <= 15:
            risco = "MÉDIO"

        else:
            risco = "BAIXO"

        dados.append({
            "sku": row["sku"],
            "descricao": row["descricao"],
            "marca": row["marca"],
            "estoqueTotal": estoque,
            "vendaTotal": venda,
            "diasRestantes": round(dias, 2),
            "risco": risco,
        })

    df = pd.DataFrame(dados)

    ordem = {
        "CRÍTICO": 0,
        "ALTO": 1,
        "MÉDIO": 2,
        "BAIXO": 3,
    }

    df["ordem"] = df["risco"].map(ordem)

    return df.sort_values(
        by=["ordem", "diasRestantes"]
    )