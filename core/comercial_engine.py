# core/comercial_engine.py


def preparar_visao_comercial(df_produtos):

    comercial = df_produtos.copy()

    # REMOVE DADOS SENSÍVEIS
    colunas_remover = [
        "custo",
        "lucroEmpresa",
        "markup",
        "margem",
    ]

    for col in colunas_remover:
        if col in comercial.columns:
            comercial = comercial.drop(columns=[col])

    return comercial