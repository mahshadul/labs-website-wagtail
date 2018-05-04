from .base import *

DEBUG = False

SECRET_KEY = get_environment_variable('SECRET_KEY')
ALLOWED_HOSTS = ['excellalabs.com']

#AWS_ACCESS_KEY_ID = get_environment_variable('AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = get_environment_variable('AWS_SECRET_ACCESS_KEY')
#AWS_STORAGE_BUCKET_NAME = get_environment_variable('AWS_STORAGE_BUCKET_NAME')
