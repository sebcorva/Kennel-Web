@echo off
echo Compilando Tailwind CSS...
echo.

REM Descargar Tailwind CLI si no existe
if not exist "tailwindcss.exe" (
    echo Descargando Tailwind CLI...
    curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-windows-x64.exe
    ren tailwindcss-windows-x64.exe tailwindcss.exe
)

REM Compilar CSS
echo Compilando CSS...
tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --watch

echo.
echo Compilación completada!
pause 