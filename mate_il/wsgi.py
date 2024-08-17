"""
WSGI config for mate_il project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

path = '/app'
if path not in sys.path:
    sys.path.append(path)
    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mate_il.settings")

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'staticfiles'))
