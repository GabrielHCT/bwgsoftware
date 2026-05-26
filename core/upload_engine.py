# core/upload_engine.py

import pandas as pd


def processar_excel_upload(arquivo):

    try:

        df = pd.read_excel(arquivo)

        return {
            "sucesso": True,
            "df": df,
        }

    except Exception as e:

        return {
            "sucesso": False,
            "erro": str(e),
        }