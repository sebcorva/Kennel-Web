# Configuración de Cron Job para Collectstatic

## ¿Qué hace este cron job?

Ejecuta automáticamente `python manage.py collectstatic` para que las imágenes subidas se vean inmediatamente sin necesidad de ejecutar el comando manualmente.

## Configuración en cPanel

### 1. Acceder a Cron Jobs
1. Inicia sesión en cPanel
2. Busca "Cron Jobs" en el panel de control
3. Haz clic en "Cron Jobs"

### 2. Configurar el comando

**Frecuencia recomendada:**
- **Cada 5 minutos**: `*/5 * * * *`
- **Cada 10 minutos**: `*/10 * * * *`
- **Cada hora**: `0 * * * *`

**Comando a ejecutar:**
```bash
/home/TU_USUARIO/public_html/kennelClubWeb/cron-collectstatic.sh
```

### 3. Personalizar el script

**Editar el archivo `cron-collectstatic.sh`:**

1. Cambia `username` por tu nombre de usuario de cPanel
2. Verifica que la ruta sea correcta
3. Ajusta la ruta del entorno virtual si es diferente

### 4. Dar permisos de ejecución

En cPanel File Manager:
1. Ve a `kennelClubWeb/`
2. Haz clic derecho en `cron-collectstatic.sh`
3. Selecciona "Change Permissions"
4. Marca "Execute" para el propietario
5. Guarda los cambios

## Configuración de Frecuencia

### Opciones recomendadas:

**Para sitios con mucho contenido:**
```bash
*/5 * * * *  # Cada 5 minutos
```

**Para sitios con contenido moderado:**
```bash
*/10 * * * *  # Cada 10 minutos
```

**Para sitios con poco contenido:**
```bash
0 * * * *  # Cada hora
```

## Verificar que funciona

### 1. Revisar logs
El script crea un archivo `cron.log` en tu proyecto. Puedes verificar que se ejecuta revisando este archivo.

### 2. Probar manualmente
1. Sube una imagen desde el admin
2. Espera a que se ejecute el cron job
3. Verifica que la imagen se vea sin ejecutar collectstatic manualmente

### 3. Monitorear
En cPanel > Cron Jobs puedes ver:
- Última ejecución
- Estado del cron job
- Logs de errores

## Solución de problemas

### El cron job no se ejecuta
1. Verifica que el archivo tenga permisos de ejecución
2. Revisa que la ruta sea correcta
3. Verifica que el entorno virtual esté configurado

### Las imágenes no se ven
1. Revisa el archivo `cron.log` para errores
2. Verifica que las carpetas `staticfiles/uploads/` existan
3. Ejecuta `collectstatic` manualmente para probar

### Error de permisos
1. Verifica que el usuario de cPanel tenga permisos en la carpeta
2. Revisa que las carpetas `static/` y `staticfiles/` tengan permisos correctos

## Comandos útiles

### Ver logs del cron job
```bash
tail -f /home/TU_USUARIO/public_html/kennelClubWeb/cron.log
```

### Ejecutar manualmente para probar
```bash
/home/TU_USUARIO/public_html/kennelClubWeb/cron-collectstatic.sh
```

### Verificar permisos
```bash
ls -la /home/TU_USUARIO/public_html/kennelClubWeb/cron-collectstatic.sh
```

## Notas importantes

- El cron job usa `settings_production.py`
- Se ejecuta en segundo plano
- No afecta el rendimiento del sitio
- Mantiene un log de ejecuciones
- Limpia logs antiguos automáticamente 