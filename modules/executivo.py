# modules/executivo.py

import streamlit as st

from core.sheets import carregar_dados
from core.dashboard import (
    preparar_dataframe_produtos,
    indicadores_executivos,
    produtos_criticos,
)
from core.helpers import moeda, percentual_formatado
from components.charts import grafico_top_marcas, grafico_margem_estoque

from core.export_engine import (
    gerar_excel,
    gerar_csv,
)

from core.filters import aplicar_filtros
from components.filters_bar import render_filters

def render_executivo(portal):
    st.title("📊 Dashboard Executivo")

    df = carregar_dados(portal)
    df_produtos = preparar_dataframe_produtos(df)

    filtros = render_filters(df_produtos)

    df_produtos = aplicar_filtros(
        df_produtos,
        marca=filtros["marca"],
        categoria=filtros["categoria"],
        somente_estoque=filtros["somente_estoque"],
    )

    if df_produtos.empty:
        st.warning("Nenhum dado encontrado.")
        return

    indicadores = indicadores_executivos(df_produtos)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Produtos", indicadores["totalProdutos"])
    col2.metric("Estoque Total", int(indicadores["estoqueTotal"]))
    col3.metric("Venda Total", int(indicadores["vendaTotal"]))
    col4.metric("Lucro Total", moeda(indicadores["lucroTotal"]))

    col5, col6, col7, col8 = st.columns(4)

    col5.metric("Margem Média", percentual_formatado(indicadores["margemMedia"]))
    col6.metric("Markup Médio", f"{indicadores['markupMedio']:.2f}")
    col7.metric("Sem Estoque", indicadores["produtosSemEstoque"])
    col8.metric("Margem Baixa", indicadores["produtosMargemBaixa"])

    st.divider()

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        grafico_top_marcas(df_produtos)

    with col_g2:
        grafico_margem_estoque(df_produtos)

    st.divider()

    st.subheader("🚨 Produtos críticos")

    criticos = produtos_criticos(df_produtos).head(20)

    if criticos.empty:
        st.success("Nenhum produto crítico encontrado.")
    else:
        st.dataframe(
            criticos[
                [
                    "sku",
                    "descricao",
                    "marca",
                    "estoqueTotal",
                    "vendaTotal",
                    "margem",
                    "giro",
                    "observacaoPreco",
                    "exposicao",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )
        
    st.divider()

    st.subheader("📥 Exportações")

    excel = gerar_excel(df_produtos)

    st.download_button(
        "📊 Exportar Excel",
        data=excel,
        file_name="dashboard.xlsx",
        mime=(
            "application/vnd.openxmlformats-"
            "officedocument.spreadsheetml.sheet"
        ),
        use_container_width=True,
    )

    csv = gerar_csv(df_produtos)

    st.download_button(
        "📄 Exportar CSV",
        data=csv,
        file_name="dashboard.csv",
        mime="text/csv",
        use_container_width=True,
    )


        