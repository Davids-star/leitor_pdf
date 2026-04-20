import os
from leitor import LeitorDocumento
from buscador import BuscadorTexto
from config import carregar_configuracoes

class ProcessadorArquivos:
    """Orquestrador que gerencia a leitura e busca em múltiplos arquivos."""

    def __init__(self, poppler_path=None, tesseract_path=None):
        self.leitor = LeitorDocumento(poppler_path, tesseract_path)
        self.buscador = BuscadorTexto()
        self.arquivos_disponiveis = None

    def _procurar_arquivos(self, base_path, extensoes):
        """Varre recursivamente uma pasta em busca de arquivos com as extensões permitidas."""
        arquivos_encontrados = []
        extensoes_limpas = [e.replace("*", "").lower() for e in extensoes]

        if not os.path.exists(base_path):
            return []

        for root, _, files in os.walk(base_path): #Irá olhar dentro das pastas ignorando as subpastas no meu BASE_PATH
            for arquivo in files:
                ext = os.path.splitext(arquivo)[1].lower()#Aqui ele olha o nome do arquivo e verifica o final dele(.pdf, .txt ...)
                if ext in extensoes_limpas:
                    arquivos_encontrados.append(os.path.join(root, arquivo))#Aqui ele junta o caminho da pasta com o nome do arquivo
        
        return arquivos_encontrados

    def configurar_busca_pc(self):

        """Varre as pastas configuradas em busca de arquivos válidos. .pdf, .txt, .docx, .xlsx"""

        config = carregar_configuracoes()
        print(f"🔍 Varrendo pastas: {', '.join(config['caminhos_busca'])}")
        
        todos_arquivos = []
        for caminho_base in config["caminhos_busca"]:
            arquivos = self._procurar_arquivos(caminho_base, config["extensoes"])
            todos_arquivos.extend(arquivos)
        
        self.arquivos_disponiveis = todos_arquivos

    def processar_tudo(self, termo="", tipo_busca="texto"):

        """Processa todos os arquivos encontrados de acordo com o tipo de busca."""

        if self.arquivos_disponiveis is None:
            self.configurar_busca_pc()

        encontrados = {}
        for caminho in self.arquivos_disponiveis:
            if not os.path.isfile(caminho):
                continue
                
            arquivo_nome = os.path.basename(caminho)
            parent_dir = os.path.basename(os.path.dirname(caminho))
            
            print(f"📄 Analisando: [{parent_dir}] {arquivo_nome}", end="\r")
            
            texto = ""
            if arquivo_nome.lower().endswith(".pdf"):
                texto = self.leitor.ler_pdf(caminho)
            elif arquivo_nome.lower().endswith(".txt"):
                texto = self.leitor.ler_txt(caminho)
            elif arquivo_nome.lower().endswith(".docx"):
                texto = self.leitor.ler_docx(caminho)
            elif arquivo_nome.lower().endswith((".xlsx", ".xls")):
                texto = self.leitor.ler_excel(caminho)
            else:
                continue
            
            res = []
            sucesso = False
            
            if tipo_busca == "cpf":
                res = self.buscador.buscar_cpf(texto)
                sucesso = bool(res)
            elif tipo_busca == "telefone":
                res = self.buscador.buscar_telefone(texto)
                sucesso = bool(res)
            elif tipo_busca == "stmb":
                res = self.buscador.buscar_stmb(texto)
                sucesso = bool(res)
            elif tipo_busca == "extrair_numero":
                res = self.buscador.buscar_numeros(texto)
                sucesso = bool(res)
            else:  # "texto"
                if self.buscador.contem_termo(texto, termo):
                    res = [termo]
                    sucesso = True

            if sucesso:
                print(f"✅ Encontrado em: {arquivo_nome}                     ")
                encontrados[caminho] = res
        
        print("\n✨ Busca concluída!                           ")
        return encontrados

    def buscar_em_lista_especifica(self, lista_nomes, termo):
        """Filtra arquivos pelo nome antes de realizar a busca de texto."""
        if self.arquivos_disponiveis is None:
            self.configurar_busca_pc()

        filtrados = [
            arq for arq in self.arquivos_disponiveis #pecorre todos os arquivos disponíveis 
            if any(n.lower() in os.path.basename(arq).lower() for n in lista_nomes) #retorna o arquivo se tiver o nome digitado
        ]   

        encontrados = {}
        for caminho in filtrados:
            print(f"🔍 Buscando em: {os.path.basename(caminho)}")
            texto = ""
            ext = caminho.lower()
            if ext.endswith(".pdf"): texto = self.leitor.ler_pdf(caminho)
            elif ext.endswith(".txt"): texto = self.leitor.ler_txt(caminho)
            elif ext.endswith(".docx"): texto = self.leitor.ler_docx(caminho)
            elif ext.endswith((".xlsx", ".xls")): texto = self.leitor.ler_excel(caminho)

            if self.buscador.contem_termo(texto, termo):
                print(f"  ✔ Encontrado!")
                encontrados[caminho] = [termo]
        
        return encontrados
