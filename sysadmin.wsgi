import site
import os
import sys
DIRS = ['/home/bossip/.virtualenvs/bauHaus/lib/python2.7/site-packages/']

for directory in DIRS:
    site.addsitedir(directory)
    sys.path.insert(0,directory)

root = os.path.join(os.path.dirname(__file__))

sys.path = ['/home/bossip/.virtualenvs/bauHaus/sysadmin/'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE']='sysadmin.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()