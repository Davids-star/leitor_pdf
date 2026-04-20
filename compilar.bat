@echo off
echo ==========================================
echo   🔨 CONSTRUINDO EXECUTAVEL PORTATIL
echo ==========================================
echo.

:: 1. Ativa o ambiente virtual e garante que as libs estao instaladas
echo [1/3] Verificando bibliotecas...
call .\venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pip install pyinstaller

:: 2. Limpa pastas antigas
echo [2/3] Limpando arquivos temporarios...
if exist build rd /s /q build
if exist dist rd /s /q dist

:: 3. Gera o executavel
:: --onefile: cria um unico .exe
:: --clean: limpa cache antes de build
echo [3/3] Gerando Buscador_Documentos.exe...
pyinstaller --onefile --clean --name "Buscador_Documentos" main.py

echo.
echo ==========================================
echo ✅ CONCLUIDO! O executavel esta na pasta 'dist'
echo ==========================================
pause
