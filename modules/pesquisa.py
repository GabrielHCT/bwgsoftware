# modules/pesquisa.py

import streamlit as st

from core.config import PORTAIS, CONFIG_APP
from core.sheets import carregar_dados
from core.product import montar_produto
from core.helpers import texto
from core.columns import criar_mapa_colunas, valor_coluna, validar_colunas_obrigatorias
from core.ai_engine import gerar_recomendacoes
from core.favorites_engine import adicionar_favorito

from components.product_header import render_product_header
from components.kpis import render_kpis
from components.alerts import render_alertas
from components.product_editor import render_editor


def buscar_produtos(df, termo):
    termo = texto(termo).lower()

    if not termo:
        return df.iloc[0:0]

    mapa = criar_mapa_colunas(df)

    resultados = []
    limite = CONFIG_APP.get("limite_resultados_pesquisa", 30)

    for _, row in df.iterrows():
        sku = texto(valor_coluna(row, mapa, "sku"))
        sku_portal = texto(valor_coluna(row, mapa, "skuPortal"))
        marca = texto(valor_coluna(row, mapa, "marca"))
        descricao = texto(valor_coluna(row, mapa, "descricao"))
        ean = texto(valor_coluna(row, mapa, "ean"))

        encontrou = (
            termo in sku.lower()
            or termo in sku_portal.lower()
            or termo in marca.lower()
            or termo in descricao.lower()
            or termo in ean.lower()
        )

        if encontrou:
            resultados.append(row)

        if len(resultados) >= limite:
            break

    if not resultados:
        return df.iloc[0:0]

    return df.loc[[r.name for r in resultados]]


def render_card_resultado(row, df):
    mapa = criar_mapa_colunas(df)

    linha = row["_linha_real"]

    sku = texto(valor_coluna(row, mapa, "sku"))
    sku_portal = texto(valor_coluna(row, mapa, "skuPortal"))
    marca = texto(valor_coluna(row, mapa, "marca"))
    descricao = texto(valor_coluna(row, mapa, "descricao"))
    ean = texto(valor_coluna(row, mapa, "ean"))

    with st.container():
        col1, col2 = st.columns([5, 1])

        with col1:
            st.markdown(
                f"""
                <div class="produto-card">
                    <div class="produto-title">
                        {descricao or "Produto sem descrição"}
                    </div>

                    <div class="produto-meta">
                        <b>SKU:</b> {sku or "-"} |
                        <b>SKU Portal:</b> {sku_portal or "-"} |
                        <b>Marca:</b> {marca or "-"} |
                        <b>EAN:</b> {ean or "-"}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            if st.button(
                "Abrir",
                key=f"abrir_{linha}",
                use_container_width=True,
            ):
                produto = montar_produto(row, df)
                st.session_state["produto"] = produto
                st.session_state["produto_portal"] = st.session_state.get(
                    "portal_pesquisa"
                )
                st.success("Produto carregado.")


def render_produto_carregado(portal, df):
    produto = st.session_state.get("produto")

    if not produto:
        return

    recomendacoes = gerar_recomendacoes(produto)

    st.divider()

    render_product_header(produto)

    st.divider()

    st.subheader("📊 KPIs")
    render_kpis(produto)

    st.divider()

    colA, colB = st.columns([1, 1])

    with colA:
        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <div style="font-size:18px;font-weight:800;color:#64748b;">
                    SCORE
                </div>

                <div style="
                    font-size:72px;
                    font-weight:900;
                    color:#2563eb;
                ">
                    {produto.get("score", 0)}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with colB:
        render_alertas(produto)

    st.divider()

    st.subheader("🤖 IA Operacional")

    if recomendacoes:
        for rec in recomendacoes:
            mensagem = f"**{rec['titulo']}**\n\n{rec['texto']}"

            if rec["tipo"] == "erro":
                st.error(mensagem)
            elif rec["tipo"] == "alerta":
                st.warning(mensagem)
            else:
                st.success(mensagem)
    else:
        st.info("Nenhuma recomendação automática encontrada.")

    st.divider()

    render_editor(produto, portal, df)

    if st.button(
        "⭐ Adicionar aos Favoritos",
        use_container_width=True,
    ):
        adicionar_favorito(produto)
        st.success("Produto adicionado aos favoritos.")


def render_pesquisa(portal_atual):
    st.title("🔎 Pesquisa de Produtos")

    portal = st.selectbox(
        "Escolha o portal para pesquisar",
        list(PORTAIS.keys()),
        index=list(PORTAIS.keys()).index(portal_atual),
        key="portal_pesquisa",
    )

    df = carregar_dados(portal, "dre")

    if df.empty:
        st.warning("Planilha vazia ou aba DRE não encontrada.")
        return

    faltando, _ = validar_colunas_obrigatorias(
        df,
        ["sku", "descricao"],
    )

    if faltando:
        st.error(
            "Colunas obrigatórias não encontradas: "
            + ", ".join(faltando)
        )
        st.info("Confira os títulos da DRE ou adicione aliases no core/columns.py.")
        return

    termo = st.text_input(
        "Pesquisar",
        placeholder="Digite SKU, SKU Portal, EAN, marca ou descrição...",
    )

    if termo:
        resultados = buscar_produtos(df, termo)

        if resultados.empty:
            st.warning("Nenhum produto encontrado.")
        else:
            st.success(f"{len(resultados)} resultado(s).")

            for _, row in resultados.iterrows():
                render_card_resultado(row, df)

    render_produto_carregado(portal, df)