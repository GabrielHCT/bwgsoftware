# components/alerts.py

import streamlit as st


def render_alertas(produto):

    analise = produto["analise"]

    st.subheader("🚨 Alertas")

    if analise["alertas"]:

        for tipo, texto in analise["alertas"]:

            if tipo == "erro":
                st.error(texto)

            elif tipo == "alerta":
                st.warning(texto)

            elif tipo == "sucesso":
                st.success(texto)

    else:
        st.success("Nenhum alerta encontrado.")

    st.subheader("💡 Insights")

    if analise["insights"]:
        for item in analise["insights"]:
            st.info(item)

    else:
        st.success("Nenhum insight crítico.")

    st.subheader("🚀 Oportunidades")

    if analise["oportunidades"]:
        for item in analise["oportunidades"]:
            st.success(item)

    else:
        st.info("Nenhuma oportunidade encontrada.")