# core/favorites_engine.py


def inicializar_favoritos():

    import streamlit as st

    if "favoritos" not in st.session_state:
        st.session_state["favoritos"] = []


def adicionar_favorito(produto):

    import streamlit as st

    inicializar_favoritos()

    sku = produto["skuSeller"]

    existe = any(
        x["skuSeller"] == sku
        for x in st.session_state["favoritos"]
    )

    if not existe:
        st.session_state["favoritos"].append(
            produto
        )


def remover_favorito(sku):

    import streamlit as st

    inicializar_favoritos()

    st.session_state["favoritos"] = [
        x
        for x in st.session_state["favoritos"]
        if x["skuSeller"] != sku
    ]