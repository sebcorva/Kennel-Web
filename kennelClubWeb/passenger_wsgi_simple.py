#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'kennelClubWeb.settings_production'

# Import Django and set it up
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 