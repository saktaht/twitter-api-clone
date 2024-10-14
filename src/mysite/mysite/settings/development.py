# dev環境でのみ使う設定を記載していきます
from .base import * # noqa: F401

DEBUG = False
ROOT_URLCONF = "mysite.urls.base"
#GCPのstrageとかをこの下に書くかもしれない