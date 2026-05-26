# core/helpers.py

import math
import re


ERROS_PLANILHA = {
    "#DIV/0!",
    "#N/A",
    "#VALUE!",
    "#REF!",
    "#NAME?",
    "#NUM!",
    "#ERROR!",
    "DIV%",
    "Infinity",
    "-Infinity",
    "NaN",
}


def limpar_erro_planilha(valor):
    if valor is None:
        return ""

    texto = str(valor).strip()

    if texto in ERROS_PLANILHA:
        return ""

    return valor


def texto(valor):
    valor = limpar_erro_planilha(valor)
    return str(valor or "").strip()


def numero(valor):
    valor = limpar_erro_planilha(valor)

    if valor is None or valor == "":
        return 0

    if isinstance(valor, (int, float)):
        if math.isfinite(valor):
            return valor
        return 0

    s = str(valor).strip()
    s = s.replace("R$", "")
    s = s.replace("%", "")
    s = s.replace(" ", "")

    if not s:
        return 0

    # Formato BR: 1.234,56
    if "," in s:
        s = s.replace(".", "").replace(",", ".")

    try:
        n = float(s)
        return n if math.isfinite(n) else 0
    except ValueError:
        return 0


def safe_percent(valor):
    n = numero(valor)

    if n > 1:
        n = n / 100

    if not math.isfinite(n):
        return 0

    return n


def converter_percentual(valor):
    return safe_percent(valor)


def percentual_formatado(valor):
    return f"{safe_percent(valor) * 100:.2f}%"


def moeda(valor):
    n = numero(valor)
    return f"R$ {n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def normalizar_url(url):
    url = texto(url)

    if not url:
        return ""

    match = re.search(r"https?://[^\"')\s;]+", url, re.IGNORECASE)

    if match:
        url = match.group(0)

    if url.startswith("//"):
        url = "https:" + url

    if url.startswith("http://"):
        url = url.replace("http://", "https://", 1)

    return url.strip()