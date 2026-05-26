# core/ai_engine.py


def gerar_recomendacoes(produto):

    recomendacoes = []

    margem = produto["margem"]
    markup = produto["markup"]
    giro = produto["giroEstoque"]
    estoque = produto["estoqueTotal"]

    # MARGEM
    if margem < 0.10:

        recomendacoes.append({
            "tipo": "erro",
            "titulo": "Margem muito baixa",
            "texto": (
                "Recomenda-se reajuste de preço "
                "ou renegociação de custo."
            )
        })

    elif margem > 0.25:

        recomendacoes.append({
            "tipo": "sucesso",
            "titulo": "Margem saudável",
            "texto": (
                "Produto possui margem operacional forte."
            )
        })

    # GIRO
    if estoque > 20 and giro < 0.5:

        recomendacoes.append({
            "tipo": "alerta",
            "titulo": "Produto parado",
            "texto": (
                "Criar campanha ou reduzir preço."
            )
        })

    if giro > 1:

        recomendacoes.append({
            "tipo": "sucesso",
            "titulo": "Alto giro",
            "texto": (
                "Produto com ótima performance."
            )
        })

    # MARKUP
    if markup < 1.2:

        recomendacoes.append({
            "tipo": "erro",
            "titulo": "Markup baixo",
            "texto": (
                "Produto pode operar com risco."
            )
        })

    elif markup >= 2:

        recomendacoes.append({
            "tipo": "sucesso",
            "titulo": "Markup premium",
            "texto": (
                "Produto com excelente retorno."
            )
        })

    return recomendacoes