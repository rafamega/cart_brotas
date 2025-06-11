from utils.utils import (
    formatar_nome,
    formatar_rg,
    formatar_cpf,
    formatar_cpf,
    formatar_valor,
    calcular_itbi
)


def coletar_dados_pessoa(label="outorgante"):
    dados = {}
    print(f"🔹 Dados do {label}:")

    sexo = input("Sexo (M/F): ").strip().lower()
    if sexo == "m":
        dados.update(
            {
                "tratamento": "o Sr.",
                "nacionalidade": "brasileiro",
                "filh": "filho",
                "nascid": "nascido",
                "portad": "portador",
                "inscrit": "inscrito",
                "domiciliad": "domiciliado",
                "solteir": "solteiro",
                "casad": "casado",
                "sm": "sua esposa",
                "divorciad": "divorciado",
                "viuv": "viúvo",
            }
        )
    else:
        dados.update(
            {
                "tratamento": "a Sra.",
                "nacionalidade": "brasileira",
                "filh": "filha",
                "nascid": "nascida",
                "portad": "portadora",
                "inscrit": "inscrita",
                "domiciliad": "domiciliada",
                "solteir": "solteira",
                "casad": "casada",
                "sm": "seu marido",
                "divorciad": "divorciada",
                "viuv": "viúva",
            }
        )

    dados["nome"] = input("Nome: ").upper()
    dados["profissao"] = input("Profissão: ").lower()
    pai = formatar_nome(input("Nome do pai: "))
    mae = formatar_nome(input("Nome da mãe: "))
    dados["filiacao"] = f"{pai} e de {mae}"
    dados["rg"] = formatar_rg(input("RG (apenas números): "))
    dados["org_exp"] = "SSP/SP"
    dados["cpf"] = formatar_cpf()

    return dados


def regime_casamento():
    regime = input("Regime do Casamento (P/U/S): ").lower()
    match regime:
        case "p":
            return "Comunhão Parcial de Bens"
        case "u":
            return "Comunhão Universal de Bens"
        case "s":
            return "Separação de Bens"
        case _:
            return "Comunhão Parcial de Bens"


def coletar_dados_valores():
    dados_valores = {}
    
    valor_ajustado_str = input("Valor ajustado: ")
    valor_venal_str = input("Valor Venal: ")
    
    # Converte os valores de string para float
    valor_ajustado_float = float(valor_ajustado_str.replace(".", "").replace(",", "."))
    valor_venal_float = float(valor_venal_str.replace(".", "").replace(",", "."))

    # Formata tudo ao final
    dados_valores["valor_ajustado"] = formatar_valor(valor_ajustado_float)
    dados_valores["valor_venal"] = formatar_valor(valor_venal_float)
    dados_valores["valor_itbi"] = calcular_itbi(valor_ajustado_float)

    return dados_valores
