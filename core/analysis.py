# core/analysis.py

from core.helpers import numero, safe_percent


def analisar_produto(produto):

    alertas = []
    insights = []
    oportunidades = []

    margem = safe_percent(produto["margem"])
    markup = numero(produto["markup"])
    estoque = numero(produto["estoqueTotal"])
    giro = numero(produto["giroEstoque"])

    # ESTOQUE
    if estoque <= 0:
        alertas.append(("erro", "Sem estoque"))

    if estoque > 20 and giro < 0.5:
        alertas.append(("alerta", "Produto parado"))
        insights.append("Estoque elevado com baixo giro.")

    if giro > 1:
        alertas.append(("sucesso", "Alto giro"))

    # MARGEM
    if margem < 0.10:
        alertas.append(("erro", "Margem baixa"))

    if margem > 0.20:
        oportunidades.append("Produto com margem saudável.")

    # MARKUP
    if markup > 1.8:
        oportunidades.append("Markup elevado.")

    if markup > 0 and markup < 1.2:
        insights.append("Markup muito baixo.")

    # OBSERVAÇÃO PREÇO
    obs = produto["observacaoPreco"]

    if obs == "Melhor Preço":
        oportunidades.append("Produto competitivo.")

    elif obs == "Preço Alto":
        insights.append("Preço acima da concorrência.")

    elif obs == "Preço Baixo":
        insights.append("Preço agressivo reduz margem.")

    return {
        "alertas": alertas,
        "insights": insights,
        "oportunidades": oportunidades,
    }