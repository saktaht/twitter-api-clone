from .base import * 

DEBUG = True

# REST_FRAMEWORKのdictにSwaggerの設定を追加するためにupdateを使用
REST_FRAMEWORK.update({"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}) # noqa: F405

INSTALLED_APPS += [ # noqa: F405
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