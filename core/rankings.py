# core/rankings.py

import pandas as pd

from core.sheets import carregar_dados
from core.columns import criar_mapa_colunas, valor_coluna
from core.helpers import texto, numero


def _nome_campo_portal(portal_nome, criterio):
    portal = str(portal_nome).strip().lower()

    mapa_portais = {
        "geral": "totalGeral",
        "amazon": "amazon",
        "casas bahia": "casasBahia",
        "casas bahia full": "casasBahiaFull",
        "martins bwg es": "martinsBwgEs",
        "magalu": "magalu",
        "mercado livre": "mercadoLivre",
        "mercos": "mercos",
        "shopee": "shopee",
        "shopee ud": "shopeeUd",
        "tik tok": "tikTok",
        "tiktok": "tikTok",
        "tray": "tray",
    }

    prefixo = mapa_portais.get(portal)

    if not prefixo:
        return None

    if criterio == "venda":
        return f"{prefixo}Venda"

    return f"{prefixo}Quantidade"


def buscar_ranking_top10_portal(
    portal_dre,
    portal_ranking="Geral",
    criterio="quantidade",
):
    df = carregar_dados(portal_dre, "setup_vendas")

    if df.empty:
        return pd.DataFrame()

    mapa = criar_mapa_colunas(df)

    campo_valor = _nome_campo_portal(
        portal_ranking,
        criterio,
    )

    if not campo_valor:
        return pd.DataFrame()

    dados = []

    for _, row in df.iterrows():
        sku = texto(valor_coluna(row, mapa, "sku"))
        ean = texto(valor_coluna(row, mapa, "ean"))
        marca = texto(valor_coluna(row, mapa, "marca"))
        descricao = texto(valor_coluna(row, mapa, "descricao"))

        valor_ranking = numero(
            valor_coluna(row, mapa, campo_valor)
        )

        venda = numero(
            valor_coluna(
                row,
                mapa,
                _nome_campo_portal(portal_ranking, "venda")
            )
        )

        quantidade = numero(
            valor_coluna(
                row,
                mapa,
                _nome_campo_portal(portal_ranking, "quantidade")
            )
        )

        if not sku and not descricao:
            continue

        if valor_ranking <= 0:
            continue

        dados.append({
            "sku": sku,
            "ean": ean,
            "marca": marca,
            "descricao": descricao,
            "portal": portal_ranking,
            "venda": venda,
            "quantidade": quantidade,
            "valorRanking": valor_ranking,
        })

    ranking = pd.DataFrame(dados)

    if ranking.empty:
        return ranking

    ranking = ranking.sort_values(
        by="valorRanking",
        ascending=False,
    ).head(10)

    ranking.insert(0, "posicao", range(1, len(ranking) + 1))

    return ranking