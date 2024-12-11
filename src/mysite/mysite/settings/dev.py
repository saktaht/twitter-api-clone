from .base import *  # noqa: F401
import os
import environ
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent 
env = environ.Env()
env_path = os.path.join(BASE_DIR, "../../../.env")
# .env ファイルから環境変数を読み込むメソッド
environ.Env.read_env(env_path)
SECRET_KEY=env("SECRET_KEY")

ALLOWED_HOSTS = ["*"]
DEBUG = True
ROOT_URLCONF = "mysite.urls.base"
STATIC_URL = "static/"


DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
    )
}

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] += [
    "rest_framework.renderers.BrowsableAPIRenderer",
]