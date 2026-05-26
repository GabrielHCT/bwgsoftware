# modules/comparar_precos.py

import streamlit as st

from core.config import PORTAIS
from core.price_compare_engine import comparar_precos_portais
from core.helpers import moeda, percentual_formatado


def render_comparar_precos():

    st.title("⚖️ Comparar Preços entre Portais")

    col1, col2 = st.columns(2)

    with col1:
        portal_1 = st.selectbox(
            "Portal 1",
            list(PORTAIS.keys()),
            key="comparar_portal_1"
        )

    with col2:
        portal_2 = st.selectbox(
            "Portal 2",
            list(PORTAIS.keys()),
            key="comparar_portal_2"
        )

    if portal_1 == portal_2:
        st.warning("Escolha dois portais diferentes.")
        return

    if st.button(
        "Comparar Portais",
        use_container_width=True,
    ):

        comparativo = comparar_precos_portais(
            portal_1,
            portal_2,
        )

        if comparativo.empty:
            st.warning(
                "Nenhum produto em comum encontrado."
            )
            return

        st.success(
            f"{len(comparativo)} produto(s) encontrados."
        )

        busca = st.text_input(
            "Filtrar produto"
        )

        if busca:

            busca = busca.lower()

            comparativo = comparativo[
                comparativo["descricao"].str.lower().str.contains(
                    busca,
                    na=False
                )
            ]

        for _, row in comparativo.iterrows():

            st.markdown(
                f"""
                <div class="produto-card">

                    <div class="produto-title">
                        {row["descricao"]}
                    </div>

                    <div class="produto-meta">
                        SKU: {row["sku"]}
                    </div>

                    <hr>

                    <p>
                        <b>{portal_1}</b><br>
                        Preço: {moeda(row["preco_1"])}<br>
                        Margem: {percentual_formatado(row["margem_1"])}
                    </p>

                    <p>
                        <b>{portal_2}</b><br>
                        Preço: {moeda(row["preco_2"])}<br>
                        Margem: {percentual_formatado(row["margem_2"])}
                    </p>

                    <hr>

                    <p>
                        <b>Diferença Preço:</b>
                        {moeda(row["diferenca_preco"])}
                    </p>

                    <p>
                        <b>Diferença Margem:</b>
                        {percentual_formatado(row["diferenca_margem"])}
                    </p>

                </div>
                """,
                unsafe_allow_html=True,
            )

        st.dataframe(
            comparativo,
            use_container_width=True,
            hide_index=True,
        )