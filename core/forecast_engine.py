# core/forecast_engine.py

import pandas as pd


def gerar_forecast(df_produtos):

    previsoes = []

    for _, row in df_produtos.iterrows():

        venda = row["vendaTotal"]
        estoque = row["estoqueTotal"]

        # previsão simples
        previsao_30d = venda * 1.15

        # risco
        if venda > 0:
            cobertura = estoque / venda
        else:
            cobertura = 999

        if cobertura <= 5:
            risco = "ALTO"

        elif cobertura <= 15:
            risco = "MÉDIO"

        else:
            risco = "BAIXO"

        previsoes.append({

            "sku": row["sku"],
            "descricao": row["descricao"],

            "vendaAtual": venda,

            "forecast30d":
                round(previsao_30d, 2),

            "estoque":
                estoque,

            "risco":
                risco,
        })

    return pd.DataFrame(previsoes)