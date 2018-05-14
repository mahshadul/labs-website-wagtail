from .base import *

DEBUG = False

SECRET_KEY = get_environment_variable('SECRET_KEY')
ALLOWED_HOSTS = ['excellalabs.com']
