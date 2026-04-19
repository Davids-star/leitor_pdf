import os
import sys
import zipfile
import urllib.request
import shutil

def get_base_path():
    """Retorna o diretório base (onde está o script ou o .exe)"""
    if getattr(sys, 'frozen', False):
        # Se for um executável compilado pelo PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Se for rodado como script .py normal
        return os.path.dirname(os.path.abspath(__file__))

def baixar_e_extrair(url, pasta_destino):
    """Faz o download do ZIP e extrai na pasta informada"""
    try:
        base_dir = get_base_path()
        zip_path = os.path.join(base_dir, "temp_deps.zip")
        deps_dir = os.path.join(base_dir, pasta_destino)

        # 1. Verifica se a pasta já existe
        if os.path.exists(deps_dir):
            print(f"✅ Pasta '{pasta_destino}' já encontrada. Pulando download.")
            return True

        # 2. Download do arquivo com barra de progresso simples
        try:
            def report(block_num, block_size, total_size):
                if total_size > 0:
                    percent = min(100, int(block_num * block_size * 100 / total_size))
                    sys.stdout.write(f"\r📥 Baixando: {percent}% [{'#' * (percent // 5)}{'.' * (20 - percent // 5)}]")
                    sys.stdout.flush()

            urllib.request.urlretrieve(url, zip_path, reporthook=report)
            print("\n✅ Download finalizado!")
            
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"\n❌ Erro 404: O link do arquivo não foi encontrado. Verifique se o nome do arquivo e a versão do Release estão corretos.")
            else:
                print(f"\n❌ Erro de conexão: {e}")
            return False
        except Exception as e:
            print(f"\n❌ Erro durante o download: {e}")
            return False

        # 3. Extração
        print(f"📂 Extraindo arquivos em: {deps_dir}...")
        os.makedirs(deps_dir, exist_ok=True)
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(deps_dir)
        except Exception as e:
            print(f"❌ Erro ao extrair ZIP: {e}")
            return False

        # 4. Limpeza (deleta o zip temporário)
        os.remove(zip_path)
        print("✨ Configuração concluída com sucesso!")
        return True

    except Exception as e:
        print(f"⚠ Falha crítica no sistema de dependências: {e}")
        return False

def configurar_caminhos():
    """Retorna os caminhos configurados baseados na pasta dependencias"""
    base = get_base_path()
    deps_path = os.path.join(base, "dependencias")
    
    tesseract_exe = os.path.join(deps_path, "tesseract", "tesseract.exe")
    poppler_bin = os.path.join(deps_path, "poppler", "Library", "bin")
    
    return tesseract_exe, poppler_bin
