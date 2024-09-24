FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir code
WORKDIR /code

COPY req.txt .
COPY wsgi-entrypoint.sh ./

RUN apt update && \
    apt install -y --no-install-recommends curl tree && \
    python3 -m pip install --upgrade pip && \
    pip install -r req.txt && \
    pip install setuptools && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

COPY src/ /code/
