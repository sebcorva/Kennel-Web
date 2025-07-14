@echo off
echo ========================================
echo PREPARANDO PROYECTO PARA PRODUCCIÓN
echo ========================================
echo.

REM 1. Compilar CSS optimizado
echo [1/4] Compilando CSS optimizado...
call build-css-production.bat

REM 2. Recolectar archivos estáticos
echo.
echo [2/4] Recolectando archivos estáticos...
python manage.py collectstatic --noinput --settings=kennelClubWeb.settings_production

REM 3. Hacer migraciones
echo.
echo [3/4] Aplicando migraciones...
python manage.py migrate --settings=kennelClubWeb.settings_production

REM 4. Verificar configuración
echo.
echo [4/4] Verificando configuración de producción...
python manage.py check --deploy --settings=kennelClubWeb.settings_production

echo.
echo ========================================
echo ¡PROYECTO LISTO PARA PRODUCCIÓN!
echo ========================================
echo.
echo Archivos generados:
echo - static/css/output.css (CSS optimizado)
echo - staticfiles/ (archivos estáticos recolectados)
echo.
echo Para ejecutar en producción:
echo python manage.py runserver --settings=kennelClubWeb.settings_production
echo.
pause 