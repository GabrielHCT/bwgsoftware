# components/product_header.py

import streamlit as st

from core.helpers import moeda, percentual_formatado


def render_product_header(produto):

    col1, col2 = st.columns([1, 2])

    with col1:

        imagem = produto["imagem"]

        if imagem:
            st.image(imagem, use_container_width=True)

        else:
            st.info("Produto sem imagem.")

    with col2:

        st.markdown(
            f"""
            <div class="card">

            <h2 style="font-size:32px;font-weight:900;color:#0f172a;">
                {produto["descricao"]}
            </h2>

            <p style="color:#64748b;font-size:15px;">
                <b>SKU Seller:</b> {produto["skuSeller"]}<br>
                <b>SKU Portal:</b> {produto["skuPortal"]}<br>
                <b>Marca:</b> {produto["marca"]}<br>
                <b>Categoria:</b> {produto["categoria"]}
            </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric(
                "Preço Vista",
                moeda(produto["precoVista"])
            )

        with colB:
            st.metric(
                "Margem",
                percentual_formatado(produto["margem"])
            )

        with colC:
            st.metric(
                "Markup",
                f"{produto['markup']:.2f}"
            )