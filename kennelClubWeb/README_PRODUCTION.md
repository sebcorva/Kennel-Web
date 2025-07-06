# Guía de Despliegue a Producción - Kennel Club Web

## Configuración para cPanel

### 1. Preparación del Proyecto

Antes de subir a producción, asegúrate de:

- [ ] Ejecutar `python manage.py collectstatic --settings=kennelClubWeb.settings_production`
- [ ] Ejecutar `python manage.py migrate --settings=kennelClubWeb.settings_production`
- [ ] Generar una nueva SECRET_KEY para producción
- [ ] Configurar la base de datos MySQL en cPanel

### 2. Archivos a Subir

Sube todos los archivos del proyecto a tu directorio público en cPanel, incluyendo:

- `index.py` (archivo principal)
- `.htaccess` (configuración del servidor)
- `settings_production.py` (configuración de producción)
- `env_production.py` (variables de entorno)
- `requirements.txt` (dependencias)
- Carpeta `core/` (aplicación principal)
- Carpeta `staticfiles/` (archivos estáticos recolectados)
- Carpeta `media/` (archivos subidos por usuarios)
- Carpeta `templates/` (plantillas HTML)

### 3. Configuración en cPanel

#### Base de Datos MySQL
1. Ve a "Bases de datos MySQL" en cPanel
2. Crea una nueva base de datos
3. Crea un usuario y asígnale permisos
4. Actualiza `env_production.py` con los datos de conexión

#### Variables de Entorno
Edita `env_production.py` y actualiza:

```python
os.environ['DB_NAME'] = 'tu_nombre_de_base_de_datos'
os.environ['DB_USER'] = 'tu_usuario_de_base_de_datos'
os.environ['DB_PASSWORD'] = 'tu_password_de_base_de_datos'
os.environ['SECRET_KEY'] = 'tu-clave-secreta-muy-segura'
```

#### Dominio
Edita `settings_production.py` y actualiza `ALLOWED_HOSTS`:

```python
ALLOWED_HOSTS = [
    'tu-dominio.com',
    'www.tu-dominio.com',
]
```

### 4. Instalación de Dependencias

En cPanel, ve a "Python Apps" y:

1. Crea una nueva aplicación Python
2. Selecciona la versión de Python (3.8+)
3. Instala las dependencias desde `requirements.txt`

### 5. Configuración del Servidor

El archivo `.htaccess` ya está configurado para:
- Redirigir peticiones a Django
- Servir archivos estáticos
- Configurar caché y compresión
- Configurar seguridad

### 6. Verificación

Después del despliegue, verifica:

- [ ] El sitio web carga correctamente
- [ ] Los archivos estáticos se sirven
- [ ] La base de datos funciona
- [ ] El panel de administración es accesible
- [ ] Las imágenes se suben correctamente

### 7. Comandos Útiles

```bash
# Recolectar archivos estáticos
python manage.py collectstatic --settings=kennelClubWeb.settings_production

# Ejecutar migraciones
python manage.py migrate --settings=kennelClubWeb.settings_production

# Crear superusuario
python manage.py createsuperuser --settings=kennelClubWeb.settings_production

# Verificar configuración
python manage.py check --settings=kennelClubWeb.settings_production
```

### 8. Solución de Problemas

#### Error 500
- Verifica los logs de error en cPanel
- Asegúrate de que todas las dependencias estén instaladas
- Verifica la configuración de la base de datos

#### Archivos estáticos no cargan
- Ejecuta `collectstatic` nuevamente
- Verifica que la carpeta `staticfiles/` esté en el directorio correcto
- Revisa la configuración de `STATIC_ROOT` en settings

#### Base de datos no conecta
- Verifica las credenciales en `env_production.py`
- Asegúrate de que el usuario tenga permisos en la base de datos
- Verifica que el host sea `localhost`

### 9. Seguridad

- [ ] Cambia la SECRET_KEY por defecto
- [ ] Configura HTTPS si es posible
- [ ] Mantén Django actualizado
- [ ] Revisa regularmente los logs de error
- [ ] Haz respaldos regulares de la base de datos

### 10. Mantenimiento

- Actualiza regularmente las dependencias
- Monitorea el uso de recursos
- Haz respaldos automáticos de la base de datos
- Revisa los logs de error periódicamente 