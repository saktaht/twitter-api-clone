from .base import *  # noqa: F401
import io
import os
import environ
import google.auth
from google.cloud import secretmanager

# localの.envファイルはdocker image内だとうまく起動できないからsecret managerを使うしかない
# secret managerの環境変数の持ってきかたを調べる
# BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False),
)

try:
    _, os.environ["GOOGLE_CLOUD_PROJECT"] = google.auth.default()
except google.auth.exceptions.DefaultCredentialsError:
    print('error')

if os.environ.get("GOOGLE_CLOUD_PROJECT", None):
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
    
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")
    env.read_env(io.StringIO(payload))
    
SECRET_KEY = env("SECRET_KEY")
DEBUG = False

DATABASES = {"default": env.db()}
    
GS_BUCKET_NAME = env("GS_BUCKET_NAME")
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
}
GS_DEFAULT_ACL = "publicRead"
SECURE_SSL_REDIRECT = True

ROOT_URLCONF = "mysite.urls.base"