from .base import *  # noqa: F401
import io
import os
import environ
import google.auth
from google.cloud import secretmanager


env = environ.Env(
    DEBUG=(bool, False),
)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/secrets/service-account.json/secrets/service-account.json"

    
try:
    _, os.environ["GOOGLE_CLOUD_PROJECT"] = google.auth.default()
except google.auth.exceptions.DefaultCredentialsError as e:
    print(f"DefaultCredentialsError: {e}")
    raise ValueError("認証できませんでした")

if os.environ.get("GOOGLE_CLOUD_PROJECT", None):
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    settings_name ='DJANGO_SETTINGS'   
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")
    env.read_env(io.StringIO(payload))

SECRET_KEY = env("SECRET_KEY")
DEBUG = False

DATABASES = {"default": env.db()}
    
GS_BUCKET_NAME = env("GS_BUCKET_NAME")
GS_QUERYSTRING_AUTH = False
STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
}
GS_DEFAULT_ACL = "publicRead"
ALLOWED_HOSTS = [env("ALLOWED_HOSTS")]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

APPEND_SLASH = False
SECURE_SSL_REDIRECT = False

ROOT_URLCONF = "mysite.urls.base"