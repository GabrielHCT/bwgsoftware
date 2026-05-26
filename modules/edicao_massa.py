# modules/edicao_massa.py

import streamlit as st

from core.sheets import carregar_dados, atualizar_linha_por_titulos
from core.dashboard import preparar_dataframe_produtos
from core.columns import criar_mapa_colunas


def render_edicao_massa(portal):
    st.title("🛠️ Edição em Massa")

    df_original = carregar_dados(portal, "dre")

    if df_original.empty:
        st.warning("Nenhum dado encontrado.")
        return

    produtos = preparar_dataframe_produtos(df_original)

    if produtos.empty:
        st.warning("Nenhum produto carregado.")
        return

    mapa = criar_mapa_colunas(df_original)

    st.info("Atualize vários produtos ao mesmo tempo.")

    selecionados = st.multiselect(
        "Produtos",
        options=produtos.to_dict("records"),
        format_func=lambda x: f"{x['sku']} - {x['descricao']}",
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        nova_comissao = st.number_input(
            "Nova Comissão %",
            min_value=0.0,
            value=15.0,
        )

    with col2:
        novo_bseller = st.number_input(
            "Novo B Seller %",
            min_value=0.0,
            value=5.0,
        )

    with col3:
        novo_bportal = st.number_input(
            "Novo B Portal %",
            min_value=0.0,
            value=0.0,
        )

    if st.button(
        "💾 Atualizar Produtos",
        use_container_width=True,
    ):
        if not selecionados:
            st.warning("Selecione pelo menos um produto.")
            return

        valores = {}

        if mapa.get("comissao"):
            valores[mapa["comissao"]] = nova_comissao / 100

        if mapa.get("bSeller"):
            valores[mapa["bSeller"]] = novo_bseller / 100

        if mapa.get("bPortal"):
            valores[mapa["bPortal"]] = novo_bportal / 100

        if not valores:
            st.error(
                "Nenhuma coluna editável encontrada na planilha "
                "(Comissão, B Seller ou B Portal)."
            )
            return

        total = 0

        for produto in selecionados:
            atualizar_linha_por_titulos(
                portal=portal,
                tipo_aba="dre",
                linha=int(produto["linha"]),
                valores=valores,
            )

            total += 1

        st.success(f"{total} produto(s) atualizado(s).")