from .base import *  # noqa: F401
import io
import os
import environ
import google.auth
from pathlib import Path
from google.cloud import secretmanager
from urllib.parse import urlparse


BASE_DIR = Path(__file__).resolve().parent.parent 
env = environ.Env(
    DEBUG=(bool, False),
)
# collectstaticするためにローカルでもjsonを得られるようにしておく
# base_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(base_dir, "Twitter Clone IAM Project (1).json")
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']=file_path

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

# GCSの設定
GS_BUCKET_NAME = env("GS_BUCKET_NAME")
GS_QUERYSTRING_AUTH = False
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
}
GS_DEFAULT_ACL = None

# Logging
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

# CORS設定
INSTALLED_APPS += [ # noqa: F405
    "corsheaders",
]

MIDDLEWARE += [ # noqa: F405
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOW_ALL_ORIGINAS = False
CORS = env("CLOUD_URL")
CORS_ALLOWED_ORIGINS = [
    CORS,
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "OPTIONS",
]

# CSRF設定
# Cloud Runでアプリが動作する許可されたURLがカンマ区切りで設定
# CSRF_TRUSTED_ORIGINS = env("CLOUD_URL").split(",")
# # urlparse(url).netlocでhttps部分を省き、有効なURLだけ許可する
# ALLOWED_HOSTS = [urlparse(url).netloc for url in CSRF_TRUSTED_ORIGINS]
ALLOWED_HOSTS = [env('ALLOWED_HOST', default=None)]
# HTTPリクエストをHTTPSにリダイレクト
SECURE_SSL_REDIRECT = True
# リクエストがCloud Runを通過する場合、HTTPSで通信しているかどうかをDjangoが検知するためのヘッダー情報を指定
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False

ROOT_URLCONF = "mysite.urls.base"