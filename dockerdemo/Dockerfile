FROM python:latest

WORKDIR /src/scripts

ADD hello.py .
ADD world.py .

RUN touch main.py
RUN apt update -y
RUN apt install nano -y

ENV dog corgi

EXPOSE 80

