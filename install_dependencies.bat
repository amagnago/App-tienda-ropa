@echo off
REM Script de instalación para Windows
echo Instalando dependencias para la app de gestión de prendas...

REM Verificar si Python está instalado
where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python no está instalado.
    echo Por favor descarga Python desde:
    echo https://www.python.org/downloads/windows/
    echo Asegúrate de marcar "Add Python to PATH" durante la instalación.
    pause
    exit /b
)

REM Verificar pip
python -m pip --version > nul 2>&1
if %errorlevel% neq 0 (
    echo pip no está instalado.
    echo Instalando pip...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    del get-pip.py
)

REM Instalar dependencias
echo Instalando pandas y openpyxl...
python -m pip install pandas openpyxl

if %errorlevel% equ 0 (
    echo ¡Todo instalado correctamente!
    echo Ejecuta la app con: python app_tienda_ropa.py
) else (
    echo Error al instalar dependencias
)

pause