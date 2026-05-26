# core/pagination.py

import math
import streamlit as st


def render_paginacao(
    total,
    por_pagina=50,
):

    paginas = max(
        1,
        math.ceil(total / por_pagina)
    )

    pagina = st.number_input(
        "Página",
        min_value=1,
        max_value=paginas,
        value=1,
    )

    return pagina