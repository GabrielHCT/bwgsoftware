# core/export_engine.py

import pandas as pd
import io


def gerar_excel(df):

    output = io.BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Produtos"
        )

    output.seek(0)

    return output


def gerar_csv(df):

    csv = df.to_csv(index=False)

    return csv.encode("utf-8")