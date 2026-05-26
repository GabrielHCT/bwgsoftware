# core/ranking_day_engine.py

import pandas as pd

from core.sheets import carregar_dados
from core.columns import criar_mapa_colunas, valor_coluna
from core.helpers import texto, numero


def top10_vendidos_dia_anterior(portal, criterio="quantidade"):
    """
    Busca o Top 10 vendidos no dia anterior usando a aba
    Setup Vendas Portal do portal selecionado.
    """

    df = carregar_dados(
        portal,
        "setup_vendas_portal",
    )

    if df.empty:
        return pd.DataFrame()

    mapa = criar_mapa_colunas(df)

    dados = []

    for _, row in df.iterrows():
        sku = texto(
            valor_coluna(row, mapa, "sku")
        )

        ean = texto(
            valor_coluna(row, mapa, "ean")
        )

        marca = texto(
            valor_coluna(row, mapa, "marca")
        )

        descricao = texto(
            valor_coluna(row, mapa, "descricao")
        )

        qtd = numero(
            valor_coluna(
                row,
                mapa,
                "vendaDiaAnteriorQuantidade",
            )
        )

        valor = numero(
            valor_coluna(
                row,
                mapa,
                "vendaDiaAnteriorValor",
            )
        )

        if not sku and not descricao:
            continue

        if qtd <= 0 and valor <= 0:
            continue

        dados.append(
            {
                "sku": sku,
                "ean": ean,
                "marca": marca,
                "descricao": descricao,
                "quantidadeDiaAnterior": qtd,
                "valorDiaAnterior": valor,
            }
        )

    ranking = pd.DataFrame(dados)

    if ranking.empty:
        return ranking

    coluna_ordem = (
        "valorDiaAnterior"
        if criterio == "valor"
        else "quantidadeDiaAnterior"
    )

    ranking = ranking.sort_values(
        by=coluna_ordem,
        ascending=False,
    ).head(10)

    ranking.insert(
        0,
        "posicao",
        range(1, len(ranking) + 1),
    )

    return ranking