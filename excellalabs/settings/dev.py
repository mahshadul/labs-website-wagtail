from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['labs-website-wagtail.herokuapp.com']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8n)huzsw288jgey-i=r6_t5dbqu_6ip6z@=#3t@h*8x(j@n4*p'

# AWS access credentials
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

MEDIA_URL = 'https://{}/'.format(AWS_S3_CUSTOM_DOMAIN)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
