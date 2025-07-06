@echo off
echo ========================================
echo COLECTANDO ARCHIVOS ESTATICOS
echo ========================================

echo.
echo 1. Configurando Django...
set DJANGO_SETTINGS_MODULE=kennelClubWeb.settings_production

echo.
echo 2. Recolectando archivos estáticos...
python manage.py collectstatic --noinput

echo.
echo 3. Verificando que las carpetas existen...
if not exist "staticfiles\uploads" mkdir "staticfiles\uploads"
if not exist "staticfiles\uploads\noticias" mkdir "staticfiles\uploads\noticias"
if not exist "staticfiles\uploads\jueces" mkdir "staticfiles\uploads\jueces"
if not exist "staticfiles\uploads\clubes" mkdir "staticfiles\uploads\clubes"
if not exist "staticfiles\uploads\historia_razas" mkdir "staticfiles\uploads\historia_razas"
if not exist "staticfiles\uploads\tramites" mkdir "staticfiles\uploads\tramites"
if not exist "staticfiles\uploads\curriculums" mkdir "staticfiles\uploads\curriculums"
if not exist "staticfiles\uploads\rankings" mkdir "staticfiles\uploads\rankings"
if not exist "staticfiles\uploads\reglamentos" mkdir "staticfiles\uploads\reglamentos"

echo.
echo ========================================
echo ¡ARCHIVOS ESTATICOS COLECTADOS!
echo ========================================
echo.
echo Las imágenes ahora deberían verse correctamente.
echo Si no se ven, recarga la página o limpia la caché del navegador.
echo.
pause 