# components/dark_mode.py

import streamlit as st


def toggle_dark_mode():

    if "dark_mode" not in st.session_state:
        st.session_state["dark_mode"] = False

    dark = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state["dark_mode"]
    )

    st.session_state["dark_mode"] = dark

    return dark