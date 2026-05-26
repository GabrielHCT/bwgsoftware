# core/filters.py


def aplicar_filtros(
    df,
    marca=None,
    categoria=None,
    somente_estoque=False,
):

    filtrado = df.copy()

    if marca:
        filtrado = filtrado[
            filtrado["marca"] == marca
        ]

    if categoria:
        filtrado = filtrado[
            filtrado["categoria"] == categoria
        ]

    if somente_estoque:
        filtrado = filtrado[
            filtrado["estoqueTotal"] > 0
        ]

    return filtrado