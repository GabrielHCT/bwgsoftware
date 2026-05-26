# components/loading.py

import streamlit as st


def skeleton():

    with st.container():

        st.markdown(
            """
            <div style="
                height:120px;
                background:#e2e8f0;
                border-radius:22px;
                margin-bottom:18px;
                animation:pulse 1.4s infinite;
            "></div>

            <style>
            @keyframes pulse{
                0%{opacity:.5;}
                50%{opacity:1;}
                100%{opacity:.5;}
            }
            </style>
            """,
            unsafe_allow_html=True,
        )