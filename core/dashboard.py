# core/dashboard.py

import pandas as pd

from core.helpers import numero, safe_percent, texto
from core.columns import criar_mapa_colunas, valor_coluna


def preparar_dataframe_produtos(df):
    if df.empty:
        return pd.DataFrame()

    mapa = criar_mapa_colunas(df)

    dados = []

    for _, row in df.iterrows():
        estoque_total = numero(valor_coluna(row, mapa, "estoqueTotal"))
        venda_total = numero(valor_coluna(row, mapa, "vendaTotal"))
        venda_portal = numero(valor_coluna(row, mapa, "vendaPortal"))
        margem = safe_percent(valor_coluna(row, mapa, "margem"))
        markup = numero(valor_coluna(row, mapa, "markup"))
        preco = numero(valor_coluna(row, mapa, "precoVista"))
        custo = numero(valor_coluna(row, mapa, "custo"))
        lucro = numero(valor_coluna(row, mapa, "lucroEmpresa"))

        giro = venda_total / estoque_total if estoque_total > 0 else 0
        eficiencia = venda_portal / venda_total if venda_total > 0 else 0

        dados.append({
            "linha": row["_linha_real"],
            "sku": texto(valor_coluna(row, mapa, "sku")),
            "skuPortal": texto(valor_coluna(row, mapa, "skuPortal")),
            "marca": texto(valor_coluna(row, mapa, "marca")),
            "descricao": texto(valor_coluna(row, mapa, "descricao")),
            "ean": texto(valor_coluna(row, mapa, "ean")),
            "categoria": texto(valor_coluna(row, mapa, "categoria")),

            "estoqueTotal": estoque_total,
            "estoqueFull": numero(valor_coluna(row, mapa, "estoqueFull")),
            "vendaTotal": venda_total,
            "vendaPortal": venda_portal,

            "margem": margem,
            "markup": markup,
            "precoVista": preco,
            "custo": custo,
            "lucroEmpresa": lucro,

            "giro": giro,
            "eficienciaPortal": eficiencia,

            "abcGeral": texto(valor_coluna(row, mapa, "abcGeral")),
            "abcPortal": texto(valor_coluna(row, mapa, "abcPortal")),

            "observacaoPreco": texto(valor_coluna(row, mapa, "observacaoPreco")),
            "observacaoFrete": texto(valor_coluna(row, mapa, "observacaoFrete")),
            "exposicao": texto(valor_coluna(row, mapa, "exposicao")),
            "itemExclusivo": texto(valor_coluna(row, mapa, "itemExclusivo")),
        })

    return pd.DataFrame(dados)


def indicadores_executivos(df_produtos):
    if df_produtos.empty:
        return {
            "totalProdutos": 0,
            "estoqueTotal": 0,
            "vendaTotal": 0,
            "margemMedia": 0,
            "markupMedio": 0,
            "lucroTotal": 0,
            "produtosSemEstoque": 0,
            "produtosMargemBaixa": 0,
            "produtosParados": 0,
        }

    return {
        "totalProdutos": len(df_produtos),
        "estoqueTotal": df_produtos["estoqueTotal"].sum(),
        "vendaTotal": df_produtos["vendaTotal"].sum(),
        "margemMedia": df_produtos["margem"].mean(),
        "markupMedio": df_produtos["markup"].mean(),
        "lucroTotal": df_produtos["lucroEmpresa"].sum(),
        "produtosSemEstoque": len(
            df_produtos[df_produtos["estoqueTotal"] <= 0]
        ),
        "produtosMargemBaixa": len(
            df_produtos[df_produtos["margem"] < 0.10]
        ),
        "produtosParados": len(
            df_produtos[
                (df_produtos["estoqueTotal"] > 20)
                & (df_produtos["giro"] < 0.5)
            ]
        ),
    }


def produtos_criticos(df_produtos):
    if df_produtos.empty:
        return pd.DataFrame()

    criticos = df_produtos[
        (df_produtos["estoqueTotal"] <= 0)
        | (df_produtos["margem"] < 0.10)
        | (
            (df_produtos["estoqueTotal"] > 20)
            & (df_produtos["giro"] < 0.5)
        )
    ].copy()

    if criticos.empty:
        return criticos

    return criticos.sort_values(
        by=["margem", "giro"],
        ascending=[True, True],
    )