# core/scheduler_engine.py


def verificar_produtos_criticos(df_alertas):

    criticos = df_alertas[
        df_alertas["prioridade"] >= 9
    ]

    return criticos