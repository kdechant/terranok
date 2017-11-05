"""
WSGI config for terranok project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/vhosts/terranok')
sys.path.append('/var/www/vhosts/terranok/venv/lib/python3.5/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "terranok.settings")

try:
    application = get_wsgi_application()
    print('WSGI without exception')
except Exception:
    print('handling WSGI exception')
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
