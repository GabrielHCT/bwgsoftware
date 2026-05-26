# core/alerts_engine.py

import pandas as pd


def gerar_alertas_globais(df_produtos):

    alertas = []

    for _, row in df_produtos.iterrows():

        # SEM ESTOQUE
        if row["estoqueTotal"] <= 0:
            alertas.append({
                "tipo": "erro",
                "categoria": "Ruptura",
                "sku": row["sku"],
                "descricao": row["descricao"],
                "mensagem": "Produto sem estoque",
                "prioridade": 10,
            })

        # MARGEM BAIXA
        if row["margem"] < 0.10:
            alertas.append({
                "tipo": "erro",
                "categoria": "Margem",
                "sku": row["sku"],
                "descricao": row["descricao"],
                "mensagem": "Margem abaixo de 10%",
                "prioridade": 9,
            })

        # PRODUTO PARADO
        if (
            row["estoqueTotal"] > 20
            and row["giro"] < 0.5
        ):
            alertas.append({
                "tipo": "alerta",
                "categoria": "Giro",
                "sku": row["sku"],
                "descricao": row["descricao"],
                "mensagem": "Produto parado",
                "prioridade": 8,
            })

        # MARKUP MUITO BAIXO
        if (
            row["markup"] > 0
            and row["markup"] < 1.2
        ):
            alertas.append({
                "tipo": "alerta",
                "categoria": "Markup",
                "sku": row["sku"],
                "descricao": row["descricao"],
                "mensagem": "Markup muito baixo",
                "prioridade": 7,
            })

        # FRETE ALTO
        if row["observacaoFrete"] == "Frete Alto":
            alertas.append({
                "tipo": "alerta",
                "categoria": "Frete",
                "sku": row["sku"],
                "descricao": row["descricao"],
                "mensagem": "Frete alto",
                "prioridade": 6,
            })

    if not alertas:
        return pd.DataFrame()

    df_alertas = pd.DataFrame(alertas)

    return df_alertas.sort_values(
        by="prioridade",
        ascending=False,
    )