# 🔍 Buscador Global de Documentos (OCR)

Este é um projeto robusto em Python projetado para buscar informações dentro de múltiplos tipos de arquivos (`.pdf`, `.docx`, `.xlsx`, `.txt`) de forma recursiva em pastas do sistema.

O grande diferencial deste projeto é a integração com **OCR (Optical Character Recognition)**, permitindo que ele "leia" PDFs que são apenas imagens (fotos de documentos), além de arquivos de texto nativos.

---

## 🚀 Funcionalidades Principal

- **Busca de Texto Integral**: Encontre qualquer palavra ou frase em centenas de arquivos simultaneamente.
- **Extração de Dados Inteligente**:
  - 💳 **CPFs**: Localiza padrões de CPF formatados ou apenas números.
  - 📞 **Telefones**: Identifica números de telefone nos documentos.
  - 📑 **STMBs**: Busca por códigos de identificação específicos.
  - 🔢 **Extração Numérica**: Lista todos os números encontrados em um documento.
- **Filtro Avançado**: Permite filtrar a busca por nomes específicos de arquivos.
- **Portabilidade**: O sistema baixa e configura automaticamente as dependências do Tesseract e Poppler caso não existam.
- **Suporte Multi-formato**: Funciona com PDF, Word, Excel e Texto simples.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **OCR**: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- **Processamento de PDF**: [PyMuPDF (fitz)](https://github.com/pymupdf/PyMuPDF) e [PyPDF2](https://pypi.org/project/PyPDF2/)
- **Documentos Office**: `python-docx` e `openpyxl`
- **Imagens**: `Pillow`

---

## ⚙️ Como Funciona?

O processamento segue um fluxo inteligente:
1. **Varredura**: O programa percorre todas as pastas configuradas no `configuracoes.json`.
2. **Leitura**:
   - Se for um PDF de texto, ele extrai o texto diretamente.
   - Se for um PDF de imagem, ele converte as páginas para imagem e usa o Tesseract OCR para "ler" o que está escrito.
3. **Busca**: Utiliza expressões regulares (Regex) para encontrar padrões como CPFs e telefones de forma precisa.
4. **Configuração**: Você pode adicionar ou remover pastas de busca diretamente pelo menu do programa.

---

## 📥 Instalação

### Pré-requisitos
- Ter o Python instalado.
- O programa tentará baixar o Tesseract e Poppler automaticamente na primeira execução, mas certifique-se de ter conexão com a internet.

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/Davids-star/leitor_pdf.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Como Usar

### Via Python
Basta rodar o arquivo principal:
```bash
python main.py
```

### Menu de Opções
Ao iniciar, você verá o menu:
1. **Buscar Termo**: Digite uma palavra e veja em quais arquivos ela aparece.
2. **Buscar CPFs/Telefones**: O programa listará todos os dados encontrados.
3. **Configurar Pastas**: Adicione os caminhos (ex: `C:\MeusDocumentos`) onde o programa deve procurar.

---

## 🔨 Gerando o Executável (.exe)

Se você quiser transformar o projeto em um programa para Windows que roda sem precisar de Python instalado:

1. Execute o arquivo `compilar.bat`.
2. O script irá configurar o ambiente, instalar as bibliotecas necessárias e gerar o arquivo na pasta `dist/`.

---

## 💡 Ativando o Buscador via CMD

Se você quiser abrir o buscador rapidamente apenas digitando um comando no seu terminal (CMD/PowerShell), você pode criar um arquivo de atalho `.bat`.

### Como criar o atalho:
1. Abra o **Bloco de Notas**.
2. Cole o código abaixo:
   ```batch
   @echo off
   :: Mude o caminho abaixo para onde o seu projeto está salvo
   start "" "C:\CAMINHO_PARA_O_PROJETO\dist\Buscador_Documentos.exe"
   ```
3. Salve o arquivo com o nome **`busca.bat`** (ou o nome que preferir).
4. **Dica de Ouro**: Se você salvar esse arquivo `.bat` dentro da pasta `C:\Windows`, você poderá simplesmente abrir o CMD em qualquer lugar e digitar `busca` para iniciar o programa instantaneamente!

---

## 📄 Licença

Este projeto é de uso livre para estudos e melhorias. Sinta-se à vontade para contribuir!

---
*Desenvolvido por Davids-star*
