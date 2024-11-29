from .base import *
import os
import environ
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
env_path = os.path.join(BASE_DIR, "../../../.env")
# .env ファイルから環境変数を読み込むメソッド
environ.Env.read_env(env_path)
SECRET_KEY=env("SECRET_KEY")

ALLOWED_HOSTS = ["*"]
DEBUG = True

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
    )
}

# REST_FRAMEWORKのdictにSwaggerの設定を追加するためにupdateを使用
REST_FRAMEWORK.update(  # noqa: F405
    {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}
)  # noqa: F405

INSTALLED_APPS += [  # noqa: F405
    "drf_spectacular",
]

SPECTACULAR_SETTINGS = {
    "TITLE": "twitter-clone",
    "DESCRIPTION": "twitterの簡単な機能をapiで作った",
    "VERSION": "1.0.0",
}

# 後述するurls.pyをlocal用・dev用に分ける際にlocal用を使用
ROOT_URLCONF = "mysite.urls.local"

# Djangoのメールの設定
EMAIL_HOST = "mail"
EMAIL_HOST_USER = "fafa"
EMAIL_HOST_PASSWORD = "fafa86487"
# SMTPの1025番ポートを指定
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
