@echo off
echo Compilando Tailwind CSS para PRODUCCIÓN...
echo.

REM Descargar Tailwind CLI si no existe
if not exist "tailwindcss.exe" (
    echo Descargando Tailwind CLI...
    curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-windows-x64.exe
    ren tailwindcss-windows-x64.exe tailwindcss.exe
)

REM Compilar CSS optimizado para producción
echo Compilando CSS optimizado...
tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --minify

echo.
echo CSS optimizado para producción generado!
echo Archivo: static/css/output.css
pause 