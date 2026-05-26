# core/theme.py

import streamlit as st


def aplicar_tema(dark=False):

    if dark:

        st.markdown(
            """
            <style>

            .stApp{
                background:#0f172a;
                color:white;
            }

            .card{
                background:#111827 !important;
                border:1px solid #1e293b !important;
            }

            div[data-testid="stMetric"]{
                background:#111827 !important;
                border:1px solid #1e293b !important;
            }

            .main-title,
            .produto-title{
                color:white !important;
            }

            .produto-meta,
            .main-subtitle{
                color:#cbd5e1 !important;
            }

            </style>
            """,
            unsafe_allow_html=True,
        )