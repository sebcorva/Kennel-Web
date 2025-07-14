@echo off
echo Compilando Tailwind CSS v3...
echo.

REM Descargar Tailwind CLI v3 si no existe
if not exist "tailwindcss-v3.exe" (
    echo Descargando Tailwind CLI v3...
    curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/download/v3.4.1/tailwindcss-windows-x64.exe
    ren tailwindcss-windows-x64.exe tailwindcss-v3.exe
)

REM Compilar CSS
echo Compilando CSS...
tailwindcss-v3.exe -i ./static/css/input.css -o ./static/css/output.css

echo.
echo Compilación completada!
pause 