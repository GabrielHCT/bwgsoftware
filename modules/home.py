# modules/home.py

import streamlit as st


def ir_para_modulo(nome_modulo):
    st.session_state["modulo_selecionado"] = nome_modulo
    st.rerun()


def card_modulo(icone, titulo, texto, status, modulo):
    st.markdown(
        f"""
        <div class="home-card">
            <div class="home-card-icon">{icone}</div>
            <div class="home-card-title">{titulo}</div>
            <div class="home-card-text">{texto}</div>
            <div class="home-card-status">{status}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(f"Abrir {titulo}", key=f"abrir_{titulo}", use_container_width=True):
        ir_para_modulo(modulo)


def render_home():
    st.markdown(
        """
        <div class="home-hero">
            <div>
                <span class="home-badge">BWG SHOP</span>
                <h1>Central Inteligente de Produtos</h1>
                <p>
                    Painel operacional para análise de DRE, pesquisa de produtos,
                    rankings, comparação de portais, alertas, ruptura e simulações.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        card_modulo(
            "🔎",
            "Pesquisa",
            "Busque produtos por SKU, EAN, marca ou descrição.",
            "Principal",
            "🔎 Pesquisa",
        )

    with col2:
        card_modulo(
            "📊",
            "Executivo",
            "KPIs gerais, gráficos e produtos críticos.",
            "Dashboard",
            "📊 Executivo",
        )

    with col3:
        card_modulo(
            "⚖️",
            "Comparar Preços",
            "Compare preço à vista e margem entre portais.",
            "Novo",
            "⚖️ Comparar Preços",
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        card_modulo(
            "🔥",
            "Top 10",
            "Ranking por venda e quantidade.",
            "Ranking",
            "🔥 Top 10 Rankings",
        )

    with col5:
        card_modulo(
            "📅",
            "Dia Anterior",
            "Top 10 produtos vendidos no dia anterior.",
            "Ranking",
            "📅 Ranking Dia Anterior",
        )

    with col6:
        card_modulo(
            "🧮",
            "Simulador",
            "Simule preço, custo, margem, comissão e markup.",
            "Ferramenta",
            "🧮 Simulador",
        )

    col7, col8, col9 = st.columns(3)

    with col7:
        card_modulo(
            "🚨",
            "Alertas",
            "Produtos críticos, margem baixa e problemas operacionais.",
            "Inteligente",
            "🚨 Alertas",
        )

    with col8:
        card_modulo(
            "📦",
            "Ruptura",
            "Previsão de risco de falta de estoque.",
            "Estoque",
            "📦 Ruptura",
        )

    with col9:
        card_modulo(
            "🏷️",
            "Tags",
            "Classificação estratégica automática dos produtos.",
            "Operacional",
            "🏷️ Tags",
        )