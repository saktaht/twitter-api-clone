#!/bin/bash

# エラーが発生した場合にスクリプトを停止
set -e

# マイグレーションの実行
echo "Running migrations..."
python manage.py migrate --noinput

# サーバーの起動
echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:8080 mysite.wsgi:application
