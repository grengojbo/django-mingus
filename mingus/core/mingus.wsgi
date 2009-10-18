import os
import sys
 
# activate virtualenv
activate_this = os.path.expanduser("~/daonb/.virtualenv/libby/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))
 
# tell django where our settings module is
sys.path.insert(0, os.path.expanduser("~/daonb/sites/libby/release/current"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mingus.settings'
 
# run django
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
