import requests

from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


def formatar_nome(nome):
    conectores = {"da", "de", "do", "dos", "das", "e"}
    palavras = nome.strip().lower().split()
    return " ".join([p if p in conectores else p.capitalize() for p in palavras])


def formatar_rg(rg):
    match len(rg):
        case 9:
            return f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8]}"
        case 8:
            return f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}"
        case _:
            return rg


def validar_cpf(cpf):
    cpf = "".join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    def calcular_digito(fator):
        soma = sum(int(d) * (fator - i) for i, d in enumerate(cpf[: fator - 1]))
        return (soma * 10 % 11) % 10

    return cpf[-2:] == f"{calcular_digito(10)}{calcular_digito(11)}"


def formatar_cpf():
    while True:
        cpf = input("CPF (apenas números): ").strip()
        if len(cpf) == 11 and cpf.isdigit() and validar_cpf(cpf):
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        elif cpf == "":
            return ""
        print("CPF inválido, digite novamente: ")


def formatar_data(data):
    return f"{data[:2]}/{data[2:4]}/{data[4:]}" if len(data) == 8 else data


def cartorio():
    cartorio = input("Cartório: ")
    if cartorio == "":
        return "desta Comarca de Brotas/SP"
    else:
        return cartorio


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


def unir_outorgante_e_conjuge(outorgante, conjuge):
    dados = {}

    # Copia todos os dados do outorgante normalmente
    dados.update(outorgante)

    # Copia os dados do cônjuge com sufixo _conjuge
    for chave, valor in conjuge.items():
        dados[f"{chave}_conjuge"] = valor
    return dados


# *** ENDEREÇO *** ============================================================


def buscar_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code != 200:
        raise Exception("⚠️ Erro ao acessar o ViaCEP")
    dados = resposta.json()
    if "erro" in dados:
        raise ValueError("⚠️ CEP não encontrado")
    return {
        "rua": dados.get("logradouro", "").title(),
        "bairro": dados.get("bairro", "").title(),
        "cidade": dados.get("localidade", ""),
        "estado": dados.get("uf", ""),
    }


def verifica_complemento():
    complemento = input("Complemento: ")
    return f"{complemento}, " if complemento else ""


def coletar_endereco_interativo():
    dados = {"nesta-na": "na"}  # Valor padrão

    if input("Deseja buscar o endereço pelo CEP? (S/N): ").lower().strip() == "s":
        dados.update(obter_dados_por_cep())
    else:
        dados.update(obter_dados_manual())

    dados["nesta-na"] = "nesta" if dados["cidade"].lower() == "brotas" else "na"
    return dados


def obter_dados_por_cep():
    dados = {}
    while True:
        cep = input("CEP (apenas números): ").strip()
        if len(cep) == 8 and cep.isdigit():
            try:
                endereco = buscar_endereco_por_cep(cep)
                dados.update(
                    {
                        "cep": f"{cep[:5]}-{cep[5:]}",
                        "rua": endereco["rua"],
                        "bairro": endereco["bairro"],
                        "cidade": formatar_nome(endereco["cidade"]),
                        "estado": endereco["estado"].upper(),
                        "numero": input("Número: ").strip(),
                        "complemento": verifica_complemento(),
                    }
                )
                return dados
            except Exception as e:
                print(f"Erro so buscar CEP: {e}")
                print("Preencha os dados manualmente.")
                return obter_dados_manual()
        print("CEP inválido.")


def obter_dados_manual():
    return {
        "rua": formatar_nome(input("Rua: ") or ""),
        "numero": input("Número: ").strip(),
        "bairro": formatar_nome(input("Bairro: ") or ""),
        "complemento": verifica_complemento(),
        "cidade": formatar_nome(input("Cidade: ") or ""),
        "estado": (input("Estado (sigla): ") or "").upper().strip(),
        "cep": formatar_cep(input("CEP (apenas números): ") or ""),
    }


def formatar_cep(cep):
    cep = "".join(filter(str.isdigit, cep))
    if len(cep) != 8:
        return "______________"
    return f"{cep[:5]}-{cep[5:]}"


# Interface Tkinter para escolher local do download
def escolher_local_salvamento(nome_sugestao="qualificacao.docx"):
    root = Tk()
    root.withdraw()  # Oculta a janela principal do tkinter
    root.attributes("-topmost", True)
    root.update()
    caminho = asksaveasfilename(
        defaultextension=".docx",
        filetypes=[("Documentos Word", "*.docx")],
        initialfile=nome_sugestao,
        title="Salvar como",
    )
    root.destroy()
    return caminho
