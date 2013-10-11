"""Production settings and globals."""


from os import environ

from common import *
SERVER_EMAIL = EMAIL_HOST_USER
SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)
ALLOWED_HOSTS = ['.herokuapp.com']
SEND_SMS = True
