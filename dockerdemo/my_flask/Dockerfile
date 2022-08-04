FROM python:latest

WORKDIR /src/my_flask

RUN apt update -y
RUN pip install Flask

ENV FLASK_APP hello

CMD flask run --host=0.0.0.0

ADD hello.py .
