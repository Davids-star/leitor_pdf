import json
import os
from pathlib import Path

SETTINGS_FILE = "configuracoes.json"

#           Configurações do sistema de buscar_pdf

def obter_pastas_padrao():
    """
    Detecta automaticamente as pastas do usuário atual (Documentos, Downloads, Desktop).
    Retorna uma lista de caminhos (Path objects) que realmente existem.
    """
    home = Path.home()
    
    # Mapeamento de nomes comuns (incluindo variações em português)

    mapa_pastas = {
        "Documents": ["Documents", "Documentos"],
        "Downloads": ["Downloads"],
        "Desktop": ["Desktop", "Área de Trabalho"]
    }
    
    pastas_validas = []

    #Processo de busca pelas pastas existente dentro da minha lista

    for _, variacoes in mapa_pastas.items():
        for nome in variacoes:
            caminho = home / nome
            if caminho.exists() and caminho.is_dir():
                pastas_validas.append(caminho)
                break # Para cada categoria, pega a primeira variação encontrada
                
    return pastas_validas

def carregar_configuracoes():
    """Carrega as preferências do arquivo JSON ou retorna valores padrão."""
    config_padrao = {
        "caminhos_busca": [str(p) for p in obter_pastas_padrao()],
        "extensoes": ["*.txt", "*.pdf", "*.docx", "*.xlsx", "*.xls"]
    }
    
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar configurações: {e}")
            
    return config_padrao

def salvar_configuracoes(config):
    """Salva as configurações atuais no arquivo JSON."""
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar configurações: {e}")

def configurar_caminhos_manualmente():
    """Permite ao usuário adicionar caminhos personalizados."""
    config = carregar_configuracoes()
    print("\n--- CONFIGURAÇÃO DE CAMINHOS ---")
    print("Caminhos atuais:")
    for i, p in enumerate(config["caminhos_busca"]):
        print(f"{i+1}. {p}")
        
    print("\nOpções:")
    print("1. Adicionar novo caminho")
    print("2. Limpar todos e adicionar novo")
    print("3. Manter atuais")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        novo_path = input("Digite o caminho completo da pasta: ").strip()
        if os.path.exists(novo_path):
            config["caminhos_busca"].append(novo_path)
            salvar_configuracoes(config)
            print("\n✅ Caminho adicionado com sucesso!")
            print("Nova lista de caminhos:")
            for p in config["caminhos_busca"]:
                print(f" - {p}")
        else:
            print("\n❌ Caminho inválido ou não encontrado. Verifique se digitou corretamente.")
    elif opcao == "2":
        novo_path = input("Digite o caminho completo da pasta: ").strip()
        if os.path.exists(novo_path):
            config["caminhos_busca"] = [novo_path]
            salvar_configuracoes(config)
            print("Configurações atualizadas!")
        else:
            print("Caminho inválido.")
    
    return config
