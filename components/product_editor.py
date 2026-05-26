# components/product_editor.py

import streamlit as st

from core.config import OPCOES
from core.sheets import abrir_aba, limpar_cache_dados
from core.columns import criar_mapa_colunas


def atualizar_por_titulo(portal, df, linha, valores):
    aba = abrir_aba(portal)
    mapa = criar_mapa_colunas(df)

    for campo_padrao, valor in valores.items():
        nome_coluna = mapa.get(campo_padrao)

        if not nome_coluna:
            continue

        coluna_numero = list(df.columns).index(nome_coluna) + 1

        # +1 porque df tem _linha_real na posição 0, mas a planilha não
        coluna_planilha = coluna_numero

        if nome_coluna == "_linha_real":
            continue

        aba.update_cell(linha, coluna_planilha, valor)

    limpar_cache_dados()


def render_editor(produto, portal, df):
    st.subheader("✏️ Editar Produto")

    with st.form("editar_produto"):
        col1, col2 = st.columns(2)

        with col1:
            preco = st.number_input(
                "Preço Vista",
                value=float(produto["precoVista"]),
            )

            b_seller = st.number_input(
                "B Seller (%)",
                value=float(produto["bSeller"] * 100),
            )

            b_portal = st.number_input(
                "B Portal (%)",
                value=float(produto["bPortal"] * 100),
            )

        with col2:
            comissao = st.number_input(
                "Comissão (%)",
                value=float(produto["comissao"] * 100),
            )

            obs_preco = st.selectbox(
                "Observação Preço",
                OPCOES["observacaoPreco"],
                index=(
                    OPCOES["observacaoPreco"].index(produto["observacaoPreco"])
                    if produto["observacaoPreco"] in OPCOES["observacaoPreco"]
                    else 0
                )
            )

            obs_frete = st.selectbox(
                "Observação Frete",
                OPCOES["observacaoFrete"],
                index=(
                    OPCOES["observacaoFrete"].index(produto["observacaoFrete"])
                    if produto["observacaoFrete"] in OPCOES["observacaoFrete"]
                    else 0
                )
            )

        salvar = st.form_submit_button("💾 Salvar Produto")

        if salvar:
            atualizar_por_titulo(
                portal,
                df,
                produto["linha"],
                {
                    "precoVista": preco,
                    "bSeller": b_seller / 100,
                    "bPortal": b_portal / 100,
                    "comissao": comissao / 100,
                    "observacaoPreco": obs_preco,
                    "observacaoFrete": obs_frete,
                }
            )

            st.success("Produto salvo com sucesso.")