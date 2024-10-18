#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='root', email='ratroniii@gmail.com', phone='+996500162325', password='admin')"
python manage.py runserver 0.0.0.0:8000
