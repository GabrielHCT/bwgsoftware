# core/sheets.py

import streamlit as st
import pandas as pd
import gspread

from google.oauth2.service_account import Credentials

from core.config import (
    GOOGLE_CREDENTIALS_PATH,
    PORTAIS,
    ABAS_CONFIG,
)

from core.config import MODO_LOCAL, ARQUIVO_LOCAL_MAGALU

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


@st.cache_resource
def conectar_google():
    credentials = Credentials.from_service_account_file(
        GOOGLE_CREDENTIALS_PATH,
        scopes=SCOPES,
    )

    return gspread.authorize(credentials)


def abrir_planilha_portal(portal: str):
    client = conectar_google()

    config = PORTAIS.get(portal)

    if not config:
        raise ValueError(f"Portal não configurado: {portal}")

    nome_planilha = config.get("spreadsheet")

    if not nome_planilha:
        raise ValueError(f"Nome da planilha não configurado para o portal: {portal}")

    return client.open(nome_planilha)


def get_nome_aba(portal: str, tipo_aba: str = "dre"):
    config = PORTAIS.get(portal)

    if not config:
        raise ValueError(f"Portal não configurado: {portal}")

    abas = config.get("abas", {})
    nome_aba = abas.get(tipo_aba)

    if not nome_aba:
        raise ValueError(
            f"Aba '{tipo_aba}' não configurada para o portal: {portal}"
        )

    return nome_aba


def abrir_aba(portal: str, tipo_aba: str = "dre"):
    planilha = abrir_planilha_portal(portal)
    nome_aba = get_nome_aba(portal, tipo_aba)

    return planilha.worksheet(nome_aba)


def preencher_mesclagem_horizontal(linha):
    preenchida = []
    ultimo_valor = ""

    for valor in linha:
        valor = str(valor or "").strip()

        if valor:
            ultimo_valor = valor

        preenchida.append(ultimo_valor)

    return preenchida


def limpar_titulo_coluna(valor):
    valor = str(valor or "").strip()
    return " ".join(valor.split())


def montar_cabecalho_simples(linha):
    cabecalho = []

    for i, valor in enumerate(linha):
        nome = limpar_titulo_coluna(valor)

        if not nome:
            nome = f"COLUNA_{i + 1}"

        cabecalho.append(nome)

    return cabecalho


def montar_cabecalho_composto(linha_1, linha_2):
    linha_1 = preencher_mesclagem_horizontal(linha_1)

    tamanho = max(len(linha_1), len(linha_2))
    cabecalho = []

    for i in range(tamanho):
        grupo = limpar_titulo_coluna(
            linha_1[i] if i < len(linha_1) else ""
        )

        sub = limpar_titulo_coluna(
            linha_2[i] if i < len(linha_2) else ""
        )

        if grupo and sub:
            nome = f"{grupo} {sub}"
        elif grupo:
            nome = grupo
        elif sub:
            nome = sub
        else:
            nome = f"COLUNA_{i + 1}"

        cabecalho.append(nome)

    return cabecalho


def normalizar_tamanho_linhas(linhas, tamanho):
    novas_linhas = []

    for linha in linhas:
        linha = list(linha)

        if len(linha) < tamanho:
            linha += [""] * (tamanho - len(linha))

        elif len(linha) > tamanho:
            linha = linha[:tamanho]

        novas_linhas.append(linha)

    return novas_linhas


def tornar_colunas_unicas(colunas):
    vistas = {}
    resultado = []

    for coluna in colunas:
        nome = coluna

        if nome not in vistas:
            vistas[nome] = 1
            resultado.append(nome)
        else:
            vistas[nome] += 1
            resultado.append(f"{nome}__{vistas[nome]}")

    return resultado


def detectar_header_rows(tipo_aba: str):
    config = ABAS_CONFIG.get(tipo_aba, {})
    return int(config.get("header_rows", 1))


def dataframe_da_aba(portal: str, tipo_aba: str = "dre"):
    aba = abrir_aba(portal, tipo_aba)
    dados = aba.get_all_values()

    if not dados:
        return pd.DataFrame()

    header_rows = detectar_header_rows(tipo_aba)

    if header_rows == 2:
        if len(dados) < 3:
            return pd.DataFrame()

        cabecalho = montar_cabecalho_composto(
            dados[0],
            dados[1],
        )

        inicio_dados = 2
        linha_real_inicio = 3

    else:
        if len(dados) < 2:
            return pd.DataFrame()

        cabecalho = montar_cabecalho_simples(dados[0])

        inicio_dados = 1
        linha_real_inicio = 2

    cabecalho = tornar_colunas_unicas(cabecalho)

    linhas = dados[inicio_dados:]
    linhas = normalizar_tamanho_linhas(
        linhas,
        len(cabecalho),
    )

    df = pd.DataFrame(
        linhas,
        columns=cabecalho,
    )

    df.insert(
        0,
        "_linha_real",
        range(
            linha_real_inicio,
            linha_real_inicio + len(df),
        ),
    )

    return df


@st.cache_data(ttl=300, show_spinner="Carregando dados...")
def carregar_dados(portal: str, tipo_aba: str = "dre"):

    if MODO_LOCAL:
        nome_aba = PORTAIS[portal]["abas"][tipo_aba]

        df = pd.read_excel(
            ARQUIVO_LOCAL_MAGALU,
            sheet_name=nome_aba,
            header=0 if tipo_aba in ["dre", "setup_produtos"] else [0, 1],
        )

        df.insert(0, "_linha_real", range(2, len(df) + 2))

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [
                " ".join([str(x) for x in col if str(x) != "nan"]).strip()
                for col in df.columns
            ]

        return df

    return dataframe_da_aba(portal, tipo_aba)


def limpar_cache_dados():
    st.cache_data.clear()


def atualizar_celula_por_titulo(
    portal: str,
    tipo_aba: str,
    linha: int,
    nome_coluna: str,
    valor,
):
    aba = abrir_aba(portal, tipo_aba)
    df = dataframe_da_aba(portal, tipo_aba)

    if nome_coluna not in df.columns:
        raise ValueError(f"Coluna não encontrada: {nome_coluna}")

    coluna_df = list(df.columns).index(nome_coluna)

    if nome_coluna == "_linha_real":
        raise ValueError("Não é permitido atualizar a coluna _linha_real.")

    # df tem _linha_real na posição 0.
    # A planilha NÃO tem essa coluna.
    coluna_planilha = coluna_df

    aba.update_cell(
        linha,
        coluna_planilha,
        valor,
    )

    limpar_cache_dados()


def atualizar_linha_por_titulos(
    portal: str,
    tipo_aba: str,
    linha: int,
    valores: dict,
):
    aba = abrir_aba(portal, tipo_aba)
    df = dataframe_da_aba(portal, tipo_aba)

    for nome_coluna, valor in valores.items():
        if nome_coluna == "_linha_real":
            continue

        if nome_coluna not in df.columns:
            continue

        coluna_df = list(df.columns).index(nome_coluna)

        # df tem _linha_real na posição 0.
        # A planilha NÃO tem essa coluna.
        coluna_planilha = coluna_df

        aba.update_cell(
            linha,
            coluna_planilha,
            valor,
        )

    limpar_cache_dados()