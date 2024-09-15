#!/bin/sh

echo "Checking for src/.env file"
sleep 2
if [ -e .env ]; then
    echo "src/.env file already exists"
else
    cp .env.example .env
    echo "Created a default .env file"
fi
sleep 2

python manage.py migrate
python manage.py collectstatic --noinput
