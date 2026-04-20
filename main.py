import os
import sys

from processador import ProcessadorArquivos
from setup_dependencies import baixar_e_extrair, configurar_caminhos
from config import carregar_configuracoes, configurar_caminhos_manualmente

# --- CONFIGURAÇÃO DE DEPENDÊNCIAS ---
# Garante que as dependências de sistema (Tesseract/Poppler) existam
URL_DEPENDENCIAS = "https://github.com/Davids-star/leitor_pdf/releases/download/v1.0/zip.zip"
baixar_e_extrair(URL_DEPENDENCIAS, "dependencias")
TESSERACT_PATH, POPPLER_PATH = configurar_caminhos()

def mostrar_menu():
    print("\n" + "="*45)
    print("      🔍 BUSCADOR GLOBAL DE DOCUMENTOS")
    print("="*45)
    print(" 1. Buscar Termo (Texto Completo)")
    print(" 2. Buscar CPFs")
    print(" 3. Buscar Telefones")
    print(" 4. Buscar STMBs")
    print(" 5. Extrair Todos os Números")
    print(" 6. Filtrar por Nome de Arquivo + Termo")
    print(" 7. Configurar Pastas de Busca")
    print(" 0. Sair")
    print("-" * 45)
    return input(" Escolha uma opção: ")

def main():
    app = ProcessadorArquivos(poppler_path=POPPLER_PATH, tesseract_path=TESSERACT_PATH)

    while True:
        opcao = mostrar_menu()

        if opcao == "0":
            print("\nEncerrando... Até logo!")
            break
        
        elif opcao in ["1", "6"]:
            termo = input("\n🔎 Digite o termo que deseja encontrar: ")
            
            if opcao == "1":
                resultados = app.processar_tudo(termo)
            else:
                nomes = input("📝 Digite partes do nome dos arquivos (separadas por vírgula): ").split(",")
                nomes = [n.strip() for n in nomes]
                resultados = app.buscar_em_lista_especifica(nomes, termo)

            print(f"\n📂 Resultados encontrados para '{termo}':")
            for i, (caminho, _) in enumerate(resultados.items()):
                print(f" {i+1}. {os.path.basename(caminho)} -> {os.path.dirname(caminho)}")

        elif opcao == "2":
            resultados = app.processar_tudo("", tipo_busca="cpf")
            for arq, cpfs in resultados.items():
                print(f"\n📄 {os.path.basename(arq)}: {', '.join(cpfs)} -> {os.path.dirname(arq)}")

        elif opcao == "3":
            resultados = app.processar_tudo("", tipo_busca="telefone")
            for arq, tels in resultados.items():
                print(f"\n📄 {os.path.basename(arq)}: {', '.join(tels)} -> {os.path.dirname(arq)}")

        elif opcao == "4":
            resultados = app.processar_tudo("", tipo_busca="stmb")
            for arq, stmbs in resultados.items():
                print(f"\n📄 {os.path.basename(arq)}: {', '.join(stmbs)} -> {os.path.dirname(arq)}")

        elif opcao == "5":
            resultados = app.processar_tudo("", tipo_busca="extrair_numero")
            for arq, nums in resultados.items():
                print(f"📄 {os.path.basename(arq)} ({len(nums)} números) -> {os.path.dirname(arq)}")

        elif opcao == "7":
            configurar_caminhos_manualmente()
            # Reseta arquivos para forçar nova varredura2
            app.arquivos_disponiveis = None
        
        else:
            print("\n❌ Opção inválida!")

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")
        input("Pressione ENTER para fechar...")