FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN makir code
WORKDIR /code

COPY req.txt .
ADD wsgi-entrypoint.sh .

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl tree && \
    python3 -m pip install --upgrade pip && \
    pip install -r req.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY src/ /code/
