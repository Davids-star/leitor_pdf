from main import ProcessadorArquivos

def pegar_termo():
    return input("Digite o que deseja buscar: ")
if __name__ == "__main__":
    # Inicializa sem parametros, o que ativará a busca no PC na primeira pesquisa
    app = ProcessadorArquivos()

    print("=== BUSCADOR GLOBAL DE DOCUMENTOS ===")
    
    termo = input("\nDigite o que deseja encontrar no seu PC: ")

    print("\nO QUE DESEJA BUSCAR?")
    print("1 - O termo digitado (Busca de texto)")
    print("2 - Buscar CPFs")
    print("3 - Buscar Telefones")
    print("4 - Buscar STMBs")
    print("5 - Extrair todos os números")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        resultados = app.processar_tudo(termo)
        print("\nArquivos encontrados com o termo:")
        for i, (arq, achados) in enumerate(resultados.items()):
            print(f"{i} - {arq}")

    elif opcao == "2":
        resultados = app.processar_tudo("", tipo_busca="cpf")
        print("\nCPFs Encontrados:")
        for arq, cpfs in resultados.items():
            print(f"\n📄 Arquivo: {arq}")
            for cpf in cpfs:
                print(f"  ✔ {cpf}")

    elif opcao == "3":
        resultados = app.processar_tudo("", tipo_busca="telefone")
        print("\nTelefones Encontrados:")
        for arq, telefones in resultados.items():
            print(f"\n📄 Arquivo: {arq}")
            for tel in telefones:
                print(f"  ✔ {tel}")

    elif opcao == "4":
        resultados = app.processar_tudo("", tipo_busca="stmb")
        print("\nSTMBs Encontrados:")
        for arq, stmbs in resultados.items():
            print(f"\n📄 Arquivo: {arq}")
            for stmb in stmbs:
                print(f"  ✔ {stmb}")

    elif opcao == "5":
        resultados = app.processar_tudo("", tipo_busca="extrair_numero")
        print("\nExtração de Números Concluída:")
        for arq, numeros in resultados.items():
            print(f" - {arq} ({len(numeros)} números encontrados)")
