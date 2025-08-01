"""
Configuración de variables de entorno para producción
Ajusta estos valores según tu configuración de cPanel
"""

import os

# Configuración de la base de datos MySQL en cPanel
os.environ['DB_NAME'] = 'kennelcl_kennel_db'
os.environ['DB_USER'] = 'kennelcl_kennel_production'
os.environ['DB_PASSWORD'] = 'qxF3l4CMp=nx*8xpd!*'
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '3306'

# Clave secreta de Django (genera una nueva para producción)
os.environ['SECRET_KEY'] = 'i4ldq)nscz=aq_c-zs(y5a#=7uj62)=g^pj*gyf946q%xn&r6q'

# Configuración de debug
os.environ['DEBUG'] = 'False'

# Configuración de dominio
os.environ['ALLOWED_HOSTS'] = 'kennelclubdechile.cl,www.kennelclubdechile.cl'

# Configuración de correo electrónico para producción
os.environ['EMAIL_HOST'] = 'mail.kennelclubdechile.cl'
os.environ['EMAIL_PORT'] = '465'
os.environ['EMAIL_USE_SSL'] = 'True'
os.environ['EMAIL_USE_TLS'] = 'False'
os.environ['EMAIL_HOST_USER'] = 'prueba@kennelclubdechile.cl'
os.environ['EMAIL_HOST_PASSWORD'] = ',QIV%[Z;iyp&w6NY' 