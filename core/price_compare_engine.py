# core/price_compare_engine.py

import pandas as pd

from core.sheets import carregar_dados
from core.dashboard import preparar_dataframe_produtos


def preparar_base_comparacao(portal):
    df = carregar_dados(portal)
    produtos = preparar_dataframe_produtos(df)

    if produtos.empty:
        return pd.DataFrame()

    return produtos[
        [
            "sku",
            "skuPortal",
            "descricao",
            "marca",
            "precoVista",
            "margem",
        ]
    ].copy()


def comparar_precos_portais(portal_1, portal_2):
    df1 = preparar_base_comparacao(portal_1)
    df2 = preparar_base_comparacao(portal_2)

    if df1.empty or df2.empty:
        return pd.DataFrame()

    comparativo = pd.merge(
        df1,
        df2,
        on="sku",
        how="inner",
        suffixes=(f"_{portal_1}", f"_{portal_2}")
    )

    if comparativo.empty:
        return comparativo

    comparativo["diferencaPreco"] = (
        comparativo[f"precoVista_{portal_1}"]
        - comparativo[f"precoVista_{portal_2}"]
    )

    comparativo["diferencaMargem"] = (
        comparativo[f"margem_{portal_1}"]
        - comparativo[f"margem_{portal_2}"]
    )

    comparativo["portalMaisBarato"] = comparativo.apply(
        lambda row: portal_1
        if row[f"precoVista_{portal_1}"] < row[f"precoVista_{portal_2}"]
        else portal_2,
        axis=1
    )

    comparativo["melhorMargem"] = comparativo.apply(
        lambda row: portal_1
        if row[f"margem_{portal_1}"] > row[f"margem_{portal_2}"]
        else portal_2,
        axis=1
    )

    return comparativo