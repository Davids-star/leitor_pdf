import os

def procurar_arquivos(base_path, pastas, extensoes):
    arquivos_encontrados = []

    # Se base_path for um objeto Path (devido à transição), convertemos para string
    if not isinstance(base_path, str):
        base_path = str(base_path)

    # Normaliza as extensões procuradas (remove o '*' se o usuário passou)
    extensoes_limpas = [e.replace("*", "").lower() for e in extensoes]

    for pasta in pastas:
        caminho_pasta = os.path.join(base_path, pasta)
        
        if os.path.exists(caminho_pasta):
            print(f"Buscando em: {caminho_pasta}")
            for root, dirs, files in os.walk(caminho_pasta):
                for arquivo in files:
                    # Verifica se a extensão do arquivo está na lista de extensoes
                    # Nota: o usuário passou "*.pdf", então removemos o "*" se necessário
                    ext = os.path.splitext(arquivo)[1].lower()
                    
                    
                    if ext in extensoes_limpas:
                        caminho_completo = os.path.join(root, arquivo)
                        arquivos_encontrados.append(caminho_completo)
                        print("Arquivo válido:", caminho_completo)
                        
    return arquivos_encontrados
def buscar(termo):
    print(f"Buscando por: {termo}")
    return ["resultado1", "resultado2"]
