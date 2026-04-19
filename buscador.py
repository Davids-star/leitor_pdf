import re
import unicodedata
import difflib

class BuscadorTexto:
    """Classe responsável por normalizar textos e realizar buscas de padrões."""

    def normalizar(self, texto):
        """Remove acentos e converte para minúsculas."""
        if not texto:
            return ""
        return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("utf-8").lower()

    def contem_termo(self, texto, termo):
        """Verifica se o texto contém o termo ou palavras similares (80%+)."""
        texto_norm = self.normalizar(texto)
        termo_norm = self.normalizar(termo)
        
        if termo_norm in texto_norm:
            return True
        
        palavras_texto = texto_norm.split()
        palavras_busca = termo_norm.split()
        
        for p_busca in palavras_busca:
            encontrou_similar = False
            for p_texto in palavras_texto:
                similaridade = difflib.SequenceMatcher(None, p_busca, p_texto).ratio()
                if similaridade > 0.8:
                    encontrou_similar = True
                    break
            if not encontrou_similar:
                return False
        
        return True

    def buscar_cpf(self, texto):
        return re.findall(r"\d{3}\.\d{3}\.\d{3}-\d{2}", texto)

    def buscar_telefone(self, texto):
        return re.findall(r"(?:\(?\d{2}\)?\s?)?(?:9\s?)?\d{4}[-\s]?\d{4}", texto)

    def buscar_stmb(self, texto):
        return re.findall(r"STMB[\s-]?\d+", texto, re.IGNORECASE)

    def buscar_numeros(self, texto):
        return re.findall(r"\d+", texto)
