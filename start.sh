#!/bin/bash

if [ -f .env ]; then
    echo ".env file found. Starting Docker Compose."
else
    echo ".env file not found. Using .env.example instead."
    cp .env.example .env
fi

docker-compose up -d || sudo docker-compose up -d
