# core/config.py

APP_NAME = "Sistema Produtos"
EMPRESA = "BWG SHOP"

MODO_LOCAL = True

ARQUIVO_LOCAL_MAGALU = "data/dre_magalu.xlsx"

GOOGLE_CREDENTIALS_PATH = "credentials/google_credentials.json"

PORTAIS = {
    "Magalu": {
        "spreadsheet": "DRE MAGALU",
        "abas": {
            "dre": "DRE - Magalu",
            "setup_produtos": "Setup Produtos",
            "setup_vendas": "Setup Vendas",
            "setup_vendas_portal": "Setup Vendas Portal",
            "setup_produtos_portal": "Setup Produtos Portal",
        },
    },

    # Quando for adicionar outro portal, copie este modelo:
    #
    # "Casas Bahia": {
    #     "spreadsheet": "NOME EXATO DA PLANILHA",
    #     "abas": {
    #         "dre": "DRE - Casas Bahia",
    #         "setup_produtos": "Setup Produtos",
    #         "setup_vendas": "Setup Vendas",
    #         "setup_vendas_portal": "Setup Vendas Portal",
    #         "setup_produtos_portal": "Setup Produtos Portal",
    #     },
    # },
}

PORTAL_PADRAO = "Magalu"

ABAS_CONFIG = {
    "dre": {
        "header_rows": 1,
    },

    "setup_produtos": {
        "header_rows": 1,
    },

    "setup_vendas": {
        "header_rows": 2,
    },

    "setup_vendas_portal": {
        "header_rows": 2,
    },

    "setup_produtos_portal": {
        "header_rows": 2,
    },
}

TIPOS_ABAS = {
    "dre": "DRE",
    "setup_produtos": "Setup Produtos",
    "setup_vendas": "Setup Vendas",
    "setup_vendas_portal": "Setup Vendas Portal",
    "setup_produtos_portal": "Setup Produtos Portal",
}

OPCOES = {
    "observacaoAnuncio": [
        "",
        "Inativo",
        "Anúncio Não Reflete no Front",
        "Bloqueado",
        "Problema FULL",
        "Sem Campanha",
    ],

    "observacaoPreco": [
        "",
        "Preço Alto",
        "Preço Baixo",
        "Competitivo",
        "Melhor Preço",
    ],

    "observacaoFrete": [
        "",
        "Frete Grátis",
        "Frete Alto",
        "Frete Não Cota",
    ],

    "exposicao": [
        "",
        "Baixa Exposição",
        "Sem Exposição",
    ],

    "itemExclusivo": [
        "",
        "Item Exclusivo",
    ],
}

RANKING_PORTAIS = [
    "Amazon",
    "Casas Bahia",
    "Casas Bahia FULL",
    "Martins BWG ES",
    "Magalu",
    "Mercado Livre",
    "Mercos",
    "Shopee",
    "Shopee UD",
    "Tik Tok",
    "Tray",
]

RANKING_DIA_ANTERIOR = {
    "aba": "setup_vendas_portal",

    "criterios": {
        "quantidade": "vendaDiaAnteriorQuantidade",
        "valor": "vendaDiaAnteriorValor",
    },
}

CONFIG_APP = {
    "cache_ttl": 300,
    "limite_resultados_pesquisa": 30,
    "limite_ranking": 10,
    "usar_colunas_por_titulo": True,
    "permitir_cabecalho_composto": True,
}