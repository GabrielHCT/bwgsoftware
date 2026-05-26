# core/tags_engine.py

import pandas as pd


def gerar_tags(df_produtos):

    tags = []

    for _, row in df_produtos.iterrows():

        produto_tags = []

        # CAMPEÃO DE VENDA
        if row["vendaTotal"] >= 100:
            produto_tags.append("🔥 Campeão de Venda")

        # ESTOQUE PARADO
        if (
            row["estoqueTotal"] > 20
            and row["giro"] < 0.5
        ):
            produto_tags.append("📦 Estoque Parado")

        # ALTA MARGEM
        if row["margem"] >= 0.25:
            produto_tags.append("💰 Alta Margem")

        # ITEM PREMIUM
        if row["markup"] >= 2:
            produto_tags.append("⭐ Premium")

        # ITEM EXCLUSIVO
        if row["itemExclusivo"]:
            produto_tags.append("🏷️ Exclusivo")

        # FULL
        if row["estoqueFull"] > 0:
            produto_tags.append("🚚 FULL")

        tags.append({
            "sku": row["sku"],
            "descricao": row["descricao"],
            "marca": row["marca"],
            "tags": " | ".join(produto_tags)
        })

    return pd.DataFrame(tags)