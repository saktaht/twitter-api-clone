#### settings.pyそれぞれの役割
・dev        ← 開発用

・local      ← swagger uiを見れる

・production ← 本番環境


#### .envファイルでlocalやproduction, devを切り替える
DJANGO_SETTINGS_MODULE==project.settings.の後ろを変える

#### dockerの起動コマンドまとめ
docker compose up --build --detach

docker exec -it drf /bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

docker compose down --rmi all -v

#### JET認証のパスワードを作成

python manage.py createsuperuser

ユーザー名: admin

メールアドレス: fjla32@gmail.com

パスワード: fafa86487

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "fafa86487"}' \
  http://localhost:8000/api/token/

これはurlを作ってないからできなかった

curl \
  -X GET \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  http://localhost:8000/api/