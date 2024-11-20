FROM alpine:3.20.3

WORKDIR app

COPY . .

RUN apk update &&\
    apk install nodejs npm &&\
    npm install
