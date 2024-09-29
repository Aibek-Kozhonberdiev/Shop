#!/bin/bash

if [ -f .env ]; then
    echo ".env file found. Starting Docker Compose."
else
    echo ".env file not found. Using .env.example instead."
    cp .env.example .env
fi

if [[ $(uname) == "Darwin" ]]; then
    docker-compose up -d
else
    if sudo -v &> /dev/null; then
        sudo docker-compose up -d
    else
        docker-compose up -d
    fi
fi
