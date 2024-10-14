# dev環境でのみ使う設定を記載していきます
from .base import *

DEBUG = False
ROOT_URLCONF = "mysite.urls.base"
#GCPのstrageとかをこの下に書くかもしれない