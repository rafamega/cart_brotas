from num2words import num2words


def formatar_valor(valor) -> str:
    # Se for string, converte para float (aceita vírgula como separador decimal)
    if isinstance(valor, str):
        valor = float(valor.replace(".", "").replace(",", ".").strip())

    # Formatação com símbolo
    valor_formatado = (
        f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

    # Separação por extenso
    parte_inteira = int(valor)
    centavos = int(round((valor - parte_inteira) * 100))

    extenso = f"{num2words(parte_inteira, lang='pt_BR')} Reais"
    if centavos > 0:
        extenso += f" e {num2words(centavos, lang='pt_BR')} centavos"

    return f"{valor_formatado} ({extenso})"


def calcular_itbi(valor_base) -> str:
    """Recebe valor base como float ou string e retorna o ITBI formatado"""
    # Converte para float, se for string
    if isinstance(valor_base, str):
        valor_base = float(valor_base.replace(".", "").replace(",", "."))

    itbi = round(valor_base * 0.03, 2)
    return formatar_valor(itbi)
