from .base import *  # noqa: F401
import io
import os
import environ
import google.auth
from google.cloud import secretmanager
from urllib.parse import urlparse


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
STATIC_URL = "static/"
# STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        # "BUCKET_NAME": GS_BUCKET_NAME
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

# CORS設定
INSTALLED_APPS += [ # noqa: F405
    "corsheaders",
]

MIDDLEWARE += [ # noqa: F405
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOW_ALL_ORIGINAS = False
# ALLOWED_URL_NAME = env("ALLOWED_HOSTS")
# CLOUD_URL = f"https://{ALLOWED_URL_NAME}"
CLOUD_URL = env('CLOUD_URL', default=None)
CORS_ALLOWED_ORIGINS = [
    CLOUD_URL,
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "OPTIONS",
]

# CSRF設定
if CLOUD_URL:
    # Cloud Runでアプリが動作する許可されたURLがカンマ区切りで設定
    CSRF_TRUSTED_ORIGINS = env("CLOUDRUN_SERVICE_URLS").split(",")
    # urlparse(url).netlocでhttps部分を省き、有効なURLだけ許可する
    ALLOWED_HOSTS = [urlparse(url).netloc for url in CSRF_TRUSTED_ORIGINS]
    # HTTPリクエストをHTTPSにリダイレクト
    SECURE_SSL_REDIRECT = True
    # リクエストがCloud Runを通過する場合、HTTPSで通信しているかどうかをDjangoが検知するためのヘッダー情報を指定
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False

ROOT_URLCONF = "mysite.urls.base"