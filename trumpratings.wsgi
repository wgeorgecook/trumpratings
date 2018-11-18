import sys
import logging
python_home = '/var/www/trumpratings/python3_env'
activate_this = python_home + '/bin/activate_this.py'
exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/trumpratings")

from trumpratings import app as application
