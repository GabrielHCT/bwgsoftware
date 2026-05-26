# core/calculations.py

from core.helpers import numero, safe_percent


def calcular_giro(venda, estoque):
    venda = numero(venda)
    estoque = numero(estoque)

    if estoque <= 0:
        return 0

    return venda / estoque


def calcular_cobertura(estoque, venda):
    estoque = numero(estoque)
    venda = numero(venda)

    if venda <= 0:
        return estoque

    return estoque / venda


def calcular_eficiencia_portal(venda_portal, venda_total):
    venda_portal = numero(venda_portal)
    venda_total = numero(venda_total)

    if venda_total <= 0:
        return 0

    return venda_portal / venda_total


def calcular_score(produto):
    score = 100

    margem = safe_percent(produto["margem"])
    markup = numero(produto["markup"])
    giro = numero(produto["giroEstoque"])
    estoque = numero(produto["estoqueTotal"])

    if estoque <= 0:
        score -= 50

    if margem < 0.10:
        score -= 25

    if margem > 0.20:
        score += 10

    if giro > 1:
        score += 10

    if markup > 1.8:
        score += 10

    if markup > 0 and markup < 1.2:
        score -= 15

    return max(0, min(100, score))