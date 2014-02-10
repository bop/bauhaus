import site
import os
import sys
DIRS = ['/home/bop/.virtualenvs/bauhaus/lib/python2.7/site-packages/']

for directory in DIRS:
    site.addsitedir(directory)
    sys.path.insert(0,directory)

root = os.path.join(os.path.dirname(__file__))

sys.path = ['/home/bop/.virtualenvs/bauhaus/sysadmin'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE']='sysadmin.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()