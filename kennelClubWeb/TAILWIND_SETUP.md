# Configuración de Tailwind CSS

Este proyecto usa Tailwind CSS con el CLI standalone (sin Node.js).

## Archivos de configuración

- `tailwind.config.js` - Configuración de Tailwind
- `static/css/input.css` - Archivo de entrada con directivas de Tailwind
- `static/css/output.css` - CSS compilado (generado automáticamente)

## Cómo compilar CSS

### Opción 1: Compilación con watch (desarrollo)
```bash
# En Windows
build-css.bat

# O manualmente
tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --watch
```

### Opción 2: Compilación única (desarrollo)
```bash
# En Windows
build-css-once.bat

# O manualmente
tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css
```

### Opción 3: Compilación para producción (optimizada)
```bash
# En Windows
build-css-production.bat

# O manualmente
tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --minify
```

## Ventajas de usar Tailwind CLI vs CDN

✅ **Mejor rendimiento** - CSS optimizado y más pequeño
✅ **Sin dependencia de internet** - Funciona offline
✅ **Personalizable** - Puedes modificar colores, espaciados, etc.
✅ **Solo incluye clases usadas** - CSS más eficiente
✅ **No requiere Node.js** - Más simple para proyectos Django

## Personalización

Para agregar estilos personalizados, edita:
- `tailwind.config.js` - Para configurar tema, colores, etc.
- `static/css/input.css` - Para agregar CSS personalizado

## Comandos útiles

```bash
# Ver ayuda
tailwindcss.exe --help

# Compilar con minificación
tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --minify

# Ver qué archivos está escaneando
tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --content ./templates/**/*.html

## Despliegue en Producción

### Preparación completa para producción
```bash
# Script automático (recomendado)
deploy-production.bat

# O manualmente:
# 1. Compilar CSS optimizado
tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --minify

# 2. Recolectar archivos estáticos
python manage.py collectstatic --noinput --settings=kennelClubWeb.settings_production

# 3. Aplicar migraciones
python manage.py migrate --settings=kennelClubWeb.settings_production

# 4. Verificar configuración
python manage.py check --deploy --settings=kennelClubWeb.settings_production
```

### Configuración de producción
- El proyecto usa `settings_production.py` para producción
- WhiteNoise está configurado para servir archivos estáticos
- Los archivos estáticos se recolectan en la carpeta `staticfiles/`

### Archivos importantes para producción
- `static/css/output.css` - CSS optimizado y minificado
- `staticfiles/` - Archivos estáticos recolectados
- `passenger_wsgi.py` - Configuración para servidores web

## Seguridad en Producción

### Problemas de seguridad solucionados:

1. **CKEditor 4 → CKEditor 5**
   ```bash
   # Migrar a CKEditor 5 (más seguro)
   migrate-ckeditor.bat
   ```

2. **SSL/HTTPS configurado**
   - `SECURE_SSL_REDIRECT = True`
   - `SECURE_PROXY_SSL_HEADER` configurado
   - Cookies seguras habilitadas

3. **Headers de seguridad**
   - HSTS habilitado
   - XSS protection
   - Content type sniffing deshabilitado
   - Clickjacking protection

### Verificar seguridad:
```bash
python manage.py check --deploy --settings=kennelClubWeb.settings_production
``` 