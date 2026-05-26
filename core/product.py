# core/product.py

from core.helpers import texto, numero, safe_percent
from core.columns import criar_mapa_colunas, valor_coluna
from core.calculations import (
    calcular_giro,
    calcular_cobertura,
    calcular_eficiencia_portal,
    calcular_score,
)
from core.analysis import analisar_produto


def montar_produto(row, df=None):
    if df is None:
        raise ValueError("É necessário passar o DataFrame para mapear as colunas.")

    mapa = criar_mapa_colunas(df)

    produto = {
        "linha": int(row["_linha_real"]),

        "skuSeller": texto(valor_coluna(row, mapa, "sku")),
        "skuPortal": texto(valor_coluna(row, mapa, "skuPortal")),
        "marca": texto(valor_coluna(row, mapa, "marca")),
        "descricao": texto(valor_coluna(row, mapa, "descricao")),
        "ean": texto(valor_coluna(row, mapa, "ean")),
        "categoria": texto(valor_coluna(row, mapa, "categoria")),

        "imagem": texto(valor_coluna(row, mapa, "imagem")),
        "linkAnuncio": texto(valor_coluna(row, mapa, "linkAnuncio")),

        "estoqueCentral": numero(valor_coluna(row, mapa, "estoqueCentral")),
        "estoqueFull": numero(valor_coluna(row, mapa, "estoqueFull")),
        "estoqueSudeste": numero(valor_coluna(row, mapa, "estoqueSudeste")),
        "estoqueNordeste": numero(valor_coluna(row, mapa, "estoqueNordeste")),
        "estoqueTotal": numero(valor_coluna(row, mapa, "estoqueTotal")),

        "vendaTotal": numero(valor_coluna(row, mapa, "vendaTotal")),
        "vendaPortal": numero(valor_coluna(row, mapa, "vendaPortal")),

        "precoVista": numero(valor_coluna(row, mapa, "precoVista")),
        "precoPrazo": numero(valor_coluna(row, mapa, "precoPrazo")),
        "custo": numero(valor_coluna(row, mapa, "custo")),

        "margem": safe_percent(valor_coluna(row, mapa, "margem")),
        "markup": numero(valor_coluna(row, mapa, "markup")),

        "comissao": safe_percent(valor_coluna(row, mapa, "comissao")),
        "bSeller": safe_percent(valor_coluna(row, mapa, "bSeller")),
        "bPortal": safe_percent(valor_coluna(row, mapa, "bPortal")),

        "abcPortal": texto(valor_coluna(row, mapa, "abcPortal")),
        "abcGeral": texto(valor_coluna(row, mapa, "abcGeral")),
        "abcTriPortal": texto(valor_coluna(row, mapa, "abcTriPortal")),
        "abcTriGeral": texto(valor_coluna(row, mapa, "abcTriGeral")),

        "observacaoAnuncio": texto(valor_coluna(row, mapa, "observacaoAnuncio")),
        "observacaoPreco": texto(valor_coluna(row, mapa, "observacaoPreco")),
        "observacaoFrete": texto(valor_coluna(row, mapa, "observacaoFrete")),
        "exposicao": texto(valor_coluna(row, mapa, "exposicao")),
        "itemExclusivo": texto(valor_coluna(row, mapa, "itemExclusivo")),
    }

    produto["giroEstoque"] = calcular_giro(
        produto["vendaTotal"],
        produto["estoqueTotal"]
    )

    produto["coberturaEstoque"] = calcular_cobertura(
        produto["estoqueTotal"],
        produto["vendaTotal"]
    )

    produto["eficienciaPortal"] = calcular_eficiencia_portal(
        produto["vendaPortal"],
        produto["vendaTotal"]
    )

    produto["score"] = calcular_score(produto)
    produto["analise"] = analisar_produto(produto)

    return produto