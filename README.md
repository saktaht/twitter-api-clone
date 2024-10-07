docker compose up --build --detach

docker exec -it drf /bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

docker compose down --rmi all -v