import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from utils.utils import escolher_local_salvamento

from qualificacoes.solteiro import criar_qualificacao_solteiro, pergunta_dados_solteiro
from qualificacoes.casado_simples import (
    criar_qualificacao_casado_simples,
    pergunta_dados_casado_simples,
)
from qualificacoes.casado_completa import (
    criar_qualificacao_casado_completa,
    pergunta_dados_casado_completa,
)
from qualificacoes.casado_anuindo import (
    criar_qualificacao_casado_anuente,
    pergunta_dados_casado_anuente,
)
from qualificacoes.divorciado import (
    criar_qualificacao_divorciado,
    pergunta_dados_divorciado,
)
from qualificacoes.viuvo import criar_qualificacao_viuvo, pergunta_dados_viuvo


def main():
    while True:
        print("\n========= MENU DE QUALIFICAÇÃO =========")
        print("1. Solteiro")
        print("2. Casado - Simples")
        print("3. Casado - Completo")
        print("4. Casado - Anuente")
        print("5. Divorciado")
        print("6. Viúvo")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            dados = pergunta_dados_solteiro()
            caminho = escolher_local_salvamento(
                f"Qualificação_Solteiro - {dados['nome'].title().replace(' ', '_')}.docx"
            )
            if caminho:
                criar_qualificacao_solteiro(dados, caminho)

        elif opcao == "2":
            dados = pergunta_dados_casado_simples()
            caminho = escolher_local_salvamento(
                f"Qualificação_Casado_Simples - {dados['nome'].title().replace(' ', '_')}.docx"
            )
            if caminho:
                criar_qualificacao_casado_simples(dados, caminho)

        elif opcao == "3":
            dados = pergunta_dados_casado_completa()
            caminho = escolher_local_salvamento(
                f"Qualificação_Casado_Completo - {dados['nome'].title().replace(' ', '_')}.docx"
            )
            if caminho:
                criar_qualificacao_casado_completa(dados, caminho)
        
        elif opcao == "4":
            dados = pergunta_dados_casado_anuente()
            caminho = escolher_local_salvamento(
                f"Qualificação_Casado_Completo - {dados['nome'].title().replace(' ', '_')}.docx"
            )
            if caminho:
                criar_qualificacao_casado_anuente(dados, caminho)

        elif opcao == "5":
            dados = pergunta_dados_divorciado()
            caminho = escolher_local_salvamento(
                f"Qualificação_Divorciado - {dados['nome'].title().replace(' ', '_')}.docx"
            )
            if caminho:
                criar_qualificacao_divorciado(dados, caminho)

        elif opcao == "6":
            dados = pergunta_dados_viuvo()
            caminho = escolher_local_salvamento(
                f"Qualificação_Viuvo - {dados['nome'].title().replace(' ', '_')}.docx"
            )
            if caminho:
                criar_qualificacao_viuvo(dados, caminho)

        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("\n\n⚠️  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
