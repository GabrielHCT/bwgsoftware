# core/cache_manager.py

import streamlit as st


def limpar_todos_caches():

    st.cache_data.clear()
    st.cache_resource.clear()