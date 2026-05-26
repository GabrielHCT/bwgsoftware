# components/filters_bar.py

import streamlit as st


def render_filters(df):

    marcas = sorted(
        [
            x for x in df["marca"].dropna().unique()
            if x
        ]
    )

    categorias = sorted(
        [
            x for x in df["categoria"].dropna().unique()
            if x
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        marca = st.selectbox(
            "Marca",
            [""] + marcas
        )

    with col2:

        categoria = st.selectbox(
            "Categoria",
            [""] + categorias
        )

    with col3:

        somente_estoque = st.checkbox(
            "Somente com estoque"
        )

    return {
        "marca": marca,
        "categoria": categoria,
        "somente_estoque": somente_estoque,
    }