FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir code
WORKDIR /code

COPY req.txt .
COPY wsgi-entrypoint.sh ./

RUN apk update && \
    apk add --no-cache curl tree && \
    pip install --root-user-action=ignore && \
    python3 -m pip install --upgrade pip && \
    pip install -r req.txt

COPY src/ /code/
