# core/simulator_engine.py


def calcular_simulacao(
    preco,
    custo,
    comissao,
    bseller,
    bportal,
):

    preco = float(preco)
    custo = float(custo)

    comissao = float(comissao)
    bseller = float(bseller)
    bportal = float(bportal)

    # %
    total_taxas = (
        comissao
        + bseller
        + bportal
    )

    valor_taxas = preco * total_taxas

    lucro = preco - custo - valor_taxas

    margem = 0

    if preco > 0:
        margem = lucro / preco

    markup = 0

    if custo > 0:
        markup = preco / custo

    return {
        "lucro": lucro,
        "margem": margem,
        "markup": markup,
        "taxas": valor_taxas,
    }