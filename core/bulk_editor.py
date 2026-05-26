# core/bulk_editor.py

from core.sheets import atualizar_linha_por_titulos
from core.columns import criar_mapa_colunas


def atualizar_produtos_massa(
    portal,
    produtos,
    campos,
    tipo_aba="dre",
):
    """
    Atualiza vários produtos em massa usando títulos de coluna,
    não posição fixa.

    portal: nome do portal, ex: "Magalu"
    produtos: lista de dicts vindos do dataframe preparado
    campos: dict com campo_padrao -> valor
        exemplo:
        {
            "comissao": 0.15,
            "bSeller": 0.05
        }
    tipo_aba: normalmente "dre"
    """

    if not produtos:
        return 0

    total = 0

    for produto in produtos:
        linha = produto.get("linha")

        if not linha:
            continue

        # Aqui os nomes são campos padrão.
        # O atualizar_linha_por_titulos espera nome real da coluna,
        # então vamos resolver isso dentro do módulo de edição em massa depois.
        atualizar_linha_por_titulos(
            portal=portal,
            tipo_aba=tipo_aba,
            linha=int(linha),
            valores=campos,
        )

        total += 1

    return total