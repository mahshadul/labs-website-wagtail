from .base import *

DEBUG = False

SECRET_KEY = get_environment_variable('SECRET_KEY')
ALLOWED_HOSTS = ['excellalabs.com']

MEDIA_URL = 'https://{}/'.format(AWS_S3_CUSTOM_DOMAIN)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
