FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir code
WORKDIR /code

COPY req.txt .
COPY wsgi-entrypoint.sh ./

RUN apt update 
RUN   apt install -y --no-install-recommends curl tree 
RUN    python3 -m pip install --upgrade pip 
RUN    pip install -r req.txt 
RUN    pip install setuptools 
RUN    apt clean 
RUN    rm -rf /var/lib/apt/lists/*

COPY src/ /code/
