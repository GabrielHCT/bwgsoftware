# core/columns.py

import unicodedata
import re


COLUMN_ALIASES = {
    "sku": [
        "SKU SELLER",
        "SKU Seller",
        "SKU",
        "CÓD. INTERNO",
        "COD INTERNO",
        "CODIGO INTERNO",
        "CÓDIGO INTERNO",
    ],

    "skuPortal": [
        "SKU PORTAL",
        "SKU Portal",
        "SKU MARKETPLACE",
        "SKU CANAL",
    ],

    "marca": [
        "MARCA",
        "Marca",
        "Brand",
    ],

    "descricao": [
        "DESCRIÇÃO",
        "DESCRICAO",
        "Descrição",
        "Descricao",
        "PRODUTO",
        "Produto",
        "NOME PRODUTO",
        "Nome Produto",
        "TÍTULO",
        "TITULO",
    ],

    "ean": [
        "EAN",
        "CÓDIGO DE BARRAS",
        "CODIGO DE BARRAS",
    ],

    "idPortal": [
        "ID",
        "ID MAGALU",
    ],

    "linkAnuncio": [
        "LINK ANÚNCIO",
        "LINK ANUNCIO",
        "URL ANÚNCIO",
        "URL ANUNCIO",
        "LINK",
    ],

    "imagem": [
        "IMAGEM",
        "FOTO",
        "URL IMAGEM",
        "IMAGE",
    ],

    "categoria": [
        "CATEGORIA",
        "Categoria",
        "Category",
    ],

    "estoqueCentral": [
        "ESTOQUE CENTRAL",
    ],

    "estoqueFull": [
        "ESTOQUE FULL",
        "FULL",
        "ESTOQUE FULL ",
    ],

    "estoqueSudeste": [
        "ESTOQUE SUDESTE",
    ],

    "estoqueNordeste": [
        "ESTOQUE NORDESTE",
    ],

    "estoqueTotal": [
        "ESTOQUE TOTAL",
        "ESTOQUE",
        "QTD ESTOQUE",
    ],

    "projecaoEstoque": [
        "PROJEÇÃO EST. PRÓX. MÊS",
        "PROJECAO EST PROX MES",
        "PROJEÇÃO ESTOQUE",
        "PROJECAO ESTOQUE",
    ],

    "projecaoVenda": [
        "PROJEÇÃO VENDA MÊS",
        "PROJECAO VENDA MES",
        "PROJEÇÃO MÊS",
        "PROJECAO MES",
    ],

    "vendaTotal": [
        "VENDA TOTAL",
        "VENDAS TOTAL",
        "GERAL VENDAS",
        "TOTAL GERAL QUANTIDADE",
        "QTD VENDIDA",
        "QUANTIDADE VENDIDA",
    ],

    "vendaPortal": [
        "VENDA PORTAL",
        "VENDA MARKETPLACE",
        "VENDA CANAL",
    ],

    "vendaOoh": [
        "VENDA OoH",
        "VENDA OOH",
    ],

    "vendaMom": [
        "VENDA MoM",
        "VENDA MOM",
    ],

    "vendaYoy": [
        "VENDA YoY",
        "VENDA YOY",
    ],

    "vendaTriPortal": [
        "VENDA TRI - PORTAL",
        "VENDA TRI PORTAL",
    ],

    "vendaTriGeral": [
        "VENDA TRI - GERAL",
        "VENDA TRI GERAL",
    ],

    "precoCheio": [
        "PREÇO CHEIO",
        "PRECO CHEIO",
    ],

    "precoPadrao": [
        "PREÇO PADRÃO",
        "PRECO PADRAO",
    ],

    "precoAcao": [
        "PREÇO AÇÃO",
        "PRECO ACAO",
    ],

    "precoVista": [
        "PREÇO À VISTA",
        "PREÇO A VISTA",
        "PRECO A VISTA",
        "PREÇO VISTA",
        "PRECO VISTA",
        "PV",
    ],

    "precoPrazo": [
        "PREÇO À PRAZO",
        "PREÇO A PRAZO",
        "PRECO A PRAZO",
        "PREÇO PRAZO",
        "PRECO PRAZO",
    ],

    "acrescimoFt": [
        "ACRESC. FT",
        "ACRESC FT",
    ],

    "cupom": [
        "CUPOM",
    ],

    "custo": [
        "CUSTO",
        "CUSTO UN",
        "CUSTO PRODUTO",
        "CUSTO BWG",
    ],

    "bSeller": [
        "B | SELLER",
        "B SELLER",
        "B_SELLER",
        "BONUS SELLER",
    ],

    "bPortal": [
        "B | PORTAL",
        "B PORTAL",
        "B_PORTAL",
        "BONUS PORTAL",
    ],

    "comissao": [
        "COMISSÃO",
        "COMISSAO",
        "COMISSÃO %",
        "COMISSAO %",
    ],

    "lucroEmpresa": [
        "LUCRO DA EMPRESA",
        "LUCRO EMPRESA",
        "LUCRO",
        "LUCRO R$",
    ],

    "margem": [
        "MARGEM%",
        "MARGEM",
        "MARGEM %",
        "% MARGEM",
    ],

    "comissaoRs": [
        "COMISSÃO R$",
        "COMISSAO R$",
    ],

    "markup": [
        "MARKUP",
        "MARK UP",
    ],

    "abcTriGeral": [
        "ABC TRI - GERAL",
        "ABC TRI GERAL",
        "ABC TRIMESTRE GERAL",
    ],

    "abcTriPortal": [
        "ABC TRI - PORTAL",
        "ABC TRI PORTAL",
        "ABC TRIMESTRE PORTAL",
    ],

    "abcPortal": [
        "ABC PORTAL",
    ],

    "abcGeral": [
        "ABC GERAL",
    ],

    "giroProdutoPortal": [
        "GIRO PRODUTO PORTAL",
    ],

    "giroProdutoFull": [
        "GIRO PRODUTO FULL",
    ],

    "giroMarca": [
        "GIRO MARCA",
    ],

    "markupMarca": [
        "MARKUP MARCA",
    ],

    "observacaoAnuncio": [
        "OBSERVÇÃO ANÚNCIO",
        "OBSERVAÇÃO ANÚNCIO",
        "OBSERVACAO ANUNCIO",
        "OBS ANÚNCIO",
        "OBS ANUNCIO",
    ],

    "observacaoPreco": [
        "OBSERVAÇÃO PREÇO",
        "OBSERVACAO PRECO",
        "OBS PREÇO",
        "OBS PRECO",
    ],

    "observacaoFrete": [
        "OBSERVAÇÃO FRETE",
        "OBSERVACAO FRETE",
        "OBS FRETE",
    ],

    "exposicao": [
        "EXPOSIÇÃO",
        "EXPOSICAO",
    ],

    "itemExclusivo": [
        "ITEM EXCLUSIVO",
        "EXCLUSIVO",
    ],

    "agressivar": [
        "AGRESSIVAR",
    ],

    "concorrentes": [
        "CONCORRENTES",
    ],

    "pvRelampago": [
        "PV RELÂMPAGO/AÇÃO",
        "PV RELAMPAGO/ACAO",
    ],

    "relampago": [
        "RELÂMPAGO?",
        "RELAMPAGO?",
    ],

    "payday": [
        "PAYDAY",
    ],

    "pma": [
        "PMA",
    ],

    "campanhaDisponivel": [
        "CAMPANHA DISPONÍVEL",
        "CAMPANHA DISPONIVEL",
    ],

    "perfilProduto": [
        "PERFIL DO PRODUTO",
    ],

    "ajustePreco": [
        "AJUSTE DE PREÇO",
        "AJUSTE DE PRECO",
    ],

    "arredondandoPv": [
        "ARREDONDANDO PV",
    ],

    "vendaDiaAnteriorQuantidade": [
        "MAGALU QUANTIDADE",
        "MAGALU VENDAS QUANTIDADE",
        "VENDAS DIA ANTERIOR QUANTIDADE",
        "VENDA DIA ANTERIOR QUANTIDADE",
        "DIA ANTERIOR QUANTIDADE",
        "ONTEM QUANTIDADE",
        "QUANTIDADE DIA ANTERIOR",
    ],

    "vendaDiaAnteriorValor": [
        "MAGALU VENDA",
        "MAGALU VENDAS R$",
        "MAGALU VENDAS VALOR",
        "VENDAS DIA ANTERIOR R$",
        "VENDA DIA ANTERIOR R$",
        "DIA ANTERIOR R$",
        "ONTEM R$",
        "VALOR DIA ANTERIOR",
    ],
}


def normalizar_nome_coluna(nome):
    nome = str(nome or "").strip().lower()
    nome = re.sub(r"__\d+$", "", nome)

    nome = unicodedata.normalize("NFD", nome)

    nome = "".join(
        c for c in nome
        if unicodedata.category(c) != "Mn"
    )

    nome = re.sub(r"[^a-z0-9]+", "", nome)

    return nome


def criar_mapa_colunas(df):
    mapa = {}

    colunas_normalizadas = {
        normalizar_nome_coluna(col): col
        for col in df.columns
    }

    for campo_padrao, aliases in COLUMN_ALIASES.items():
        for alias in aliases:
            alias_norm = normalizar_nome_coluna(alias)

            if alias_norm in colunas_normalizadas:
                mapa[campo_padrao] = colunas_normalizadas[alias_norm]
                break

    return mapa


def get_coluna(df, campo_padrao):
    mapa = criar_mapa_colunas(df)
    return mapa.get(campo_padrao)


def valor_coluna(row, mapa_colunas, campo_padrao, padrao=""):
    coluna = mapa_colunas.get(campo_padrao)

    if not coluna:
        return padrao

    try:
        return row[coluna]
    except Exception:
        return padrao


def validar_colunas_obrigatorias(df, obrigatorias):
    mapa = criar_mapa_colunas(df)

    faltando = [
        campo for campo in obrigatorias
        if campo not in mapa
    ]

    return faltando, mapa